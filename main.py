from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["jogos"]
collec = db["jogos_flask"]


@app.route("/")
def home():
    jogos = [jogo for jogo in collec.find({}, {"_id": 0,  "nome": 1, "categorias": 1})]

    return render_template("index.html", jogos=jogos)


@app.route("/form")
def form_jogo():
    return render_template("form.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar_jogo():
    collec.insert_one({
        "nome": request.form["nome"].title().strip(),
        "categorias": request.form["categorias"].split(" ")
    })

    return redirect("/")


app.run(port=8080, debug=True)
