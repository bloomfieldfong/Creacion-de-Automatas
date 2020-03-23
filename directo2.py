from funciones import *

import os
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
    n.append("#")
    n.append(".")
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
                    
                    respuesta.append(y)
                else:
                    respuesta.append(firstpos(n,a))
    nodos = []
    letras = []
    for i in range(len(n)):
        if n[i] in s:
            nodos.append(i)
            letras.append(n[i])
            
    return [respuesta, nodos, letras]
        

def directo(tabla):
    tabla = followpos(tabla)
    print(tabla)
    nodos = tabla[1]
    letras = tabla[2]

    asa = []
    izq = tabla[0]
    if isinstance(izq[0], list):
        for i in range(len(izq[0])):
            asa.insert(0,izq[0][i])
        izq.pop(1)
    
    for i in range(len(izq)):
        if isinstance(izq[i],list):
            pass
        else:
            asa.append(izq[i])
            
    print("ASA")
    print(asa)
    izq = asa
    
    
    posi = ["a","b","c","d"]
    res  =[]
    res.append(izq[0])
    movi = []
    i = 0
    while i< len(res):
        print(res)
        listas  = []
        letritas = []
        for x in range(len(res[i])): #{0,1,4}
            nuevaizq = list(res[i])
            for m in posi: #["a","b"]#
                if letras[nodos.index(nuevaizq[x])] == m:
                    listas.append(izq[nodos.index(nuevaizq[x])])
                    letritas.append(m)

        a = []
        b = []
        c = []
        for e in range(len(letritas)):
            if letritas[e] == "a":
                a.append(list(listas[e]))
            if letritas[e] == "b":
                b.append(list(listas[e]))
            if letritas[e] == "c":
                c.append(list(listas[e]))
                        
        a = set().union(*a)
        b = set().union(*b)
        c = set().union(*c)
        if len(a) != 0:
            movi.append([res[i], "a", a])
            
        if len(b) != 0:
            movi.append([res[i], "b", b])
        if len(c) != 0:
            movi.append([res[i], "c", c])
        
        
        if a not in res and len(a) != 0:
            res.append(a)
        if b not in res and len(b) != 0:
            res.append(b)
        if c not in res and len(c) != 0:
            res.append(c)
        i+=1
        
    alfabeto =["A","B","C","D","E","F","G","H","I","J"]
    x = 0
    print("Movimientos sin cambio de variables")
    print(movi)
    while x < len(movi):
        indice1 = res.index(movi[x][0])
        movi[x][0] = alfabeto[indice1]
        indice1 = res.index(movi[x][2])
        movi[x][2] = alfabeto[indice1]
        x +=1
    x = 0
    infin =[alfabeto[res.index(res[0])], alfabeto[res.index(res[len(res)-1])] ]
    return movi, infin



        


                
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
x = ['b', 'b', '|', '*', 'a', '.', 'b', '.', 'b', '.', 'a', 'b', '|', '*', '.']
#x = ['a', 'b', '|', '*', 'a', '.', 'b', '.', 'b', '.']
#for n in range(len(x)):
#    print(firstpos(x,n))
#print(followpos(x))

#print(directo(x))
            
