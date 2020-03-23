from funciones import * 
from operator import itemgetter
from graphviz import Digraph
from subconjuntos import *
import os
##environment de mi graficadora
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

def thomson_grafic(ingreso, numero = 2):
        #variables iniciales

    i = 0
    trans = []
    infin = []
    cant = 0
    concat = []
    respuesta = []

    while i < len(ingreso):
        
        ## si se ingresa un or entonces crea la grafica 
        if ingreso[i] == "|":
     
            s = concat[-1]
            concat.pop()
            o = concat[-1]
            concat.pop()
            concat.append([s,o, [numero,"e", infin[-2][0]],[numero,"e",infin[-1][0]],[infin[-2][1],"e",numero+1],[infin[-1][1],"e",numero+1]])
            inicial = numero
            final = numero +1
            numero +=2
            infin.pop()
            infin.pop()
            infin.append([inicial,final])
            
            
        ## se realiza kle
        elif ingreso[i] == "*":
        
            inicial = infin[-1][0]
            final = infin[-1][1]
            x = [numero, "e", inicial]
            y = [final, "e", inicial]
            inicial = numero
            numero +=1
            z = [final, "e", numero]
            k = [inicial, "e", numero]
            final = numero
            v = concat[-1]
            concat.pop()
            concat.append([v,x,y,z,k])
            infin.pop()
            infin.append([inicial, final])
            numero += 1
        
        ##concatenacion
        elif ingreso[i] == ".":
            primera = concat[-1]
            concat.pop()
            segunda = concat[-1]
            concat.pop()
            orden_ultima = infin[-1]
            infin.pop()
            orden_penultima = infin[-1]
            infin.pop()
            try:
                 segunda = flat(segunda, [])
                 for a in range(len(segunda)):
                     for n in range(0,3):
                         if segunda[a][n] == orden_penultima[1]:
                             segunda[a][n] = orden_ultima[0]
                            
            except:
                for a in range(len(segunda)):
                    if segunda[a] == orden_penultima[1]:
                        segunda[a] = orden_ultima[0]
            

            infin.append([orden_penultima[0], orden_ultima[1]])
            concat.append([segunda, primera])
        
        ##variable nomral
        elif ingreso[i] != "." and ingreso[i] != "|" and ingreso[i] != "*" :
            concat.append([numero, ingreso[i], numero+1])
            infin.append([numero, numero +1])
            numero +=2
        
        i+=1

    resultado = sorted(flat(concat,[]), key= itemgetter(0))
    return resultado, infin


##imprime el automata
#resultado = las transiciones del automata
#infin = estado inicial y final
def impresion(resultado, infin):
    
    estados = []
    simbolos = []
    for i in range(len(resultado)):
        if resultado[i][0] not in estados:
            estados.append(resultado[i][0])
                
        if resultado[i][2] not in estados:
            estados.append(resultado[i][2])
                
        if resultado[i][1] not in simbolos:
            simbolos.append(resultado[i][1])
                
    print("--------------------------------------------------------------------------------------")
    print("Q -> Estados")
    print(estados)
    print("--------------------------------------------------------------------------------------")
    print("E -> simbolos")
    print(simbolos)
    print("--------------------------------------------------------------------------------------")
    print("q0 -> Estado inicial: ")
    for i in range(len(infin)):
        print(infin[i][0])
    print("--------------------------------------------------------------------------------------")
    print("F -> Estado de Aceptacion: ")
    for i in range(len(infin)):
        print(infin[i][1])
    print("--------------------------------------------------------------------------------------")
    print("Transiciones:")
    print(resultado)
    print("--------------------------------------------------------------------------------------")
        
    
##junta los nfa (cuando son mas de 1)
#resultado = las transiciones del automata
#infin = estado inicial y final
def juntar_nfa(resultados, infins):
    
    infins =  sorted(infins, key= itemgetter(1))

    alto = len(infins)-1

    numero = infins[alto][1] + 1
    respuesta = flat(resultados, [])
    final = []
    
    for i in range(0,len(infins)):
        respuesta.append([numero,"e",infins[i][0]])
        final.append([numero, infins[i][1]])
        
    
    return respuesta, final
        
        
        
