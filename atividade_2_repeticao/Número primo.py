num = int(input("Número: "))

if num <= 1:
    print("Inválido")
else:
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        print("Chave Válida (Primo)")
    else:
        print("Chave Inválida (Composto)")