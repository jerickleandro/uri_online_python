def pg(num ):
    if(num == 1):
        return 1
    else:
        return pg(num-1)*9
i = 51
while i>= 1:
    print(pg(i))
    i=i-1 

for c in range(1,51):
    print(pg(c))



