from funciones import * 
from operator import itemgetter
from graphviz import Digraph
import os

##environment de mi graficadora
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

##Ingrese el numero 
ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
print(ingreso)

#variables iniciales
i = 0
trans = []
numero = 2
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
print(resultado)

##Grafica nuestro automata 
f = Digraph('finite_state_machine', filename='./automata.gv')
f.attr(rankdir='LR', size='8,5')
f.attr('node', shape='doublecircle')
f.node(str(infin[0][1]))
f.attr('node', shape='circle')
for i in range(len(resultado)):
    f.edge(str(resultado[i][0]), str(resultado[i][2]), label= str(resultado[i][1]))

f.view()

