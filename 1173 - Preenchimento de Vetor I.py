valor  = int(input())
v = []
tamanhoDoVetorMax =10
v.append(valor)
ultimoValor = valor

for i in range(0,tamanhoDoVetorMax):
    v.append(ultimoValor*2)
    ultimoValor = ultimoValor*2

for j in range(0,tamanhoDoVetorMax):
    print("N[{}] = {}".format(j,v[j]))