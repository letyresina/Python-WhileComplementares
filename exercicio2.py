'''
    Exercício 2:
    Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a tabuada de N.
'''

from re import I


num = int(input("Informe um número inteiro para realizar sua tabuada: "))

i = 1

while i <= 10:
    tabuada = num * i 
    print(f"{num} x {i} = {tabuada}")
    i += 1