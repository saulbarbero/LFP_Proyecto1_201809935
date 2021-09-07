from tkinter import filedialog, Tk

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
        gestor.obtenerData(dato)  
    else:
        print("Error lectura")

if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Analizar Archivo \n 3.Ver Reporte \n 4.Seleccionar imagen \n 5.Ver Imagen \n 6.Salir"))

    

    while opcion != 6:

        if opcion == 1: #Cargar Archivo
           pass

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
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Analizar Archivo \n 3.Ver Reporte \n 4.Seleccionar imagen \n 5.Ver Imagen \n 6.Salir"))
