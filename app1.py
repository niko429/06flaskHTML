from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    PRODUKTY = ["woda", "owoc"]
    return render_template("06index1.html", imie="Nikodem", produkt="flaskHTML", produkty=PRODUKTY, cena=1.23)

@app.route("/login")
def log():
    return render_template("06index1.html", zalogowany=True, rola="sprzedawca")

@app.route("/admin")
def ad():
    return "Storna"

@app.route("/magazyn")
def mag():
    return "Strona ale inna"

@app.route("/lista")
def lsit():
    return render_template("06lista1.html", produkty=["Laptop", "Mysz", "Klawiatura"])

@app.route("/ceny")
def cena():
    return render_template("06ceny1.html", ceny={"Laptop": 2999, "Mysz": 49})

PRODUKTY = [
    {"id": 1, "nazwa": "Laptop", "cena": 2999, "dostępny": True},
    {"id": 2, "nazwa": "Mysz", "cena": 49, "dostępny": False},
    {"id": 3, "nazwa": "Klawiatura", "cena": 199, "dostępny": True},
]

@app.route("/produkty")
def pro():
    return render_template("06produkty1.html", produkty=PRODUKTY)

if __name__ == "__main__":
    app.run(debug=True)