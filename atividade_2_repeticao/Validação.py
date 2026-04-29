num = int(input("Digite um número (1-10): "))

while num < 1 or num > 10:
    num = int(input("Inválido. Digite novamente: "))

print("Valor válido:", num)