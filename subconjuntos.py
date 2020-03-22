from thomson_grafic import *


##eclosure del primer numero 
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
            
    
#eclusure 
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

#nos dice a donde se mueve en los estados que se le proporciona
# nodos = nodos en el que se encuentra ahorita
# cadena = que letra vamos a mover
# lenguaje = nuestras transiciones
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

#nos indica los posibles movimientos que podemos tomar
#nodo = de que nodo queremos ver los movimientos
#cadena = que simbolo queremos buscar los posibles movimientos
#atomata = las transiciones de nuestro automata
def posibles_movimientos(nodo,cadena, automata):
    movimientos = []
    for n in automata:
        if n[0] == nodo and n[1] == str(cadena):
            movimientos.append(n) 
    return movimientos

#nos indica si la cadena existe en nuestro lenguaje
#cadena = la cadena que queremos saber si existe en nuestro lenguaje
#lenguaje = las transiciones de nuestro lenguaje
#infin = el estado final y el inicial
def existe(cadena, lenguaje,infin):
    i = 0
    inicial = infin[0][0]
    print(inicial)
    for n in cadena:
        x = move(inicial, n, lenguaje)
        if len(x)==0:
            return "NO"
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
        

##Funciones necesarias: eclosure(nodos, lenguaje), move(nodos, cadena, lenguaje)
##Utiliza: todos los estados, todos los simbolos, las transiciones, estado final e inicial 
def dfa_nfa(transiciones, infin):
    
    ## nos retorna los simbolos que existen en nuestras transiciones
    simbolos = []
    for i in range(len(transiciones)):
        if transiciones[i][1] != "e":
            if transiciones[i][1] not in simbolos:
                simbolos.append(transiciones[i][1])
                
        
    #transiciones
    i = 0
    Dstate =[]
    tablita = []
    Dstate.append(eclosure(infin[0][0], transiciones))
    infin_nuevo =[]
    infin_nuevo.append(eclosure(infin[0][0], transiciones))
    
    
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
    
    
    print("Proceso de cambio de NFA a DFA")
    for m in tablita:
        print(m)
    print("--------------------------------------------------------------------------------------")
    ##Editamos lo que nos devuelve ya que tenemos vacios
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
    
    
    print(Dstate)
    print(tablita)
    print(infin_nuevo)
    #cambiamos el estado final y el inicial 
    while x < len(infin_nuevo):
        indice1 = Dstate.index(infin_nuevo[x])
        infin_nuevo[x]= alfabeto[indice1]
        x+=1
    y = []
    
    for i in range(1,len(infin_nuevo)):
        y.append([infin_nuevo[0],infin_nuevo[i]])
    return tablita, y
        
    

#tablita, y = dfa_nfa([[1,"e",2],[1,"e",8],[2,"e",3],[2,"e",4], [3,"a",5], [4,"b",6], [5,"e",7], [6,"e",7], [7,"e",2],[8,"a",9], [9,"e",10], [9,"e",13], [10,"e",11], [10,"e",12], [11,"a",14], [12,"b",15], [13,"e",16], [14,"e",17], [15,"e",17],[16,"e",18],[17,"e",18] ], [[1,18]])
#graficadora(tablita, y)



                
    