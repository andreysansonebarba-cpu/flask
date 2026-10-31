from flask import Flask
import random

app = Flask(__name__)

fatti_curiosi = [
    "Eugene Shoemaker, il co-scopritore della famosa cometa Shoemaker-Levy 9 e fondatore dell’esogeologia, sarebbe dovuto essere il primo geologo a mettere piede sulla Luna, ma sfortunatamente, i suoi problemi di salute gli impedirono di intraprendere il viaggio finché era ancora in vita",
    "Il nome “Italia” ha un’origine animale",
    "Il termine deriva dal greco italos, che significa “vitello”. Fu usato inizialmente per la Calabria dai coloni greci nell’VIII secolo a.C. e poi esteso a tutta la penisola Augusto Cesare",
    "Non tutti lo sanno ma la storia di Pinocchio è stata scritta a Collodi (provincia di Pistoia) nel 1880 dalle mani di Carlo Collodi.",
    "Esiste un parco tematico a Collodi. Per chi volesse visitarlo è davvero carino soprattutto se ci portate i vostri figli. In realtà è adatto anche agli adulti che sono nati e cresciuti con la magica storia di Pinocchio."
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/build")
def build():
    return "<p>Welcome to the build page!</p>"

@app.route("/login")
def login():
    return "<p>Welcome to the login page!</p>"

@app.route("/user/<username>")
def user(username):
    return f"<p>Hello, {username}!</p>"

@app.route("/search")
def search():
    return "<p>Welcome to the search page!</p>"

@app.route("/fatti_curiosi")
def fatti_curiosi():
    fatto_random = random.choice(fatti_curiosi)
    return f"<p>un fatto curioso è: {fatto_random}</p>"
app.run(debug=True)