'''
Escreva uma função chamada e_par que recebe um número inteiro e retorna True se o número for par e False se for ímpar.
'''
numero = int(input("Digite um núemro: "))
def e_par (numero):
    return numero % 2 == 0
print("Caso o número seja par ele retorna True, caso seja impar ele retorna False", e_par(numero))