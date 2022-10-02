

numeros= [-14, 18, 17, 20, 5, 51, 7]
def separar(*args):
    lista= sorted(args)
    pares= []
    impares= []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares

    
pares, impares = separar(*numeros)
print(pares) 
print(impares)