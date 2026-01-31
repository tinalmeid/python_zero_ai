"""
Docstring for src/projetos/executa_ponto_steak.py
Descrição: Executa a função ponto_steak e interage com o usuário.
Utiliza a função ponto_steak do módulo projetos.ponto_steak para determinar o ponto da carne
com base na temperatura fornecida pelo usuário.

Autora: Tina Almeida
Data: 2026-01-29
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.projetos.ponto_steak import ponto_steak

def executar_ponto_steak():
    # Execução interativa da função ponto_steak
    print(" ")
    print("\n" + "="*16+ " Ponto do Steak " + "="*16)
    temperatura_input = input("🌡️ Informe a temperatura da carne em Celsius: ")
    print(ponto_steak(temperatura_input))
    print("\n" + "="*40)
    print("🏁 FIM DO PROJETO PONTO DO STEAK")
    print(" ")

#====== Execução Do Script ======
if __name__ == "__main__":
    executar_ponto_steak()
# Fim do arquivo executa_ponto_steak.py
