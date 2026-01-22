import os
import pickle
# esta libreria convierte texto en vectores
from sklearn.feature_extraction.text import CountVectorizer
# esta libreria se encarga de buscar las relacion con las respuestas
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR="models"
MODEL_PATH=os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWER_PATH=os.path.join(MODEL_DIR,"answers.pkl")

# funcion de entrenamiento preguntas y respuestas
def build_and_train_model(Train_pairs):
    # Train_pairs lista de pares (preguntas y respuestas)
    # Ejemplo [ ("hola", "¡Hola!",) , ("adios", "¡Hasta luego!") ]
    # Separar las preguntas y respuestas en dos listas
    
    questions = [q for q, _ in Train_pairs]# lista de preguntas
    answers = [a for _, a in Train_pairs]  # lista de respuestas
    # creamos el vectorizado, que traducira del texto a numeros
    vectorizer=CountVectorizer()
    #entrenamiento del modelo
    x = vectorizer.fit_transform(questions) # Convertir las preguntas en vectores
    #obtenemos una lista de respuestas unicas
    unique_answers = sorted(set(answers))
    # crear el diccionario con las etiquetas
    answer_to_label = {a: i for i, a in enumerate(unique_answers)}
    #creamos una lista
    y= [answer_to_label[a] for a in answers]
    #Modelo claseificador de texto
    model = MultinomialNB()
    #entrenamos el modelo
    model.fit(x,y)
    # Crear carpeta para guardar el modelo si no existe
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    #guardar los objetos entrenados
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(ANSWER_PATH,"wb") as f:
        pickle.dump(unique_answers,f)
    print("🆗 Modelo entrenado y guardado correctamente")
    #guardar los objetos entrenados
    return model, vectorizer, unique_answers

def load_model():
    """
    Carga el modelo, del vectorizao y las respuestas si existe.
    """
    
    if(
        os.path.exists(MODEL_PATH)
        and os.path.exists( VECTORIZER_PATH)
        and os.path.exists( ANSWER_PATH)
        
    ):
        with open(MODEL_PATH,"rb") as f:
            model=pickle.load(f)
        with open(VECTORIZER_PATH,"rb") as f:
            vectorizer=pickle.load(f)
        with open(ANSWER_PATH,"rb") as f:
            unique_answers=pickle.load(f)
        print("📂 Modelo cargado desde disco.")
        return model,vectorizer,unique_answers
    else:
        print("⚠️ No hay modelo guardado, será necesario entrenarlo")
        return None,None,None 
        

# funcion para predecir la respuesta
def predict_answer(model, vectorizer, unique_answers, user_text):
        # Convertir la entrada del usuario en un vector
        X = vectorizer.transform([user_text])
        # Predecir la etiqueta de la respuesta
        label = model.predict(X)[0]
        return unique_answers[label]