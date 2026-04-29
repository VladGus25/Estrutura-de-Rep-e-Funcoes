maior = 0
dia_melhor = 0

for i in range(7):
    venda = float(input(f"Dia {i+1}: "))
    total += venda

    if venda > maior:
        maior = venda
        dia_melhor = i + 1

print("Total:", total)
print("Melhor dia:", dia_melhor)