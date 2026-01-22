#
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#function de entrenamiento preguntas y respuestas
def build_and_train_model(train_pairs):
    #train_pairs listar pares(pregunta, respuestas)
    #ejemplo [("hola", "¡Hola!"),("adios", "¡Hasta luego!")]
    #separamos las preguntas y respuestas en dos listas
    questions= [q for q, _ in train_pairs] #lista de preguntas
    answer= [a for _, a in train_pairs] #lista de preguntas
    #creamos el vectorizado, que traducira el texto a numeros
    vectorizer=CountVectorizer()
    #entrenamiento
    x = vectorizer.fit_transform(questions)
    #obtenemos una lista de respuestas unicas
    unique_answers = sorted(set(answer))
    #crear el diccionario con las etiquetas
    answers_to_label={a: i for i, a in enumerate(unique_answers)}
    #crear el diccionarop con las etiquetas
    y = [answers_to_label[a] for a in answer]
    #modelo clacificación de texto
    model =MultinomialNB()
    #eNTRENAR EL MODELO
    model.fit(x,y)
    return model, vectorizer, unique_answers
#funcion predict_answer
def predict_answer(model, vectorizer, unique_answer, user_text):
    #convertir el texto a numeros
    x = vectorizer.transform([user_text])
    #el modelo predice la etiqueta de la respueta correcta
    label = model.predict(x)[0]
    return unique_answer[label]
#programa principal
if __name__== "__main__":
    training_data=[
        ("gracias", "Gracias a ti por comunicarte con nosotros ¡Que tengas un excelente día!"),
        ("buenos días", "¡Muy buenos días! 😊 Es un gusto atenderte, ¿en qué puedo ayudarte?"),
        ("hola", "¡Hola! 👋 Bienvenido/a, dime por favor cómo puedo ayudarte."),
        ("buenas tardes", "¡Muy buenas tardes! 🌷 Estoy aquí para ayudarte en lo que necesites."),
        ("buenas noches", "¡Buenas noches! ✨ Gracias por escribirnos, ¿en qué podemos apoyarte?"),
        ("necesito ayuda", "¡Con mucho gusto! 😊 Cuéntame qué necesitas y lo revisamos juntos."),
        ("tengo una pregunta", "¡Claro que sí! 💬 Estoy atenta para resolver tu pregunta."),
        ("quiero información", "¡Será un placer brindarte la información! 📄 ¿Sobre qué tema te gustaría saber?"),
        ("gracias", "¡Con todo gusto! 🌸 Estamos para servirte, no dudes en escribirnos nuevamente."),
        ("no entiendo", "No te preocupes 😊, con gusto te lo explico paso a paso."),
        ("hasta luego", "¡Hasta luego! 👋 Que tengas un excelente día, fue un placer atenderte."),
        ("Cuentame un chiste", "Claro que si, habia una vez un pollito que levanto una patica, levanto la otra patica y se cayó, jajajajajja si quieres te cuento uno mejor?")
        ]
    
    model, vectorizer, unique_answers = build_and_train_model(training_data)
    #mostrar un mensaje inicial al usuario
    print("👋 Bienvenido/a, dime por favor cómo puedo ayudarte, o escribe salir para terminar, \n")
    while True:
        #pedimos una frase al usuario 
        user = input("Tu: ").strip()
        if user.lower() in {"salir", "exit","quit"}:
            print("Bot: ¡Hasta pronto!")
            break
        response =predict_answer(model, vectorizer, unique_answers, user)
        print("Bot: ", response)