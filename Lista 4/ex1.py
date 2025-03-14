import random
num = random.sample(range(1, 101), 10)
print(num)
maior = num[0]
menor = num[0]
x = 0
while x <= len(num) - 1:
    if num[x] > maior:
        maior = num[x]
    if num[x] < menor:
        menor = num[x]
    x = x+1
print(maior, menor)
