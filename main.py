
def calcularPorcentagemHabilidade(habilidades, profissoes):
    total_habilidades = sum(habilidades.values())
    porcentagens = {}

    for profissao, habilidades_profissao in profissoes.items():
        total_correspondencias = 0

        for habilidade in habilidades_profissao:
            if habilidade in habilidades:
                total_correspondencias += habilidades[habilidade]

        porcentagem = (total_correspondencias / total_habilidades) * 100
        porcentagens[profissao] = porcentagem

    return porcentagens


def obtemHabilidades():
    profissoes = {
        "Engenheiro": ["Matemática", "Física", "Logística"],
        "Mecânico": ["Eletrônica", "Matemática", "Programação"],
        "Designer": ["Criatividade", "Artes visuais", "Composição"],
        "Programador": ["Lógica", "Matemática", "Resolução de problemas"],
        "Biólogo": ["Biologia", "Química", "Observação"],
        "Médico": ["Biologia", "Química", "Empatia"],
        "Professor": ["Didática", "Pensamento crítico", "Criatividade"],
        "Psicólogo": ["Empatia", "Observação", "Comunicação"],
        "Jornalista": ["Comunicação", "Oratória", "Idiomas"]
    }

    habilidades = {}

    print("\nInforme suas habilidades de acordo com a lista abaixo\n- Primeiro, escolha o número da habilidade desejada\n- Segundo, digite o valor da habilidade ")

    listaHabilidades = [
        "01 - Matemática",
        "02 - Física",
        "03 - Química",
        "04 - Biologia",
        "05 - Artes Visuais",
        "06 - Eletrônica",
        "07 - Criatividade",
        "08 - Lógica",
        "09 - Resolução de Problemas",
        "10 - Observação",
        "11 - Didática",
        "12 - Comunicação",
        "13 - Idiomas",
        "14 - Oratória",
        "15 - Pensamento Crítico",
        "16 - Composição",
        "17 - Eletrônica",
        "00 - SAIR"
    ]
    print("\n01 - Matemática\n02 - Física\n03 - Química\n04 - Biologia\n05 - Artes Visuais\n06 - Lógica\n07 - Criatividade\n08 - Empatia\n09 - Resolução de Problemas\n10 - Observação\n11 - Didática\n12 - Comunicação\n13 - Idiomas\n14 - Oratória\n15 - Pensamento Crítico\n16 - Composição\n17 - Eletrônica\n00 - SAIR")
    
    cont_habi = 1
    while True:
        habilidade = int(input("\nHabilidade: "))
        if cont_habi >= 3:
            if habilidade == 00:
                break
        if habilidade == 00:
            print('Escolha no mínimo três habilidades!')
        valorHabilidade = int(input("Valor da habilidade (de 1 a 10): "))
        cont_habi += 1
        habilidades[listaHabilidades[habilidade - 1]] = valorHabilidade
        # habilidades[listaHabilidades[habilidade]] = valorHabilidade
    print(f'\nBaseado em suas habilidades: \n{habilidades}\n')
    
    print('Sua porcentagem de compatibilidade com cada profissão é: \n')
    porcentagens = calcularPorcentagemHabilidade(habilidades, profissoes)
    for profissao, porcentagem in porcentagens.items():
        print(f"{profissao}: {porcentagem}%")


obtemHabilidades()
# porcentagens = calcular_porcentagem_habilidades(habilidades, profissoes)
