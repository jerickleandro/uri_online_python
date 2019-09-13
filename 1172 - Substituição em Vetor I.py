vetor = []
for i in range(0,10):
    vetor.append(int(input()))

for j in range(0,10):
    if(vetor[j]<=0):
        print("X[{}] = 1".format(j))
    else:
        print("X[{}] = {}".format(j,vetor[j]))
        