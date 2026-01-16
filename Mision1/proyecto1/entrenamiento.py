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

texto="Mi número es 57*12345-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado{resultado}") 
""" separa todos los numero 
 """
texto="Mi número es 57*12345-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado{resultado}") 

#ejercicio1
texto="cc.75.055.60"
resultado=("".join(re.findall(r"\d+",texto)))
print(f"{(resultado)}")


documento1="cc.75.055.60"

def clean_id(documento):
    return re.sub(r'\D',"", documento)
print(clean_id(documento1))


#ejemplo2
correo = "ana@gmail.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
    print("Correo válido")
else:
    print("Correo inválido")




