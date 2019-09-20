velha = [[0,0,0],[0,0,0],[0,0,0]]
jogador_n1 = ""
jogador_n2 = ""
vez = ""


def prencher_matriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[1])):
            matriz[i][j] = int(-1)

def imprime_matriz(matriz):
    for i in range(0,len(matriz)):
        print(matriz[i])

def verifica_ganhador(matriz):
    if(matriz[0][0]==1 and matriz[1][1]==1 and matriz[2][2]==1):
    #Diagonal Principal    
        return True
    elif(matriz[0][2]==1 and matriz[1][1]==1 and matriz[2][0]==1):
    #Diagonal secundaria
        return True
    elif(matriz[0][0]==1 and matriz[1][0]==1 and matriz[2][0]==1):
    #Primeira coluna
        return True
    elif(matriz[0][1]==1 and matriz[1][1]==1 and matriz[2][1]==1):
    #Segunda coluna
        return True
    elif(matriz[0][2]==1 and matriz[1][2]==1 and matriz[2][2]==1):
    #Terceira coluna
        return True
    elif(matriz[0][0]==1 and matriz[0][1]==1 and matriz[0][2]==1):
    #Primeira linha
        return True
    elif(matriz[1][0]==1 and matriz[1][1]==1 and matriz[1][2]==1):
    #Segunda linha
        return True
    elif(matriz[2][0]==1 and matriz[2][1]==1 and matriz[2][2]==1):
    #Terceira linha
        return True
    else:
        return False
    
    
def imprime_vitoria(vez):
    print("Parabenz {}, você ganhou!".format(vez))

def deu_velha(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[1])):
            if(matriz[i][j]==0):
                return False
            else:
                return True

def fim_de_jogo(matriz):
    if(verifica_ganhador(matriz)):
        imprime_vitoria(vez)
        return True
    if(deu_velha(matriz)):
        print("Deu velha, ninguem ganhou!")
        return True
def jogar(vez,jogador_n1,jogador_n2,matriz):
    print("{}, é sua vez.".format(vez))
    imprime_matriz(matriz)
    linha = int(input("Escolha a linha: "))
    coluna = int(input("Escolha a coluna: "))
    if(vez==jogador_n1):
        matriz[linha][coluna] = 'O'
        vez = jogador_n2
    else:
        matriz[linha][coluna] = 'X'
        vez = jogador_n1
    imprime_matriz(matriz)
    if(verifica_ganhador(matriz)):
        verifica_ganhador(matriz)
        return True
    else:
        return False

jogador_n1 = input("Digite o nome do primeiro jogador: ")
jogador_n2 = input("Digite o nome do segundo jogador: ")
vez = jogador_n1

# imprime_matriz(velha)
# prencher_matriz(velha)
# imprime_matriz(velha)

while(jogar(vez,jogador_n1,jogador_n2,velha) is False):
    jogar(vez,jogador_n1,jogador_n2,velha)