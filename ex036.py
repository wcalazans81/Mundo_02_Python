print('\033[33m=0\033[m' * 20)
print('Programa de crédito bancário imobiliário\ndigite os dado abaixo e confira seu crédito pode ser aprovado.\n\033[31mNão perca sua chance a hora é agora!!!\033[n')
print('\033[33m=0\033[m' * 20)
casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o salário R$ '))
prestações = int(input('Digite em qunatas anos deseja pagar? '))
vprestações = casa / (prestações * 12)
porc = salario - vprestações
if salario - porc > (salario * 30 / 100):
    print('Credito não aproavdo \033[31mexcede o limite de 30% do salário\033[m')
else:
    print('Parabéns seu credito foi aprovado com sucesso.')
print('Valor de cada prestação será de R${:.2f}'.format(vprestações))
print('O salário discontando a prestação é de R${:.2f}'.format(porc))
