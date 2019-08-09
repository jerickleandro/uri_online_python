idade = int(input())

ano = int(idade/365)
resto = idade % 365
mes = int(resto/30)
dia = resto % 30



print(ano,'ano(s)')
print(mes,'mes(es)')
print(dia,'dia(s)')