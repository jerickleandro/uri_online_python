value = float(input())

real = int(value)
centavo = value % real
centavo = (int(round(centavo, 2)*100))
cem = int(real/100)
resto = (real % 100)
cinq = int(resto / 50)
resto = (resto % 50)
vinte = int(resto/20)
resto = (resto % 20)
dez = int(resto/10)
resto = (resto % 10)
cinc = int(resto/5)
resto = (resto%5)
dois = int(resto/2)
resto = (resto%2)
um = resto


cinqc = int(centavo / 50)
resto = (centavo % 50)
vintec = int(resto/25)
resto = (resto % 25)
dezc = int(resto/10)
resto = (resto % 10)
cincc = int(resto/5)
resto = (resto%5)
umc = int(resto)

print('NOTAS:')
print(cem, 'nota(s) de R$ 100.00')
print(cinq, 'nota(s) de R$ 50.00')
print(vinte, 'nota(s) de R$ 20.00')
print(dez, 'nota(s) de R$ 10.00')
print(cinc, 'nota(s) de R$ 5.00')
print(dois, 'nota(s) de R$ 2.00')

print('MOEDAS:')
print(um, 'moeda(s) de R$ 1.00')
print(cinqc, 'moeda(s) de R$ 0.50')
print(vintec, 'moeda(s) de R$ 0.25')
print(dezc, 'moeda(s) de R$ 0.10')
print(cincc, 'moeda(s) de R$ 0.05')
print(umc, 'moeda(s) de R$ 0.01')