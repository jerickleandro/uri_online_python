N = int(input())

for c in range(1,N+1):
    text = input()
    
    X = int(text.split(" ")[0])
    
    Y = int(text.split(" ")[1])
    
    soma = 0
    # _max
    # _min

    if X>Y:
        _max = X
        _min = Y
    else:
        _max = Y
        _min = X

    for i in range(_min,_max):
        if i != _min & i != _max:    
            if i % 2 != 0 :
                
                soma = soma + i
    print(soma)

   