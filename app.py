from flask import Flask, render_template, request, redirect, url_for, session
import random
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "loti_slepena_atslega_kavejumu_priekam"
def get_db_connection():
    conn = sqlite3.connect("kavejumi.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def sakums():
	return render_template("layout.html")

@app.route("/pieslegties", methods=['GET', 'POST'])
#Šeit varēs ieiet savā kontā
def pieslegties():
    if request.method == 'POST':
        lietotajvards = request.form.get('lietotajvards')
        parole = request.form.get('parole')
        
        conn = sqlite3.connect("kavejumi.db")
        conn.row_factory = sqlite3.Row
        user = conn.execute("SELECT * FROM Lietotajs WHERE lietotajvards = ?", (lietotajvards,)).fetchone()
        conn.close()
        

        if user and check_password_hash(user['parole'], parole):
            session['id'] = user['liet_id']
            session['vards'] = user['vards']
            session['loma'] = user['loma']
            return redirect(url_for('sakums'))
            
    return render_template('pieslegties.html')

@app.route("/registreties", methods=['GET', 'POST'])
#Šeit varēs izveidot kontu
def registreties( ):
    if request.method == 'POST':
        vards = request.form.get('vards')
        lietotajvards = request.form.get('lietotajvards')
        parole = request.form.get('parole')
        uzvards = request.form.get('uzvards')
        klase = request.form.get('klase')
        

        paroles_hesh = generate_password_hash(parole)
        
        conn = sqlite3.connect("kavejumi.db")
        cur = conn.cursor()

        cur.execute("INSERT INTO Lietotajs (vards, uzvards, klase, lietotajvards, loma, parole) VALUES (?, ?, ?, ?, ?, ?)",
                    (vards, uzvards, klase, lietotajvards, 'skolnieks', paroles_hesh))
        conn.commit()
        conn.close()
        return redirect(url_for('pieslegties'))
    return render_template('registreties.html')



#Šeit varēs pieteikt kavējumu
@app.route("/pieteikt", methods=['GET', 'POST'])
def pieteikt():
    # 1. Pārbaudām, vai lietotājs ir ielogojies
    if 'id' not in session:
        return redirect(url_for('pieslegties'))

    if request.method == 'POST':
        # 2. Saņemam datus no formas
        datums = request.form.get('datums')
        ned_st = float(request.form.get('ned_st'))
        neapm = float(request.form.get('neapm'))
        
        # 3. Aprēķinām kavējumu procentu
        if ned_st > 0:
            procents = (neapm / ned_st) * 100
        else:
            procents = 0
            
        # 4. Saglabājam datubāzē
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO stundas (Liet_ID, ned_st, neapm, datums, procents) 
            VALUES (?, ?, ?, ?, ?)
        """, (session['id'], ned_st, neapm, datums, round(procents, 2)))
        conn.commit()
        conn.close()
        
        # 5. Pēc saglabāšanas aizsūtam uz nedēļas plānu
        return redirect(url_for('stundas'))

    return render_template("pieteikt.html")
@app.route("/profils")
def profils():
    if 'id' not in session:
        return redirect(url_for('pieslegties'))

    conn = get_db_connection()
    # Iegūstam ielogotā lietotāja datus [cite: 30]
    user = conn.execute("SELECT * FROM Lietotajs WHERE liet_id = ?", (session['id'],)).fetchone()
    
    # Saskaitām visas kavētās stundas (neapm) šim lietotājam [cite: 30]
    kavetas_summa = conn.execute("SELECT SUM(neapm) FROM stundas WHERE Liet_ID = ?", (session['id'],)).fetchone()[0]
    conn.close()

    # Ja datu nav, SUM atgriež None, nomainām uz 0
    kavetas_stundas = kavetas_summa if kavetas_summa else 0

    return render_template("profils.html", lietotajs=user, kavetas=kavetas_stundas)
@app.route("/par")
#Šeit būs par mājaslapas veidotājiem
def par():
	return render_template("par.html")


#Šeit būs pieejamas visas stundas 
@app.route("/stundas")
def stundas():
    if 'id' not in session:
        return redirect(url_for('pieslegties'))
    
    conn = get_db_connection()
    # Atlasām visus ierakstus no tabulas 'stundas' [cite: 30]
    plana_ieraksti = conn.execute("SELECT * FROM stundas WHERE Liet_ID = ?", (session['id'],)).fetchall()
    conn.close()
    
    return render_template("stundas.html", plani=plana_ieraksti)

@app.route("/kavets")
#Šeit varēs redzēt cik procentuāli un skaitā ir kavētas stundas
def kavets():
    if 'id' not in session:
        return redirect(url_for('pieslegties'))

    conn = get_db_connection()
    # Atlasām tikai tos ierakstus, kur ir kavētas stundas
    tikai_kavejumi = conn.execute("""
        SELECT * FROM stundas 
        WHERE Liet_ID = ? AND neapm > 0 
        ORDER BY datums DESC
    """, (session['id'],)).fetchall()
    
    # Aprēķinām kopējo kavēto stundu skaitu
    kopsavilkums = conn.execute("""
        SELECT SUM(neapm), AVG(procents) 
        FROM stundas 
        WHERE Liet_ID = ?
    """, (session['id'],)).fetchone()
    
    conn.close()

    return render_template("kavets.html", 
                           saraksts=tikai_kavejumi, 
                           summa=kopsavilkums[0] or 0, 
                           videjais=round(kopsavilkums[1] or 0, 2))
@app.route('/iziet')
def iziet():
    session.clear() 
    return redirect(url_for('sakums'))

@app.route("/admin")
def admin_panelis():
    # 1. Pārbaude: vai lietotājs ir ielogojies un vai viņš ir admins
    # Piezīme: Tavā reģistrācijas formā loma tiek saglabāta kā 'klients' vai 'admins'
    if 'id' not in session or session.get('loma') != 'admin':
        return "Pieeja liegta! Šī lapa ir tikai administratoriem.", 403

    conn = get_db_connection()
    
    # 2. SQL JOIN vaicājums, lai dabūtu lietotāja vārdu kopā ar viņa kavējumu datiem
    visi_kavejumi = conn.execute('''
        SELECT Lietotajs.vards, Lietotajs.uzvards, Lietotajs.klase, 
               stundas.datums, stundas.ned_st, stundas.neapm, stundas.procents
        FROM stundas
        JOIN Lietotajs ON stundas.Liet_ID = Lietotajs.liet_id
        ORDER BY stundas.datums DESC
    ''').fetchall()
    
    # 3. Saskaitām kopējo sistēmas kavējumu skaitu statistikai
    kopskaits = conn.execute('SELECT SUM(neapm) FROM stundas').fetchone()[0] or 0
    
    conn.close()
    
    return render_template("admin.html", kavejumi=visi_kavejumi, kopskaits=kopskaits)

if __name__ == "__main__":
	app.run(debug = True)
