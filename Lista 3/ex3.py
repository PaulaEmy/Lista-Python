a = 80000.0
b = 200000.0
x = 1
while a != b or a > b:
    a = a * (3/100)
    b = b * (1.5/100)
    x = x + 1
print(x)
