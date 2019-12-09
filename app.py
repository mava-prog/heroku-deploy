from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/") #dekorator; dekorator funkcijo prime jo malo spremeni ter vrne nazaj; točno ta aplikacije ko pride na ta naslov polaufaj funkcijo, ki sledi; njen rezultat se bo pokazal na spletni strani;
def index():
    trenutni_cas = datetime.datetime.now()
    return f"<h1>Moja prva spletna stran</h1><p>{trenutni_cas}</p>"

@app.route("/about")
def on_about():
    #Preberi datoteko:
    #with open("index.html") as html_datoteka:
        #vsebina =html_datoteka.read()
    #return vsebina
    return render_template("index.html")
    # ti htmlji ki so tukaj jih vedno na novo generiramo z odpiranjem
if __name__ == "__main__":
    app. run()