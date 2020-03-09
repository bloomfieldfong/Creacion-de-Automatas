from funciones import * 
from operator import itemgetter
from graphviz import Digraph
import os
from thomson_grafic import *
from subconjuntos import *

##environment de mi graficadora
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

x = True
while x:
    
    menu = input("1. Contruccion de Thomson \n2. Contruccion de Subconjuntos \n3. NFA \n4. DFA\n")

    ##crea un grafo con la contruccion de Thomson
    if menu == "1":
        ##ingrese el lenguaje 
        ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
        ##resultado son los movimientos y infin es el estado inicial y el final
        resultado, infin = thomson_grafic(ingreso)
        #imprime el automata
        impresion(resultado,infin)
        ##Grafica nuestro automata
        #graficadora(resultado, infin)
        print(infin)
        mensaje = input("Ingrese el mensaje que desea saber si pertenece al lenguaje: ")
        
        
        
    ##crea un grafo con la contruccion de Thomson y utiliza lols subconjuntos para realizar un dfa 
    if menu == "2":
        ##ingrese el lenguaje 
        ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
        ##resultado son los movimientos y infin es el estado inicial y el final
        resultado, infin = thomson_grafic(ingreso)
        #imprime el automata
        impresion(resultado,infin)
        ##Grafica nuestro automata
        #graficadora(resultado, infin)
        
    if menu == "3":
        
        ##Nos pregunta cuantos lenguajes vamos a utilizar
        ingreso_cantidad = int(input("Cuantos lenguajes ingresara: "))
        resultados = []
        infins = []
        cantidad = 2
        ##ingrese la cantidad de lenguajes que se estaran ingresando
        for i in range((ingreso_cantidad)):
            ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
            resultado, infin = thomson_grafic(ingreso, cantidad)
            resultados.append(resultado)
            print(infin)
            infins.append(infin[0])
            cantidad = infin[0][1] + 1
            
        resultado, final = nfa(resultados, infins)
        
        impresion(resultado, final)

        ##Grafica nuestro automata
        #graficadora(resultado, final)


