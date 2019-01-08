import math
cat_opo = float(input('Digite o comprimento do cateto oposto: '))
cat_adja = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(cat_opo, cat_adja)
print('A hipotenusa vai medir {:.2f}'.format(hi))