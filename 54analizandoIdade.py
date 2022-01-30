from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = date.today().year - nasc
    if idade < 21:
        totmenor += 1
    else:
        totmaior += 1
print('São {} pessoas menores de idade e {} possoas miores de idade'.format(totmenor, totmaior))