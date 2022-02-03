s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou \033[32m{c}\033[m e soma entre eles é iqual a \033[33m{s}.')    
