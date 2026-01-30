import os
import groq
os.environ["GROQ_API_KEY"]="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"
from groq import Groq
client = Groq (
    api_key=os.environ.get("GROQ_API_KEY")
)
chat_completion =client.chat.completions.create (
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"system",
            "content":(
            "Actua como un experto en excel y base de datos"
            "Tu tarea es interpretar instrucciones en lenguaje natural "
             "y extraer la instrucción del usuario. \n\n"
             "Debes identificar:\n"
             "- la acción principal (sumar, filtrar, ordenar, agrupar, etc.)\n"
             " - las columnas involucradas\n"
             "- las condiciones si existen \n"
             "Devuelve SIEMPRE la respuesta en formato JSON con esta estructura: \n"
             "{\n"
              '"accion":"",\n'
              ' "Columnas":[], \n'
              ' "Condiciones":[],\n'
              ' "Resultado":"",\n'
                )
        },
        {
            "role":"user",
            "content":"quiero saber el salario de los nombres del 2026"
        }
    ],
    
)
""" print(chat_completion.choices[0].message.content) """