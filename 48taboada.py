num = int(input('Digite um número par ver sua TABOADA: '))
for c in range(1, 11):
    print('{:2} + {:2} = {:2}'.format(num, c, num + c))
for c in range(1, 11): 
     print('')
     print('{:2} X {:2} = {:2}'.format(num, c, num * c))  