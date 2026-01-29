"""
Docstring for estatistica/main.py
Descrição: Ponto de entrada principal para o módulo estatistica.
Demonstra o uso das funções do pacote estatistica.

Autora: Tina Almeida
Data: 2026-01-29
Task: CDD-12: [CDD] [PYTHON] Modularização, Imports e Packages
"""

import sys
import os

# Adiciona o diretório src ao sys.path para permitir imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Verifica se o diretório foi adicionado corretamente
print(f"Diretórios no sys.path: {sys.path}")

# ----------- Forma 1: Importação mais limpa graças ao pacote __init__.py  -----------
# É a forma recomendada de importação quando se trabalha com pacotes.
from estatistica import (
    calcular_media,
    calcular_soma)

# ---------- Forma 2: Importação direta do módulo estatistica.py -----------
# É útil quando se quer ser bem explicito sobre a origem das funções.
import src.estatistica.estatistica as estatistica_basica

def main():
    print(" ")
    print("\n" + "="*10 + " Estatística Básica - Usando Pacote " + "="*10 + "\n")
    print("        📦 MÓDULOS E PACOTES (CDD-12)")
    print("\n" + "="*56 + "\n")

    dados = [10, 20, 30, 40, 50]
    print(f"📊 Dados brutos: {dados}")

    # Usando a Forma 1 de importação (Direto do pacote)
    media = calcular_media(dados)
    print(f"📈 Média (usando pacote): {media}")

    #usando a Forma 2 de importação (Direto do módulo)
    soma = estatistica_basica.calcular_soma(dados)
    print(f"➕ Soma (usando módulo): {soma}")

    print("\n" + "="*40)
    print("🏁 FIM DO CURSO BÁSICO DE PYTHON")
    print("="*40)

if __name__ == "__main__":
    main()

