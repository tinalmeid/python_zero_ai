import pytest
from src.controle_fluxo.aula_estruturas import (
    demonstrar_condicionais,
    demonstrar_loops,
    demonstrar_while_e_ternario )
from src.controle_fluxo.lab_desafio import filtrar_dados_sujos

"""
Docstring para test.controle_fluxo
Este módulo contém testes unitários para as funções do módulo controle_fluxo.

Autora: Tina de Almeida
Data: 2026-01-27
Task: CDD-6: [CDD] [PYTHON] Estruturas de Controle (If, For, While)
"""
# =================================================
# Testes: Arquivo lab_desafio.py
# =================================================

def test_demonstrar_condicionais_pode_dirigir(capsys):
    # Testa o caminho onde a pessoa é maior de idade e possui CNH
    demonstrar_condicionais(idade=25, possui_cnh=True)
    captured = capsys.readouterr() # Captura a saída do print
    assert "✅ Pode dirigir." in captured.out

def test_condicionais_sem_cnh(capsys):
    # Testa o caminho onde a pessoa é maior de idade mas não possui CNH
    demonstrar_condicionais(idade=30, possui_cnh=False)
    captured = capsys.readouterr()
    assert "⚠️ Maior de idade, mas precisa tirar a CNH." in captured.out

def test_condicionais_menor_idade(capsys):
    # Testa o caminho onde a pessoa é menor de idade
    demonstrar_condicionais(idade=16, possui_cnh=False)
    captured = capsys.readouterr()
    assert "⛔ Não pode dirigir." in captured.out

def test_loops_deve_imprimir_sequencia(capsys):
    # Testa se os loops estão funcionando corretamente e imprimindo a saída esperada
    demonstrar_loops()
    captured = capsys.readouterr()
    # Verifica se passou pelos 3 tipos
    assert "Número atual: 1" in captured.out
    assert "Letra atual: P" in captured.out
    assert "Coordenada: (1, 1)" in captured.out

def test_while_bateria(capsys):
    # Testa o loop while que simula a descarga da bateria
    demonstrar_while_e_ternario(bateria=40)
    captured = capsys.readouterr()
    # Verifica se o status mudou conforme a bateria descarregou
    assert "Nível: 40%, Status: 🔵 Normal" in captured.out
    assert "Nível: 20%, Status: 🟢 Crítico" in captured.out
    assert "🔴 Bateria esgotada!" in captured.out

# =================================================
# Testes: Arquivo lab_desafio.py
# =================================================

def test_desafio_separacao_sucesso(capsys):
    # Testa se o algoritmo separa corretamente números e letras
    input_sujo = "T3st32026"
    filtrar_dados_sujos(input_sujo)

    captured = capsys.readouterr()

    # Verifica se as letras forma agrupadas
    assert "📝 Letras encontradas: Tst" in captured.out

    # Verifica se os números foram agrupados
    assert "🔢 Números encontrados: 332026" in captured.out

def test_desafio_simbolos_ignorados(capsys):
    # Testa se o algoritmo ignora caracteres especiais (@, _, !)
    input_sujo = "D@d0s#2026!"
    filtrar_dados_sujos(input_sujo)

    captured = capsys.readouterr()

    # Verifica se os símbolos foram ignorados
    assert "⚠️ Ignorando caractere não alfanumérico: @" in captured.out
    assert "⚠️ Ignorando caractere não alfanumérico: #" in captured.out
    assert "⚠️ Ignorando caractere não alfanumérico: !" in captured.out

    # Verifica se as letras forma agrupadas
    assert "📝 Letras encontradas: Dds" in captured.out

    # Verifica se os números foram agrupados
    assert "🔢 Números encontrados: 02026" in captured.out
