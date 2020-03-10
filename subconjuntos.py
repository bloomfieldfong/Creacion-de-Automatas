def eclosure_alone(nodos, lenguaje):
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

def eclosure(nodos, lenguaje):
    
    if isinstance(nodos, list):
        for n in nodos:
            move = posibles_movimientos(n, "e", lenguaje)
            for x in move:
                if x[2] not in nodos:
                    nodos.append(x[2])
    
    comparacion = nodos
    x = eclosure_alone(nodos, lenguaje) 
    if  x == comparacion:
        s = set()
        for item in comparacion:
            s.add(item)
        return s
    else:
        eclosure(nodos, lenguaje)
    

def move(nodos, cadena, lenguaje):
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
    print(inicial)
    for n in cadena:
        print(n)
        print(inicial)
        x = move(inicial, n, lenguaje)
        inicial = x[0]
        
    if inicial == infin[0][1]:
        return "YES"
    else:
        return "NO"

print(move([5,6],"e",[[2, 'a', 6], [4, 'a', 5], [5, 'e', 4], [5, 'e', 7], [6, 'e', 4], [6, 'e', 7]]))


##Funciones necesarias: eclosure(nodos, lenguaje), move(nodos, cadena, lenguaje)
def dfa_nfa(transiciones, infin[0]):
    
    estados = []
    simbolos = []
    for i in range(len(transiciones)):
        if transiciones[i][0] not in estados:
            estados.append(transiciones[i][0])
                
        if transiciones[i][2] not in estados:
            estados.append(transiciones[i][2])
                
        if transiciones[i][1] not in simbolos:
            simbolos.append(transiciones[i][1])
            
    #infin[0] = inicial
    #transiciones
    i = 0
    Dstate =[]
    Dstate.append(eclosure_alone(infin[0], transiciones))
    
    while i < len(Dstate):
    
    
    
            
    
    
                
    