
def calcularPorcentagemHabilidade(habilidades, profissoes):
    return


def obtemHabilidades():
    profissoes = {
        "Engenheiro": ["Matemática", "Física", "Logística"],
        "Mecânico": ["Eletrônica", "Matemática", "Programação"],
        "Designer": ["Criatividade", "Artes visuais", "Composição"],
        "Programador": ["Lógica", "Matemática", "Resolução de problemas"],
        "Biólogo": ["Biologia", "Química"],
        "Médico": ["Biologia", "Química"]
    }

    habilidades = {}

    print("Por favor, informe suas habilidades (digite 'fim' para encerrar):")
    while True:
        habilidade = input("Habilidade: ")
        if habilidade == "fim":
            break
        valor_habilidade = int(input("Valor da habilidade (de 1 a 10): "))
        habilidades[habilidade] = valor_habilidade
    print(habilidades)

# porcentagens = calcular_porcentagem_habilidades(habilidades, profissoes)
