a, b = 1, 1
x = 2
n = int(input(" "))
while x <= n - 1:
    a, b = b, a+b
    x = x + 1
    print(a, b)
print(b)
