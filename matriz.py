matriz = [[0,0,0],[0,0,0],[0,0,0]]
# print(matriz[1][1])
# matriz[1][1] = 20
# print(matriz[1][1])
def preencheMatriz(matriz):
    for i in range(0,3):
        for j in range(0,3):
            matriz[i][j] = int(input("Digite um numero no indice {} {}: ".format(i,j)))
    print(matriz)
def matrizIdentidade(matriz):
    for i in range(0,3):
        for j in range(0,3):
            if(i==j):
                if(matriz[i][j]!=1):
                    return False
            else:
                if(matriz[i][j]!=0):
                    return False
    return True


preencheMatriz(matriz)

if(matrizIdentidade(matriz)):
    print("Essa matriz é identidade")
else:
    print("Essa matriz não é identidade")


