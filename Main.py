from ListaSimple import ListaSimple
from Parser import Parser
from tkinter import filedialog, Tk

p = Parser()
figuras = ListaSimple()

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
        p.obtenerData(dato)  
    else:
        print("Error lectura")


def llenarTerrenos(lista):
        figura = ''
        i = 0
        end = len(lista)
        num_rows=0
        num_cols=0
        while i< end:
            x=lista[i];
            if(x=='t'):
                if(figura==''):
                    figura = Figura()
                else:
                    figuras.insertar(figura)
                    figura=''

            elif(x=='titulo'):
                i+=1
                figura.titulo = lista[i]

            elif(x=='ancho'):
                i+=2
                figura.ancho = int(lista[i])-1
                i+=1
            elif(x=='alto'):
                i+=2
                figura.alto = int(lista[i])-1
                i+=1
            elif(x=='filas'):
                i+=2
                figura.n = int(lista[i])-1
                i+=1
            elif(x=='columnas'):
                i+=2
                figura.m = int(lista[i])-1
                i+=1
            elif(x=='filtros'): #Aqui no se si esta bien
                i+=2
                figura.filtro.append(int(lista[i])-1)
                i+=1
            else:
                pass
            i+=1

if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Analizar Archivo \n 3.Ver Reporte \n 4.Seleccionar imagen \n 5.Ver Imagen \n 6.Salir  \n"))

    

    while opcion != 6:

        if opcion == 1: #Cargar Archivo
           prueba()
           print(p.tokens)

        elif opcion == 2: #Analizar Archivo
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
