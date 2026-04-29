'''
Desenvolva uma função aplicar_desconto que recebe o valor de um produto e a porcentagem de desconto.
A função deve retornar o valor final após o desconto.
Entrada: 100, 15
Saída esperada: 85.0
'''
valor_produto = (float(input("Digite o valor do produto: ")))
porcentagem_desconto = (int(input("Qual a porcentagem de desconto? ")))
def aplicar_desconto (valor_produto):
    return valor_produto - (valor_produto * porcentagem_desconto / 100)
print(f"O valor do produto é  {valor_produto}, a porcentagem do desconto foi de {porcentagem_desconto}%, O valor final foi de", aplicar_desconto(valor_produto))