capital = float(input("Capital inicial: "))
aporte = float(input("Aporte mensal: "))
taxa = float(input("Taxa (%): ")) / 100

saldo = capital
meses = 0

while saldo < capital * 2:
    saldo += saldo * taxa
    saldo += aporte
    meses += 1
    print(f"Mês {meses}: {saldo:.2f}")

anos = meses // 12
resto = meses % 12

print(f"Objetivo em {anos} anos e {resto} meses")