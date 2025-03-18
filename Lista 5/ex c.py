x = 0
for i in range (1067, 3627):
    if i % 2 == 0 and i % 7 == 0:
        x = x + 1
print(f'{x} números entre 1067 e 3627 são pares e divisíveis por 7')
