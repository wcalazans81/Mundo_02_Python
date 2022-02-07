# comando para criar uma ligação entre listas
from re import A


a = [2, 3 , 4, 7]
b = a 
# coma a um ligação entre listas o proxímo comando adiciona o valor nas duas listas
b[2] = 8
b.append(9)
b.insert(2, 5)
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('\033[34m=-\033[m'*10)
# comando para fazer um copia de outras listas
c = [2, 3 , 4, 7]
d = c[:]

c[2] = 8
c.append(9)
c.insert(2, 5)
print(f'Lista C: {c}')
print(f'Lista D: {d}')
print('\033[34m=-\033[m'*10)