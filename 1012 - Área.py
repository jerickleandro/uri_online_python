text = input()
A = float(text.split(" ")[0])
B = float(text.split(" ")[1])
C = float(text.split(" ")[2])
pi = 3.14159
TRIANGULO = (A*C)/2
CIRCULO = pi*(C*C)
TRAPEZIO = ((A+B)/2)*C
QUADRADO = B*B
RETANGULO = A*B

print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))