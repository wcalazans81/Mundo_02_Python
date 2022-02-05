n = int(input('Digite um número entre 0 e 20: '))
while True:

    ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Deze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'dezesete', 'Dezoito', 'Dezenove', 'Vinte')
    mostra = ext
    if n <= -1 or n > 20:
        n = int(input('Por favor digite um número entre 0 e 20: '))

    if 0 <= n <= 20:
        print(f'{ext[n]}')
        break