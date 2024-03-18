from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "João Saquetto mandou um olá!"
