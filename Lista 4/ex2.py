import random
num = random.sample(range(1, 101), 20)
print(num)
par = []
impar = []
x = 0
while x <= len(num) - 1:
    if num[x] % 2 == 0:
        par.append(num[x])
    else:
        impar.append(num[x])
    x = x+1
print(par)
print(impar)

