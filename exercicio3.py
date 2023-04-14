'''
    Exercício 3:
    Construa um algoritmo que mostre todos os valores ímpares entre X e Y, onde X e Y são 
    fornecidos pelo usuário
'''

x = int(input("Informe um número inteiro qualquer: "))
y = int(input("Informe outro número inteiro qualquer: "))

while x <= y:
    if x % 2 != 0:
        print(x)
    x += 1
    