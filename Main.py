from Reporte import Reporte
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
import numpy as np
from Parser import Parser
from tkinter import Menu, filedialog,Tk
from Figura import Figura
from Reservadas import PR
from Celda import Celda
from Reporte import Reporte
p = Parser()
r = Reporte()
figuras =  []



def abrir():
    
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo PXLA",
        initialdir = "./",
        filetypes = (
            ("archivos PXLA", "*.pxla"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        MessageBox.showerror(title="Carga",message="No se seleccionó ningun archivo")
        
        return None
    else:
        texto = archivo.read()
        archivo.close()
        MessageBox.showinfo(title="Lectura",message="Exito") # título, mensaje
        return texto

def prueba ():
    txt = abrir()
    if txt is not None:
        dato = txt
        dato+="@"
        p.obtenerData(dato)  
    else:
        MessageBox.showerror(title="Error",message="Error de lectura")
        


def llenarFigura(lista):
        titulo = ''
        ancho = 0
        alto = 0
        filas = 0
        columnas = 0
        celdas=[]
        filtros = []
        validacion = ''
        i = 0
        end = len(lista)
        while i< end:
            token = lista[i]
            if token.token == PR.CADENA :
                titulo = token.lexema
            elif token.token == PR.ID:
                if(validacion=="filtros"):
                    filtros.append(token.lexema)
                else:
                    validacion =token.lexema.lower()
            elif token.token == PR.NUM:
                if(validacion=="ancho"):
                    ancho = int(token.lexema)
                elif(validacion=="alto"):
                    alto = int(token.lexema)
                elif(validacion=="filas"):
                    filas = int(token.lexema)
                elif(validacion=="columnas"):
                    columnas = int(token.lexema)
                elif(validacion=="celdas"):
                    celda = Celda()
                    celda.x= int(token.lexema)
                    i+=2
                    token = lista[i]
                    celda.y= int(token.lexema)
                    i+=2
                    token = lista[i]
                    celda.activo = token.lexema
                    i+=2
                    token = lista[i]
                    celda.color = token.lexema
                    celdas.append(celda)

            elif token.lexema == "@":
                if(titulo!=''):
                    figuras.append(Figura(titulo,ancho,alto,filas,columnas,filtros,celdas))
                    titulo = ''
                    ancho = 0
                    alto = 0
                    filas = 0
                    columnas = 0
                    celdas=[]
                    filtros = []
                    validacion = ''
            i+=1

def cargarArchivos():
    prueba()
    llenarFigura(p.tokens)
    MessageBox.showinfo(title="Carga",message="Exito") # título, mensaje

def generarTokens():
    r.reporteToken(p.tokens)

def generarErrores():
    r.reporteErrores(p.lista_errores)
    
    
def generar():
    for i in range(len(figuras)):
        figuras[i].generarImagen("MIRRORN") 
        figuras[i].generarImagen("MIRRORX")
        figuras[i].generarImagen("MIRRORY")
        figuras[i].generarImagen("MIRRORD")
    MessageBox.showinfo(title="Generar",message="Exito")
    

def imagen():
    titulo =askopenfilename(filetypes = (("Imagenes", "*.jpg"), ("All files", "*")))
    img = Image.open(titulo)
    new_img = img.resize((500,300))
    render = ImageTk.PhotoImage(new_img)
    ing1 = Label(ventana, image=render)
    ing1.image = render
    ing1.place(x=10,y=30)

def salirAplicacion():
    salir = messagebox.askquestion("Salir", "¿Desea salir?")
    if salir =="yes":
        ventana.quit()
                    

    

if __name__ == "__main__":
    
    ventana = Tk()
    ventana.geometry("450x675+300+10")
    ventana.title("Menu")
    ventana.iconbitmap("img\python_94570.ico")
    fondo = PhotoImage(file="img\Pin-en-Movimiento.gif")
    fondo1= Label(ventana, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)

    barraMenu=Menu(ventana)
    cargarArchivo=Menu(barraMenu,tearoff=0)
    generarImagen=Menu(barraMenu,tearoff=0)
    verReporte=Menu(barraMenu,tearoff=0)
    verImagen=Menu(barraMenu,tearoff=0)
    salir = Menu(barraMenu,tearoff=0)

    cargarArchivo.add_command(label="Abrir",command=cargarArchivos)

    generarImagen.add_command(label="Generar imagenes", command=generar)

    verReporte.add_command(label="Tokens",command=generarTokens)
    verReporte.add_separator()
    verReporte.add_command(label="Errores", command=generarErrores)

    verImagen.add_command(label="Ver Imagen", command=imagen)
    

    salir.add_command(label="Salir",command=salirAplicacion)



    barraMenu.add_cascade(label="Archivo",menu=cargarArchivo)
    barraMenu.add_cascade(label="Generar",menu=generarImagen)
    barraMenu.add_cascade(label="Reporte",menu=verReporte)
    barraMenu.add_cascade(label="Ver",menu=verImagen)
    barraMenu.add_cascade(label="Salir",menu=salir)


    ventana.config(menu=barraMenu)
    ventana.mainloop()
  
    