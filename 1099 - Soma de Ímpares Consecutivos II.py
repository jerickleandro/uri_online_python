N = int(input())

for c in range(1,N+1):
    text = input()
    
    X = int(text.split(" ")[0])
    
    Y = int(text.split(" ")[1])
    
    soma = 0
    max = 0
    min = 0

    if(X>Y):
        max = X
        min = Y
    else:
        max = Y
        min = X

    for i in range(min,max):
        if i != min & i != max:    
            if i % 2 != 0 :
                
                soma = soma + i
    print(soma)

   