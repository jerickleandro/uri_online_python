
def mult2(num, t=0):
    
    if(num>=1000):
        return t
    else:
        
        return mult2(num*2, t+1)
