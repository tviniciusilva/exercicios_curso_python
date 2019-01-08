frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A apareceu a primeira vez na posição {}'.format(frase.find('A')+1))
print('Última letra A na posição {}'.format(frase.rfind('A')+1))

