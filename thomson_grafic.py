from funciones import * 
from operator import itemgetter
from graphviz import Digraph
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
                
    print("----------------------------------------------")
    print("Q -> Estados")
    print(estados)
    print("----------------------------------------------")
    print("E -> simbolos")
    print(simbolos)
    print("----------------------------------------------")
    print("q0 -> Estado inicial: ")
    for i in range(len(infin)):
        print(infin[i][0])
    print("----------------------------------------------")
    print("F -> Estado de Aceptacion: ")
    for i in range(len(infin)):
        print(infin[i][1])
    print("----------------------------------------------")
    print("Transiciones:")
    print(resultado)
    print("----------------------------------------------")
        
    
##junta los nfa (cuando son mas de 1)
def nfa(resultados, infins):
    
    infins =  sorted(infins, key= itemgetter(1))
    print(infins)
    alto = len(infins)-1
    print(alto)
    numero = infins[alto][1] + 1
    respuesta = flat(resultados, [])
    final = []
    
    for i in range(0,len(infins)):
        respuesta.append([numero,"e",infins[i][0]])
        final.append([numero, infins[i][1]])
        
        
    print(respuesta)
    
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
        
        
    
    
    
    