"""
Docstring para src.estrutura_dados.dicionarios_sets
Descrição: Este módulo contém exemplos e explicações sobre o uso de dicionários e conjuntos (sets) em Python.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-9 [CDD] [PYTHON] Estruturas de Dados (Listas, Sets, Dicts) e Lambda
"""

def criar_relatorio_funcionario(nome: str, salario: float, cargo: str) -> dict:
    """
    Demonstra um dicionário (JSON-LIKE) representando um relatório de funcionário.

    Args:
        nome (str): Nome do funcionário
        salario (float): Salário do funcionário
        cargo (str): Cargo do funcionário

    Returns:
        dict: Dicionário com as informações do funcionário
    """
    return {
        "nome": nome,
        "salario_anual": salario * 12,
        "cargo": cargo,
        "ativo": True
    }

def limpar_lista_emails(emails_sujos: list) -> list:
    """
    Recebe uma lista de emails duplicados e retorna uma lista limpa
    Utilizando conjuntos (sets) para remover duplicatas.

    Args:
        emails_sujos (list): Lista de emails com possíveis duplicatas

    Returns:
        list: Lista de emails únicos (emails_unicos)
    """

    #Converte para set (remove duplicatas) e volta para lista
    emails_unicos = list(set(emails_sujos))

    # Ordena a lista de emails únicos
    emails_unicos.sort()

    return emails_unicos