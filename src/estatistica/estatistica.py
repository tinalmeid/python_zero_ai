"""
Docstring for estatistica/estatistica.py
Descrição: Implementa exemplos de Módulos, importação e Pacotes em Python.

Autora: Tina Almeida
Data: 2026-01-28
Task: CDD-12: [CDD] [PYTHON] Modularização, Imports e Packages
"""

from typing import List, Union

def calcular_media(numeros: List[float]) -> float:
    """
    Calcula a média de uma lista de números.

    Args:
    numeros (List[float]): Lista de números float.

    Retorna:
    float: A média dos números fornecidos.
    """

    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

def calcular_soma(numeros: List[float]) -> float:
    """
    Calcula a soma de uma lista de números.

    Args:
    numeros (List[float]): Lista de números float.

    Retorna:
    float: A soma dos números fornecidos.
    """

    return sum(numeros)
