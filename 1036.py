
linha = input('').split(' ')

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

x = (b**2) - (4*a*c)

if a == 0.0 or x < 0:
    print('Impossivel calcular')
else:
    x1 = (-b + (x ** (1/2))) / (2*a)
    x2 = (-b - (x ** (1/2))) / (2*a)
    print('R1 = %.5f' % x1)
    print('R2 = %.5f' % x2)

# R1 = -0.29788
# R2 = -1.71212
