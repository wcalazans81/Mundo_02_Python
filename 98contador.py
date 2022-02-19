from time import sleep
def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)   
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)  
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c += p
        print('Fim!')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c -= p
    print('Fim!')
    print('-=' * 20)


cont(1, 10, 1)
cont(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(ini, fim, passo)