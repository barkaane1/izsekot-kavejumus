from flask import Flask, render_template, request, redirect, url_for, session
import random
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
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
        
        conn = sqlite3.connect("pica.db")
        conn.row_factory = sqlite3.Row
        user = conn.execute("SELECT * FROM Lietotajs WHERE lietotajvards = ?", (lietotajvards,)).fetchone()
        conn.close()
        

        if user and check_password_hash(user['parole'], parole):
            session['id'] = user['id']
            session['vards'] = user['vards']
            session['loma'] = user['loma']
            return redirect(url_for(''))
            
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
                    (vards, uzvards, klase, lietotajvards, 'klients', paroles_hesh))
        conn.commit()
        conn.close()
        return redirect(url_for('pieslegties'))
    return render_template('registreties.html')


@app.route("/pieteikt")
#Šeit varēs pieteikt kavējumu
def pieteikt():
	pass


@app.route("/profils")
#Šeit būs lietotāja profils
def profils():
	pass

@app.route("/par")
#Šeit būs par mājaslapas veidotājiem
def par():
	return render_template("par.html")

@app.route("/stundas")
#Šeit būs pieejamas visas stundas 
def stundas():
	pass

@app.route("/kavets")
#Šeit varēs redzēt cik procentuāli un skaitā ir kavētas stundas
def kavets():
	pass

if __name__ == "__main__":
	app.run(debug = True)
