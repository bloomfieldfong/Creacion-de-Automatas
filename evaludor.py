from funciones import * 


        


ingreso = infix_to_postfix(expandir(input("Ingrese un lenguaje: ")))
print(ingreso)
i = 0
trans = []
numero = 0
infin = []
cant = 0
concat = []
respuesta = []
while i < len(ingreso):
    
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
        
    elif ingreso[i] != "." and ingreso[i] != "|" and ingreso[i] != "*" :
        concat.append([numero, ingreso[i], numero+1])
        infin.append([numero, numero +1])
        numero +=2
    
    i+=1
    
print(flat(concat,[]))