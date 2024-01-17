#tips python
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


tips = {
    "tkinter - treeview":##### 1
'''
    # -------------------------------------------------------------------------- TREEVIEW -------------------------------------------------
    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(data_n_tree)
    treeFrame.grid(row=0, column=1)

    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3, 4), height=12)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)

    # Treeview columns
    treeview.column("#0", width=100)
    treeview.column(1, anchor="w", width=100)
    treeview.column(2, anchor="w", width=100)
    treeview.column(3, anchor="w", width=100)
    treeview.column(4, anchor="w", width=100)

    # Treeview headings
    treeview.heading("#0", text="Nombre", anchor="center")
    treeview.heading(1, text="Descripcion", anchor="center")
    treeview.heading(2, text="Pictogramas", anchor="center")
    treeview.heading(3, text="Indicacion", anchor="center")
    treeview.heading(4, text="revision", anchor="center")
''',
    "tkinter - Combobox":### 2
    '''# --COMBOBOX------------------------------------------------OPCION 3-----------------------------------------------------------------------------------------
    ############# Option 3 content                                                                      # BANNER
    option_frames[lista_opciones[2]] = tk.Frame(d3)
    banners_var = tk.StringVar()
    # OPCIONES DE LOS BANNERS
    lista_banners = ['b1 BANNER DE PREPARACION ',
                     'b2 BANNER DE EPP',
                     'b3 BANNER DE PESE, CALCULE, ANOTE, AÑADA, TIRE',
                     'b4 BANNER DE MEZCLAR EN 4 PARTES',
                     'b5 BANNER DE advert. de explosion',
                     'b6 ADVERTENCIA DEL TDI',
                     'b7 CONSIDERACIONES BÁSICAS ANTES DE EMPEZAR EL PROCESO',
                     'b8 MANTENGA LIMPIO SU REACTOR',
                     'b9 PASE MUESTRA A CALIDAD'
                     ]
    tk.Label(option_frames[lista_opciones[2]], text="Agregar Banner").grid(row=row, column=0)# ETIQUETA 
    banner_combo = ttk.Combobox(option_frames[lista_opciones[2]], textvariable=banners_var, values=lista_banners)# MENU COMBOBOX
    banner_combo.current(0)
    banner_combo.grid(row=row, column=1)''',
    "tkinter - boton":##### 3
    '''
    # Funcion para que el boton sea activado presionando ENTER
    def on_enter(event):
        event.widget.invoke()  # Simular clic en el botón al presionar Enter
    # --BOTONES: -----------------------------------------------------------------------------------------------------------------
    br = tk.Button(d5,text="Reactivo",command=agregar_r,bg=colores[1], state=tk.DISABLED)
    br.grid(row=0, column=0)
    br.bind("<Return>", on_enter)''',
    "tkinter - Entry":##### 4
    '''
    # ENTRY        
    # Crear una variable de tipo StringVar
    presion_var = tk.StringVar()
    # Establecer un valor predeterminado inicial
    presion_var.set("1")
    presion_entry = tk.Entry(d2,textvariable=presion_var,font=("Helvetica",15))
    presion_entry.grid(row=0, column=0)
''',
    "tkinter - grafica Matplotlib":#### 5
    '''import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    # Crear datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 7, 5]

    subgrafico.plot(x, y, label='Datos de ejemplo')
    lienzo.draw()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gráfico en Tkinter")

# Botón para graficar
boton_graficar = ttk.Button(ventana, text="Graficar", command=graficar)
boton_graficar.pack(pady=10)

# Crear la figura de Matplotlib
figura = Figure(figsize=(5, 4), dpi=100)
subgrafico = figura.add_subplot(1, 1, 1)

subgrafico.set_title('Gráfico de Ejemplo')
subgrafico.set_xlabel('Eje X')
subgrafico.set_ylabel('Eje Y')
subgrafico.legend("Soy una leyenda")

# Crear el lienzo de Tkinter
lienzo = FigureCanvasTkAgg(figura, master=ventana)


# Empaquetar el lienzo en la ventana
lienzo.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Iniciar el bucle principal
ventana.mainloop()
''',
    "tkinter - diccionario(key:value) key en combobox y values en texto":#### 6
    '''# Crear la función principal
def mostrar_dropdown_y_cuadro_texto(diccionario):
    def mostrar_valor_seleccionado(event):
        # Obtener la clave seleccionada
        clave_seleccionada = dropdown_var.get()

        # Obtener el valor correspondiente a la clave
        valor_correspondiente = diccionario.get(clave_seleccionada, "Valor no encontrado")

        # Actualizar el cuadro de texto con el valor correspondiente
        cuadro_texto.config(state=tk.NORMAL)
        cuadro_texto.delete(1.0, tk.END)
        cuadro_texto.insert(tk.END, valor_correspondiente)
        cuadro_texto.config(state=tk.DISABLED)
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Dropdown y Cuadro de Texto")

    # Variables Tkinter
    dropdown_var = tk.StringVar()

    # Crear DropdownMenu con las claves del diccionario
    dropdown_menu = ttk.Combobox(ventana, textvariable=dropdown_var, values=list(diccionario.keys()),width=150)
    dropdown_menu.bind("<<ComboboxSelected>>", mostrar_valor_seleccionado)
    dropdown_menu.pack(pady=10)

    # Crear Cuadro de Texto para mostrar el valor correspondiente
    cuadro_texto = tk.Text(ventana, height=100, width=300, state=tk.DISABLED)
    cuadro_texto.pack(pady=10)

    # Iniciar el bucle principal
    ventana.mainloop()

tipps = {'pregunta 1':'texto 1',
         'pregunta 2':'texto 2',
         'pregunta 3':'texto 3',
         'pregunta 4':'texto 4',}
# Llamar a la función principal con el diccionario
mostrar_dropdown_y_cuadro_texto(tips)
''',
    "tkinter - Scrollbar a un tk.text":#### 7
    '''
import tkinter as tk
from tkinter import scrolledtext

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Text con Scrollbar")

# Crear un widget Text
texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)

# Crear un widget Scrollbar
scrollbar = tk.Scrollbar(ventana, command=texto.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar la conexión entre el Text y el Scrollbar
texto.config(yscrollcommand=scrollbar.set)

# Agregar texto de ejemplo al Text
texto.insert(tk.END, "Este es un ejemplo de texto largo. " * 10)

# Empaquetar el widget Text
texto.pack(padx=10, pady=10)

# Iniciar el bucle principal
ventana.mainloop()

''',
    "tkinter - Toplevel :multiples ventanas":#### 8
    '''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
import time
# Configurar tecla para alternar fullscreen (por ejemplo, F11)
def toggle_fullscreen(event=None):
    estado_fullscreen = second_window.attributes('-fullscreen')
    second_window.attributes('-fullscreen', not estado_fullscreen)
## Ventana Padre
root = tk.Tk()
root.config(bg="black")
root.title("PETRA: GENERADOR DE METODOS")
root.focus_force()
root.option_add("*tearOff", False) # This is always a good idea
# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=2)
##root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=2)
root.rowconfigure(index=1, weight=1)

def ventana_hija(ventana_padre):
    #FRAMES
    second_window = tk.Toplevel(root,bg="#046546")# 0
    second_window.title("Crear Metodo de Fabricación Estandar")
    # Make the app responsive
    second_window.columnconfigure(index=0, weight=1)
    second_window.columnconfigure(index=1, weight=1)
    second_window.columnconfigure(index=2, weight=1)
    second_window.rowconfigure(index=0, weight=1)
    second_window.rowconfigure(index=1, weight=1)
    second_window.rowconfigure(index=2, weight=1)
    # Hacer que la ventana sea fullscreen desde el inicio
    second_window.attributes('-fullscreen', False)
    second_window.bind('<F11>', toggle_fullscreen)
    second_window.bind('<Escape>', lambda event: second_window.attributes('-fullscreen', False))
    second_window.focus_force()
ventana_hija(root)
''',
    "pyinstaller - Metodo : guardar imagenes":
    '''
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
''',
    "tkinter - LabelFrame":#### 9
    '''
    label = ttk.LabelFrame(datos, text="Crear Metodo de Fabricación Estandar")
    label.grid(row=0, column=0,padx = (10,10),pady=(10,10))
''',
    "tkinter - Checkbuttons":#### 10
    '''
    # CHebuttons menu: EQUIPO A UTILIZAR
    # CODIGO PROVISTO POR CHATGPT-------------------------------------------------------
    chopciones = {}
    chopcion1 = tk.Checkbutton(d4, text="Dispersor",bg=colores[1])
    chopcion2 = tk.Checkbutton(d4, text="Reactor",bg=colores[1])
    chopcion3 = tk.Checkbutton(d4, text="Tina",bg=colores[1])    
    chopcion4 = tk.Checkbutton(d4, text="Tambor de proceso",bg=colores[1])
    # Agregar las casillas de verificación al diccionario y asignarles una variable de control
    chopciones["Dispersor"] = tk.BooleanVar()
    chopciones["Reactor"] = tk.BooleanVar()
    chopciones["Tina"] = tk.BooleanVar()
    chopciones["Tambor de proceso"] = tk.BooleanVar()

    chopcion1.config(variable=chopciones["Dispersor"], command=actualizar_seleccion)
    chopcion2.config(variable=chopciones["Reactor"], command=actualizar_seleccion)
    chopcion3.config(variable=chopciones["Tina"], command=actualizar_seleccion)
    chopcion4.config(variable=chopciones["Tambor de proceso"], command=actualizar_seleccion)
    
    # Colocar las casillas de verificación en la ventana
    chopcion1.grid(row=0,column=0)
    chopcion2.grid(row=0,column=1)
    chopcion3.grid(row=1,column=0)
    chopcion4.grid(row=1,column=1)
''',
    "tkinter - centrar ventana":#### 11
    '''
    # Center the window, and set minsize
    second_window.update()
    second_window.minsize(second_window.winfo_width(), second_window.winfo_height())
    x_cordinate = int((second_window.winfo_screenwidth()/2) - (second_window.winfo_width()/2))
    y_cordinate = int((second_window.winfo_screenheight()/2) - (second_window.winfo_height()/2))
    second_window.geometry("+{}+{}".format(x_cordinate, y_cordinate))''',
    "tkinter - sizegrip":#### 12
    '''
    # Sizegrip
    sizegrip = ttk.Sizegrip(second_window)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))''',
    "tkinter - inhabilitar widgets":#### 13
    '''def disable_all():# Func-20
        # Blocking widgets
        mallaopcion1.config(state=tk.DISABLED)
        chopcion1.config(state=tk.DISABLED)
        chopcion2.config(state=tk.DISABLED)
        chopcion3.config(state=tk.DISABLED)    
        chopcion4.config(state=tk.DISABLED)
        name_prod_entry.config(state=tk.DISABLED)
        no_prod_entry.config(state=tk.DISABLED)
        picto_prod_entry.config(state=tk.DISABLED)
        etiq_prod_entry.config(state=tk.DISABLED)
        mues_prod_entry.config(state=tk.DISABLED)
        caracmalla_entry.config(state=tk.DISABLED)''',
    "CSV - extraer informacion de file.csv":#### 14
    '''
    # ------.CSV_FILES-----------------------------------------------------------------------------
    # Lista para almacenar los datos
    datos_eq_ant = []
    nombres = []
    archivo_csv = 'antoine.csv'

    # Abrir el archivo CSV y leer su contenido
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
        # Crear un lector CSV
        lector = csv.DictReader(archivo)

        # Iterar sobre las filas del archivo y agregar a la lista
        for fila in lector:
            nombres.append(fila['Compound Name'])
            datos_eq_ant.append(dict(fila))
    print(nombres)
''',
    "python - escribir un archivo python":#### 15
    '''
    with open('mirror.py', 'w', encoding='utf-8') as archivo:
    # Escribir contenido en el archivo
    archivo.write('Aqui va la Documentación')
''',
    "filedialog - cuadro de diálogo para seleccionar archivo":#### 16
    '''
        def seleccionar_archivo():
    # Mostrar el cuadro de diálogo para seleccionar archivo
    archivo = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    # Imprimir la ruta del archivo seleccionado
    print("Archivo seleccionado:", archivo)
''',
    "dict - como agregar un elemento a un diccionario":#### 17
    '''
    # Crear un programa sobre un treeview
    Programa = {'root': {
        "propiedades":{
            "titulo":"Taller de Fernando",
            "color":"#ffffff",
            "active":True
            },
        "Frame 1":{
            "propiedades":{
                "padre":"root",
                "row":0,
                "column":0,
                "color":"#000000"
                },
            "Frame 1.1":{
                "propiedades":{
                    "padre":"root",
                    "row":0,
                    "column":0,
                    "color":"#000000"
                    }
                }
            }
        }
    }
    print(Programa)
    Programa['root']["Frame 1"]["Frame 1.2"] = {
                "propiedades":{
                    "padre":"root",
                    "row":0,
                    "column":0,
                    "color":"#000000"
                    }}
''',
    "tkinter - treeview, method: dict to treeview":#### 18
    '''def mostrar_dicc(tree, diccionario, parent=""):# args: (treeview object, dict, (optional) parent)
        for key, value in diccionario.items():
            if isinstance(value, dict):
                # Si el valor es un diccionario, recurrir de forma recursiva
                nuevo_parent = tree.insert(parent, 'end', text=str(key), open=True)
##                print(f' Nuevo parent es : {nuevo_parent}')
                mostrar_dicc(tree, value, parent=nuevo_parent)
            else:
                # Si el valor no es un diccionario, agregarlo como un elemento
                tree.insert(parent, 'end', text=str(key), values=(str(value)))''',
    "subprocess - open a program using python":#### 19
        '''
import subprocess

# Replace 'your_script.py' with the actual path to your Python file
python_file_path = 'C:/Users/Fer/AppData/Local/Programs/Python/Python310/los_codigos/Taller de fernando/Proyecto_1/dicctotree.py'

try:
    # Run IDLE with the specified Python file
    subprocess.run(['python', python_file_path])#, python_file_path
except FileNotFoundError:
    print("Error: IDLE not found. Make sure it is installed and in your system's PATH.")
except subprocess.CalledProcessError as e:
    print(f"Error: Failed to open '{python_file_path}' with IDLE. Return code: {e.returncode}")

''',
    "tkinter - button Metodo : btn changes to list when pressed":#### 20
    '''def cambiar_widget():
    # Ocultar el botón
    boton_mas.pack_forget()

    # Crear y mostrar el ListBox
    lista.pack(pady=10)

def mostrar_seleccion():
    # Obtener la selección del ListBox
    seleccion = lista.get(tk.ACTIVE)

    # Ocultar el ListBox
    lista.pack_forget()

    # Crear y mostrar el Label con la selección
    label_seleccion.config(text=f"Seleccionado: {seleccion}")
    label_seleccion.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Cambio de Widgets")

# Crear el botón de "+" y asociarle la función cambiar_widget
boton_mas = tk.Button(ventana, text="+", command=cambiar_widget)
boton_mas.pack(pady=10)

# Crear el ListBox y asociarle algunos elementos
elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]
lista = tk.Listbox(ventana, selectmode=tk.SINGLE)
for elemento in elementos:
    lista.insert(tk.END, elemento)

# Crear el Label que mostrará la selección y ocultarlo inicialmente
label_seleccion = tk.Label(ventana, text="")
label_seleccion.pack_forget()

# Configurar la función mostrar_seleccion para ser llamada cuando se seleccione un elemento en el ListBox
lista.bind('<<ListboxSelect>>', lambda event: mostrar_seleccion())''',
    "tkinter - list, metodo : autocompletar":#### 21
    '''def autocompletar(event):
    entrada_texto = entry.get().lower()
    sugerencias = [item for item in lista_palabras if entrada_texto in item.lower()]

    mostrar_sugerencias(sugerencias)

def mostrar_sugerencias(sugerencias):
    if sugerencias:
        lista_sugerencias.delete(0, tk.END)
        for sugerencia in sugerencias:
            lista_sugerencias.insert(tk.END, sugerencia)
        lista_sugerencias.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height())
    else:
        lista_sugerencias.place_forget()

def seleccionar_sugerencia(event):
    entry.delete(0, tk.END)
    entry.insert(0, lista_sugerencias.get(tk.ACTIVE))
    lista_sugerencias.place_forget()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Autocompletado con Entry")

# Lista de palabras para autocompletar
lista_palabras = ["manzana", "banana", "kiwi", "mango", "pera", "uva", "sandía", "papaya"]

# Crear el Entry
entry = tk.Entry(ventana)
entry.pack(pady=10)

# Crear la lista desplegable de sugerencias
lista_sugerencias = tk.Listbox(ventana)
lista_sugerencias.place_forget()

# Asociar eventos
entry.bind('<KeyRelease>', autocompletar)
lista_sugerencias.bind('<ButtonRelease-1>', seleccionar_sugerencia)''',
    "json - insertar dict en archivo json":#### 21
    '''
import json

# Tu diccionario
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}

# Nombre del archivo donde se guardará el diccionario JSON
nombre_archivo = 'mi_archivo.json'

# Guardar el diccionario en el archivo JSON
with open(nombre_archivo, 'w') as archivo:
    json.dump(mi_diccionario, archivo)

print(f"El diccionario se ha guardado en '{nombre_archivo}'.")
''',
    "json - cargar dict de json":#### 22
    '''
import json

# Nombre del archivo JSON
nombre_archivo = 'mi_archivo.json'

# Cargar el diccionario desde el archivo JSON
with open(nombre_archivo, 'r') as archivo:
    diccionario_cargado = json.load(archivo)

print("Diccionario cargado:")
print(diccionario_cargado)

''',
    "tkinter - treeview, method : actualizar treeview desde archivo json":#### 23
'''
def actualizar():
    def mostrar_dicc(tree, diccionario, parent=""):# args: (treeview object, dict, (optional) parent)
        for key, value in diccionario.items():
            if isinstance(value, dict):
                # Si el valor es un diccionario, recurrir de forma recursiva
                nuevo_parent = tree.insert(parent, 'end', text=str(key), open=True)
        ##                print(f' Nuevo parent es : {nuevo_parent}')
                mostrar_dicc(tree, value, parent=nuevo_parent)
            else:
                # Si el valor no es un diccionario, agregarlo como un elemento
                tree.insert(parent, 'end', text=str(key), values=(str(value)))
    with open('datos.json', 'r') as archivo:# extraer la info previa
        treeview_datan.clear()
        treeview_datan.update(json.load(archivo))
    for item in treeview.get_children():# eliminar todos los elementos del treeview
        treeview.delete(item)
    mostrar_dicc(treeview,treeview_datan)

''',
    "dict.items() - key value returned as tuple ('KEY', 'VALUE')":####24
    '''
# para una Lista de tk.booleanVar()
# Paso4) creamos una lista
seleccion = []
# Paso 5) iteramos a traves de un diccionario
for opcion, valor in chopciones.items():
    if valor.get():
        seleccion.append(opcion)
''',
    "pygame - plantilla con un jugador":#### 25
    '''
import pygame, sys
import numpy as np
import math
from controls import Controls
# Initialize the pygame
pygame.init()
#Create the screen
HEIGHT, WIDTH = 600,600
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
#Create the clock
clock = pygame.time.Clock()
 # variables
segundero = 0
 # [X, Y]
cur_vel = [0, 0]
cur = [100,100]
# Funciones de dibujo
def dot(xi,yi,r):
    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
def line(xi,yi,xf,yf):
    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
def rect(xi,yi,w,h):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
def text(string,xi,yi):
    textsurface = font.render(string,False,(10,100,100))
    screen.blit(textsurface,(xi,yi))
def panel(xi,yi,string):
    w,h = 250,40
    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
    textsurface = font.render(string,False,(255,255,255))
    screen.blit(textsurface,(xi,yi))
def cursor(xi,yi):
    ri,re = 10,12
    pygame.draw.circle(screen,(0,0,0),(xi,yi),re)
    pygame.draw.circle(screen,(255,255,255),(xi,yi),ri)
def vaso(xi,yi,w,h,e):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
    pygame.draw.rect(screen,(0,0,0),(xi+e,yi,w-2*e,h-e))
    
while True:
    tiempo = pygame.time.get_ticks()
    # LOS CONTROLES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # EL ORDEN DE ESTOS DOW SI IMPORTA
            pygame.quit()
            sys.exit()
            
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel[1] = -10
            if event.key == pygame.K_a:
                cur_vel[0] = -10
            if event.key == pygame.K_x:
                pass
            if event.key == pygame.K_d:
                cur_vel[0] = 10
            if event.key == pygame.K_s:
                cur_vel[1] = 10
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel[1] = 0
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_vel[0] = 0
            if event.key == pygame.K_s:
                cur_vel[1] = 0
            if event.key == pygame.K_d:
                cur_vel[0] = 0
            if event.key == pygame.K_f:
                pass
    # A partir de aqui dibujas
    screen.fill((0,0,0))
    #cursor
    cur[0] += cur_vel[0]
    cur[1] += cur_vel[1]
    vaso(cur[0],cur[1],100,100,10)
    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)

''',
    "pygame - mousebuttondown controls":#### 26
    '''
import pygame
pygame.init()

SCREEN = pygame.display.set_mode((420, 720))
pygame.display.set_caption("Ubicacion de los clicks del mouse")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mouse button
                print("left mouse button")
            elif event.button == 2:# middle mouse button
                print("middle mouse button")
            elif event.button == 3:# right mouse button
                print("right mouse button")
            elif event.button == 4:# mouse wheel up
                print("mouse wheel up")
            elif event.button == 5:# mouse wheel down
                print("mouse wheel down")

''',
    "numpy - array(), zeros() & matrix()":#### 27
    '''
import numpy as np

PMlist_R2 = np.array([45.5, 71, 86, 31.5])
conversion_line =  np.zeros((len(coefficients)))
projection_matrix = np.matrix([
            [1,0,0],
            [0,1,0]])
''',
    "pygame - projection & rotation class":#### 28
    '''
import pygame, sys
import numpy as np
from math import *
class Tridi_drawing:
    @staticmethod
    def projection(points,scale,cubepos,rotations,screen,color_pointa,showpoints,feature):
    # Recibe una lista de puntos 3d y devuelve una lista de listas
    # que en realidad son las coordenadas de donde esta el punto
    # 3d pero en el espacio 2d
    # f(Lista de puntos Puntos 3D) = lista de puntos 2d proyectados sobre screen
    # none #0
    # star 'star'
        projection_matrix = np.matrix([
            [1,0,0],
            [0,1,0]])
        black = (0,0,0)
        i = 0
        projected_points = [[n,n] for n in range(len(points))]
        for point in points:
            rotated2d = np.dot(rotations[2], point.reshape((3,1)))
            rotated2d = np.dot(rotations[1], rotated2d)
            rotated2d = np.dot(rotations[0], rotated2d)
            
            projected2d = np.dot(projection_matrix, rotated2d)
            
            x = int(projected2d[0][0] * scale) + cubepos[0]
            y = int(projected2d[1][0] * scale) + cubepos[1]

            projected_points[i] = [x,y]
            if showpoints:
                pygame.draw.circle(screen, "Black", (x,y), 5)
    ##            if i== 0:
    ##                pygame.draw.circle(screen, color_pointa, (x,y), 5)
            if feature == 'star':# only when we have a star structure
                pygame.draw.circle(screen, color_pointa, (x,y), 5)
                pygame.draw.line(screen,color_pointa,(cubepos[0],cubepos[1]),(x,y))
            i += 1
        return projected_points

    @staticmethod
    def rotation(anglex,angley,anglez):#
    # Recibe 3 valores llamados angulos y devuelve 3 matrices
    #que representan el movimiento de rotacion en tal direccion
        rotation_z = np.matrix([
            [cos(anglez),-sin(anglez),0],
            [sin(anglez),cos(anglez),0],
            [0,0,1]
            ])

        rotation_y = np.matrix([
            [cos(angley),0,sin(angley)],
            [0,1,0],
            [-sin(angley),0,cos(angley),]
            ])

        rotation_x = np.matrix([
            [1,0,0],
            [0,cos(anglex),-sin(anglex)],
            [0,sin(anglex),cos(anglex)]
            ])
        return rotation_x, rotation_y, rotation_z
''',
    "Set() - .union(),.list()":#### 29
    '''R1 = [['A','B','C','D'],['1','1','1','1'],['R','R','P','P']]# 2d LISTS
R2 = [['C','B','E','D'],['1','1','1','1'],['R','R','P','P']]

set1 = set(R1[0][:])
set2 = set(R2[0][:])
set3 = set1.union(set2)
RT = list(set3)
RT = sorted(RT)
''',
    "pygame - flujo method":#### 30
    '''def flujo(A,B,mass,segundero):
    chunks = 100
    dx = (B[0]-A[0])/chunks
    dy = (B[1]-A[1])/chunks
    listpositions = np.ones((chunks+1,2))
    for it in range(chunks+1):
        listpositions[it,0] = A[0] + it*dx
        listpositions[it,1] = A[1] + it*dy
    for i in range(chunks):
        f = int((255*math.sin(0.2*i-segundero)**2))
        # por que 255*math.sin()**2?
        #   como sin()**2 tiene un rango entre 0 y 1, al multriplicarlo por un
        #   numero n da una variacion entre cero y ese numero n
        # el segundero es lo que actua como un desfasador lo que hace que se mueva en un sentido
        pygame.draw.line(screen,(0,f,f),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))
''',
    "smtplib - send an Email":#### 31
    '''
import smtplib

# Set up the email message
sender_email = "escherichiacoli.enteroinvasiva@gmail.com"
receiver_email = "politropic123@gmail.com"
subject = "Correo de prueba"
body = "CUerpo de prueba"

message = f"Subject: {subject}\n\n{body}"

# Set up the SMTP server connection
smtp_server = "smtp.example.com"
smtp_port = 25  # Replace with the appropriate port for your server
smtp_username = "your_email@example.com"
smtp_password = "your_email_password"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message)
''',
    "random - randint":#### 32
    '''import random
conceptos = {1: 'caja',
             2: 'clientes',
             3: 'deudores diversos',
             4: 'documentos por cobrar',
             5: 'mobiliario'}
for i in range(10):
    print(conceptos[random.randint(1,5)])
''',
    "PyQt5 - plantilla basica":#### 33
    '''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainApp(QMainWindow):
    def __init__(self, parent=None,*args):
        super(MainApp, self).__init__(parent=parent)

##        self.setMinimumSize(500,300)
##        self.setMaximumSize(700,500)
        self.setFixedSize(500,300)
        self.setWindowTitle("Primera App")

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        label = QLabel("Primer Label", self)
##        label.setGeometry(0,0,width,height)
        label.setStyleSheet("background:#424242;, color:#fff")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
''',
    "pygame - button class":#### 34
    '''class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                    self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
            if self.image is not None:
                    screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                    return True
            return False

    def changecolor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")
            
button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (200, 75))

button = Button(button_surface, 200, 200, "Click me!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkforinput(pygame.mouse.get_pos())

    screen.fill(("black"))

    button.update()
    button.changecolor(pygame.mouse.get_pos())
    segundero = segundero + 1
    pygame.display.update()
''',
    "pygame - pendulo player movement method":#### 35
    '''import pygame, sys
import numpy as np
import math
HEIGHT, WIDTH = 400,400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()

centropendulo = np.array([200,50])
tb = 200
side = 0
speedr = 0
speedt = 0

while True:

    for event in pygame.event.get():
        
        #print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speedr = -5
            if event.key == pygame.K_s:
                speedr =5
            if event.key == pygame.K_a:
                speedt = -math.pi/100
            if event.key == pygame.K_d:
                speedt = math.pi/100
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speedr = 0
            if event.key == pygame.K_s:
                speedr = 0
            if event.key == pygame.K_a:
                speedt = 0
            if event.key == pygame.K_d:
                speedt =o 0


    screen.fill((0,0,0))
    tb = tb + speedr
    side = side +speedt
    playerposition = np.array([(tb*math.cos(-side + math.pi/2)),(tb*math.sin(-side+math.pi/2))])+centropendulo
    pygame.draw.line(screen,(255,0,0),centropendulo,playerposition)

# A partir de aqui terminas
    pygame.display.update()
    clock.tick(30)
''',
    "math - sine & cosine examples":#### 36
    '''import math
segundero = 100
a = math.cos(segundero)
b = math.sin(segundero)
''',
    "pygame - Mac_sprites original code":#### 37
    '''import pygame
import numpy as np
from math import *
from ysort import Camera_group

projection_matrix = np.matrix([
    [1,0,0],
    [0,1,0]])
class Sendtransformedcoordinates():
    def __init__(self):
        self.memory = []
    def add(self,point):
        self.memory.append(point)
    def returnback(self):
        return self.memory
    def clear(self):
        self.memory = []

conexion = Sendtransformedcoordinates()

# ---------------------------------------------------------------        
##XXXX COPY THIS TO IMPORT THE FUNCTION OF ADDING SEVERAL IMAGES
#-----------------------------------------------------------------
# titlespos is  the collections of all 3d positions
# who_list is the collection of all the names of each position
# Creas un sprite group recuerdalo
def addimages(group,titlespos,who_list,scale,cubepos,rotation_x, rotation_y, rotation_z):# FUNCION TIPO CREATE
##    images = pygame.sprite.Group()# hERE IT CREATES THE SPRITE
    machines = []
    conexion.clear()
    for i,j in enumerate(titlespos):# TRANSFORMS THE  3D COORDINATE VECTOR INTO 2D PROJECTED VECTOR
        title2d = np.dot(rotation_z, titlespos[i].reshape((3,1)))
        title2d = np.dot(rotation_y, title2d)
        title2d = np.dot(rotation_x, title2d)
        
        conexion.add(title2d)
        title = np.dot(projection_matrix, title2d)
        x = int(title[0][0] * scale) + cubepos[0]
        y = int(title[1][0] * scale) + cubepos[1]
        
        machines.append(Machines(group,x,y,who_list[i],scale,i,title2d))# THEN WE FINALLY ADD TO THE SPRITE GROUP OBJECT CALLED images
        # A CLASS OBJECT FROM Mac CLASS, SO NOW THE OBJECT WITH THE POSITION, THE IMAGE  THE SCALE AND ITS ID ARE LOADED INTO THE SPRITE GROUP OBJECT
        # SO NOW, EVERY MAC OBJECTT STORED IN IMAGES CAN BE DISPLAYED ONTO THE SCREEN
    return machines

# HOT NEW
class Machines(pygame.sprite.Sprite):
    def __init__(self,group,xpos,ypos,who,scale,id,title2d):
        super().__init__(group)
        self.who = who# who is a number string, always it most be a string
        # bc off the line of code below, it references to the name of the image
        # you want to use
        if self.who == "None":
            self.image = pygame.image.load("images/button.png").convert_alpha()
        else:
            self.image = pygame.image.load("images/"+self.who+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale,scale))
        if self.who == "11":
            self.image = pygame.transform.scale(self.image,(2*scale,scale))
        self.rect =self.image.get_rect(center =(xpos, ypos))
        self.direction = pygame.math.Vector2()
        self.direction.y = ypos
        self.direction.x = xpos
        self.transformx = title2d[0]
        self.transformy = title2d[1]
        self.transformz = title2d[2]
        self.id = id# adds an ID variable
#--------------------------------------------------------------------------------------

class Mac(pygame.sprite.Sprite):# Clase hija
    def __init__(self,xpos,ypos,who,scale,id):# asks this for a x annd y position and a reference
        super(Mac, self).__init__()
        self.who = who# who is a number string, always it most be a string
        # bc off the line of code below, it references to the name of the image
        # you want to use
        if self.who == "None":
            self.image = pygame.image.load("images/button.png").convert_alpha()
        else:
            self.image = pygame.image.load("images/"+self.who+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale,scale))
        if self.who == "11":
            self.image = pygame.transform.scale(self.image,(2*scale,scale))
        # the height and width of a given image
        self.rect = self.image.get_rect(center=(xpos, ypos))# this is the cntral position of the image
        self.id = id# adds an ID variable

''',
    "collections - Counter (list to dict, frequency)":#### 38
    '''
import re
from collections import Counter
a = ['hola','laho','lada','folala','hola','laho','folala','folala']
a_counted = Counter(a)
print(a_counted)
a_sd = set(a)
print(a_sd)
a_sdl = list(a_sd)
for i,j in enumerate(a_sdl):
    x = len(re.findall('la',j))
    print(x)

''',
    "re - findall()":#### 39
    '''#re.findall() returns a list of the string asked to be found, if the
# str is found 3 times, te.findall will return
# ['askedword','askedword','askedword']
import re
from collections import Counter
a = ['hola','laho','lada','folala','hola','laho','folala','folala']
a_counted = Counter(a)
print(a_counted)
a_sd = set(a)
print(a_sd)
a_sdl = list(a_sd)
for i,j in enumerate(a_sdl):
    x = len(re.findall('la',j))
    print(x)

''',
    "open() - opening .txt ":#### 40
    '''# Se inicializa el archivo
abrirmuestra = open(f'prueba4.txt','r')
# se usa un metodo llamado read y se transforma a str
muestra = str(abrirmuestra.read())
print(muestra)
''',
    "python - Herencia ¿Como funciona?":#### 41
    '''# herencia

#cuando tienes 2 clases similares, puedes crearlas a partir de una clase superior
# o tambien llamado, parent

#Example

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(F" i AM {self.name} and I am {self.age} years old")

    def speak(self):
        print('This is a message from the parent class')


class Cat (Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        
    def speak(self):
        print("Meow")

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and i am {self.color}')
    
class Dog(Pet):
    def speak(self):
##        print("Bark")
        pass
p  = Pet("Tim", 19)
p.show()
p.speak()
d = Dog('snow',10)
d.show()
d.speak()
c = Cat('Bill',12,'brown')
c.show()
c.speak()
''',
    "dict - using dict to index list":
    '''
m = [[] for i in range(5)]
print(m)
nombres = {'a':1,'b':2,'c':3}


text_document = 'bca'
for i, letra in enumerate(text_document):
    print(m[nombres[letra]])
    m[nombres[letra]].append(letra)

for i,lista in enumerate(m):
    print(i,lista)
print(m)
''',
    "pygame - rect drawed inside a circle using keyboard":#### 42
    '''def rect_in_circle(screen,cur_x,cur_y):
    #first point
    p= np.array([200*math.cos(-cur_x)+200,200*math.sin(-cur_x)+200])
    #second point
    l = np.array([200*math.cos(cur_x)+200,200*math.sin(cur_x)+200])
    #first point
    y = np.array([-200*math.cos(-cur_x)+200,-200*math.sin(-cur_x)+200])
    #second point
    u = np.array([-200*math.cos(cur_x)+200,-200*math.sin(cur_x)+200])

    rect(y[0],y[1],(p[0]-y[0]),(p[1]-l[1]))
    
    line(p[0],p[1],l[0],l[1])
    line(l[0],l[1],y[0],y[1])
    line(y[0],y[1],u[0],u[1])
    line(u[0],u[1],p[0],p[1])
    
    pygame.draw.circle(screen,(0,100,100),(p),4)
    pygame.draw.circle(screen,(255,100,100),(l),4)
    pygame.draw.circle(screen,(2,100,100),(y),4)
    pygame.draw.circle(screen,(255,100,10),(u),4)
''',
    "pygame - class_projection":#### 43
    '''
import pygame, sys
import numpy as np
from math import *
##from Mac_sprites import Mac

class Draw3d:
    def __init__(self,screen,scale,cubepos):
        self.projection_matrix = np.matrix([
            [1,0,0],
            [0,1,0]])
        self.screen = screen
        self.scale = scale
        self.cubepos = cubepos
         
     
    def projection(self,points,showpoints,feature,color):# Reicbe una lista de
    # puntos 3d y devuelve una lista de listas que en realidad son las coordenadas
    # de donde esta el punto 3d pero proyectado en 2d
    # f(Lista de puntos Puntos 3D) = lista de puntos 2d proyectados sobre screen
        i = 0
        projected_points = [[n,n] for n in range(len(points))]
        for point in points:
            rotated2d = np.dot(self.rotations[2], point.reshape((3,1)))
            rotated2d = np.dot(self.rotations[1], rotated2d)
            rotated2d = np.dot(self.rotations[0], rotated2d)
            
            projected2d = np.dot(self.projection_matrix, rotated2d)
            
            x = int(projected2d[0][0] * self.scale) + self.cubepos[0]
            y = int(projected2d[1][0] * self.scale) + self.cubepos[1]

            projected_points[i] = [x,y]
            if showpoints:
                pygame.draw.circle(self.screen, "Black", (x,y), 5)
            if feature == 'star':
                self.star(color,x,y)
            elif feature == 'no':
                pass
            else:
                self.text(feature,x,y,20,color)
            i += 1
        return projected_points

    def set_rotations(self,rotations):
        self.rotations = rotations

    def star(self,color,x,y):# AQUI YA ESTA STAR
        pygame.draw.circle(self.screen, color, (x,y), 5)
        pygame.draw.line(self.screen,color,(self.cubepos[0],self.cubepos[1]),(x,y))

    def drawtubo(self,tubo,isflowing,segundero,state,showpoints):# FUNCION TTPO DRAW
        extremos = self.projection(tubo,showpoints,'no','no')# los extremos 3D proyectalos en screen 2D 
        pygame.draw.line(self.screen,(200,200,200),(extremos[0][:]),(extremos[1][:]),6)#Tuberia gris (OFF)
        if isflowing:
            self.flujo((extremos[0][:]),(extremos[1][:]),5,segundero,state)# flujo proyectados sobre la tuberia (ON)

    def flatsurface(self,n,planes):# Funcion tipo DRAW
        # "n" : LA MITAD DEL LADO DE UN CUADRADO
        # planes: los puntos 3d que forman la rejilla o el plano 
        m = 2*n+1# EL LADO DEL CUADRADO + 1
        projectedsurfaces = self.projection(planes,False,'no','no')# 3D to proj_2D
        for i in range(int(2*m)):
            pygame.draw.line(self.screen,(0,0,10),(projectedsurfaces[i*2][0],projectedsurfaces[i*2][1]),(projectedsurfaces[2*i+1][0],projectedsurfaces[2*i+1][1]))

    def drawcube(self,points,showpoints):# FUNCION TIPO DRAW
    # Recibe un listado de puntos 3D Y DIBUJA LAS ARISTAS DE LOS VERTICES CONTENIDOS EN LA LISTA DE PUNTOS 3D
    # PROYECTADOS A 2D
        projected_points  = self.projection(points,showpoints,'no','no')# De 3D a "d proyectados en screen
        for i in range(4):# esta funcion dibuja las aristas del cubo
            pygame.draw.line(self.screen,"Black",(projected_points[i][0],projected_points[i][1]),(projected_points[i+4][0],projected_points[i+4][1]))
            pygame.draw.line(self.screen,"Black",(projected_points[i*2][0],projected_points[i*2][1]),(projected_points[i*2+1][0],projected_points[i*2+1][1]))
            if i >= 2:
                q = i+2
                pygame.draw.line(self.screen,"Black",(projected_points[q][0],projected_points[q][1]),(projected_points[q+2][0],projected_points[q+2][1]))
            else:
                pygame.draw.line(self.screen,"Black",(projected_points[i][0],projected_points[i][1]),(projected_points[i+2][0],projected_points[i+2][1]))

    def flujo(self,A,B,mass,segundero,state):# FUNCION TIPO DRAW (X,Y)
        chunks = 50
        dx = (B[0]-A[0])/chunks
        dy = (B[1]-A[1])/chunks
        listpositions = np.ones((chunks+1,2))
        for it in range(chunks+1):
            listpositions[it,0] = A[0] + it*dx
            listpositions[it,1] = A[1] + it*dy
        for i in range(chunks):
            f = int((255*sin(0.7*i+segundero)**2))
            # por que 255*sin()**2?
            #   como sin()**2 tiene un rango entre 0 y 1, al multriplicarlo por un
            #   numero n da una variacion entre cero y ese numero n
            # el segundero es lo que actua como un desfasador lo que hace que se mueva en un sentido
            if state == 'liq':
                pygame.draw.line(self.screen,(0,f,f),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))
            elif state == 'vap':
                pygame.draw.line(self.screen,(f,0,0),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))
            elif state == 'wst':
                v = int(f/2+20)
                pygame.draw.line(self.screen,(v,v,v),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))



#### THE MURDERER SECTION ####
    def draw_the_murder(self,mur_coor):
        projected_points  = self.projection(mur_coor,True,'no','no')

    
    def text(self,string,xi,yi,size,color):# Funcion tipo DRAW
    # ingresas un string recibes un screen.blit
        font = pygame.font.SysFont('Comic Sans MS', size)
        textsurface = font.render(string,False,color)
        text_rect = textsurface.get_rect(center=(xi,yi))
        self.screen.blit(textsurface,text_rect)

    def addimages(self,titlespos,who_list,scale,cubepos,rotation_x, rotation_y, rotation_z):# FUNCION TIPO CREATE
        images = pygame.sprite.Group()# hERE IT CREATES THE SPRITE
        for i,j in enumerate(titlespos):# TRANSFORMS THE  3D COORDINATE VECTOR INTO 2D PROJECTED VECTOR
            rotated2d = np.dot(self.rotations[2], j.reshape((3,1)))
            rotated2d = np.dot(self.rotations[1], rotated2d)
            rotated2d = np.dot(self.rotations[0], rotated2d)
            title = np.dot(projection_matrix, title2d)
            x = int(title[0][0] * scale) + cubepos[0]
            y = int(title[1][0] * scale) + cubepos[1]
            images.add(Mac(x,y,who_list[i],scale,i))# THEN WE FINALLY ADD TO THE SPRITE GROUP OBJECT CALLED images
            # A CLASS OBJECT FROM Mac CLASS, SO NOW THE OBJECT WITH THE POSITION, THE IMAGE  THE SCALE AND ITS ID ARE LOADED INTO THE SPRITE GROUP OBJECT
            # SO NOW, EVERY MAC OBJECTT STORED IN IMAGES CAN BE DISPLAYED ONTO THE SCREEN
        return images

    @staticmethod
    def tubo (A,B):# FUNCION TIPO CREATE
    # funcion que recibe 2 arrays 3D y los guarda en una lista
    # devuelve una losta con los exxtrems en array
        tube = []
        tube.append(np.matrix([A]))
        tube.append(np.matrix([B]))
        return tube

    @staticmethod
    def cubo(centro,l):# FUNCION TIPO CREATE
    # Recibe un punto 3d y devuelve una lsita de puntos 3d indicando cada vertice
    # crea una lista con todos los vertices de un cubo 
        cubox  = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    cubox.append(np.matrix([centro[0]+(-1)**i*l/2,centro[1]+(-1)**j*l/2,centro[2]+(-1)**k*l/2]))

        return cubox
    
    @staticmethod
    def planemaker(n):# FUNCION CREATE LIST , RECIBE UN PARAMETRO Y SOBRE ESE
    # CREA Y DEVUELVE UNA LISTA DE PUNTOS 3D 
        planes = []
        m = 2*n+1# EL LADO DEL CUADRADO + 1
        for i in range(m):# de 0 a Lado del cuadrado
            planes.append(np.matrix([n-i,0,n]))
            planes.append(np.matrix([n-i,0,-n]))
        for i in range(m):
            planes.append(np.matrix([n,0,n-i]))
            planes.append(np.matrix([-n,0,n-i]))
        return planes
    
    @staticmethod
    def starmaker(n):
        star = []
        for i in range(3):
            for j in range(2):
                print(j)
                point = np.zeros((3))
                point[i] = n*(-1**j)
                star.append(point)
        return star
''',
    "pygame - colorfade (cuadrado latiendo) metodo":#### 44
    '''def colorfade(t,xi,yi,w,h):
    ut = math.sin(t/20)**2
    pygame.draw.rect(screen,(25-25*ut,2-2*ut,125-125*ut),(xi,yi,w,h))
# EN en WHILE LOOP
colorfade(segundero,100,100,200,200)
''',
    "pandas - basic dataframe manipulation":#### 45
    '''
import pygame, sys
import numpy as np
import math
import csv
import pandas as pd

# ABRIR EL ARCHIVO .CSV
with open("Concrete_Data_Yeh.csv") as datafile:
    data = pd.read_csv(datafile)

# SE MUESTRA LA INFORMACIÓN
print(data)
# SE MUESTRA EL TAMAÑO DE LOS DATOS
print(f'DATA.SIZE : {data.size}')
# SE MUESTRA LOS ENCABEZADOS DE LA TABLA
print(f'DATA.HEAD : {data.head()}')
# haremos un extractor de columnas

# extraemos 3 variables/ columnas
varnum3 = data[["cement","slag","flyash"]]
col1 = data[["cement"]]
col2 = data[["slag"]]
col = data[["flyash"]]
print("___________________________________")
print(varnum3)
print(type(varnum3))
print("___________________________________")
tabla = varnum3.to_numpy()
col = col.to_numpy()
col1 = col1.to_numpy()
col2 = col2.to_numpy()
print(tabla)

### no modificar
##print(max(col))
##print(min(col))
d = max(col)-min(col)
for i in range(len(col)):
    tabla[i,2] = int((tabla[i,2]/d)*255)
    tabla[i,0] = tabla[i,0] - min(tabla[:,0])
    tabla[i,1] = tabla[i,1] - min(tabla[:,1])
print(tabla)
print("___________________________________")
first = col1[0:(len(col1)-1),:]
second = col1[1:(len(col1)),:]
third = col2[0:(len(col2)-1),:]
fourth = col2[1:(len(col2)),:]
print((first))
print(second)
print(third)
print(fourth)
''',
    "pygame - Sprite count class":#### 46
    '''# Attributes NOTE super important to remember

class Sprite:
    number_of_sprites = 0
    def __init__(self,name):
        self.name = name
        print(f'{self.name}')
        Sprite.number_of_sprites += 1

sprites = [Sprite(f'Sprite{i}') for i in range(10)]
print(Sprite.number_of_sprites)

''',
    "pygame - bg text changes when press a key from de keyboard":#### 47
    '''
# pygame: change color background when clicked a key
zpressed = (0,0,0)}
fontsize = 40
keyspace = np.zeros((6))
keyboard = ['z','x','c','v','b','n']
for i in range(6):
    keyspace[i] = fontsize + i*(fontsize+10)
print(keyspace)
def button(string,xi,yi,colorbg):
    pygame.draw.rect(screen,colorbg,(xi,yi,fontsize+20,fontsize+20))
    textsurface = font.render(string,1,(180,10,100))
    screen.blit(textsurface,(xi+10,yi+10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                zpressed = (255,255,255)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                zpressed = (0,0,0)
        button(keyboard[0],keyspace[0],50,zpressed)
''',
    "pygame - menu example":#### 48
    '''# Dibujador de quimica organica
import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dibujador de quimica")



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('freesansbold.ttf', size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill("Black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
''',
    "tkinter - example widgets template":#### 49
    '''"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Checkbuttons", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
check_1 = ttk.Checkbutton(check_frame, text="Unchecked", variable=a)
check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
check_2 = ttk.Checkbutton(check_frame, text="Checked", variable=b)
check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
check_3 = ttk.Checkbutton(check_frame, text="Third state", variable=c)
check_3.state(["alternate"])
check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
check_4 = ttk.Checkbutton(check_frame, text="Disabled", state="disabled")
check_4.state(["disabled !alternate"])
check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(radio_frame, text="Deselected", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable=d, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Mixed")
radio_3.state(["alternate"])
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Entry")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# Spinbox
spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
spinbox.insert(0, "Spinbox")
spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Combobox
combobox = ttk.Combobox(widgets_frame, values=combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")

# Read-only combobox
readonly_combo = ttk.Combobox(widgets_frame, state="readonly", values=readonly_combo_list)
readonly_combo.current(0)
readonly_combo.grid(row=3, column=0, padx=5, pady=10,  sticky="ew")

# Menu for the Menubutton
menu = tk.Menu(widgets_frame)
menu.add_command(label="Menu item 1")
menu.add_command(label="Menu item 2")
menu.add_separator()
menu.add_command(label="Menu item 3")
menu.add_command(label="Menu item 4")

# Menubutton
menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# OptionMenu
optionmenu = ttk.OptionMenu(widgets_frame, e, *option_menu_list)
optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# Button
button = ttk.Button(widgets_frame, text="Button")
button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Accentbutton", style="Accent.TButton")
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

# Togglebutton
button = ttk.Checkbutton(widgets_frame, text="Togglebutton", style="ToggleButton")
button.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# Switch
switch = ttk.Checkbutton(widgets_frame, text="Switch", style="Switch")
switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=120)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Column 1", anchor="center")
treeview.heading(1, text="Column 2", anchor="center")
treeview.heading(2, text="Column 3", anchor="center")

# Define treeview data
treeview_data = [
    ("", "end", 1, "Parent", ("Item 1", "Value 1")),
    (1, "end", 2, "Child", ("Subitem 1.1", "Value 1.1")),
    (1, "end", 3, "Child", ("Subitem 1.2", "Value 1.2")),
    (1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
    (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4")),
    ("", "end", 6, "Parent", ("Item 2", "Value 2")),
    (6, "end", 7, "Child", ("Subitem 2.1", "Value 2.1")),
    (6, "end", 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
    (8, "end", 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
    (8, "end", 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
    (8, "end", 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
    (6, "end", 12, "Child", ("Subitem 2.3", "Value 2.3")),
    (6, "end", 13, "Child", ("Subitem 2.4", "Value 2.4")),
    ("", "end", 14, "Parent", ("Item 3", "Value 3")),
    (14, "end", 15, "Child", ("Subitem 3.1", "Value 3.1")),
    (14, "end", 16, "Child", ("Subitem 3.2", "Value 3.2")),
    (14, "end", 17, "Child", ("Subitem 3.3", "Value 3.3")),
    (14, "end", 18, "Child", ("Subitem 3.4", "Value 3.4")),
    ("", "end", 19, "Parent", ("Item 4", "Value 4")),
    (19, "end", 20, "Child", ("Subitem 4.1", "Value 4.1")),
    (19, "end", 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
    (21, "end", 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
    (21, "end", 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
    (21, "end", 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
    (19, "end", 25, "Child", ("Subitem 4.3", "Value 4.3"))
    ]

# Insert treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True) # Open parents

# Select and scroll
treeview.selection_set(10)
treeview.see(7)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Tab 1")

# Scale
scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# Progressbar
progress = ttk.Progressbar(tab_1, value=0, variable=g, mode="determinate")
progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

# Label
label = ttk.Label(tab_1, text="Forest ttk theme", justify="center")
label.grid(row=1, column=0, pady=10, columnspan=2)

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
''',
    "pyautogui - screenshot":####
    '''import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height=300)
canvas1.pack()

def take_screenshot():
    myScreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenshot.save(save_path+'_screenshot.png')
myButton = tk.Button(text="Take SS",command=take_screenshot,font=10)
canvas1.create_window(150,150,window=myButton)

root.mainloop()
''',
    "pyautogui - moving mouse":####
    '''import pyautogui as pag
import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
''',
    "pytesseract - detecting text from an image":####
    '''from PIL import Image
from pytesseract import pytesseract
path_to_tes = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
path_to_image = r'C:/Users/Fer/AppData/Local/Programs/Python/Python310/los_codigos/Lector de codigos python/img1.png'

pytesseract.tesseract_cmd = path_to_tes
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)
''',
    "PIL - detecting text from an image":####
    '''from PIL import Image
from pytesseract import pytesseract
path_to_tes = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
path_to_image = r'C:/Users/Fer/AppData/Local/Programs/Python/Python310/los_codigos/Lector de codigos python/img1.png'

pytesseract.tesseract_cmd = path_to_tes
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)
''',
    "BeautifulSoup - extracting names":####
    '''
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Walmart - 403 responce
# Aurrera - 403 responce
# mercadolibre - 200 Ok


url = 'https://listado.mercadolibre.com.mx/lenovo-laptop#D[A:lenovo%20laptop]'
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.content, 'html.parser')

file_object = open("textpage.txt","w+")
titles = soup.find_all('h2',class_='ui-search-item__title')
prices = soup.find_all('span',class_='price-tag-fraction')
pricelist = []
gate = False
count = 1
for i,val in enumerate(prices):# cada elemento extraido del sitio
    # 2, 5, 8, 11
    # f(x) = a*b + 2
    # f(x) = 3*b - 1
    print(i,3*count-2,val)
    if i == 3*count - 2:
        pricelist.append(val)
        count += 1
        
            
##print(pricelist)

df1 = pd.DataFrame({'Nombre':titles})
df2 = pd.DataFrame({'precio':prices})
print(df1)
print(df2)
''',
    "filedialog - seleccionar imagen":####
    '''def seleccionar_imagen():# Func-2: Pide al usuario la ruta de una imagen: INCCOMPLETO
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])
    if ruta_imagen:
        # Guardar la ruta de la imagen en un archivo JSON
        guardar_ruta_en_json(ruta_imagen)

        # Mostrar la imagen en la ventana
        mostrar_imagen(ruta_imagen)
''',
    "Matplotlib - adding multiple curves to one plot":####
    '''import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear el gráfico y agregar las líneas
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='tan(x)')

# Configurar el gráfico (etiquetas, leyenda, etc.)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Funciones trigonométricas')
plt.legend()

# Mostrar el gráfico
plt.show()''',
    "tkinter - como enviar informacion de una ventana a otra":####
    '''
import tkinter as tk

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root, text="Haz clic en el botón para abrir la segunda ventana")
        self.label.pack()

        self.button = tk.Button(root, text="Abrir segunda ventana", command=self.abrir_segunda_ventana)
        self.button.pack()

    def abrir_segunda_ventana(self):
        # Crea una nueva instancia de la ventana secundaria y pásale la variable compartida
        segunda_ventana = SegundaVentana(self.root, self.actualizar_label)

    def actualizar_label(self, nueva_informacion):
        # Esta función se llama desde la ventana secundaria
        self.label.config(text=f"Información recibida: {nueva_informacion}")

class SegundaVentana:
    def __init__(self, root, funcion_retorno):
        self.root = tk.Toplevel(root)
        self.funcion_retorno = funcion_retorno

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button_aceptar = tk.Button(self.root, text="Aceptar", command=self.devolver_informacion)
        self.button_aceptar.pack()

    def devolver_informacion(self):
        # Obtén la información de la Entry y llama a la función de retorno en la ventana principal
        informacion = self.entry.get()
        self.funcion_retorno(informacion)
        self.root.destroy()  # Cierra la ventana secundaria

# Crea la ventana principal
root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()
''',
    "json - Crear un archivo json en python":####
    '''import json

# Datos a guardar en el archivo JSON
datos = {
    "nombre": "Ejemplo",
    "edad": 25,
    "ciudad": "Ejemplolandia"
}

# Nombre del archivo donde se guardará el JSON
nombre_archivo = "ejemplo.json"

# Escribir datos en el archivo JSON
with open(nombre_archivo, 'w') as archivo:
    json.dump(datos, archivo)

print(f"Archivo JSON '{nombre_archivo}' creado exitosamente.")
''',
    "tkinter - transferir información entre ventanas":#### 
    '''
import tkinter as tk

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root, text="Haz clic en el botón para abrir la segunda ventana")
        self.label.pack()

        self.button = tk.Button(root, text="Abrir segunda ventana", command=self.abrir_segunda_ventana)
        self.button.pack()

    def abrir_segunda_ventana(self):
        # Crea una nueva instancia de la ventana secundaria y pásale la variable compartida
        segunda_ventana = SegundaVentana(self.root, self.actualizar_label)

    def actualizar_label(self, nueva_informacion):
        # Esta función se llama desde la ventana secundaria
        self.label.config(text=f"Información recibida: {nueva_informacion}")

class SegundaVentana:
    def __init__(self, root, funcion_retorno):
        self.root = tk.Toplevel(root)
        self.funcion_retorno = funcion_retorno

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button_aceptar = tk.Button(self.root, text="Aceptar", command=self.devolver_informacion)
        self.button_aceptar.pack()

    def devolver_informacion(self):
        # Obtén la información de la Entry y llama a la función de retorno en la ventana principal
        informacion = self.entry.get()
        self.funcion_retorno(informacion)
        self.root.destroy()  # Cierra la ventana secundaria

# Crea la ventana principal
root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()

''',
    "tkinter - Text Metodo: .get()":####
    '''import tkinter as tk

def obtener_texto():
    contenido_texto = texto.get("1.0", "end-1c")  # Obtiene el contenido del widget Text
    print("Contenido del Text:", contenido_texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Tkinter con Text")

# Crear un widget Text
texto = tk.Text(ventana, height=10, width=40)
texto.pack(pady=10)

# Crear un botón para obtener el texto
boton_obtener_texto = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton_obtener_texto.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

'''
    }
tips = dict(sorted(tips.items()))
# Nombre del archivo donde se guardará el diccionario JSON
nombre_archivo = 'tips.json'
### 3) ESCRIBIRLO
### Guardar el diccionario en el archivo JSON
with open(nombre_archivo, 'w') as archivo:
    json.dump(tips, archivo)

##print(f"El diccionario se ha guardado en '{nombre_archivo}'.")

