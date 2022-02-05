p = ('Video', 'Python', 'Gratis', 'banco', 'transporte',
     'linha', 'feijoa', 'carboidrato', 'listagem', 'abndonado', 'pararelélepipedo')
for i in p:
    print(f'\nNa palavra {i.upper()} temos', end='      ')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' - ')
