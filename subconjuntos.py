def eclosure_alone():
    pass

def eclosue(nodo, lenguaje):
    pass

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
        
