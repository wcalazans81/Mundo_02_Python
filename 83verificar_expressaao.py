from time import sleep
expr = str(input('Digite a expressão:'))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('\033[31mANALIZANDO EXPRESSÃO....\033[m')
sleep(3)
if len(pilha) == 0:
    print('Sua expressão é Válida!')
else:
    print('Sua expressão está errada!!!')