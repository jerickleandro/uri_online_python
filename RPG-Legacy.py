op = True
print("Bem vindo ao sistema de RPG Legacy, vamos começar?")
name = input("Primeiramente digite seu nome:\n")
print("Muito bem {} agora digite a opção referente a sua raça:".format(name))
while(op): 
    raca = int(input("1 - HUMANO\n2 - ELFO\n3 - ANÃO\n"))
    if(raca == 1):
        print("Boa escolha {}, agora você é um HUMANO".format(name) )
        op = False
    elif(raca == 2):
        print("Boa escolha {}, agora você é um ELFO".format(name) )
        op = False
    elif(raca == 3):
        print("Boa escolha {}, agora você é um ANÃO".format(name) )
        op = False
    else:
        print("Opção Invalida. Escolha novamente")
        op = True
print("GAME OVER!")