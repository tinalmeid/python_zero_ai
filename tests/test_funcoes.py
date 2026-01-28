import pytest
from src.funcoes.aula_funcoes import (
    saudacao,
    soma_numeros,
    funcao_com_print,
    somar_varios_numeros
)
from src.funcoes.calculadora import (
    calcular_imc,
    classificar_imc
)
"""
Docstring para test.funcoes
Este módulo contém testes unitários para as funções do módulo funcoes.

Autora: Tina de Almeida
Data: 2026-01-27
Task: CDD-8: [CDD] [PYTHON] Funções, Argumentos Dinâmicos e Módulos
"""

# =================================================
# Testes: Arquivo aula_funcoes.py
# =================================================

def test_saudacao_padrao():
    # Testa se usa a mensagem default quando nenhuma mensagem é fornecida
    assert saudacao("Tina") == "Bem-vinda(o) ao sistema!, Tina!"  # A função não retorna nada

def test_saudacao_personalizada():
    # Testa se substitui a mensagem default pela personalizada
    assert saudacao("Tina", "Seja bem-vinda!") == "Seja bem-vinda!, Tina!"  # A função não retorna nada

def test_soma_numeros():
    # Testa a soma de dois números
    assert soma_numeros(3, 5) == 8
    assert soma_numeros(-2, 2) == 0
    assert soma_numeros(0, 0) == 0

def test_funcao_com_print(capsys):
    # Testa se a função que usa print (retorna None e não um valor)
    retorno = funcao_com_print("Teste de Print")
    captured = capsys.readouterr()

    assert "📢 AVISO -> Função exibindo: Teste de Print" in captured.out
    assert retorno is None # Verifica se o retorno é None

def test_args_dinamicos():
    # Testa a função que usa *args para somar vários números
    assert somar_varios_numeros(1, 2, 3) == 6
    assert somar_varios_numeros(10, 20, 30, 40) == 100
    assert somar_varios_numeros() == 0
    assert somar_varios_numeros(1) == 1

# =================================================
# Testes: Arquivo calculadora.py
# =================================================

def test_calcular_imc():
    # Testa o cálculo do IMC
    assert calcular_imc(1.75, 70) == 22.86
    assert calcular_imc(0, 70) == 0.0  # Testa altura zero para evitar divisão por zero
    assert calcular_imc(1.60, 50) == 19.53

def test_classificar_imc():
    # Testa a classificação do IMC
    assert classificar_imc(22.0) == "Peso Normal"
    assert classificar_imc(17.5) == "Abaixo do Peso"
    assert classificar_imc(27.0) == "Sobrepeso"
    assert classificar_imc(32.0) == "Obesidade"
    assert classificar_imc(0.0) == "IMC Inválido"
    assert classificar_imc(-5.0) == "IMC Inválido"

