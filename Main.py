from Reporte import Reporte
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
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

def prueba ():
    txt = abrir()
    if txt is not None:
        dato = txt
        dato+="@"
        p.obtenerData(dato)  
    else:
        print("Error lectura")


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
    #r.reporteToken()
    
    
    for i in range(len(figuras)):
     figuras[i].generarImagen()
    
    print(p.tokens)


                    

    

if __name__ == "__main__":
    
    ventana = Tk()
    ventana.geometry("800x600+50+50")
    ventana.title("Menu")
    barraMenu=Menu(ventana)
    cargarArchivo=Menu(barraMenu)
    generarImagen=Menu(barraMenu)
    verReporte=Menu(barraMenu)
    verImagen=Menu(barraMenu)
    salir = Menu(barraMenu)

    cargarArchivo.add_command(label="Abrir",command=cargarArchivos)

    generarImagen.add_command(label="Generar imagenes")

    verReporte.add_command(label="Tokens")
    verReporte.add_command(label="Errores")

    verImagen.add_command(label="Original")
    verImagen.add_command(label="MirroX")
    verImagen.add_command(label="MirroY")
    verImagen.add_command(label="DoubleMirror")

    salir.add_command(label="Salir",command=ventana.destroy)



    barraMenu.add_cascade(label="Archivo",menu=cargarArchivo)
    barraMenu.add_cascade(label="Generar",menu=generarImagen)
    barraMenu.add_cascade(label="Reporte",menu=verReporte)
    barraMenu.add_cascade(label="Imagen",menu=verImagen)
    barraMenu.add_cascade(label="Salir",menu=salir)


    ventana.config(menu=barraMenu)
    ventana.mainloop()
  
    '''print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Analizar Archivo \n 3.Ver Reporte \n 4.Seleccionar imagen \n 5.Ver Imagen \n 6.Salir  \n"))

    

    while opcion != 6:

        if opcion == 1: #Cargar Archivo
            prueba()
            llenarFigura(p.tokens)
            print(figuras)
            figuras[1].generarImagen()
                

        elif opcion == 2: #Generar imagen
            
            pass
        elif opcion == 3: #Ver Reporte
            pass
        elif opcion == 4: #Selecioanr Imagen
            pass
        elif opcion == 5: #Ver imagen
            pass
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Analizar Archivo \n 3.Ver Reporte \n 4.Seleccionar imagen \n 5.Ver Imagen \n 6.Salir \n"))
'''