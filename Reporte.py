from os import error
from Token import Token
from Parser import Parser
from Error import Error
from tkinter import *
from tkinter import messagebox as MessageBox
from Reservadas import PR
class Reporte:
    def __init__(self):
        var=0

    def reporteErrores(self,lista_errores):
        
        f = open('reporteErrores.html','w')

        text_reporte = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <meta http-equiv="X-UA-Compatible" content="ie=edge" />
                <title>Reporte Errores</title>

                
                <link rel="stylesheet" href="style.css" />
            </head>

            <h2>Tabla de Errores</h2>
            <div class="table-wrapper">
                <table class="fl-table">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Cadena</th>
                        <th>Fila</th>
                        <th>Columna</th>
                    </tr>
                    </thead>
                    <tbody>

            '''
        i = 0
        size = len(lista_errores)
        while(i<size):
            error = lista_errores[i]
            print(error.cadena)
                
            text_reporte+='''
                    <tr>
                        <td>'''+str(i)+'''</td>
                        <td>'''+str(error.cadena)+'''</td>
                        <td>'''+str(error.fila)+'''</td>
                        <td>'''+str(error.columna)+'''</td>
			        </tr>
            
            '''
            i+=1

        text_reporte+='''
                        </tbody>
                </table>
            </div>
        '''
        
        f.write(text_reporte)
        f.close()
        MessageBox.showinfo("Reporte","Reporte creado con Exito") # título, mensaje





    def reporteToken(self,lista_token):
        
        f = open('reporteToken.html','w')

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
        i = 0
        size = len(lista_token)
        while(i<size):
            x = lista_token[i]
            print(x.lexema)
                
            text_reporte+='''
                    <tr>
                        <td>'''+str(i)+'''</td>
                        <td>'''+str(x.token)+'''</td>
                        <td>'''+str(x.lexema)+'''</td>
                        <td>'''+str(x.fila)+'''</td>
                        <td>'''+str(x.columna)+'''</td>
                    </tr>
                    
            '''

            
            i+=1
        text_reporte+='''
                        </tbody>
                </table>
            </div>
        '''
        
        f.write(text_reporte)
        f.close()
        MessageBox.showinfo("Reporte","Reporte creado con Exito") # título, mensaje


