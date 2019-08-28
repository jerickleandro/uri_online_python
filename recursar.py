def oi(vezes):
    if(vezes>0):
        vezes -= 1
        oi(vezes)
        print(vezes)

oi(10)