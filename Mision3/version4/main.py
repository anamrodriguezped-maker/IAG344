from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model, predict_answer, load_model
from chatbot.model2 import chat_completion as groq_chat
import pandas as pd
import json

# =====================================
# Cargar Excel (base de datos)
# =====================================
df = pd.read_excel("asistencias.xlsx")  # Ajusta la ruta si es necesario

# =====================================
# Función para consultar Excel
# =====================================
def consultar_excel(df, llm_json):
    # Validar que sea JSON
    if not llm_json or not llm_json.strip().startswith("{"):
        raise ValueError("La respuesta del modelo no es un JSON válido")

    instrucciones = json.loads(llm_json)
    resultado = df.copy()

    for condicion in instrucciones.get("condiciones", []):
        # Soporte para búsquedas parciales (ej: Luis)
        if "CONTAINS" in condicion:
            campo, valor = condicion.split("CONTAINS")
            campo = campo.strip()
            valor = valor.strip().replace('"', '').replace("'", "")

            if campo not in resultado.columns:
                raise ValueError(f"La columna '{campo}' no existe en el Excel")

            resultado = resultado[
                resultado[campo]
                .astype(str)
                .str.lower()
                .str.contains(valor.lower())
            ]
        else:
            campo, valor = condicion.split("=")
            campo = campo.strip()
            valor = valor.strip().replace('"', '').replace("'", "")

            if campo not in resultado.columns:
                raise ValueError(f"La columna '{campo}' no existe en el Excel")

            resultado = resultado[
                resultado[campo].astype(str).str.lower()
                == valor.lower()
            ]

    columnas = instrucciones.get("columnas", [])
    return resultado[columnas] if columnas else resultado

# =====================================
# Flask App
# =====================================
app = Flask(__name__)

# =====================================
# Modelo clásico
# =====================================
model, vectorizer, unique_answers = load_model()
if model is None:
    model, vectorizer, unique_answers = build_and_train_model(training_data)

# =====================================
# Rutas
# =====================================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/homechatbot")
def homechatbot():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message", "").strip()

    if not user_text:
        return jsonify({"response": "Por favor escribe algo 🙄"})

    # Palabras que indican consulta de datos
    palabras_llm = [
        "salario", "nombre", "id",
        "hora", "fecha", "excel", "base de datos"
    ]

    if any(p in user_text.lower() for p in palabras_llm):
        try:
            llm_response = groq_chat(user_text)
            print("RESPUESTA DEL LLM >>>", llm_response)

            resultado_df = consultar_excel(df, llm_response)

            if resultado_df.empty:
                response = "No encontré resultados con esos datos 😕"
            else:
                response = resultado_df.to_string(index=False)

        except Exception as e:
            response = f"Error procesando el Excel: {str(e)}"
    else:
        response = predict_answer(
            model, vectorizer, unique_answers, user_text
        )

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

