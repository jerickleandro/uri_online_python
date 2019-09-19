velha = [[0,0,0],[0,0,0],[0,0,0]]
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
    
    

        
imprime_matriz(velha)
prencher_matriz(velha)
imprime_matriz(velha)