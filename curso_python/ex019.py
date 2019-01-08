from random import choice
n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno esolhido foi {}'.format(escolhido))
