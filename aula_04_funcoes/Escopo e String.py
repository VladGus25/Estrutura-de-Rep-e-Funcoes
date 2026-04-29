def gerar_email(nome, sobrenome):
    return f"{nome.lower()}.{sobrenome.lower()}@escola.com"

# Entrada de dados
nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")

# Gerar e mostrar o e-mail
email = gerar_email(nome, sobrenome)
print("Email gerado:", email)