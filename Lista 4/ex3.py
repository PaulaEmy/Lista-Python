import random
num1 = random.sample(range(1, 101), 10)
num2 = random.sample(range(1, 101), 10)
print(num1)
print(num2)
num3 = []
x = 0
while x <= 10 - 1:
    num3.append(num1[x])
    num3.append(num2[x])
    x = x +1
print(num3)


