# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
#CAMBIOS  filedialog, messagebox
from tkinter import messagebox, filedialog
from controller import procesar_instruccion
#PUSE ESTE proceso
from processor import process_excel_safe

def seleccionar_excel():
    return filedialog.askopenfilename(
    title="Seleccionar archivo Excel",
    filetypes=[("Archivo Excel","*.xlsx")]
    )

def on_clic_procesar():
    archivo = seleccionar_excel()
    messagebox.showinfo("Archivo seleccionado", archivo)


def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    boton = tk.Button(
        root,
        text="seleccionar archivo excel",
        command=on_clic_procesar,
        width=30,
        height=2
    )
    boton.pack(pady=60)

    # Etiqueta2
   #tk.Label(root, text=archivo).pack(pady=10)

    # Etiqueta
    tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    # Acción del botón
    def ejecutar():
        texto = entrada.get()
        ruta=seleccionar_excel()
        exito, mensaje = procesar_instruccion(texto, ruta)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)


    # Botón
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)

    root.mainloop()
