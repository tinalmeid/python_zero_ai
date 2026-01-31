"""
Docstring for tests/test_imc.py
Este módulo contém testes unitários para as funções de cálculo do Índice de Massa Corporal (IMC).

Autora: Tina de Almeida
Data: 2026-01-30
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import pytest

from src.projetos.calculo_imc import (
    calcular_imc,
    obter_valor_float
)

@pytest.mark.parametrize("peso, altura, esperado_imc, esperado_magreza_classificacao", [
    (30, 1.75, 9.8, "Magreza"),
    (45, 1.60, 17.6, "Magreza"),
    (53.2, 1.70, 18.4, "Magreza"),
])
def test_calcular_imc_magreza_sucesso(peso, altura, esperado_imc, esperado_magreza_classificacao):
    imc, classificacao = calcular_imc(peso, altura)
    assert round(imc, 1) == esperado_imc
    assert classificacao == esperado_magreza_classificacao

@pytest.mark.parametrize("peso, altura, esperado_imc, esperado_normal_classificacao", [
    (60, 1.70, 20.8, "Normal"),
    (53.5, 1.70, 18.5, "Normal"),
    (72, 1.70, 24.9, "Normal"),
])
def test_calcular_imc_normal_sucesso(peso, altura, esperado_imc, esperado_normal_classificacao):
    imc, classificacao = calcular_imc(peso, altura)
    assert round(imc, 1) == esperado_imc
    assert classificacao == esperado_normal_classificacao

@pytest.mark.parametrize("peso, altura, esperado_imc, esperado_sobrepeso_classificacao", [
    (75, 1.65, 27.5, "Sobrepeso"),
    (72.3, 1.70, 25.0, "Sobrepeso"),
    (86.4, 1.70, 29.9, "Sobrepeso"),
])
def test_calcular_imc_sobrepeso_sucesso(peso, altura, esperado_imc, esperado_sobrepeso_classificacao):
    imc, classificacao = calcular_imc(peso, altura)
    assert round(imc, 1) == esperado_imc
    assert classificacao == esperado_sobrepeso_classificacao

@pytest.mark.parametrize("peso, altura, esperado_imc, esperado_obesidade_classificacao", [
    (95, 1.70, 32.9, "Obesidade"),
    (86.7, 1.70, 30.0, "Obesidade"),
    (115.3, 1.70, 39.9, "Obesidade"),
])
def test_calcular_imc_obesidade_sucesso(peso, altura, esperado_imc, esperado_obesidade_classificacao):
    imc, classificacao = calcular_imc(peso, altura)
    assert round(imc, 1) == esperado_imc
    assert classificacao == esperado_obesidade_classificacao

@pytest.mark.parametrize("peso, altura, esperado_imc, esperado_obesidade_grave_classificacao", [
    (115.6, 1.69, 40.5, "Obesidade grave"),
    (150, 1.75, 49.0, "Obesidade grave"),
])
def test_calcular_imc_obesidade_grave_sucesso(peso, altura, esperado_imc, esperado_obesidade_grave_classificacao):
    imc, classificacao = calcular_imc(peso, altura)
    assert round(imc, 1) == esperado_imc
    assert classificacao == esperado_obesidade_grave_classificacao

@pytest.mark.parametrize("peso, altura, esperado_exception_negativo, esperado_msg", [
    (-70, 1.75, ValueError, "🚫 A altura e o peso devem ser maiores que zero."),
    (70, -1.75, ValueError, "🚫 A altura e o peso devem ser maiores que zero."),
    (0, 1.75, ValueError, "🚫 A altura e o peso devem ser maiores que zero."),
    (70, 0, ValueError, "🚫 A altura e o peso devem ser maiores que zero."),
])
def test_calcular_imc_invalidos_negativos(peso, altura, esperado_exception_negativo, esperado_msg):
    with pytest.raises(esperado_exception_negativo) as excinfo:
        calcular_imc(peso, altura)
    assert str(excinfo.value) == esperado_msg

@pytest.mark.parametrize("peso, altura, esperado_exception_none, esperado_msg", [
    (None, 1.75, ValueError, "🚫 A altura e o peso dem ter valores válidos."),
    (70, None, ValueError, "🚫 A altura e o peso dem ter valores válidos."),
])
def test_calcular_imc_invalidos_none(peso, altura, esperado_exception_none, esperado_msg):
    with pytest.raises(esperado_exception_none) as excinfo:
        calcular_imc(peso, altura)
    assert str(excinfo.value) == esperado_msg

@pytest.mark.parametrize("peso, altura, esperado_exception_invalido, mensagem_erro", [
    ("peso", 1.75, TypeError, "🚫 A altura e o peso devem ser números(int ou float)."),
    (70, "altura", TypeError, "🚫 A altura e o peso devem ser números(int ou float)."),
])
def test_calcular_imc_tipos_invalidos(peso, altura, esperado_exception_invalido, mensagem_erro):
    with pytest.raises(esperado_exception_invalido) as excinfo:
        calcular_imc(peso, altura)
    assert str(excinfo.value) == mensagem_erro

@pytest.mark.parametrize("entradas, esperado, mensagem_erro", [
    (["abc", "70"], 70.0, "🚫 A altura e o peso devem ser números(int ou float)."),
    (["!", "1.75"], 1.75, "🚫 A altura e o peso devem ser números(int ou float)."),
    (["-50", "70", "70"], 70.0, "🚫 Por favor, insira um valor maior que zero."),
    (["0", "1.75", "1.75"], 1.75, "🚫 Por favor, insira um valor maior que zero."),

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
