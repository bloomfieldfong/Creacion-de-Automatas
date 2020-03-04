from funciones import * 

class Arbolito:

    def __init__(self, padre, izq, der):

        self.izq = izq
        self.der = der
        self.padre = padre


    def PrintTree(self):
        print(self.padre)
        print(self.izq)
        print(self.der)

root = Arbolito("*", Arbolito("*","",""), ",")

root.PrintTree()


ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
print(ingreso)



