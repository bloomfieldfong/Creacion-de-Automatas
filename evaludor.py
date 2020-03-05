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
print(ingreso)


i = 0
trans = []
numero = 0
while i < len(ingreso):
    
    if ingreso[i] == "|":
        arriba_iz = trans[-2][0]
        abajo_iz = trans[-1][0]
        arriba_der = trans[-2][2]
        abajo_der = trans[-1][2]
        trans.append([numero,"e",arriba_iz])
        trans.append([numero,"e",abajo_iz])
        numero +=1
        trans.append([arriba_der,"e",numero])
        trans.append([abajo_der,"e",numero])
        numero +=1
        
    if ingreso[i] == "*":
        pass
    if ingreso[i] == ".":
        x = trans[-1]
        trans.pop()
        trans.append([trans[-1][2],x[1],x[2]])
    elif ingreso[i] != "." and ingreso[i] != "|" and ingreso[i] != "*" :
        trans.append([numero, ingreso[i], numero+1])
        numero +=2
        
    print(trans)

    i+=1

print(trans)



