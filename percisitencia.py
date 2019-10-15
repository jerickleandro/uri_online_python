dados = open('teste.txt','w')

dados.write('escreva no arquivo \n')

dados.close()

dados = open('teste.txt','a')

dados.write('Essa é a segunda linha\n')

dados.close()


dados = open('teste.txt','r')

linhas = dados.readlines()

print(linhas)

dados.close()