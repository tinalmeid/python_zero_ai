"""
Docstring for src/projetos/calculo_area_parede.py
Descrição: Módulo para calcular a área de paredes.

REGRA DE NEGÓCIO:
- A área da parede é calculada multiplicando a largura pela altura.
Ex: Largura: 5m, Altura: 3m -> Área = 5 * 3 = 15m²

Autora: Tina Almeida
Data: 2026-01-30
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import math

def calcular_area_parede(largura, altura):
    """
    Calcula a área de uma parede.

    Parâmetros:
    largura (float): A largura da parede em metros.
    altura (float): A altura da parede em metros.

    Retorna:
    float: A área da parede em metros quadrados.
    """

    if largura is None or altura is None:
        raise ValueError("🚫 Largura e altura não podem ser None.")

    if not isinstance(largura, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("🚫 Largura e altura devem ser números (int ou float).")

    if largura < 0 or altura < 0:
        raise ValueError("🚫 Largura e altura devem ser valores não negativos.")

    if largura == 0 or altura == 0:
        return 0.0

    area = largura * altura
    return area

def calcular_rendimento_tinta(area, rendimento_por_litro):
    """
    Calcula a quantidade de tinta necessária para pintar uma área.

    Parâmetros:
    area (float): A área a ser pintada em metros quadrados.
    rendimento_por_litro (float): O rendimento da tinta em metros quadrados por litro.

    Retorna:
    float: A quantidade de tinta necessária em litros.
    """

    if rendimento_por_litro is None:
        raise ValueError("🚫 Rendimento por litro não podem ser None.")

    if not isinstance(rendimento_por_litro, (int, float)):
        raise TypeError("🚫 Rendimento por litro deve ser um número (int ou float).")

    if rendimento_por_litro < 0:
        raise ValueError("🚫 Rendimento por litro não deve ser negativo.")

    if rendimento_por_litro == 0:
        return 0.0

    tinta_necessaria = area / rendimento_por_litro
    return tinta_necessaria

def obter_valor_float(mensagem):
    """
    Solicita ao usuário um valor float com tratamento de erros.

    Parâmetros:
        mensagem (str): A mensagem a ser exibida ao solicitar o valor.

    Retorno:
        float: O valor float fornecido pelo usuário.
    """

    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("🚫 Entrada inválida. Por favor, insira um número(int ou float).")
            print("")


# Fim do arquivo calculo_area_parede.py
