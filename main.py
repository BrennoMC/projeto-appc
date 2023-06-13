# Projeto "Recomendação baseada em dicionários"

# Autores:
# Brenno Martiniano Cavalcante  RA: 22898449
# João Pedro Costa Malta        RA: 23002743

# Calculando a porcentagem das habilidades
def calcularPorcentagemHabilidade(habilidades, profissoes):
    ptos = 0
    porcentagens = {}
    for prof in profissoes:
        nomeProf = prof["Profissão"]
        for skillBuscada in habilidades:
            for skillEncontrada, valor in prof["Habilidades"].items():
                # total de pontos dentro da profissão
                total = sum(prof["Habilidades"].values())
                if skillEncontrada == skillBuscada and ptos <= total:
                    ptos += valor
            percent = (ptos / total) * 100
        ptos = 0
        porcentagens[nomeProf] = percent
    return porcentagens

# Obtendo as habilidades
def obtemHabilidades():
    profissoes = [
        {
            "Profissão": "Engenheiro Civil",
            "Habilidades": {
                "Matemática": 8,
                "Física": 7,
                "Comunicação": 7
            }
        },
        {
            "Profissão": "Engenheiro de Controle e Automação",
            "Habilidades": {
                "Eletrônica": 8,
                "Matemática": 7,
                "Programação": 6
            }
        },
        {
            "Profissão": "Designer",
            "Habilidades": {
                "Criatividade": 9,
                "Artes Visuais": 7,
                "Desenho": 7
            }
        },
        {
            "Profissão": "Programador",
            "Habilidades": {
                "Lógica": 9,
                "Matemática": 7,
                "Resolução de problemas": 7
            }
        },
        {
            "Profissão": "Biólogo",
            "Habilidades": {
                "Biologia": 8,
                "Química": 7,
                "Observação": 6
            }
        },
        {
            "Profissão": "Médico",
            "Habilidades": {
                "Biologia": 8,
                "Química": 8,
                "Empatia": 8
            }
        },
        {
            "Profissão": "Professor",
            "Habilidades": {
                "Didática": 9,
                "Pensamento crítico": 8,
                "Empatia": 7
            }
        },
        {
            "Profissão": "Psicólogo",
            "Habilidades": {
                "Empatia": 9,
                "Humanas": 8,
                "Comunicação": 8
            }
        },
        {
            "Profissão": "Jornalista",
            "Habilidades": {
                "Comunicação": 8,
                "Leitura e Escrita": 9,
                "Idiomas": 6
            }
        }
    ]

    habilidades = []

    print("\nInforme pelo menos 3 habilidades da lista abaixo:")

    listaHabilidades = {
        1: "Matemática",
        2: "Física",
        3: "Química",
        4: "Biologia",
        5: "Artes Visuais",
        6: "Eletrônica",
        7: "Criatividade",
        8: "Empatia",
        9: "Resolução de Problemas",
        10: "Observação",
        11: "Didática",
        12: "Comunicação",
        13: "Idiomas",
        14: "Oratória",
        15: "Pensamento Crítico",
        16: "Composição",
        17: "Lógica",
        18: "Programação",
        19: "Humanas",
        20: "Leitura e Escrita",
        21: "Desenho"
    }
    print("\n1 - Matemática\n2 - Física\n3 - Química\n4 - Biologia\n5 - Artes Visuais\n6 - Eletrônica", 
          "\n7 - Criatividade\n8 - Empatia\n9 - Resolução de Problemas\n10 - Observação\n11 - Didática",
          "\n12 - Comunicação\n13 - Idiomas\n14 - Oratória\n15 - Pensamento Crítico\n16 - Composição",
          "\n17 - Lógica\n18 - Programação\n19 - Humanas\n20 - Leitura e Escrita\n21 - Desenho\n\n0 - CALCULAR\n")

# Vaidação do input do usuário
    habilidadesArmazenadas = []
    while True:
        habilidade = int(input("Habilidade: "))
        try:
            if habilidade >= 0 and habilidade <= 21:
                if habilidade == 0:
                    if len(habilidadesArmazenadas) >= 3:
                        break
                habilidadeSelecionada = listaHabilidades[habilidade]
                if habilidadeSelecionada not in habilidadesArmazenadas:
                    habilidadesArmazenadas.append(habilidadeSelecionada)
                    habilidades.append(habilidadeSelecionada)
                else:
                    print("Você já selecionou essa habilidade. Escolha outra.")
            else:
                print("Habilidade inválida. Escolha um número entre 1 e 21.")
        except:
            print("Habilidade inválida. Escolha um número entre 1 e 21.")

#Exibição de resultado na tela
    print(f'\nBaseado em suas habilidades: \n{habilidades}\n')
    print('Sua porcentagem de compatibilidade com cada profissão é: \n')

    porcentagens = calcularPorcentagemHabilidade(habilidades, profissoes)
    for profissao, porcentagem in porcentagens.items():
        print(f"{profissao}: {round(porcentagem, 2)}%")

obtemHabilidades()
