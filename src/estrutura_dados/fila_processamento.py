"""
Docstring para src.estrutura_dados.fila_processamento
Descrição: Este módulo contém exemplos e explicações sobre Listas, Sets e Loops em Python.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-9 [CDD] [PYTHON] Estruturas de Dados (Listas, Sets, Dicts) e Lambda
"""

def organizar_tarefa(todas_tarefas: list) -> list:
    """
    Demonstra o uso de listas para organizar tarefas.
    1. Removes duplicates using set.
    2. Separates urgent tasks (containing "URGENTE") from non-urgent ones.
    3. Returns a dictionary with organized task lists.

    Args:
        todas_tarefas (list): Lista de tarefas a serem organizadas.

    Returns:
        dict: Dicionário com listas de tarefas organizadas.
        prioridade_alta (list): Tarefas urgentes.
        prioridade_baixa (list): Tarefas não urgentes.
    """

    # Remove duplicatas usando set e converte de volta para lista
    tarefas_unicas = list(set(todas_tarefas))

    urgentes = []
    nao_urgentes = []

    # Separa tarefas urgentes das não urgentes
    for tarefa in tarefas_unicas:
        if "URGENTE" in tarefa.upper():
            urgentes.append(tarefa)
        else:
            nao_urgentes.append(tarefa)

    return {
        "prioridade_alta": urgentes,
        "prioridade_baixa": nao_urgentes
    }
