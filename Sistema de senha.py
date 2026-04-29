tentativas = 0

while tentativas < 3:
    senha = input("Senha: ")
    
    if senha == "1234":
        print("Acesso permitido")
        break
    
    tentativas += 1
else:
    print("Acesso bloqueado")