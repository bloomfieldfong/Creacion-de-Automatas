from funciones import * 
# Cambia de infix a postdfix
def postfix_arbol(cadena):
    
    # operadores validos
    op_validos = ["|", "*"]
    # stack
    stack = []
    # output
    valores = []
    i = 0

    primero =  0
    while i < len(cadena):
        # Si tenemos un parantesis abierto entonces se ira al stack
        if cadena[i] == "(":
            stack.append(cadena[i])
        # Si es un parentesis cerrado entonces saca todo del stack
        # hasta encontrar un parentesis abierto
        elif cadena[i] == ")":
            x = len(stack) - 1
            while stack[x] != "(":
                # se agrega el ultimo valor de stack a mi output
                valores.append(stack[x])
                # se realiza pop del ultimo numero
                stack.pop()
                x -= 1
            # elimina el parentesis abierto
            stack.pop()

        # Si es un operador entonces se agrega al stack (depende de presedencia)
        elif cadena[i] in op_validos:
            # Revisa si el stack no esta vacio
            if len(stack) == 0:
                stack.append(cadena[i])
            else:
                # Si el operador anterior no es un parentesis
                if stack[-1] != '(':
                    # Si la precendencia de la cadena es menor a la del stack
                    if precedencia(cadena[i]) < precedencia(stack[-1]):
                        # Si en el stack solo hay un objeto
                        z = len(stack) - 1
                        if z != 0:
                            # Se saca todo del stack y se agrega el valor nuevo al stack
                            # se saca todos menos el parentesis
                            while stack[z] != '(':
                                valores.append(stack[-1])
                                stack.pop()
                                z -= 1
                            stack.append(cadena[i])
                        else:
                            # Se saca lo que hay y se agrega el valor nuevo
                            valores.append(stack[-1])
                            stack.pop()
                            stack.append(cadena[i])
                    # si la precedencia es mayor se agrega al stack
                    elif precedencia(cadena[i]) >= precedencia(stack[-1]):
                        stack.append(cadena[i])
                else:
                    # Si no hay nada solo se agrega al stack
                    stack.append(cadena[i])
        # si es un valor se agrega a los valores
        else:
            if cadena[i] == ".":
                primero +=1
            
            if primero == 1:
                print("")
                primero +=1
            else: 
                valores.append(cadena[i])
        # contador
        i += 1
    

    # Si se termino el ciclo y aun hay cosas en el stack entonces las saca
    if len(stack) != 0:
        for i in range(len(stack)):
            valores.append(stack[-1])
            stack.pop()
    
    if primero > 0:
        valores.append(".")
    return valores



def nullable(n,pos):
    if n[pos] == "e":
        respuesta =  True
    elif n[pos] == "|":
        x = []
        for s in range(pos):
            if n[s] == "|":
                x.pop()
                x.pop()
            x.append(nullable(n,s))        
        respuesta = x[-1] or x[-2]
    elif n[pos] == ".":
        x = []
        for s in range(pos):
            if n[s] == "|":
                x.pop()
                x.pop()
            x.append(nullable(n,s))        
        respuesta = x[-1] and x[-2]
    elif n[pos] == "*":
        respuesta = True
    else:
        respuesta = False
    return respuesta


def firstpos(n,pos):
    if n[pos] == "e":
        respuesta =  0
    elif n[pos] == "|":
        respuesta = firstpos(n,pos-1).union(firstpos(n,pos-2))
    elif n[pos] == ".":
        x = []
        for s in range(pos):
            if n[s] == "|":
                x.pop()
                x.pop()
            x.append(firstpos(n,s))
        if nullable(n,pos-2):
            respuesta = x[-1].union(x[-2])
        else:
            respuesta = x[-2]             
    elif n[pos] == "*":
        x = []
        for s in range(pos):
            x.append(firstpos(n,s))
        respuesta = x[-1]
    else:
        respuesta = {pos}
    return respuesta

