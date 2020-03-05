from funciones import * 

#Es un arbolito
class Arbolito:

    def __init__(self, padre, izq, der):
        self.izq = izq
        self.der = der
        self.padre = padre


    def PrintTree(self):
        print(self.padre)
        print(self.izq)
        print(self.der)

ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))

i = 0
trans = []
numero = 0
infin = []
cant = 0
concat = []
while i < len(ingreso):
    
    if ingreso[i] == "|":
        arriba_iz = infin[-2][0]
        abajo_iz = infin[-1][0]
        arriba_der = infin[-2][1]
        abajo_der = infin[-1][1]
        x = [numero,"e",arriba_iz]
        y = [numero,"e",abajo_iz]
        inicial = numero
        numero +=1
        z = [arriba_der,"e",numero]
        k = [abajo_der,"e",numero]
        concat.append([x,y,z,k])
        final = numero
        numero +=1
        infin.pop()
        infin.pop()
        print([inicial, final])
        infin.append([inicial,final])
        
        
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
    
        
        

    elif ingreso[i] == ".":
        x = concat[-1]
        concat.pop()
        y = concat[-1]
        concat.pop()
        automata = infin[-2]
        final = infin[-1][1]

        try:

            for a in range(len(x)):
                for n in range(0,2):
                    if x[a][n] == infin[-1][0]:
                        x[a][n] = automata[1]

        except:
            for a in range(len(x)):
                    if x[a] == infin[-1][0]:
                        x[a] = automata[1]
                        

        infin.pop()
        infin.pop()
        infin.append([automata[0], final])
        concat.append([y,x])

    elif ingreso[i] != "." and ingreso[i] != "|" and ingreso[i] != "*" :
        concat.append([numero, ingreso[i], numero+1])
        infin.append([numero, numero +1])
        numero +=2
    
    i+=1
    
    
    
print(concat)

