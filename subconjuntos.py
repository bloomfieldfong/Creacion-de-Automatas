from thomson_grafic import *


def eclosure_alone(nodo, lenguaje):
    nodos =[]
    nodos.append(nodo)
    move = posibles_movimientos(nodo, "e", lenguaje)
    
    for x in move:
        if x[2] not in nodos:
            nodos.append(x[2])
    s = set()
    if isinstance(nodos,list):
        for item in nodos:
            s.add(item)
        return s
    else:
        s.add(nodos)
            
    

def eclosure(x, lenguaje):
    if isinstance(x, int):
        nodos = []
        nodos.append(x)
    else: 
        nodos = list(x)
  
    if isinstance(nodos, list):
        for n in nodos:
            move = posibles_movimientos(n, "e", lenguaje)
            for x in move:
                if x[2] not in nodos:
                    nodos.append(x[2])
    
    s = set()
    for item in nodos:
        s.add(item)
    return s


def move(nodos, cadena, lenguaje):
 
    nodos = list(nodos)
    movimiento = []
    if isinstance(nodos, list):
        for n in nodos:
            move = posibles_movimientos(n, cadena, lenguaje)
            for x in move:
                if x[2] not in movimiento:
                    movimiento.append(x[2])
        
        
        s = set()
        for item in movimiento:
            s.add(item)
        return s
    
    else:
        move = posibles_movimientos(nodos, cadena, lenguaje)
        for x in move:
            if x[2] not in movimiento:
                movimiento.append(x[2])
                
                
        s = set()
        for item in movimiento:
            s.add(item)
        return s


def posibles_movimientos(nodo,cadena, automata):
    movimientos = []
    for n in automata:
        if n[0] == nodo and n[1] == str(cadena):
            movimientos.append(n)
            
    return movimientos

def existe(cadena, lenguaje,infin):
    i = 0
    inicial = infin[0][0]
    for n in cadena:
        x = move(inicial, n, lenguaje)
        x = list(x)
        inicial = x[0]
    
    i = 0 
    for n in range(len(infin)):
        if inicial == infin[n][1]:
            i += 1
            
    if i !=0:
        return "YES"
    else:
        return "NO"
        

#existe("aaaa",[['A', 'a', 'B'], ['B', 'a', 'D'], ['B', 'b', 'E'], ['D', 'a', 'F'], ['D', 'b', 'G'], ['E', 'a', 'F'], ['E', 'b', 'G']],[['A', 'F'], ['A', 'G'], ['A', 'F'], ['A', 'G']])


##Funciones necesarias: eclosure(nodos, lenguaje), move(nodos, cadena, lenguaje)
##Utiliza: todos los estados, todos los simbolos, las transiciones, estado final e inicial 
def dfa_nfa(transiciones, infin):
    estados = []
    simbolos = []
    for i in range(len(transiciones)):
        
        if transiciones[i][0] not in estados:
            estados.append(transiciones[i][0])
                
        if transiciones[i][2] not in estados:
            estados.append(transiciones[i][2])
              
        if transiciones[i][1] != "e":
            if transiciones[i][1] not in simbolos:
                simbolos.append(transiciones[i][1])
                
        
    #infin[0] = inicial
    #transiciones
    i = 0
    Dstate =[]
    tablita = []
    Dstate.append(eclosure(infin[0], transiciones))
    infin_nuevo =[]
    
    infin_nuevo.append(eclosure(infin[0], transiciones))
    
    
    ##algoritmo utilizado en clase
    while i < len(Dstate):
        for n in simbolos:
            u = eclosure(move(Dstate[i],n,transiciones),transiciones)
            tablita.append([Dstate[i],n,u])
            for w in infin:
                if w[1] in u:
                    infin_nuevo.append(u)
            if u not in Dstate and u is not None:
                Dstate.append(u)
                
                       
        i+=1

    x = 0
    while x < len(tablita):
        if tablita[x][0] == set() or tablita[x][2] == set():
            tablita.pop(x)
            x-=1
            
        x +=1
    
    ##cambiando los estados a letras
    alfabeto =["A","B","C","D","E","F","G","H","I","J"]
    x = 0 
    while x < len(tablita):
        indice1 = Dstate.index(tablita[x][0])
        tablita[x][0] = alfabeto[indice1]
        indice1 = Dstate.index(tablita[x][2])
        tablita[x][2] = alfabeto[indice1]
        x +=1
    x = 0
    
    while x < len(infin_nuevo):
        indice1 = Dstate.index(infin_nuevo[x])
        infin_nuevo[x]= alfabeto[indice1]

        x+=1
    
    y = []
    for i in range(1,len(infin_nuevo)):
        y.append([infin_nuevo[0],infin_nuevo[i]])
        
   
    return tablita, y
        
    
   
    
  

                
    