"""
Docstring for src/projetos/calculo_imc.py
Descrição: Módulo para calcular o Índice de Massa Corporal (IMC) e classificar o estado nutricional.
O usuário fornece peso e altura, e o programa retorna o IMC e a classificação correspondente.

REGRA DE NEGÓCIO:
- Menor que 18.5: Abaixo do peso
- Entre 18.5 e 24.9: Peso normal
- Entre 25 e 29.9: Sobrepeso
- Entre 30 e 39.9: Obesidade
- 40 ou mais: Obesidade grave

Autora: Tina Almeida
Data: 2026-01-30
Task: Tasks:CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import math

def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC) e retorna a classificação.

    Parametros:
    peso (float): Peso em quilogramas.
    altura (float): Altura em metros.

    Retorna:
    tuple: IMC (float) e classificação (str).
    """

    if altura is None or peso is None:
        raise ValueError("🚫 A altura e o peso dem ter valores válidos.")

    if not isinstance(altura, (int, float)) or not isinstance(peso, (int, float)):
        raise TypeError("🚫 A altura e o peso devem ser números(int ou float).")

    if altura <= 0 or peso <= 0:
        raise ValueError("🚫 A altura e o peso devem ser maiores que zero.")

    imc = round(peso / (altura ** 2), 1)
    if imc < 18.5:
        classificacao = "Magreza"
    elif 18.5 <= imc < 25:
        classificacao = "Normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 40:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade grave"

    return imc, classificacao

def obter_valor_float(mensagem):
    """Solicita ao usuário um valor float com tratamento de erros."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("🚫 Por favor, insira um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("🚫 A altura e o peso devem ser números(int ou float).")

# Fim do arquivo calculo_imc.py
