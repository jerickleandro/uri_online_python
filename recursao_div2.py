def div2(num):
    if(num<=0.005):
        return num
    else:
        return int(div2(num/2)+1)

print(div2(1))