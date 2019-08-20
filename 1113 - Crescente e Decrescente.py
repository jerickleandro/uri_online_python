while(True):
    entrada = input()
    X = int(entrada.split(" ")[0])
    Y = int(entrada.split(" ")[1])
    if(X == Y):
        break
    elif(X > Y):
        print('Decrescente')
    else:
        print('Crescente')