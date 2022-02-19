# A variável dentro da função é local funciona dentro ou se torna global se declarada assim "global variável"
def funcao():
    global n2
    n1 = 4
    n2 = 5
    print(f'N1 e N2 dentro vale {n1}, {n2}')

funcao()
n1 = 2

print(f'N1 e N2 fora vale {n1}, {n2}')