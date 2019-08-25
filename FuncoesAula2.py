def divAporB(a,b):
    if(a%b==0):
        return True

def proximaLetra(a):
        teste = int(ord(a))
        return chr(teste+1)

a = input("Digite uma letra")
b = proximaLetra(a)
print("A proxima letra é ",b)