"""
Docstring para src.projetos.estados_brasil
Descrição: Módulo para listar os estados do Brasil e suas respectivas capitais.

REGRA DE NEGÓCIO:
- O arquivo executar_estados_brasil.py deve interagir com o usuário para exibir os estados do Brasil e suas capitais.
- O programa deve solicitar ao usuário que informe um estado do Brasil.
- O programa deve exibir a capital do estado informado pelo usuário.
- O programa deve conter um dicionário com os estados do Brasil como chaves e suas capitais como valores.
- O programa deve lidar com casos em que o estado informado pelo usuário não esteja presente no dicionário, exibindo uma mensagem de erro apropriada.
- O programa deve permitir que o usuário continue consultando estados até que ele decida encerrar a aplicação.
- O programa deve exibir uma mensagem de despedida quando o usuário decidir encerrar a aplicação.

Autora: Tina Almeida
Data: 2026-02-09
Task: CDD-16: [CDD] [PYTHON] Manipulação de Estados Brasileiros com Dicionários e Operações de Conjuntos (Sistema de Geografia de Viagens)
"""
# Dicionário com os estados do Brasil e suas capitais
estados_brasil = {
    "AC": {"nome": "Acre", "capital": "Rio Branco 🦕"}, # Referência aos fósseis/dinossauros encontrados na região
    "AL": {"nome": "Alagoas", "capital": "Maceió 🏖️"}, # Praias paradisíacas
    "AP": {"nome": "Amapá", "capital": "Macapá 🏰"}, # Fortaleza de São José de Macapá
    "AM": {"nome": "Amazonas", "capital": "Manaus 🛶"}, # Encontro das águas e floresta amazônica
    "BA": {"nome": "Bahia", "capital": "Salvador 🥁"}, # Olodum/Carnaval/Axé
    "CE": {"nome": "Ceará", "capital": "Fortaleza ☀️"}, # Praias e clima quente
    "DF": {"nome": "Distrito Federal", "capital": "Brasília 🏛️"}, # Arquitetura Niemeyer
    "MA": {"nome": "Maranhão", "capital": "São Luís 🦁"}, # Bumba Meu Boi
    "MG": {"nome": "Minas Gerais", "capital": "Belo Horizonte 🧀"}, # Queijo e culinária mineira
    "PA": {"nome": "Pará", "capital": "Belém 🥭"}, # Frutas tropicais
    "PB": {"nome": "Paraíba", "capital": "João Pessoa 🌅"}, # Pôr do sol na praia
    "PE": {"nome": "Pernambuco", "capital": "Recife ☂️"}, # Carnaval e frevo
    "PI": {"nome": "Piauí", "capital": "Teresina 🏺"}, # História e cultura indígena
    "RJ": {"nome": "Rio de Janeiro", "capital": "Rio de Janeiro 🎭"}, # Carnaval e paisagens
    "RN": {"nome": "Rio Grande do Norte", "capital": "Natal 🐪"}, # Dunas e praias
    "RO": {"nome": "Rondônia", "capital": "Porto Velho 🚂"}, # Estrada de ferro Madeira-Mamoré
    "RR": {"nome": "Roraima", "capital": "Boa Vista ⛰️"}, # Monte Roraima
    "SE": {"nome": "Sergipe", "capital": "Aracaju 🦀"}, # Passarela do Caranguejo
}
def informar_sigla_estado():
    """
    Docstring para informar_sigla_estado
    Descrição: Função para solicitar ao usuário a sigla de um estado do Brasil e exibir sua capital.

    Regras de Negócio:
    - A função deve solicitar ao usuário que informe a sigla de um estado do Brasil.
    - A função deve verificar se a sigla informada pelo usuário está presente no dicionário de estados_brasil.
    - Se a sigla estiver presente, a função deve exibir a capital do estado correspondente.
    - Se a sigla não estiver presente, a função deve exibir uma mensagem de erro indicando que o estado não foi encontrado.
    - A função deve permitir que o usuário continue consultando estados até que ele decida encerrar a aplicação. (O usuário pode digitar 'sair' para encerrar)
    - A função deve exibir uma mensagem de despedida quando o usuário decidir encerrar a aplicação.

    Args:
        None
    Returns:
        None
    """
    while True:
        # Solicitar ao usuário que informe a sigla de um estado do Brasil
        estado_input = input("Digite a sigla do estado (ou 'sair' para encerrar): ").strip().upper()
        # Se o usuário digitar 'sair', encerrar a aplicação
        if estado_input == 'SAIR':
            print("Obrigado por usar o sistema de geografia de viagens! Até a próxima! 👋")
            break
        # Verificar se a sigla informada está presente no dicionário de estados_brasil
        elif estado_input in estados_brasil:
            capital = estados_brasil[estado_input]["capital"]
            print(f"A capital do estado {estados_brasil[estado_input]['nome']} é {capital}.")
            print("")
        else:
            print("Estado não encontrado. Por favor, tente novamente.")
            print("")

def analisar_viagens(usuario1_destinos=None, usuario2_destinos=None):
    """
    Docstring para analisar_viagens
    Descrição: Função para analisar viagens de dois usuários usando Sets (realizando operações de conjuntos).

    Regras de Negócio:
    Funções que deve existir:
     - Interseção: Deve identificar os destinos que ambos os usuários têm em comum.
     - Diferença do Usuário 1: Deve identificar os destinos que o Usuário 1 tem, mas o Usuário 2 não tem.
     - Diferença do Usuário 2: Deve identificar os destinos que o Usuário 2 tem, mas o Usuário 1 não tem.
    - União: Deve identificar todos os destinos únicos que ambos os usuários têm, sem duplicatas.
    Retorne os resultados em dicionarios.

    Args:
        None

    Returns:
        dict: Um dicionário contendo os resultados das operações de conjuntos (interseção, diferenças e união).
    """
    # Sets de destinos de viagem para dois usuários
    if usuario1_destinos is None:
        usuario1_destinos = {"RJ", "SP", "MG", "BA", "CE", "MA"}
    if usuario2_destinos is None:
        usuario2_destinos = {"SE", "MG", "AM", "BA", "PE", "PI"}

    # Realizar as operações de conjuntos
    # Interseção: Destinos em comum
    interseccao = usuario1_destinos.intersection(usuario2_destinos)

    # Diferença do Usuário 1: Destinos que o Usuário 1 tem, mas o Usuário 2 não tem
    diferenca_usuario1 = usuario1_destinos.difference(usuario2_destinos)

    # Diferença do Usuário 2: Destinos que o Usuário 2 tem, mas o Usuário 1 não tem
    diferenca_usuario2 = usuario2_destinos.difference(usuario1_destinos)

    # União: Todos os destinos únicos que ambos os usuários têm, sem duplicatas
    uniao = usuario1_destinos.union(usuario2_destinos)

    # Retornar os resultados em um dicionário
    resultados = {
        "interseccao": interseccao,
        "diferenca_usuario1": diferenca_usuario1,
        "diferenca_usuario2": diferenca_usuario2,
        "uniao": uniao
    }

    return resultados

