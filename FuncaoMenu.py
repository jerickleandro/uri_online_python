def realizaSoma(a,b):
    print(a+b)
def realizaSubtracao(a,b):
    print(a-b)
def realizaMult(a,b):
    print(a*b)
def realizaDiv(a,b):
    if(b!=0):
        print(a/b)
    else:
        print("Não é possivel dividir por 0")

opt = int(input('Digite uma opção: \n1-Soma\n2-subtração\n3-Multiplicação\n4-Divisão\n'))

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

if(opt == 1):
    realizaSoma(a,b)
elif(opt == 2):
    realizaSubtracao(a,b)
elif(opt == 3):
    realizaMult(a,b)
elif(opt == 4):
    realizaDiv(a,b)
else:
    print("Opção invalida")
