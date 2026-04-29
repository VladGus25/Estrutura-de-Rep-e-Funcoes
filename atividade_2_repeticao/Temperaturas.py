soma = 0
temps = []

for i in range(10):
    t = float(input("Temperatura: "))
    temps.append(t)
    soma += t

media = soma / 10

acima = 0
for t in temps:
    if t > media:
        acima += 1

print("Média:", media)
print("Dias acima:", acima)