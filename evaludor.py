## evaluador de expresiones
## 100 x 25


def evaluate(digito1, digito2, operador):
    if(operador == "+"):
        return digito1+digito2
    if(operador == "-"):
        return digito1-digito2
    if(operador == "*"):
        return digito1*digito2
    if(operador == "/"):
        return digito1/digito2
    
    
def principal(token):
    lista = []
    operadores = []
    for i in range(0,len(token)):
        if token[i] == "*" or token[i] == "/" or token[i] == "+" or token[i] == "-":
            operadores.append(token[i])
        else:
            
            lista.append(token[i])
    return lista, operadores


def jerarquia(lista):
    jerarquia = []
    for i in range(0,len(lista)):
        if lista[i] == "*" or lista[i] == "/":
            jerarquia.append("1")
        else:
            jerarquia.append("0")
    return jerarquia

          

x = principal("2*1+2")
print(x)
print(jerarquia(x[1]))

def hola(lista):
    orden = principal(lista)
    jerarquia = jerarquia(x[1])
    respuesta = []
    for i in range(0, len(jerarquia)):
        if jerarquia[i] == 1:
            if orden[1][i] == "*":
                orden[0][i] = orden[1][i] * orden[1][i+1] 
           

hola("2*1+2")
        



##print(x)
##print(evaluate(int(x[0]), int(x[2]), x[1]))