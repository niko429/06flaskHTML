from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("06index.html", imie="Nikodem", projekt="flaskHTML")

LISTA = [
    {"id": 1, "nazwa": "Laptop", "firma": "Samsung", "Cena": 3999,"gamingowy": False},
    {"id": 2, "nazwa": "Myszka", "firma": "Redragon", "Cena": 49,"gamingowy": True},
    {"id": 3, "nazwa": "Myszka", "firma": "Chinska", "Cena": 29,"gamingowy": False},
    {"id": 4, "nazwa": "Komputer", "firma": "Domowa", "Cena": 9999,"gamingowy": True},
    {"id": 5, "nazwa": "Drukarka", "firma": "Brother", "Cena": 699,"gamingowy": False},
]

@app.route("/lista")
def list():
    return render_template("06lista.html", lista=LISTA)



if __name__ == "__main__":
    app.run(debug=True)