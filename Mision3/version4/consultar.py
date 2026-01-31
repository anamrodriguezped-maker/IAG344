import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import os
from datetime import datetime

# ==========================
# CONFIGURACIÓN
# ==========================
ARCHIVO = "asistencias.xlsx"
FOTOS = "dataset"
COLOR_PRINCIPAL = "#6fbf4a"  # Verde oscuro
COLOR_SECUNDARIO = "#A5D6A7"  # Verde claro

if not os.path.exists(FOTOS):
    os.makedirs(FOTOS)

# ==========================
# INICIALIZAR EXCEL
# ==========================
def inicializar_excel():
    if not os.path.exists(ARCHIVO):
        df = pd.DataFrame(columns=["id", "nombre", "fecha", "hora", "tipo", "salario"])
        df.to_excel(ARCHIVO, index=False)

# ==========================
# CALCULAR NÓMINA
# ==========================
def calcular_nomina(id_emp, mes, anio):
    if not os.path.exists(ARCHIVO):
        return 0, 0

    df = pd.read_excel(ARCHIVO)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    filtro = df[(df["id"] == id_emp) &
                (df["fecha"].dt.month == mes) &
                (df["fecha"].dt.year == anio) &
                (df["tipo"] == "entrada")]

    filtro = filtro.drop_duplicates(subset=["fecha"])

    if filtro.empty:
        return 0, 0, ""

    dias = len(filtro)
    salario = filtro["salario"].mean()
    nombre = filtro.iloc[0]["nombre"]

    return dias, dias * salario, nombre

# ==========================
# BUSCAR FOTO
# ==========================
def buscar_foto(id_emp):
    for archivo in os.listdir(FOTOS):
        if archivo.startswith(f"user.{id_emp}."):
            return os.path.join(FOTOS, archivo)
    return None

# ==========================
# CONSULTAR EMPLEADO
# ==========================
def consultar():
    try:
        id_emp = int(entry_id.get())
        mes = int(entry_mes.get())
        anio = int(entry_anio.get())
    except:
        messagebox.showerror("Error", "Datos inválidos")
        return

    dias, total, nombre = calcular_nomina(id_emp, mes, anio)

    if dias == 0:
        messagebox.showinfo("Resultado", "No hay registros")
        return

    lbl_nombre.config(text=f"Empleado: {nombre}")
    lbl_dias.config(text=f"Días asistidos: {dias}")
    lbl_total.config(text=f"Total a pagar: ${total:,.0f}")

    ruta = buscar_foto(id_emp)

    if ruta:
        img = Image.open(ruta)
        img = img.resize((150,150))
        img = ImageTk.PhotoImage(img)
        lbl_foto.config(image=img)
        lbl_foto.image = img
    else:
        lbl_foto.config(image="")
        lbl_foto.text = "Sin foto"

# ==========================
# INTERFAZ PRINCIPAL
# ==========================
root = tk.Tk()
root.title("Sistema Contable IA")
root.geometry("700x550")
root.config(bg=COLOR_SECUNDARIO)
root.resizable(False, False)

inicializar_excel()

# ==========================
# ENCABEZADO
# ==========================
header = tk.Frame(root, bg=COLOR_PRINCIPAL, height=80)
header.pack(fill="x")

lbl_titulo = tk.Label(header,
                      text="🧾SISTEMA CONTABLE IA",
                      bg=COLOR_PRINCIPAL,
                      fg="white",
                      font=("Arial", 24, "bold"))
lbl_titulo.pack(pady=20)

# ==========================
# CONTENEDOR
# ==========================
frame = tk.Frame(root, bg=COLOR_SECUNDARIO)
frame.pack(pady=20)

# ==========================
# FORMULARIO
# ==========================
tk.Label(frame, text="ID Empleado", bg=COLOR_SECUNDARIO,
         font=("Arial",12)).grid(row=0, column=0, pady=5, sticky="e")
entry_id = ttk.Entry(frame, width=25)
entry_id.grid(row=0, column=1, pady=5)


tk.Label(frame, text="Mes", bg=COLOR_SECUNDARIO,
         font=("Arial",12)).grid(row=1, column=0, pady=5, sticky="e")
entry_mes = ttk.Entry(frame, width=25)
entry_mes.grid(row=1, column=1, pady=5)


tk.Label(frame, text="Año", bg=COLOR_SECUNDARIO,
         font=("Arial",12)).grid(row=2, column=0, pady=5, sticky="e")
entry_anio = ttk.Entry(frame, width=25)
entry_anio.grid(row=2, column=1, pady=5)

# ==========================
# BOTONES
# ==========================

def limpiar():
    entry_id.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    lbl_nombre.config(text="Empleado:")
    lbl_dias.config(text="Días asistidos:")
    lbl_total.config(text="Total a pagar:")
    lbl_foto.config(image="")
    lbl_foto.image = None

btn = tk.Button(frame,
                text="🔍 Consultar Empleado",
                bg=COLOR_PRINCIPAL,
                fg="white",
                font=("Arial",12,"bold"),
                width=25,
                command=consultar)
btn.grid(row=3, column=0, columnspan=2, pady=10)

btn_limpiar = tk.Button(frame,
                        text="🧹 Limpiar",
                        bg="#4CAF50",
                        fg="white",
                        font=("Arial",11,"bold"),
                        width=25,
                        command=limpiar)
btn_limpiar.grid(row=4, column=0, columnspan=2, pady=10)

# ==========================
# RESULTADOS
# ==========================
resultado = tk.Frame(root, bg="white", bd=2, relief="groove")
resultado.pack(pady=10, padx=30, fill="x")

lbl_nombre = tk.Label(resultado, text="Empleado:", bg="white",
                      font=("Arial",12,"bold"))
lbl_nombre.pack(pady=5)

lbl_dias = tk.Label(resultado, text="Días asistidos:", bg="white",
                    font=("Arial",12))
lbl_dias.pack(pady=5)

lbl_total = tk.Label(resultado, text="Total a pagar:", bg="white",
                     font=("Arial",12))
lbl_total.pack(pady=5)

lbl_foto = tk.Label(resultado, bg="white")
lbl_foto.pack(pady=10)

# ==========================
# FOOTER
# ==========================
footer = tk.Label(
    root,
    text="COPYRIGHT © 2026 - Presentado para el BOOTCAMP DE IA\n"
         "Ana Rodriguez / Isabel Alzate / Jaime Alzate /\n"
         "Juan Fernando Díaz / Juan David Alvarez",
    bg=COLOR_PRINCIPAL,
    fg="white",
    font=("Arial",9),
    justify="center",
    wraplength=650
)

footer.pack(side="bottom", fill="x", pady=5)

# ==========================
# EJECUTAR
# ==========================
root.mainloop()
