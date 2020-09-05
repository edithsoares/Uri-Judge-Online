num_notas = int(input())
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

resto1 = num_notas // 1
num_notas -= resto1 * 1

print('{} nota(s) de R$ 100,00' .format(resto100))
print('{} nota(s) de R$ 50,00' .format(resto50))
print('{} nota(s) de R$ 20,00' .format(resto20))
print('{} nota(s) de R$ 10,00' .format(resto10))
print('{} nota(s) de R$ 5,00' .format(resto5))
print('{} nota(s) de R$ 2,00' .format(resto2))
print('{} nota(s) de R$ 1,00' .format(resto1))