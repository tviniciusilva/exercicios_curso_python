# Calcular média (robusta)

nota_1 = float(input('Digite a sua primeira nota meu caro aluno: '))
nota_2 = float(input('Digite a sua segunda nota meu caro aluno: '))
media = (nota_1 + nota_2) / 2
if media >= 6:
    print('Aluno, parabéns! Você foi aprovado.')
elif media < 6:
    print('Poxa aluno, você foi reprovado! Estude mais.')