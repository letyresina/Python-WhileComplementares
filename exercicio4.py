'''
    Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o número lido é 
    um número perfeito ou não. Número perfeito é aquele cuja soma de seus divisores, exceto ele 
    próprio, é igual ao próprio número. Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6.
'''

num = int(input("Informe um número inteiro qualquer: "))
i = 1
soma = 0

while i < num:
    if num % i == 0:
        soma += i
    i += 1

if soma == num:
    print(f"O número {num} é um número perfeito")
else:
    print(f"O número {num} não é um número perfeito")
    