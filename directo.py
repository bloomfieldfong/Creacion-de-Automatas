def nullable(n, variables):
    if n[0]== "e":
        return True
    if n[0] in variables:
        return n[1]
    

def fistpos():
    pass

def lastposs():
    pass

def nextpos():
    pass

print(nullable("i",["i","i","r"]))

