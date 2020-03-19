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
    
    menu = input("1. Contruccion de Thomson \n2. Contruccion de Subconjuntos \n3. Constuccion de de DFA de multiples automatas (Thomson y Subconjuntos)  \n4. Metodo directo\n")
    ##crea un grafo con la contruccion de Thomson
    if menu == "1":
        ##ingrese el exppresion 
        ingreso = infix_to_postfix(expandir(input("Ingrese una expresion: ")))
        
        
        i = 0
        while i < len(ingreso):
            if ingreso[i] == "(":
                ingreso.pop(i)
                i-=1
            i+=1
                
        print(ingreso)
                
        ##resultado son los movimientos y infin es el estado inicial y el final
        resultado, infin = thomson_grafic(ingreso)
        #imprime el automata
        impresion(resultado,infin)
        ##Grafica nuestro automata
        graficadora(resultado, infin)
        
        
        
    ##crea un grafo con la contruccion de Thomson y utiliza lols subconjuntos para realizar un dfa 
    if menu == "2":
        ##ingrese la expresion 
        ingreso = infix_to_postfix(expandir(input("Ingrese una expresion: ")))
        print(ingreso)
        ##resultado son los movimientos y infin es el estado inicial y el final
        resultado, infin = thomson_grafic(ingreso)
        tabla, infin_nuevo = dfa_nfa(resultado, infin)
        
        #imprime el automata
        impresion(tabla,infin_nuevo)
        ##Grafica nuestro automata
        graficadora(tabla, infin_nuevo)
        ##mensaje que queremos ver si existe
        mensaje = input("Ingrese el mensaje que desea saber si pertenece al lenguaje: ")
        print(existe(mensaje, tabla, infin_nuevo))
        
    if menu == "3":

        ## ingresa la cantidad de expresiones que se ingresaran
        ingreso_cantidad = int(input("Cuantas expresiones ingresara: "))
        resultados = []
        infins = []
        cantidad = 2
        ##realiza los automatas
        for i in range((ingreso_cantidad)):
            ingreso = infix_to_postfix(expandir(input("Ingrese una expresion: ")))
            resultado, infin = thomson_grafic(ingreso, cantidad)
            resultados.append(resultado)
            infins.append(infin[0])
            cantidad = infin[0][1] + 1

        #nos realiza un automata por todas las 
        resultado, final = juntar_nfa(resultados, infins)
        ##nfa a dfa
        tabla, infin_nuevo = dfa_nfa(resultado, final)
        #impresion de el automata
        impresion(tabla, infin_nuevo)
        #grafica el automata 
        graficadora(tabla, infin_nuevo)
        ##mensaje que queremos ver si existe
        mensaje = input("Ingrese el mensaje que desea saber si pertenece al lenguaje: ")
        print(existe(mensaje, tabla, infin_nuevo))
        
    if menu == "4":
        pass
        
        

