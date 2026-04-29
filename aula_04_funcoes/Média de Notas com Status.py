'''
Crie uma função chamada situacao_aluno que recebe três notas. Ela deve calcular a média e:
Retornar "Aprovado" se a média for maior ou igual a 7.
Retornar "Reprovado" se for menor que 7.
Desafio extra: Faça a função retornar tanto a média quanto o status.
'''



def situacao_aluno(primeira_nota, segunda_nota, terceira_nota):
    media_final =  (primeira_nota + segunda_nota + terceira_nota) / 3

    if media_final >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
    return media_final
    print (f"A media final é {media_final}")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceiar nota: "))


