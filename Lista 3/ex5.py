a = int(input("Número 1: "))
b = int(input("Número 2: "))
if a == 0:
    print(f"MDC({a},{b}) = {b}")
elif b == 0:
    print(f"MDC({a},{b}) = {a}")
else:
    while a % b != 0:
        a, b = b, a%b
print(f"O MDC é {b}")
