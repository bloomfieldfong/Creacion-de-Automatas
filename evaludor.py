from funciones import * 
from operator import itemgetter
from graphviz import Digraph
import os
from thomson_graphic import *

##environment de mi graficadora
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

x = True
while x:
    
    menu = input("1. Contruccion de Thomson \n2. Contruccion de Subconjuntos \n3. NFA \n4. DFA\n")
    ##Ingrese el numero 
    

    ##crea un grafo con la contruccion de Thomson
    if menu == "1":
        
        ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
        resultado, infin = thomson_grafic(ingreso)
        
        impresion(resultado,infin)
        ##Grafica nuestro automata 
        f = Digraph('finite_state_machine', filename='./automata.gv')
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='doublecircle')
        f.node(str(infin[0][1]))
        f.attr('node', shape='circle')
        for i in range(len(resultado)):
            f.edge(str(resultado[i][0]), str(resultado[i][2]), label= str(resultado[i][1]))

        f.view()

    if menu == "3":
        
        ingreso_cantidad = int(input("Cuantas expresiones ingresara: "))
        resultados = []
        infins = []
        cantidad = 2 
        for i in range((ingreso_cantidad)):
            print(i)
            ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
            resultado, infin = thomson_grafic(ingreso, cantidad)
            resultados.append(resultado)
            print(infin)
            infins.append(infin[0])
            cantidad = infin[0][1] + 1
            
        resultado, final = nfa(resultados, infins)
        
        impresion(resultado, final)

        ##Grafica nuestro automata 
        f = Digraph('finite_state_machine', filename='./automata.gv')
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='doublecircle')
        
        for n in range(len(final)):
            f.node(str(final[n][1]))
            
        f.attr('node', shape='circle')
        for i in range(len(resultado)):
            f.edge(str(resultado[i][0]), str(resultado[i][2]), label= str(resultado[i][1]))

        f.view()

        


