from flask import Flask, render_template, request, url_for, redirect
import sqlite3
app = Flask(__name__)

@app.route("/")
def sakums():
	return render_template("index.html")
@app.route("/kontakti")
def kontakti():
	return " <h1> ADRESE</h1><p> Aleksandra Čaka 102</p> "

@app.route("/par")
def par():
	return render_template("par.html")

@app.route("/profils")
def profils():
	darbu_saraksts = [
	{"nosaukums": "Jāiemācās tēma", "Ilgums" : 21, "Statuss" : True},
	{"nosaukums": "Jauzraksta PD", "Ilgums" : 2, "Statuss" : True},
	{"nosaukums": "Nezinu kas jādara", "Ilgums" : 205, "Statuss" : False},
	{"nosaukums": "Jaaiziet us stundu", "Ilgums" : 66, "Statuss" : True}
	]
	return render_template("profils.html" , lietotajs = "Kristīne", darbi = darbu_saraksts)
@app.route("/ievade")
def ievade():
	return render_template("ievade.html")

@app.route("/atbilde", methods = ["POST"])
def atbilde():
	nosaukums = request.form.get("nosaukums")
	gads = request.form.get("gads")
	return render_template("atbilde.html", n = nosaukums, g = gads)

@app.route("/filmas")
def filmas():
	conn = sqlite3.connect("imdb2026.db")
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
    
	nosaukums = request.args.get("nosaukums", " ")
	if nosaukums:
		cursor.execute("SELECT * FROM top_250 WHERE Title LIKE ?", (f"%{nosaukums}%", ))
	else:
		cursor.execute("SELECT * FROM top_250")
	atbilde = cursor.fetchall()
	conn.close() 
	return render_template("filmas.html", filmas = atbilde)
@app.route("/pievienot", methods=["GET", "POST"])
def pievienot():
    if request.method == "POST":
        conn = sqlite3.connect("imdb2026.db")
        cursor = conn.cursor()
        
        nosaukums = request.form.get("nosaukums")
        gads = request.form.get("gads")
        reitings = request.form.get("reitings")
        fails = request.form.get("fails")

        
        cursor.execute(
            "INSERT INTO top_250 (Title, Year, Rating, Poster) VALUES (?, ?, ?, ?)", 
            (nosaukums, gads, reitings, fails)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for('filmas'))
    else:
    	return render_template("pievienot.html")

@app.route("/pieteikties")
def pieteikties():
    return render_template("login.html")

    
@app.route('/kalkulators', methods=['GET', 'POST'])
def kalkulators():
    rezultats = None  # Sākumā rezultāta nav
    
    if request.method == 'POST':
        # Šī daļa izpildās tikai tad, kad nospiež pogu
        izteiksme = request.form.get('izteiksme')
        if izteiksme:
            rezultats = eval(izteiksme)
            
    # Atgriežam to pašu lapu, bet līdzi iedodam (vai neiedodam) rezultātu
    return render_template('kalkulators.html', r=rezultats)


@app.route("/registreties")
def registreties():
	return render_template("registreties.html")





if __name__ == "__main__":
	app.run(debug = True)
