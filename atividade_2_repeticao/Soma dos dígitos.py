num = int(input("Número: "))
soma = 0

while num > 0:
    soma += num % 10
    num //= 10

print("Soma:", soma)