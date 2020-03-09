def eclosure_alone(nodos, lenguaje):
    if isinstance(nodos, list):
        for n in nodos:
            move = posibles_movimientos(n, "e", lenguaje)
            for x in move:
                if x[2] not in nodos:
                    nodos.append(x[2])
            
    return nodos

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
        return comparacion
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
        return movimiento
    
    else:
        move = posibles_movimientos(nodos, cadena, lenguaje)
        for x in move:
            if x[2] not in movimiento:
                movimiento.append(x[2])
        return movimiento


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

print(eclosure([5],[[2, 'a', 6], [4, 'a', 5], [5, 'e', 4], [5, 'e', 7], [6, 'e', 4], [6, 'e', 7]]))


##Funciones necesarias: eclosure(nodos, lenguaje), move(nodos, cadena, lenguaje)
def dfa_nfa(lenguaje, infin):
    
    estados = []
    simbolos = []
    for i in range(len(lenguaje)):
        if lenguaje[i][0] not in estados:
            estados.append(lenguaje[i][0])
                
        if lenguaje[i][2] not in estados:
            estados.append(lenguaje[i][2])
                
        if lenguaje[i][1] not in simbolos:
            simbolos.append(lenguaje[i][1])
                
    