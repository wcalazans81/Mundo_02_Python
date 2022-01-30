# solução usando o laço de repetição for para inverter a str
print('\033[35m-=\033[m'*27)
print('Digite uma frase para ver se a mesma é um PALÍNDROMO')
print('\033[35m-=\033[m'*27)
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase digitada {} pode ser lida de traz para frente {}'.format(junto, inverso))
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada {} não pode ser lida de traz para frente {}'.format(junto, inverso))
    print('A frase digitada não é um palíndromo!')
# solução sem usar o laço de repetição for inverter a str
print('\033[35m-=\033[m'*27)
print('Digite uma frase para ver se a mesma é um PALÍNDROMO')
print('\033[35m-=\033[m'*27)
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('A frase digitada {} pode ser lida de traz para frente {}'.format(junto, inverso))
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada {} não pode ser lida de traz para frente {}'.format(junto, inverso))
    print('A frase digitada não é um palíndromo!')