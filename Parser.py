from Token import Token
from Reservadas import PR
class Parser:
    def __init__(self):
        self.tokens = []
        


    def obtenerData(self,data): 
        estado = 0 
        aux = ''
        fila = 1
        columna =0
        i = range(len(data))
        for x in i:
            if(estado==0):
                if(x == '=' or x == ' ' or x == ';' or x == ',' or x== '{'  or x == '}'  or x == '['  or x == ']' or x == '\r' or x == '\t' ): #Ignorar
                    t = Token(PR.SYMBOL,aux,fila,columna)
                    self.token.append(t)
                    pass   
                elif(x == '\n'):
                    fila+=1
                    columna=0
                elif(x.isalpha()):
                    aux +=x
                    estado = 1
                elif(x.isdigit()):
                    aux +=x
                    estado = 3
                elif(x == '"'):
                    estado = 2
                elif(x == '#'):
                    estado = 4
                else:
                    #Guardar error
                    pass
            elif (estado ==1): #ID 
                if(x.isalpha()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.ID,aux,fila,columna)
                    self.token.append(t) 
                    estado = 0
                    i-=1
                    aux = ''
                    
            elif(estado ==2): #Cualquier cadena "cadena"
                if(x!='"'):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.CADENA,aux,fila,columna)
                    self.token.append(t) 
                    estado = 0
                    i-=1
                    aux = ''
            elif(estado==3): #Cualquier numero
                if(x.isdigit()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.NUM,aux,fila,columna)
                    self.token.append(t) 
                    estado = 0
                    i-=1
                    aux = ''
            elif(estado==4): #Codigo Hexadecimal
                if(x.isalpha() or x.isdigit()):
                    aux +=x
                    columna+=1
                else:
                    t = Token(PR.CODIGO,aux,fila,columna)
                    self.token.append(t)
                    estado = 0
                    i-=1
                    columna-=1
                    aux = ''

                
