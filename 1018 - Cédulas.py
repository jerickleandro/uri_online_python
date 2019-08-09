valor = int(input())
cem = int(valor/100)
resto = valor % 100
cinq = int(resto/50)
resto = resto % 50
vint = int(resto/20)
resto = resto % 20
dez = int(resto/10)
resto = resto % 10
cinc = int(resto/5)
resto = resto % 5
dois = int(resto/2)
resto = resto % 2
um = int(resto/1)

print(valor)
print(cem, 'nota(s) de R$ 100,00')
print(cinq, 'nota(s) de R$ 50,00')
print(vint, 'nota(s) de R$ 20,00')
print(dez, 'nota(s) de R$ 10,00')
print(cinc, 'nota(s) de R$ 5,00')
print(dois, 'nota(s) de R$ 2,00')
print(um, 'nota(s) de R$ 1,00')
