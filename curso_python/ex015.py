dia = int(input('Por quantos dias será alugado? '))
kms = float(input('Quantos KMs percorridos?' ))
valor = (dia * 60) + (kms * 0.15)
print('O valor a se pagar pelo carro será de R${:.2f}'.format(valor))