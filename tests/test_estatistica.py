"""
Docstring for test/test_estatistica.py
Descrição: Testes unitários para o módulo estatistica.

Autora: Tina Almeida
Data: 2026-01-29
Task: CDD-12: [CDD] [PYTHON] Modularização, Imports e Packages
"""
import pytest
# Importe mais limpos por causa do pacote __init__.py
from src.estatistica import (
    calcular_media,
    calcular_soma)

from src.estatistica.main import main

# =================================================
# Testes: Arquivo estatistica.py
# =================================================

def test_calcular_media_lista_cheia():
    # Testa a função calcular_media com uma lista cheia
    valores = [10, 20, 30, 40, 50]
    assert calcular_media(valores) == 30.0  # Verifica se a média está correta

def test_calcular_media_lista_vazia():
    # Testa a função calcular_media com uma lista vazia sem erros (Zero Division Handling)
    valores = []
    assert calcular_media(valores) == 0.0  # Verifica se a média de uma lista vazia é 0.0

def test_calcular_soma_lista_cheia():
    # Testa a função calcular_soma com uma lista cheia
    valores = [10, 20, 30, 40, 50]
    assert calcular_soma(valores) == 150.0  # Verifica se a soma está correta

def test_calcular_soma_lista_vazia():
    # Testa a função calcular_soma com uma lista vazia
    valores = []
    assert calcular_soma(valores) == 0.0  # Verifica se a soma de uma lista vazia é 0.0

# ============================================
# Teste: Arquivo main.py
# ============================================

def test_main_execucao_sem_erro(capsys):
    # Testa se a função main executa sem erros
    # Usa capsys para capturar a saída padrão e evitar poluição do console durante os testes

    # 1. Executa a função main() diretamente
    main()

    # 2. Captura a saída padrão, tudo que foi impresso no console
    captured = capsys.readouterr()
    saida_console = captured.out

    # 3. Verifica se a saída contém algumas strings esperadas
    assert "Estatística Básica - Usando Pacote" in saida_console
    assert "📊 Dados brutos: [10, 20, 30, 40, 50]" in saida_console
    assert "📈 Média (usando pacote): 30.0" in saida_console
    assert "➕ Soma (usando módulo): 150" in saida_console
    assert "🏁 FIM DO CURSO BÁSICO DE PYTHON" in saida_console

