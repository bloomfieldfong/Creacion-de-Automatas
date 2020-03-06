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
respues = []
while i < len(ingreso):
    
    if ingreso[i] == "|":
 
        x = [numero,"e", infin[-2][0]]
        y = [numero,"e",infin[-1][0]]
        inicial = numero
        numero +=1
        z = [infin[-2][1],"e",numero]
        k = [infin[-1][1],"e",numero]
        s = concat[-1]
        concat.pop()
        o = concat[-1]
        concat.pop()
        concat.append([s,o, x,y,z,k])
        final = numero
        numero +=1
        infin.pop()
        infin.pop()
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
        primera = concat[-1]
        concat.pop()
        segunda = concat[-1]
        concat.pop()
        orden_ultima = infin[-1]
        infin.pop()
        orden_penultima = infin[-1]
        infin.pop()
        
        print(orden_ultima )
        print(orden_penultima)
        try:
             for a in range(len(segunda)):
                 for n in range(0,3):
                     if segunda[a][n] == orden_penultima[1]:
                         segunda[a][n] = orden_ultima[0]
                        
        except:
            for a in range(len(x)):
                if segunda[a] == orden_penultima[1]:
                    segunda[a] = orden_ultima[0]
        
        
        
        infin.append([orden_penultima[0], orden_ultima[1]])
        concat.append([segunda, primera])

    elif ingreso[i] != "." and ingreso[i] != "|" and ingreso[i] != "*" :
        concat.append([numero, ingreso[i], numero+1])
        infin.append([numero, numero +1])
        numero +=2
    
    i+=1
print(concat)