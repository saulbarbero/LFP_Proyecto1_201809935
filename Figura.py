import math
import numpy as np

class Figura:
    def __init__(self,titulo,ancho,alto,n,m,filtro,celdas):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.n = n #Rows
        self.m = m #Colums
        self.filtro = filtro
        self.celdas = celdas
        self.matriz = np.full((n,m), "       ") 
        self.llenarMatriz()


    def llenarMatriz(self):
        for celda in self.celdas:
            if(celda.activo=="TRUE"):
                self.matriz[celda.y,celda.x]= celda.color
            else:
                self.matriz[celda.y,celda.x]= "       "

        print(self.matriz)
                
    def generarImagen(self):

        texto_html='''
        <!DOCTYPE html>
        <html>
        <head>
        <!-- Referencias a hojas de estilos, en este caso un CSS -->
        <link rel="stylesheet" href="%p.css">
        </head>
        <body>
        <!-- div que representa el lienzo -->
        <div class="canvas"> 
        '''
        #Asignar ancho
        texto_css ='''
        body {
            background: #333333;      /* Background color de toda la página */
            height: 100vh;            
            display: flex;            /* Define contenedor flexible */
            justify-content: center;  /* Centra horizontalmente el lienzo */
            align-items: center;      /* Centra verticalmente el lienzo */
        }

        .canvas {
            width: w$px;   /* Ancho del lienzo, se asocia al ANCHO de la entrada */
            height: h$px;  /* Alto del lienzo, se asocia al ALTO de la entrada */
        }

        .pixel {
            width: w@px;    /* Ancho de cada pixel, se obtiene al operar ANCHO/COLUMNAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
            height: h@px;   /* Alto de cada pixel, se obtiene al operar ALTO/FILAS (al hablar de pixeles el resultado de la división debe ser un numero entero) */
            float: left;
            box-shadow: 0px 0px 1px #fff; /*Si lo comentan se quita la cuadricula de fondo */
        }
        '''
        texto_css= texto_css.replace("w$",str(self.ancho))
        texto_css= texto_css.replace("h$",str(self.alto))
        texto_css= texto_css.replace("%p",self.titulo)

        texto_css= texto_css.replace("w@",str(math.trunc(self.ancho/self.m)))
        texto_css= texto_css.replace("h@",str(math.trunc(self.alto/self.n)))
        i = 0 
        conteo = 0
        while(i<self.n): #Recorrer en y
            j = 0
            while(j<self.m): #Recorrer x
                conteo+=1
                if(self.matriz[i,j]!="       "):
                    texto_css+='''
                    .pixel:nth-child(num){
                        background: code ; /* Todo lo que este agrupado separado por comas antes de esta parte { background:..... } se le va a asignar el color indicado*/
                    }
                    '''
                    texto_html+='<div class="pixel"></div>\n'
                    texto_css= texto_css.replace("code",self.matriz[i,j])
                    texto_css= texto_css.replace("num",str(conteo))

                j+=1
            i+=1
        
        texto_html+='''
        </div>
        </body>
        </html>
        '''
        f = open("figura.", "w")
        f.write(texto_css)
        f.close()
        f = open(self.titulo+".html", "w")
        f.write(texto_html)
        f.close()


        print(texto_css)


