"""
Docstrings para projetos/test_rendimento_tinta.py
Este módulo contém testes unitários para as funções de cálculo de rendimento de tinta.

Autora: Tina de Almeida
Data: 2026-01-30
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import pytest
from src.projetos.calculo_area_parede import (
    calcular_area_parede,
    calcular_rendimento_tinta,
    obter_valor_float
)

def test_calcular_area_parede_sucesso():
    # Verifica cálculo de área com valores válidos
    assert calcular_area_parede(5, 3) == 15
    assert calcular_area_parede(0, 10) == 0

@pytest.mark.parametrize("largura, altura, mensagem", [
    (None, 3, "🚫 Largura e altura não podem ser None."),
    (5, None, "🚫 Largura e altura não podem ser None."),
    ("cinco", 3, "🚫 Largura e altura devem ser números (int ou float)."),
    (5, "três", "🚫 Largura e altura devem ser números (int ou float)."),
    (-5, 3, "🚫 Largura e altura devem ser valores não negativos."),
    (5, -3, "🚫 Largura e altura devem ser valores não negativos."),
])
def test_calcular_area_parede_invalidos(largura, altura, mensagem):
    # Verifica tratamento de erros para valores inválidos
    with pytest.raises((ValueError, TypeError)) as excinfo:
        calcular_area_parede(largura, altura)
    assert str(excinfo.value) == mensagem

def test_calcular_rendimento_tinta_sucesso():
    # Verifica o calculo do rendimento da tinta com valores válidos
    assert calcular_rendimento_tinta(56, 12)
    assert calcular_rendimento_tinta(67, 0) == 0

@pytest.mark.parametrize("area, rendimento, mensagem", [
    (100, None, "🚫 Rendimento por litro não podem ser None."),
    (100, "dez", "🚫 Rendimento por litro deve ser um número (int ou float)."),
    (100, -5, "🚫 Rendimento por litro não deve ser negativo."),
])
def test_calcular_rendimento_tinta_invalidos(area, rendimento, mensagem):
    with pytest.raises((ValueError, TypeError)) as excinfo:
        calcular_rendimento_tinta(area, rendimento)
    assert str(excinfo.value) == mensagem

@pytest.mark.parametrize("entradas, esperado, mensagem_erro", [
    (["abc", "10.5"], 10.5, "🚫 Entrada inválida. Por favor, insira um número(int ou float)."),
    (["!", "20"], 20.0, "🚫 Entrada inválida. Por favor, insira um número(int ou float)."),
])
def test_obter_valor_float(monkeypatch, capsys, entradas, esperado, mensagem_erro):
    # Testa a função obter_valor_float com entradas inválidas
    iterador = iter(entradas)
    # substitui o comportamento da função input()
    monkeypatch.setattr('builtins.input', lambda _: next(iterador))

    #Executa a função e verifica o resultado ou erro
    resultado = obter_valor_float("Digite um número: ")
    assert resultado == esperado

    # Verifica se a mensagem de erro foi exibida
    captured = capsys.readouterr()
    assert mensagem_erro in captured.out
