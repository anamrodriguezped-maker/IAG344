import os
os.environ["GROQ_API_KEY"]="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"
from groq import Groq

# ===============================
# Configuración API Groq
# ===============================

client = Groq(
    api_key=os.environ.get("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")
)

# ===============================
# FUNCIÓN PRINCIPAL DEL LLM
# ===============================
def chat_completion(user_text):
    """
    Convierte lenguaje natural en instrucciones JSON
    para consultar un archivo Excel
    """

    prompt = f"""
Convierte la siguiente pregunta en instrucciones JSON para consultar un Excel.

REGLAS IMPORTANTES:
- NO expliques nada
- NO escribas texto fuera del JSON
- NO uses markdown
- SOLO devuelve JSON válido
- Usa CONTAINS para nombres
- Columnas posibles: nombre, cedula, salario, año

FORMATO EXACTO:
{{
  "columnas": [],
  "condiciones": []
}}

EJEMPLOS:

Pregunta: Muéstrame el salario de Luis
Respuesta:
{{
  "columnas": ["salario"],
  "condiciones": ["nombre CONTAINS Luis"]
}}

Pregunta: Salario del empleado con cedula 123
Respuesta:
{{
  "columnas": ["salario"],
  "condiciones": ["nombre = Luis", "cedula = 123"]
}}

Pregunta del usuario:
{user_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Eres un sistema que convierte texto en JSON para consultas de Excel."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
