'''
Crie uma função chamada dias_de_vida que recebe a idade de uma pessoa em anos e retorna quantos dias ela já viveu (considere o ano com 365 dias).
Entrada: 20
Saída esperada: 7300
'''
idade = (int(input("Digite sua idade atual: ")))
def dias_de_vida (idade):
     return idade * 365
print(f"A idade informada foi {idade} anos, os dias vividos foram de ", dias_de_vida(idade))