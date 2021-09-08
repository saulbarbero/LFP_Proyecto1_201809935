from Token import Token
from Reservadas import PR

class Parser:
    def __init__(self):
        self.tokens = []
        

    def obtenerData(self,data): #Me falta guardar caracteres de @ #
        estado = 0 #curso
        aux = ''
        for x in data:
            if(estado==0):
                if(x == '=' or x == ' ' or x == '"'or x == ';' or x == ',' or x== '{'  or x == '}'  or x == '['  or x == ']' or x == '\r' or x == '\t' or x == '\n'): #Ignorar
                    pass   
                elif(x.isalpha()):
                    aux +=x
                    estado = 1
                elif(x.isdigit()):
                    aux +=x
                    estado = 3
                elif(x == '"'):
                    estado = 2
                elif(x =='['):
                    estado = 3
                elif(x == "#"):
                    estado = 4
                else:
                    pass
            elif (estado ==1):
                if(x.isalpha()):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = '' 
                    estado = 0 
                    
            elif(estado ==2):
                if(x!='"'):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = ''  
                    estado = 0
            elif(estado==3):
                if(x.isdigit()):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = ''  
                    estado = 0
            elif(estado==4):
                if(x!="]"):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = ''  
                    estado = 0

                
