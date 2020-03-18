from funciones import * 
def nullable(n, variables):
    if n[0]== "e":
        return True
    if n[0] in variables:
        return n[1]
    

#nos devuelve si es nullable 
def nullable(n,pos):
    null = anteriores_nullables(n,pos)

    if n[pos] == "e":
        return True
    elif n[pos] == "|":
        if len(null)<=2:
            return nullable(n, pos-1) or nullable(n, pos-2)
        else:
            return null[-1] or null[-2]
    elif n[pos] == ".":
        if len(null)<=2:
            return nullable(n, pos-1) and nullable(n, pos-2)
        else:
            return null[-1] and null[-2]
    elif n[pos] == "*":
        return True
    else:
        return False
  
##nos devuelve si es true o false de los nodos anteriores
def anteriores_nullables(n,pos):
    null = []
    posi = ["|", ".", "*"]
    for i in range(pos):
        if n[i] == ".":
            if n[i-1] in posi:
                null.append(null[-1] and nullable(n,i+1))
            else: 
                null.append(nullable(n,i-1) and nullable(n,i-2))
        if n[i] == "|":
            if n[i-1] in posi:
                null.append(null[-1] or null[-2])
            else:
                null.append(nullable(n, i-1) or nullable(n, i-2))
        if n[i] == "*":
            null.append(True)
            
    return null


##firstpos
def firstpos(n, pos):
    fir = anteriores_firtspos(n,pos)
    if n[pos] == "e":
        return 0
    elif n[pos] == "|":
        if len(fir)<=2:
            return firstpos(n, pos-1).union(firstpos(n,pos-2))
        else:
            return fir[-1].union(fir[-2])
    elif n[pos] == ".":
        if len(fir) <=2:
            if nullable(n,pos-2):
                return firstpos(n, pos-1).union(firstpos(n,pos+1))
            else:
                return firstpos(n,pos-2)
        else:
            if nullable(n,pos-2):
                return fir[-1].union(firstpos(n,pos+1))
            else:
                return fir[-1]
    elif n[pos] == "*":
        if len(fir)<=2:
            return firstpos(n, pos-1)
        else:
            return fir[-1]
    else:
        return {pos}
    

def lastposs():
    pass

def nextpos():
    pass

def anteriores_firtspos(n,pos):
    firts = []
    posi = ["|", ".", "*"]
    for i in range(pos):
        if n[i] == ".":
            if n[i-1] in posi:
                if nullable(n,pos-2):
                    firts.append(firts[-1].union(firts[-2]))
                else:
                    firts.append(firts[-2])
            else:
                if nullable(n,i-2):
                    fp1 = firstpos(n,i-1)
                    fp2 = firstpos(n,i-2)
                    firts.append(fp1.union(fp2))
                else:
                    firts.append(firstpos(n,i-2))
                    
        if n[i] == "|":
            if n[i-1] in posi:
                fp1 = firts[-1]
                fp2 = firts[-2]
                firts.append(fp1.union(fp2))
            else:
                fp1 = firstpos(n,i-1)
                fp2 = firstpos(n,i-2)
                firts.append(fp1.union(fp2))
        if n[i] == "*":
            if n[i-1] in posi:
                f = firts[-1]
                firts.append(f)
            else:
                firts.append({n[-2]})
    return firts





print(nullable(['a', 'a', '*', '.', 'b'],4))

print(nullable("i",["i","i","r"]))

