
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
                "Photoshop": 6
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
                "Criatividade": 7
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

    print("\nInforme pelo menos 3 habilidades da lista abaixo")

    listaHabilidades = {
        0: "SAIR",
        1: "Matemática",
        2: "Física",
        3: "Química",
        4: "Biologia",
        5: "Artes Visuais",
        6: "Eletrônica",
        7: "Criatividade",
        8: "Lógica",
        9: "Resolução de Problemas",
        10: "Observação",
        11: "Didática",
        12: "Comunicação",
        13: "Idiomas",
        14: "Oratória",
        15: "Pensamento Crítico",
        16: "Composição",
        17: "Eletrônica",
        18: "Comunicação",
        19: "Programação"
    }
    print("\n01 - Matemática\n02 - Física\n03 - Química\n04 - Biologia\n05 - Artes Visuais\n06 - Lógica\n07 - Criatividade\n08 - Empatia\n09 - Resolução de Problemas\n10 - Observação\n11 - Didática\n12 - Comunicação\n13 - Idiomas\n14 - Oratória\n15 - Pensamento Crítico\n16 - Composição\n17 - Eletrônica\n\n00 - CALCULAR")

    contadorDeHabilidadesDigitadas = 1
    while True:
        while contadorDeHabilidadesDigitadas <= 3:
            habilidade = int(input("\nHabilidade: "))
            if habilidade == 00:
                break
            habilidades.append(listaHabilidades[habilidade])
            contadorDeHabilidadesDigitadas += 1
        # continuar = input("Deseja continuar")
        break

    print(f'\nSuas Habilidades = {habilidades}\n')

    porcentagens = calcularPorcentagemHabilidade(habilidades, profissoes)
    for profissao, porcentagem in porcentagens.items():
        print(f"{profissao}: {round(porcentagem, 2)}%")


obtemHabilidades()
