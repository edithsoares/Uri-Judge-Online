n = int(input())

hours = n // 60 ** 2
n -= hours * 60 ** 2

minuts = n // 60 
n -= minuts * 60

seconds = n

print('{}:{}:{}' .format(hours, minuts, seconds))