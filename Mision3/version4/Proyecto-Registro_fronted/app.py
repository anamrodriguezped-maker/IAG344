from flask import Flask, render_template, request, redirect, url_for
import sistema   # 👈 tu archivo sistema.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capturar", methods=["POST"])
def capturar():
    id_emp = int(request.form["id"])
    sistema.capturar_rostro(id_emp)
    return redirect(url_for("index"))

@app.route("/entrenar", methods=["POST"])
def entrenar():
    sistema.entrenar()
    return redirect(url_for("index"))

@app.route("/reconocer", methods=["POST"])
def reconocer():
    nombre = request.form["nombre"]
    salario = float(request.form["salario"])
    sistema.reconocer(nombre, salario)
    return redirect(url_for("index"))

@app.route("/nomina", methods=["POST"])
def nomina():
    id_emp = int(request.form["id"])
    mes = int(request.form["mes"])
    anio = int(request.form["anio"])

    dias, total = sistema.calcular_nomina(id_emp, mes, anio)

    return render_template(
        "index.html",
        dias=dias,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)