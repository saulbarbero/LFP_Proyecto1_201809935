from Token import Token
from Parser import Parser
from tkinter import *
from tkinter import messagebox as MessageBox
class Reporte:
    def __init__(self):
        var=0

    def reporteToken():
        token = Token()
        bloque=""
        f = open('reporte.html','w')

        text_reporte = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <meta http-equiv="X-UA-Compatible" content="ie=edge" />
                <title>Reporte Tokens</title>

                
                <link rel="stylesheet" href="style.css" />
            </head>

            <h2>Tabla de Tokens</h2>
            <div class="table-wrapper">
                <table class="fl-table">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Token</th>
                        <th>Lexema</th>
                        <th>Fila</th>
                        <th>Columna</th>
                    </tr>
                    </thead>
                    <tbody>

            '''

        for i in range(len(token)):
            bloque+='''
                    <tr>
                        <td>Cell1</td>
                        <td>Cell2</td>
                        <td>Cell3</td>
                        <td>Cell4</td>
                        <td>Cell5</td>
			        </tr>
            
            '''
            bloque = bloque.replace("Cell1",str(i))
            bloque = bloque.replace("Cell2",str(token.token))
            bloque = bloque.replace("Cell3",str(token.lexema))
            bloque = bloque.replace("Cell4",str(token.fila))
            bloque = bloque.replace("Cell2",str(token.columna))

            text_reporte+=bloque
            text_reporte+='''
                            </tbody>
                    </table>
                </div>

            
            '''
        



        

        




                   

        f.write(text_reporte)
        f.close()
        MessageBox.showinfo("Reporte creado con Exito") # título, mensaje


