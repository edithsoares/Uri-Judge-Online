num_notas = float(input())
print(num_notas)

resto100 = num_notas // 100
num_notas -= resto100*100

resto50 = num_notas // 50
num_notas -= resto50 * 50

resto20 = num_notas // 20
num_notas -= resto20 * 20

resto10 = num_notas // 10
num_notas -= resto10 * 10

resto5 = num_notas // 5
num_notas -= resto5 * 5

resto2 = num_notas // 2
num_notas -= resto2 * 2

moeda1 = num_notas // 1
num_notas -= moeda1 * 1

moeda50 = num_notas // 0.5
num_notas -= moeda50 * 0.5
float(moeda50)
float(num_notas)

moeda25 = num_notas // 0.25
num_notas -= moeda25 * 0.25
float(moeda25)
float(num_notas)

moeda10 = num_notas // 0.10
num_notas -= moeda10 * 0.10
float(moeda10)
float(num_notas)

moeda05 = num_notas // 0.05
num_notas -= moeda05 * 0.05
float(moeda05)
(num_notas)

moeda01 = num_notas * 100
float( moeda01)
(num_notas)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(resto100)))
print('{} nota(s) de R$ 50.00'.format(int(resto50)))
print('{} nota(s) de R$ 20.00'.format(int(resto20)))
print('{} nota(s) de R$ 10.00'.format(int(resto10)))
print('{} nota(s) de R$ 5.00'.format(int(resto5)))
print('{} nota(s) de R$ 2.00'.format(int(resto2)))
print('MOEDAS:')
print('{:.2f} moeda(s) de R$ 1.00'.format(int(moeda1)))
print('{:.2f} moeda(s) de R$ 0.50'.format(int(moeda50)))
print('{:.2f} moeda(s) de R$ 0.25'.format(int(moeda25)))
print('{:.2f} moeda(s) de R$ 0.10'.format(int(moeda10)))
print('{:.2f} moeda(s) de R$ 0.05'.format(int(moeda05)))
print('{:.2f} moeda(s) de R$ 0.01'.format(int(moeda01)))