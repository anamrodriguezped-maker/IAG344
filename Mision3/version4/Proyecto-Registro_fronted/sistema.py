import cv2
import os
import pandas as pd
import numpy as np
from datetime import datetime

# =========================
# CONFIGURACIÓN GENERAL
# =========================

ARCHIVO = "asistencias.xlsx"
DATASET = "dataset"
MODELO = "modelo.xml"

# Ruta correcta del Haar Cascade (SOLUCIÓN CLAVE)
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

if not os.path.exists(DATASET):
    os.makedirs(DATASET)

# =========================
# INICIALIZAR EXCEL
# =========================

def inicializar_excel():
    if not os.path.exists(ARCHIVO):
        df = pd.DataFrame(columns=[
            "id", "nombre", "fecha", "hora", "tipo", "salario"
        ])
        df.to_excel(ARCHIVO, index=False)
        print("✅ Archivo de asistencias creado")

# =========================
# REGISTRAR ASISTENCIA
# =========================

def registrar_asistencia(id_emp, nombre, salario, tipo):
    inicializar_excel()

    df = pd.read_excel(ARCHIVO)
    ahora = datetime.now()

    nuevo = {
        "id": id_emp,
        "nombre": nombre,
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M"),
        "tipo": tipo,
        "salario": salario
    }

    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    df.to_excel(ARCHIVO, index=False)

    print("📝 Asistencia registrada")

# =========================
# CAPTURAR ROSTROS
# =========================

def capturar_rostro(id_emp):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ No se pudo abrir la cámara")
        return

    detector = cv2.CascadeClassifier(CASCADE_PATH)
    if detector.empty():
        print("❌ Error cargando Haar Cascade")
        return

    contador = 0
    print("📸 Capturando rostros (Q para salir)")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        caras = detector.detectMultiScale(gris, 1.3, 5)

        for (x, y, w, h) in caras:
            contador += 1
            rostro = gris[y:y+h, x:x+w]
            ruta = f"{DATASET}/user.{id_emp}.{contador}.jpg"
            cv2.imwrite(ruta, rostro)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Captura de Rostros", frame)

        if cv2.waitKey(1) & 0xFF == ord("q") or contador >= 20:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Rostros capturados")

# =========================
# ENTRENAR MODELO
# =========================

def entrenar():
    if len(os.listdir(DATASET)) == 0:
        print("❌ No hay imágenes para entrenar")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    caras, ids = [], []

    for archivo in os.listdir(DATASET):
        path = os.path.join(DATASET, archivo)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        id_emp = int(archivo.split(".")[1])

        caras.append(img)
        ids.append(id_emp)

    recognizer.train(caras, np.array(ids))
    recognizer.save(MODELO)

    print("✅ Modelo entrenado correctamente")

# =========================
# RECONOCIMIENTO FACIAL
# =========================

def reconocer(nombre, salario):
    if not os.path.exists(MODELO):
        print("❌ Modelo no entrenado")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(MODELO)

    detector = cv2.CascadeClassifier(CASCADE_PATH)
    cap = cv2.VideoCapture(0)

    registrado = False
    print("🎥 Reconociendo rostro (Q para salir)")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        caras = detector.detectMultiScale(gris, 1.3, 5)

        for (x,y,w,h) in caras:
            id_emp, conf = recognizer.predict(gris[y:y+h, x:x+w])

            if conf < 70 and not registrado:
                cv2.putText(frame, f"ID {id_emp}", (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                registrar_asistencia(id_emp, nombre, salario, "entrada")
                registrado = True

            elif conf >= 70:
                cv2.putText(frame, "Desconocido", (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Reconocimiento Facial", frame)

        if registrado or cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# =========================
# CÁLCULO DE NÓMINA
# =========================

def calcular_nomina(id_emp, mes, anio):
    if not os.path.exists(ARCHIVO):
        return 0, 0

    df = pd.read_excel(ARCHIVO)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    filtro = df[
        (df["id"] == id_emp) &
        (df["fecha"].dt.month == mes) &
        (df["fecha"].dt.year == anio) &
        (df["tipo"] == "entrada")
    ].drop_duplicates(subset=["fecha"])

    if filtro.empty:
        return 0, 0

    dias = len(filtro)
    salario = filtro["salario"].mean()
    return dias, dias * salario

# =========================
# MENÚ
# =========================

def menu():
    while True:
        print("\n===== SISTEMA IA =====")
        print("1. Registrar empleado")
        print("2. Entrenar modelo")
        print("3. Registrar asistencia")
        print("4. Calcular nómina")
        print("5. Salir")

        op = input("Seleccione: ")

        if op == "1":
            capturar_rostro(int(input("ID: ")))

        elif op == "2":
            entrenar()

        elif op == "3":
            reconocer(
                input("Nombre: "),
                float(input("Salario día: "))
            )

        elif op == "4":
            d, t = calcular_nomina(
                int(input("ID: ")),
                int(input("Mes: ")),
                int(input("Año: "))
            )
            print(f"Días trabajados: {d}")
            print(f"Total a pagar: ${t}")

        elif op == "5":
            break

# =========================
# MAIN
# =========================

def main():
    inicializar_excel()
    menu()

if __name__ == "__main__":
    main()