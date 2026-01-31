"""
Docstring para projetos/executar_calculo_imc.py
Descrição: Script principal para executar o cálculo do Índice de Massa Corporal (IMC).
O usuário é solicitado a inserir peso e altura, e o programa exibe o IMC e a classificação correspondente.

Autora: Tina Almeida
Data: 2026-01-30
Task: Tasks:CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.projetos.calculo_imc import (
    calcular_imc,
    obter_valor_float
)

def executar_calculo_imc():
    # Execução interativa da função calcular_imc
    print(" ")
    print("\n" + "="*10 + " Cálculo de IMC " + "="*10)
    print("        ⚖️ Índice de Massa Corporal (IMC)")
    print(" ")

    peso = obter_valor_float("➡️  Informe seu peso em kg: ")
    altura = obter_valor_float("➡️  Informe sua altura em metros: ")
    print(" ")

    try:
        imc, classificacao = calcular_imc(peso, altura)
        print(f"📊 Seu IMC é: {imc:.2f}")
        print(f"📋 Classificação: {classificacao}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n" + "="*40)
    print("🏁 FIM DO PROJETO CÁLCULO DE IMC")
    print(" ")



if __name__ == "__main__":
    executar_calculo_imc()
