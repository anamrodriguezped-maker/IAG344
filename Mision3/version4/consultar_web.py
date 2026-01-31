import pandas as pd
import os

ARCHIVO = "asistencias.xlsx"
FOTOS = "dataset"


def calcular_nomina(id_emp, mes, anio):

    if not os.path.exists(ARCHIVO):
        return 0, 0, ""

    df = pd.read_excel(ARCHIVO)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    filtro = df[
        (df["id"] == id_emp) &
        (df["fecha"].dt.month == mes) &
        (df["fecha"].dt.year == anio) &
        (df["tipo"] == "entrada")
    ].drop_duplicates(subset=["fecha"])

    if filtro.empty:
        return 0, 0, ""

    dias = len(filtro)
    salario = filtro["salario"].mean()
    nombre = filtro.iloc[0]["nombre"]

    return dias, dias * salario, nombre


def buscar_foto(id_emp):

    for archivo in os.listdir(FOTOS):
        if archivo.startswith(f"user.{id_emp}."):
            return f"/static/dataset/{archivo}"

    return None
