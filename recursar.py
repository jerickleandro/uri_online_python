# def oi(vezes):
#     if(vezes>0):
#         vezes -= 1
#         oi(vezes)
#         print(vezes)

# # oi(10)


# def fatorial(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n*fatorial(n-1)

# print(fatorial(1000))

# fat = int(input())
# for c in range (fat):
#    fat = fat*fat-1 
#    c-=1
# print(fat)  
#dividir um numero até chegar em 0,005 e retorna quantas vezes dividiu
d=0
def div(n):
    if(n < 0.5):
        return d
    else:
        div(n)/2
        n=n-1
        return d+1

print(div(1))

#Quantos dias a alga ocupará a pscina. a alga custa 5 a pscina tem o total 10


