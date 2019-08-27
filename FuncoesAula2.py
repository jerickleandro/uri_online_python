import re

def divAporB(a,b):
        if(a%b==0):
                return True
        else:
                return False

def quantaVezesMenor(a,b):
        if(a<b):
                return a/b
        elif(a==b):
                return 0
        else:
                return False


def calculaAreas():
        print("1-Circulo\n2-Triângulo\n3-Retângulo\n")
        op = int(input())
        if(op == 1):
                r = float(input("Digite o raio: "))
                print("A area do circulo é:",areaCirculo(r))
        elif(op == 2):
                b = float(input("Digite o valor da base: "))
                h = float(input("Digite o valor da altura: "))
                print("A area do triângulo é:",areaTriangulo(b,h))
        elif(op == 3):
                b = float(input("Digite o valor da base: "))
                h = float(input("Digite o valor da altura: "))
                print("A area do retângulo é:",areaRetangulo(b,h))
        else:
                print("Opção invalida!")

def areaRetangulo(b,h):
        return b*h
def areaCirculo(r):
        return 3.14*(r*r)
def areaTriangulo(b,h):
        return (b*h)/2


def proximaLetra(letra):
        letraConv = int(ord(letra))
        if(letraConv == 122):
                return 'a'
        elif(letraConv == 90):
                return 'A'
        elif(letraConv>64 and letraConv<91 or letraConv>96 and letraConv<123):
                return chr(letraConv+1)
        else:
                return False

def estaContido(frase,palavra):
        return re.search(palavra,frase, re.IGNORECASE)


