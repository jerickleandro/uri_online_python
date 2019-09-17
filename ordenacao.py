t = int(input("Tamanho do vetor"))
v = []

for i in range(0,t):
    v.append(int(input("Digite numero: ")))

maior = -1000

for i in range(0,t):
    if maior<v[i]:
        maior = v[i]

print(maior)

ordenado = []

for i in range(0,maior):
    ordenado.append(0)

print(ordenado)
for i in range(0,t):
    print(int(v[i]))
    print((ordenado[int(v[i])])+1)
    ordenado.insert(int(v[i]), (ordenado[int(v[i])])+1)

for i in range(0,maior):
    for j in range(0,ordenado[i]):
        print(i)

