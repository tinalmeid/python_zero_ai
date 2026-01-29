"""
Docstring do arquivo calculadora.py
Descrição: Este módulo implementa exemplo de como importar módulos em Python. (No arquivo test_funcoes.py)

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-8: [CDD] [PYTHON] Funções, Argumentos Dinâmicos e Módulos
"""

def calcular_imc(altura: float, peso: float) -> float:
    """
    Docstring para calcular_imc
    Demonstra o cálculo do Índice de Massa Corporal (IMC).

    Args:
        altura (float): Altura em metros.
        peso (float): Peso em quilogramas.

    Returns:
        float: O valor do IMC calculado.
    """
    if altura <= 0:
        return 0.0  # Evita divisão por zero ou valores inválidos
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc: float) -> str:
    """
    Docstring para classificar_imc
    Classifica o IMC em categorias padrão.

    Args:
        imc (float): O valor do IMC a ser classificado.

    Returns:
        str: A categoria do IMC.
    """
    if imc <= 0.0:
        return "IMC Inválido"
    elif imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
