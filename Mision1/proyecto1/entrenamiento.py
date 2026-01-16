# librerias 
import re
"""
Expresiones regulares en Python 
Problemas reales
"""

#Codigo
print("libreria cargada correctamente")
#ejemplo1
texto="Mi número es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado{resultado.group()}")

texto="Mi número es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado{resultado.group()}")

correo = "ana@gmail.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
    print("Correo válido")
else:
    print("Correo inválido")


