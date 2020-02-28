##########################################
##  Universidad del Valle de Guatemala  ##
##  Diseño de Lenguajes de programacion ##
##  Michelle Bloomfield Fong            ##
##  Carne: 16803                        ##
##########################################


# nos definie la precedencia entre operadores
def precedencia(op): 
    if op == '*' or op == '/': return 2
    if op == '|' or op == '-': return 1
    if op == "(": return 3
    else: return 0


def listToStr(cadena):
    nueva = ''
    for i in range(0,len(cadena)):
        nueva = nueva + str(cadena[i])         
    return nueva 
    
def expandir(cadena):
  stack = []
  variable = []
  i = 0
  catn_parentesis = 1
  while i < len(cadena):
    variable.append(cadena[i])
    if cadena[i] == "?":
      if cadena[-2] == ")":
        parentesis = []
        x = i
        while cadena[x] != "(":
          catn_parentesis += 1
          parentesis.append(cadena[x])
          variable.pop()
          x-= 1
          
        x = parentesis[::-1]
        x.pop()
        y  =  "("+listToStr(x)+"|e)"
        variable.append(y)
      else: 
        variable[i-1] = "("+variable[-2]+"|e)"
    i+=1
  print(listToStr(variable))

    
#Cambia de infix a postdfix
def infix_to_postfix(cadena):
  
  #operadores validos
  op_validos = ["|", "*",]
  ##stack
  stack = []
  ##output
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
        #se agrega el ultimo valor de stack a mi output
        valores.append(stack[x])
        #se realiza pop del ultimo numero
        stack.pop()
        x-=1
      # elimina el parentesis abierto
      stack.pop()
      
    ##Si es un operador entonces se agrega al stack (depende de presedencia)
    elif cadena[i] in op_validos:
      #Revisa si el stack no esta vacio
      if len(stack) == 0: 
        stack.append(cadena[i])
      else:
        #Si el operador anterior no es un parentesis
        if stack[-1] != '(':
          #Si la precendencia de la cadena es menor a la del stack
          if precedencia(cadena[i]) < precedencia(stack[-1]):
            #Si en el stack solo hay un objeto
            z = len(stack) - 1
            if z != 0:
                #Se saca todo del stack y se agrega el valor nuevo al stack
                #se saca todos menos el parentesis
                while stack[z] != '(':
                  valores.append(stack[-1])
                  stack.pop()
                  z -= 1
                stack.append(cadena[i])
            else:
                #Se saca lo que hay y se agrega el valor nuevo  
                valores.append(stack[-1])
                stack.pop()
                stack.append(cadena[i])
          #si la precedencia es mayor se agrega al stack
          elif precedencia(cadena[i]) >= precedencia(stack[-1]): 
            stack.append(cadena[i])
        else:
          #Si no hay nada solo se agrega al stack
          stack.append(cadena[i])
    ##si es un valor se agrega a los valores
    else:
      valores.append(cadena[i])
    ##contador
    i+=1

  ##Si se termino el ciclo y aun hay cosas en el stack entonces las saca
  if len(stack) !=0: 
    for i in range (len(stack)):
      valores.append(stack[-1])
      stack.pop()
  print(valores)


infix_to_postfix("(a|b*)")

expandir("(a|b*)?")
