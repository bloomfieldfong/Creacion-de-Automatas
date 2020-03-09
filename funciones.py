##########################################
##  Universidad del Valle de Guatemala  ##
##  Diseño de Lenguajes de programacion ##
##  Michelle Bloomfield Fong            ##
##  Carne: 16803                        ##
##########################################


# nos definie la precedencia entre operadores
def precedencia(op):
    if op == '*':
        return 3
    if op == '|':
        return 2
    
    if op == ".":
        return 1
    if op == "(":
        return 3
    else:
        return 0

#cambia de lista a string
def listToStr(cadena):
    nueva = ''
    for i in range(0, len(cadena)):
        nueva = nueva + str(cadena[i])
    return nueva

#cambia de string a lista
def str_to_list(cadena):
    i = 0
    nueva = []
    while i< len(cadena):
        nueva.append(cadena[i])
        i+= 1
    return nueva


def flat(l, a):
    x = []
    for i in l:
        if isinstance(i, list):
            flat(i, a)
        else:
            a.append(i)
    
    for i in range(0,len(a),3):
        if i != len(a):
            x.append([a[i],a[i+1],a[i+2]])
    
    return x

            

##Expande la expresion que vamos a ingresar
## cambia el ? = |3 y el a+ = aa*
def expandir(cadena):
    
    
    nueva = []
    nueva2 = []
    aqui = 0
    #recorre la cadena
    for n in cadena:
        #si la no es ? o + entonces agrega a la nueva lista
        if n != "?" and n != "+":
            nueva.append(n)
        #si es ? o +  
        if n == "?" or n == "+":
            aqui +=1
            # si existe algun parentesis y es ? o + 
            if (n == "?" and nueva[-1] != ")") or (n == "+" and nueva[-1] != ")"):
                aqui +=1
                x = True
                z = len(nueva)-1
                while x == True and z != -1:
                    #si no es un parentesis o una concatenacion
                    if nueva[z] == ")" or nueva[z] == ".":
                        #elimina el ultimo 
                        nueva.pop()
                        x = False
                    else:
                        #agrega a nuestra nueva lista lo ultimo
                        nueva2.append(nueva[z])
                        nueva.pop()
                    z-=1
                #agrega a nuestra lista un str cambiado
                if n == "?":
                   
                    aqui +=1
                    nueva.append(str("("+listToStr(nueva2[::-1])+"|e)"))
                #agrega a nuestra lista un str cambiado
                elif n == "+":
       
                    aqui +=1
                    nueva.append(str("("+listToStr(nueva2[::-1])+").("+listToStr(nueva2[::-1])+"*)"))
                nueva2 = []
            #else no es un parentesis el ultimo
            else: 
                v = len(nueva)-1
                z = True
                while z == True:
                    ##busca hasta encontrar un parentesis cerrado
                    if nueva[v] == "(" :
                        nueva2.append("(")
                        nueva.pop()
                        z = False
                    else:
                        #agrega lo cadena hasta encontrar un parentesis
                        nueva2.append(nueva[v])
                        nueva.pop()
                    v-=1
                if n == "?":
                    aqui +=1
                    #agrega a nuestra lista un str cambiado
                    
                    nueva.append(str("("+listToStr(nueva2[::-1])+"|e)"))
                elif n == "+":
                    aqui +=1
                    #agrega a nuestra lista un str cambiado
            
                    nueva.append(str("("+listToStr(nueva2[::-1])+").("+listToStr(nueva2[::-1])+"*)"))
                nueva2 = []
    
    print(nueva)
    
    i = 0
    
    asd = str_to_list(nueva)
    
    
    if asd[0] == ".":
        asd.pop(0)
    

        
    return listToStr(asd)

# Cambia de infix a postdfix
def infix_to_postfix(cadena):
    

    # operadores validos
    op_validos = ["|", "*", "."]
    # stack
    stack = []
    # output
    valores = []
    i = 0

    while i < len(cadena):
        

        # Si tenemos un parantesis abierto entonces se ira al stack
        if cadena[i] == "(":
            stack.append(cadena[i])

        # Si es un parentesis cerrado entonces saca todo del stack
        # hasta encontrar un parentesis abierto
        elif cadena[i] == ")":
            x = len(stack) - 1
            while stack[x] != "(":
                # se agrega el ultimo valor de stack a mi output
                valores.append(stack[x])
                # se realiza pop del ultimo numero
                stack.pop()
                x -= 1
            # elimina el parentesis abierto
            stack.pop()

        # Si es un operador entonces se agrega al stack (depende de presedencia)
        elif cadena[i] in op_validos:
            # Revisa si el stack no esta vacio
            if len(stack) == 0:
                stack.append(cadena[i])
            else:
                # Si el operador anterior no es un parentesis
                if stack[-1] != '(':
                    # Si la precendencia de la cadena es menor a la del stack
                    if precedencia(cadena[i]) < precedencia(stack[-1]):
                        # Si en el stack solo hay un objeto
                        z = len(stack) - 1
                        if z != 0:
                            # Se saca todo del stack y se agrega el valor nuevo al stack
                            # se saca todos menos el parentesis
                            while stack[z] != '(':
                                valores.append(stack[-1])
                                stack.pop()
                                z -= 1
                            stack.append(cadena[i])
                        else:
                            # Se saca lo que hay y se agrega el valor nuevo
                            valores.append(stack[-1])
                            stack.pop()
                            stack.append(cadena[i])
                    # si la precedencia es mayor se agrega al stack
                    elif precedencia(cadena[i]) >= precedencia(stack[-1]):
                        stack.append(cadena[i])
                else:
                    # Si no hay nada solo se agrega al stack
                    stack.append(cadena[i])
        # si es un valor se agrega a los valores
        else:
            valores.append(cadena[i])
        # contador
        i += 1

    # Si se termino el ciclo y aun hay cosas en el stack entonces las saca
    if len(stack) != 0:
        for i in range(len(stack)):
            valores.append(stack[-1])
            stack.pop()
            
    
    return valores


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result




