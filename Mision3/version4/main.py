from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model,predict_answer,load_model
from chatbot.model2 import chat_completion as groq_chat

app = Flask(__name__)
model,vectorizer,unique_answers=load_model()
if model is None:
        model,vectorizer,unique_answers=build_and_train_model(training_data)

@app.route("/homechatbot")
def homechatbot():
        return render_template("home.html")

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
        user_text = request.form.get("message","")
        if not user_text.strip():
                return jsonify({"response":"Por Favor escribe algo 🙄"})
        
        palabras_llm = ["quiero sumar las ventas por vendedor solo del año 2024", "sumar", "ventas", "filtrar", "año", "vendedor", "excel", "base de datos"]
        if any(p in user_text.lower() for p in palabras_llm):
                response = groq_chat.choices[0].message.content
        else:
                response = predict_answer(model, vectorizer, unique_answers, user_text)
        return jsonify({"response":response})
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

