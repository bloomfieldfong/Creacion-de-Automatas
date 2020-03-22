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
        
def existe2(cadena, lenguaje, infin):
    a = 0
    inicial =[]
    inicial.append(infin[0][0])

    for n in cadena:
        while a<  len(inicial):

            x = move({inicial[a]}, n, lenguaje)
            y = move({inicial[a]}, "e", lenguaje)
            
            x = list(x)
            y = list(y)
            
            if len(x)>0:
                inicial.append(x[0])
            if len(y)>0:
                
                if y[0]== infin[0][1]:
                    return "Yes"
                for z in range(len(y)):
                    x.append(posibles_movimientos(y[z],n, lenguaje))
                
                for p in range(len(x)):
                    if len(x[p])!=0:
                        s = x[p][0]
                        inicial.append(s[2])
                   
            
            a+=1
            
    z = 0
    print(inicial)
    for n in range(len(inicial)):
        if inicial[n] == infin[0][1]:
            z +=1
    
    if z >0:
        return "Yes"
    else:
        return "N0"

#    i = 0
#    print(infin)
#    inicial = infin[0][0]
#    for n in cadena:
#        print(n)
#        x = move(inicial, n, lenguaje)
#        z = move(inicial,"e",lenguaje)
#        if len(x)==0 and move(inicial, "e",lenguaje) ==0:
#            return "NO"
#        x = list(x)
#        print(z)
#        z = list(z)
#        if len(x)>0:
#            inicial = x[0]
#        else:
#            if len(y)==1:
#                inicial = y[0]
#            else:
#                print(m)
#                for m in len(y):
#                    y = move(m[0], n, lenguaje)
#    i = 0 
#    for n in range(len(infin)):
#        if inicial == infin[n][1]:
#            i += 1
#    if i !=0:
#        return "YES"
#    else:
#        return "NO"
#        
#    
    
    
    