def graficadora(resultado, infin):
    f = Digraph('finite_state_machine', filename='./automata.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    for i in range(len(infin)):
        f.node(str(infin[i][1]))
    f.attr('node', shape='circle')
    for i in range(len(resultado)):
        f.edge(str(resultado[i][0]), str(resultado[i][2]), label= str(resultado[i][1]))

    f.view()
   
   
   
def posbile_e(cadena, lenguaje, infin):
    y = move([infin[0]], "e", lenguaje)
    x = []
    y = list(y)
    
    i = 0
    while i < len(y):
        nuevo = list(move([y[i]], "e", lenguaje))
        x.append([y[i],"e" ,move([y[i]], "e", lenguaje)])
        x.append([y[i],cadena ,move([y[i]], cadena, lenguaje)])
        if len(nuevo)>0:
            for u in range(len(nuevo)):
                if nuevo[u] not in y:
                    y.append(nuevo[u])
        
        i+=1
    
    
    pos = []
    for i in range(len(y)):
        if len(move([y[i]], cadena, lenguaje)) > 0:
            pos.append(y[i])
        
        
    ol = []

    pos = set(pos)
    x = x[::-1]
    a = 0
    while a < len(pos):
        for i in range(len(x)):
            if len(pos.intersection(x[i][2]))>0 :
              
                pos.add(x[i][0])     
        a+=1

    return pos


def fin(nodo, lenguaje, infin):
    
    x = posibles_movimientos(nodo,"e", lenguaje)
    i = 0
    while i < len(x):
        a = posibles_movimientos(x[i][2], "e", lenguaje)
        for m in range(len(a)):
            if a[m] not in x:
                x.append(a[m])
        i+=1
        
    l = 0
    for i in range(len(x)):
        if x[i][2] == infin[0][1]:
            l+=1

    if l >0:
        return "YES"
    else:
        return "NO"
    

def cambio(cadena, lenguaje, infin_n):
    
    estados = []
    for i in range(len(lenguaje)):
        if lenguaje[i][0] not in estados:
            estados.append(lenguaje[i][0])
                
        if lenguaje[i][2] not in estados:
            estados.append(lenguaje[i][2])
        
    alfabeto =["A","B","C","D","E","F","G","H","I","J", "K", 'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','BB','CC','DD']
    x = 0 
    while x < len(lenguaje):
        indice1 = estados.index(lenguaje[x][0])
        lenguaje[x][0] = alfabeto[indice1]
        indice1 = estados.index(lenguaje[x][2])
        lenguaje[x][2] = alfabeto[indice1]
        x +=1
        
    x = 0

    #cambiamos el estado final y el inicial

    infin = [0,0]
    while x < len(infin_n[0]):
        indice1 = estados.index(infin_n[0][x])
        infin[x]= alfabeto[indice1]
        x+=1
    y = []
    
    x = 0
    a = 0
    inicial =[]
    inicial.append(infin[0][0])
    x = posbile_e(cadena[0], lenguaje, infin[0])
  
    s = set(infin[0])
    m = 0
    for i in range(len(cadena)):
        x = posbile_e(cadena[i], lenguaje, list(s))
        m = 0
        while m < len(x):
            x  = list(x)
            s = move([x[m]],cadena[i],lenguaje)
            m+=1
    try: 
        if existe(cadena, lenguaje, [infin]) == "YES":
            return "YES"
    except:
        print("")

            
def existe2(cadena, lenguaje, infin):
    lenguaje.append([infin[0][1]+1, "e", infin[0][1]])
    infin= [[infin[0][1]+1, infin[0][1]]]
    estados = []
    for i in range(len(lenguaje)):
        if lenguaje[i][0] not in estados:
            estados.append(lenguaje[i][0])
                
        if lenguaje[i][2] not in estados:
            estados.append(lenguaje[i][2])
            
    for i in estados:
        lenguaje.append([i,"e",i])
        

        
    x = 0
    a = 0
    inicial =[]
    inicial.append(infin[0][0])
    x = posbile_e(cadena[0], lenguaje, infin[0])
    s = set(infin[0])
  
    for i in range(len(cadena)):
        x = posbile_e(cadena[i], lenguaje, list(s))
        m = 0
        while m < len(x):
            x  = list(x)
            s = move([x[m]],cadena[i],lenguaje)
            m+=1
    

    if fin(list(s)[0], lenguaje, infin) == "YES" or cambio(cadena, lenguaje, infin) == "YES":
        return 'YES'
    else:
        return "NO"

   
    
    

#    for n in range(len(cadena)):
#        while a<  len(inicial):
#            print(inicial)
#
#            x = move({inicial[a]}, cadena[n], lenguaje)
#            y = move({inicial[a]}, "e", lenguaje)
#            
#            
#        
#            x = list(x)
#            y = list(y)
#   
#            if y[0] == infin[0][1] and len(cadena)-1 == n:
#                return "YE"
#            
#            if len x == 0:
#                a-=1
#            if len(x)>0:
#                inicial.append(x[0])
#                
#            if len(y)>0:
#                for z in range(len(y)):
#                    x.append(posibles_movimientos(y[z],"e", lenguaje))
#                
#                for p in range(len(x)):
#                    if len(x[p])!=0:
#                        s = x[p][0]
#                        inicial.append(s[2])
#            a+=1
#            
#    z = 0
#    print(inicial)
#    print(x)
#    
#    if inicial[len(inicial)-1] == infin[0][1]:
#        return "yes"
#    else:
#        return "no"
