##from tips_python import tips
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
##Crear la función principal
def toggle_fullscreen(event=None):
    estado_fullscreen = second_window.attributes('-fullscreen')
    second_window.attributes('-fullscreen', not estado_fullscreen)

def mostrar_dropdown_y_cuadro_texto():
    def agregar_tip():
        nonlocal nombre_archivo, diccionario_cargado, dropdown_menu
        def salir():
            nonlocal dropdown_menu, contenido, nombre_archivo, diccionario_cargado
            
            titulo_text = titulo_var.get()
            print(titulo_text)
            contenido_text = contenido.get("1.0","end-1c")
            print(nombre_archivo)
##            diccionario_cargado[titulo_text] = contenido_text
            with open(nombre_archivo, 'r') as archivo:
                diccionario_cargado = json.load(archivo)
            diccionario_cargado[titulo_text] = contenido_text
            with open(nombre_archivo, 'w') as archivo:
                json.dump(diccionario_cargado, archivo)
            with open(nombre_archivo, 'r') as archivo:
                diccionario_cargado = json.load(archivo)
            dropdown_menu['values'] = list(diccionario_cargado.keys())
            new_tip_window.destroy()
        new_tip_window = tk.Toplevel(ventana)
        titulo_y_contenido = tk.LabelFrame(new_tip_window,text="Titulo del tip y contenido")
        titulo_y_contenido.pack()
        titulo_var = tk.StringVar()
    # Establecer un valor predeterminado inicial
        titulo_entry = tk.Entry(titulo_y_contenido,textvariable=titulo_var,font=("Helvetica",15))
        titulo_entry.pack()
        contenido = tk.Text(titulo_y_contenido)
        contenido.pack()
        salir_btn = tk.Button(titulo_y_contenido,text="agregar",command=salir)
        salir_btn.pack()
        
    def mostrar_valor_seleccionado(event):
        # Obtener la clave seleccionada
        clave_seleccionada = dropdown_var.get()

        # Obtener el valor correspondiente a la clave
        valor_correspondiente = diccionario_cargado.get(clave_seleccionada, "Valor no encontrado")

        # Actualizar el cuadro de texto con el valor correspondiente
        cuadro_texto.config(state=tk.NORMAL)
        cuadro_texto.delete(1.0, tk.END)
        cuadro_texto.insert(tk.END, valor_correspondiente)
        
        cuadro_texto.tag_configure('text_color', foreground='white')
        cuadro_texto.tag_add('text_color', '1.0', 'end')
        cuadro_texto.config(state=tk.DISABLED)

    # Nombre del archivo donde se guardará el diccionario JSON
    nombre_archivo = 'tips.json'

    # "ABRIRLO" 1) LEERLO
    with open(nombre_archivo, 'r') as archivo:
        diccionario_cargado = json.load(archivo)
    print(diccionario_cargado)
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Python code Tips and templates by Fernando López Vázquez")
    ventana.attributes('-fullscreen', False)
    ventana.bind('<F11>', toggle_fullscreen)
    # Variables Tkinter
    dropdown_var = tk.StringVar()
    add_tip = tk.Button(ventana,text="Agregar Tip",command=agregar_tip)
    add_tip.pack()
    # Crear DropdownMenu con las claves del diccionario
    print(type(diccionario_cargado))
    dropdown_menu = ttk.Combobox(ventana, textvariable=dropdown_var, values=list(diccionario_cargado.keys()),width=150)
    dropdown_menu.bind("<<ComboboxSelected>>", mostrar_valor_seleccionado)
    dropdown_menu.pack(pady=10)

    # Crear Cuadro de Texto para mostrar el valor correspondiente
    cuadro_texto = tk.scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=200, height=80)
    cuadro_texto.configure(bg="#002240")
    # Empaquetar el widget Text
    cuadro_texto.pack(padx=10, pady=10)
    # Crear un widget Scrollbar
    scrollbar = tk.Scrollbar(ventana, command=cuadro_texto.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar la conexión entre el Text y el Scrollbar
    cuadro_texto.config(yscrollcommand=scrollbar.set)

    # Iniciar el bucle principal
    ventana.mainloop()



# Nombre del archivo donde se guardará el diccionario JSON
nombre_archivo = 'tips.json'

### "ABRIRLO" 1) LEERLO
##with open(nombre_archivo, 'r') as archivo:
##    diccionario_cargado = json.load(archivo)    

# 2) USARLO
# Llamar a la función principal con el diccionario
mostrar_dropdown_y_cuadro_texto()

### 3) ESCRIBIRLO
### Guardar el diccionario en el archivo JSON
##with open(nombre_archivo, 'w') as archivo:
##    json.dump(tips, archivo)
##
##print(f"El diccionario se ha guardado en '{nombre_archivo}'.")