def lastpos(n,pos):
    if n[pos] == "e":
        respuesta =  0
    elif n[pos] == "|":
        respuesta = firstpos(n,pos-1).union(firstpos(n,pos-2))
    elif n[pos] == ".":
        x = []
        for s in range(pos):
            if n[s] == "|":
                x.pop()
                x.pop()
            x.append(firstpos(n,s))
        if nullable(n,pos-1):
            respuesta = x[-1].union(x[-2])
        else:
            respuesta = x[-1]             
    elif n[pos] == "*":
        x = []
        for s in range(pos):
            x.append(firstpos(n,s))
        respuesta = x[-1]
    else:
        respuesta = {pos}
    return respuesta




def followpos(n):
    posi = ["*","."]
    respuesta = []
    s = ["a","b", "c","#"]
    for i in range(len(n)):
        if n[i] in posi :
            if n[i] == '.':
                for a in lastpos(n,i-1):
                    if len(respuesta) >0:
                        if isinstance(respuesta[-1], list):
                            nueva = []
                            for o in range(len(respuesta[-1])):
                                nueva.append(respuesta[-1][o].union(firstpos(n,i-1)))
                            respuesta.pop()
                            respuesta.append(nueva[0])
                            respuesta.append(nueva[1])
                            
                        else:
        
                            respuesta.append(firstpos(n,i-1))
                    else:
                        
                        if len(respuesta) == 0:
                            l = []
                            f= []
                            for z in range(i-1):
                                if n[z] in s:
                                    l.append(firstpos(n,z))
                                
                            for m in range(len(l)):
                                f.append(set().union(*l))
                            
                            respuesta.append(f)
                            if isinstance(respuesta[-1], list):
                                nueva = []
                                for o in range(len(respuesta[-1])):
                                    nueva.append(respuesta[-1][o].union(firstpos(n,i-1)))
                                respuesta.pop()
                                respuesta.append(nueva)
                                
                        respuesta.append(firstpos(n,i-1))
                    
                        
            elif n[i] == '*':
                x = []
                for a in lastpos(n,i):
                    x.append(firstpos(n,a))
                
                if len(lastpos(n,i)) >1:
                    y = []
                    
                    for w in range(len(lastpos(n,i))):
                        y.append(set().union(*x))
                    print(y)
                    respuesta.append(y)
                else:
                    respuesta.append(firstpos(n,a))
    nodos = []
    letras = []
    for i in range(len(n)):
        if n[i] in s:
            nodos.append(i)
            letras.append(n[i])
            
    return respuesta, nodos, letras
        

def directo(tabla):
    izq = tabla[0]
    nodos = tabla[1]
    nodos.pop()
    letras = tabla[2]
    letras.pop()
    print(izq)
    print(nodos)
    print(letras)
                
                
#            ## m in range der = [[0, 'a'], [1, 'b'], [4, 'a'], [6, 'b'], [8, 'b'],[10,"#"]]
#                ## lista(izq[n])[m] = 0, 1 ,4 der[s][0] = que posicion tiene cada letra
#                ## der[s][1] = der[n][1]
#                if list(respuesta[n])[m] == der[s][0] and der[s][1] == posi[s] and n!=s:
#                    respuesta.append(izq[n].union(izq[s]))
#                    otro.append(der[n][1])
#
    

                    
                
    
#print(firstpos(['a', 'b', '|', '*', 'a', '.', 'b', '.', 'b', '.','#','.'], 7))
#print(postfix_arbol(expandir("((b|b)*).a.b.b.((a|b)*)")))
#x =['a', 'b', '|', '*', 'a', '.', 'b', '.', 'b', '.', '#','.']
#x = ['b', 'b', '|', '*', 'a', '.', 'b', '.', 'b', '.', 'a', 'b', '|', '*', '.', "#", "."]
#for n in range(len(x)):
#    print(firstpos(x,n))
#print(followpos(x))

directo(([{0, 1, 4}, {0, 1, 4}, {6}, {8}, {10}], [0, 1, 4, 6, 8, 10], ['a', 'b', 'a', 'b', 'b', '#']))
            
