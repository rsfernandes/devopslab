from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Grupo 31 - KEVIN RAFA E ZE"

if __name__ == '__main__':
    app.run()