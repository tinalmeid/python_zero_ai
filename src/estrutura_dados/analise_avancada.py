"""
Docstring do arquivo analise_avancada.py
Descrição: Este módulo contém exemplos e explicações sobre análise avançada de dados utilizando estruturas de dados em Python.
Usaremos List Comprehensions, Lambda, Map, Filter.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-9 [CDD] [PYTHON] Estruturas de Dados (Listas, Sets, Dicts) e Lambda
"""

def filtrar_vendas_acima_de(vendas: list, limite: float) -> list:
    """
    Usa LIST COMPREHENSION para criar uma nova lista com vendas acima de um determinado limite.
    Forma Python de pensar filtragem de dados.

    Args:
        vendas (list): Lista de valores de vendas.
        limite (float): Valor limite para filtragem.

    Returns:
        list: Lista de vendas acima do limite.
    """

    # Tradução: Para cada venda 'v' em 'vendas', se 'v' for maior que 'limite', inclua 'v' na nova lista.
    return [v for v in vendas if v > limite]

def aplicar_desconto_geral(precos: list, desconto: float) -> list:
    """
    Usa MAP e LAMBDA para aplicar um desconto geral a uma lista de preços.
    - LAMBDA: Uma função anônima (sem nome) curta (uma linha).
    - MAP: Aplica a função a cada item da lista.

    Args:
        precos (list): Lista de preços originais.
        desconto (float): Percentual de desconto a ser aplicado (ex: 0.1 para 10%).

    Returns:
        list: Lista de preços com desconto aplicado.
    """

    # LAMBDA x : x * (1 - desconto)  => Função pega um valor e retorna o valor com desconto
    iterador = map(lambda x: x * (1 - desconto), precos)

    # MAP retorna um iterador, convertemos para lista
    return list(iterador)

def limpar_nomes_clientes(nomes: list) -> list:
    """
    Usa LIST COMPREHENSION para limpar espaços em branco (strip)
    e padronizar para Título (title)

    Args:
        nomes (list): Lista de nomes de clientes.

    Returns:
        list: Lista de nomes limpos e padronizados.
    """

    return [nome.strip().title() for nome in nomes]

def filtrar_valores_pares(valores: list) -> list:
    """
    Usa FILTER  e LAMBDA para pegar apenas números pares
    FILTER: Só deixa passar os números que retornam True na função lambda.

    Args:
        valores (list): Lista de valores.

    Returns:
        list: Lista de valores pares.
    """

    iterador = filter(lambda x: x % 2 == 0, valores)
    return list(iterador)
