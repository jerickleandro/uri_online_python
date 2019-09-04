def menorList(numeros):
    if(numeros[0]):
        menor = numeros[0]
        for i in range(0,len(numeros)):
            if(numeros[i] <= menor):
                menor = numeros[i]
        return menor
    else:
        return False

def maiorList(numeros):
    if(numeros[0]):
        maior = 0
        for i in range(0,len(numeros)):
            if(numeros[i] >= maior):
                maior = numeros[i]
        return maior
    else:
        return False

def mediaList(numeros):
    if(numeros[0]):
        soma = 0
        media = len(numeros)
        for i in range(0, len(numeros)):
            soma = soma + numeros[i]
        return soma/media
    else:
        return False

def imparesList(numeros):
    if(numeros[0]):
        impares = []
        for i in range(0,len(numeros)):
            if(numeros[i]%2!=0):
                impares.append(numeros[i])
        return impares
    else:
        return False

def div5List(numeros):
    if(numeros[0]):
        divis = []
        for i in range(0,len(numeros)):
            if(numeros[i]%5==0):
                divis.append(numeros[i])
        return divis
    else:
        return False

def mediaPresList(numeros):
    if mediaList(numeros) in numeros:
        return True
    else:
        return False

def somatorioList(numeros):
    if(numeros[0]):
        soma = 0
        for i in range(0, len(numeros)):
            soma = soma + numeros[i]
        return soma
    else:
        return False

def varianciaList(numeros):
    somatorio = 0
    for i in range(0, len(numeros)):
        somatorio = somatorio +((numeros[i]-mediaList(numeros))**2)    
    return somatorio/(len(numeros)-1)





def modaList(numeros):
    if(numeros):
        moda = 0
        maior = 0
        for i in range(0,len(numeros)):
            soma = 0
            for j in range(0,len(numeros)):
                if(numeros[i]==numeros[j]):
                    soma += 1
                    if(soma>maior):
                        moda = numeros[i]
            
        return moda
    return False


teste = [2,4,5,5,4,2,1,3,5]
var = [17,15,23,7,9,13,7]
var2 = []

print(menorList(teste))
print("{:.2f}".format(mediaList(teste)))
print(imparesList(teste))
print(div5List(teste))
print(mediaPresList(teste))
print(somatorioList(teste))
print(varianciaList(var))
print(modaList(var2))
# print(modaList(teste))

# print(teste.index(6))