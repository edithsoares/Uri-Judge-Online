n = int(input())

a = n // 365
n -= a * 365

m = n // 30
n -= m * 30

d = n

print('{} ano(s)' .format(a))
print('{} mes(es)' .format(m))
print('{} dia(s)' .format(d))