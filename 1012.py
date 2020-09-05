# OS dois exemplos tem o mesmo resultado
# -----------------Eu-fiz----------------------------
a = float(input())
b = float(input())
c = float(input())

a1 = (a*c)/2
a2 = (3.14159 * c ** 2)
a3 = ((a + b) * c)/2
a4 = (b ** 2)
a5 = (a * b)

print('TRIANGULO: {:.3f}' .format(a1)) 
print('CIRCULO: {:.3f}' .format(a2))
print('TRAPEZIO: {:.3f}' .format(a3))
print('QUADRADO: {:.3f}' .format(a4))
print('RETANGULO: {:.3f}' .format(a5))


# --------------È-aceito------------------------------

valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f"