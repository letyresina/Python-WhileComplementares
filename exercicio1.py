'''
    Exercício 1:
    Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido 
    pelo usuário.
'''

N = int(input("Informe um número inteiro qualquer: "))
i = 1

while i <= N:
    if i % 2 != 0:
        print(i)
    i += 1