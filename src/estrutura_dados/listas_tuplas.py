"""
Docstring para src.estrutura_dados.listas_tuplas
Descrição: Este módulo contém exemplos e explicações sobre o uso de listas e tuplas em Python.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-9 [CDD] [PYTHON] Estruturas de Dados (Listas, Sets, Dicts) e Lambda
"""

def processar_fila(nomes: list) -> list:
    """
    Demonstra o uso de listas para processar uma fila de nomes. (pop(0) e append(  ))
    Recebe uma lista de nomes, remove o primeiro (atendido) e adiciona dois novos nomes ao final da fila.
    Args:
        nomes (list): Lista de nomes na fila.

    Returns:
        list: Lista de nomes processados (removidos da fila).
    """
    if not nomes:
         return []

    atendido  = nomes.pop(0)  # Remove o primeiro nome da fila

    # adiciona novos nomes ao final da fila
    nomes.append("Ana é o novo nome 1")
    nomes.append("Carlos é o novo nome 2")

    return [atendido]  # Retorna a lista com o nome atendido

def obter_coordenadas_gps() -> tuple:
    """
    Demonstra o uso de tuplas para representar coordenadas GPS.
    Retorna uma tupla com latitude e longitude.

    Returns:
        tuple: Tupla contendo (latitude, longitude).
    """
    # Exemplo fixo de coordenadas GPS (cidade de BH)
    latitude = -19.916681
    longitude = -43.934493
    return (latitude, longitude)

