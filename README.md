# Clase IA
## 🤖Comandos consola
### ![imagen de Python](images.jpg)
```
python --version

```
## 🤖Comandos 
### ![imagen de git](git.jpg)
```git
git --version
git init (solo lo hago una vez por cada vez que quiero tener una version, pone en verde y oculta)
git add . (cuales para comprimir)
git commit -m "IAG344 v1" (version del archivo guardado)
git push actualiza ** y sube la información
A añadido
M modificaciones
U Nuevo
```
![git cat](image.png)
```
git branch -M main
git remote add origin https://github.com/anamrodriguezped-maker/IAG344.git
git push -u origin main
```
# Clase IA
##  😍 Muy importante
```
//si se crea otro repositorio nuevo
git status
git add .
git commit -m "IAG344 v1" 
git branch
git branch -M main
git add remote add origin https://github.com/anamrodriguezped-maker/IAG344.git
git push
cmd -> code .
cd PROFES
git clone https://github.com/fernandogh7508/IAG344
cd .. (Devolverme)
cd PERSONAL (AQUI SIII)

--v2
cd PERSONAL
git status
git remote -v
git push
git add .
git status
git commit -m "v2"
git push 

li*3
ctrl+shif+k
ctrl+x
```
#😎😎activar y desactivar
```

pip list -> LISTA  LA VERSION DE PIP -> le pertenece a python
python entrenamiento.py ABRIR PYTHON
DIR -> comandos cdm
env3.13.9/scripts/activate -> activar el entorno virtual
cd ..


```
#Comandos CDM
| COMANDO       | DESCRIPCION          |
| ------------- | -------------------- |
| cd            | cambio de directorio |
| dir           | listar               |
| alt+shif+f    | formatear table      |
| windows+punto |        emoticones              | 
 |alt+shif+A|comentarios en cada lenguaje
|       alt+z        |   justifica                 |

pip install pytest
pytest
```
```
snippets: 
PYTHON
SE CREO ese separador lindo y kiut

ws.save(path) 
define process_excel_save()
python -m venv env13.5.9 -> Crea el etorno virtual
descargar librerias
pip install (Nombre de la libreria)
openpyxl
python

libreria instalar
`pip installer pyinstaller`
crear el .exe
`pyinstaller --onefile --windowed app.py`
```

<!-- importante GIT HUB -->
😎github pages

<!-- excel trabajado en python -->
#LIBRERIAS
--
import pandas as pd #pip install pandas
--
df =pd.read_csv("./dataset.csv")
df.head(5)
--
df.describe()
--
df["favorites"]
--
df.loc[0:2]
--
df.loc[[0,1,7]]
--
df.loc[[1,7],["favorites"]]
--
#seleccionar por condición
df[df["favorites"]>400]
--
df[(df["favorites"]>400)&(df["mentions"]>20)]
--
df.loc[9:19][(df.loc[9:19]["favorites"]>400)&(df.loc[9:19]["mentions"]>9)]
--
cls limpiar el terminal

python
C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe