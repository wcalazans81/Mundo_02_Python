msg = 'Lojas Guanabara'
print('{:=^40}'.format(msg))
compra = float(input('Qual o valor de sua compra? R$ '))
avista = compra - (compra * 10 / 100)
avcartao = compra - (compra * 5 /100)
xxx = compra + (compra * 20 / 100)
print("""[1] avista em dinheiro ou cheque \033[33m com 10% de desconto\33[m
[2] A vista no cartão \033[36m com 5% de desconto\033[m
[3] em até 2X no cartão sem juros \033[35m sem juros\033[m
[4] 3X ou mais no cartão \033[31mcom 20% de acrécimo\033[m""")
op = int(input('Qual a forma de pagamento? '))
if op == 1:
    print('Você escolheu o pagar avista em dinheiro ou cheque.'
          '\n\033[36mE com desconto de 10% vai pagar o valor de\033[m\033[33m R${:.2f}\033[m'.format(avista))
elif op == 2:
    print('Você escolheu pagar avista no cartão. E com o desconto de 5% vai pagar {:.2f}'.format(avcartao))
elif op == 3:
    print('Você escolheu pagar em 02 vezes no cartão e vai pagar R${:.2f}'.format(compra))
elif op == 4:
    print('voce escolheu pagar em 03 vezes ou mais no cartão e com acrécimo de 20% vai pagar R${:.2f}'.format(xxx))
else:
    print('\033[31mOpção inválida.ESCOLHA UMA FORMA DE PAGAMENTO VÁLIDO!!!\033[m')
print('TENTE NOVAMENTE!')
