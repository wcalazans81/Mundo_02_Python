# observar que o laço de repetição for não considera o útimo número
for c in range(0, 6):
    print(c)
print('fim')
# contagem regressiva
for c in range(6, 0 ,-1):
    print(c)
print('fim')
#contagem com passos de acordo com o 3º número
for c in range(0, 11, 2):
    print(c)
print('fim')
# ler um valor e usar para passar parametros para o for
i = int(input('Digite o inicio da contagem: ')) 
f = int(input('Digite o fim da contagem: '))
passo = int(input('Digite de quantos em quantos quer a contagem: '))
for c in range(i, f+1, passo):
    print(c)
print('fim')
# ler vario valores e fazer somatorio
s = 0
s1 = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
# modo tradicional de escerver syntax de somatoria
    s = s + n
# modo simplificado de escrever syntax de somatoria
    s1 += n
print('A soma de todos os valores é s: {} e s1: {}'.format(s, s1))