"""
Docstring for test_calculadora_math.py
Descrição: Este módulo contém testes unitários para a classe Calculadora Math, garantindo que todas as operações matemáticas avançadas,
recursividade e funções lambda estejam funcionando corretamente.

Autora: Tina Almeida
Data: 2024-02_09
Task: [CDD-17] [CDD] [PYTHON] Implementação de Calculadora com Funções Avançadas, Recursividade e Lambdas.
"""
import pytest
from src.projetos.calculadora_math import (
    validar_numero,
    calcular_quadrado,
    calcular_soma,
    calcular_potencia,
    calcular_fatorial,
    calcular_dobro_e_quadrado,
    calcular_cubo_lambda,
    calcular_multiplicacao_lambda,
    calcular_par_impar_lambda,
    calcular_dobro_lista_lambda,
)

# Testes para a função validar_numero
def test_validar_numero_com_numero_valido():
    assert validar_numero("10") == 10.0
    assert validar_numero("3.14") == 3.14
    assert validar_numero("-5") == -5.0

def test_validar_numero_com_entrada_invalida():
    with pytest.raises(ValueError):
        validar_numero("abc")
    with pytest.raises(ValueError):
        validar_numero("10a")
    with pytest.raises(ValueError):
        validar_numero("")

# Testes para a função calcular_quadrado
def test_calcular_quadrado_com_numero_positivo():
    assert calcular_quadrado(2) == 4
    assert calcular_quadrado(3.5) == 12.25

def test_calcular_quadrado_com_numero_negativo():
    assert calcular_quadrado(-2) == 4
    assert calcular_quadrado(-3.5) == 12.25

# Testes para a função calcular_soma
def test_calcular_soma_com_numeros_positivos():
    assert calcular_soma(2, 3) == 5
    assert calcular_soma(1.5, 2.5) == 4.0

def test_calcular_soma_com_numeros_negativos():
    assert calcular_soma(-2, -3) == -5
    assert calcular_soma(-1.5, -2.5) == -4.0

def test_calcular_soma_com_numero_positivo_e_negativo():
    assert calcular_soma(2, -3) == -1
    assert calcular_soma(-1.5, 2.5) == 1.0

# Testes para a função calcular_potencia
def test_calcular_potencia_com_expoente_informado():
    assert calcular_potencia(2, 3) == 8
    assert calcular_potencia(5, 0) == 1

def test_calcular_potencia_com_expoente_default():
    assert calcular_potencia(2) == 4
    assert calcular_potencia(3) == 9

# Testes para a função calcular_fatorial
def test_calcular_fatorial_com_numero_positivo():
    assert calcular_fatorial(5) == 120
    assert calcular_fatorial(0) == 1
    assert calcular_fatorial(1) == 1

def test_calcular_fatorial_com_numero_negativo():
    with pytest.raises(ValueError):
        calcular_fatorial(-1)
    with pytest.raises(ValueError):
        calcular_fatorial(-5)

def test_calcular_fatorial_Um_Zero():
    assert calcular_fatorial(0) == 1
    assert calcular_fatorial(1) == 1

# Testes para a função calcular_dobro_e_quadrado
def test_calcular_dobro_e_quadrado_com_numero_positivo():
    assert calcular_dobro_e_quadrado(2) == 16
    assert calcular_dobro_e_quadrado(3) == 36

def test_calcular_dobro_e_quadrado_com_numero_negativo():
    assert calcular_dobro_e_quadrado(-2) == 16
    assert calcular_dobro_e_quadrado(-3) == 36

# Testes para a função calcular_cubo_lambda
def test_calcular_cubo_lambda_com_numero_positivo():
    assert calcular_cubo_lambda(2) == 8
    assert calcular_cubo_lambda(3.5) == 42.875

def test_calcular_cubo_lambda_com_numero_negativo():
    assert calcular_cubo_lambda(-2) == -8
    assert calcular_cubo_lambda(-3.5) == -42.875

# Testes para a função calcular_multiplicacao_lambda
def test_calcular_multiplicacao_lambda_com_numeros_positivos():
    assert calcular_multiplicacao_lambda(2, 3) == 6
    assert calcular_multiplicacao_lambda(1.5, 2.5) == 3.75

def test_calcular_multiplicacao_lambda_com_numeros_negativos():
    assert calcular_multiplicacao_lambda(-2, -3) == 6
    assert calcular_multiplicacao_lambda(-1.5, -2.5) == 3.75

def test_calcular_multiplicacao_lambda_com_numero_positivo_e_negativo():
    assert calcular_multiplicacao_lambda(2, -3) == -6
    assert calcular_multiplicacao_lambda(-1.5, 2.5) == -3.75

# Testes para a função calcular_par_impar_lambda
def test_calcular_par_impar_lambda_com_numero_par():
    assert calcular_par_impar_lambda(2) == "Par"
    assert calcular_par_impar_lambda(0) == "Par"
    assert calcular_par_impar_lambda(-4) == "Par"

def test_calcular_par_impar_lambda_com_numero_impar():
    assert calcular_par_impar_lambda(3) == "Ímpar"
    assert calcular_par_impar_lambda(-1) == "Ímpar"
    assert calcular_par_impar_lambda(-5) == "Ímpar"

# Testes para a função calcular_dobro_lista_lambda
def test_calcular_dobro_lista_lambda_com_lista_vazia():
    assert calcular_dobro_lista_lambda([]) == []

def test_calcular_dobro_lista_lambda_com_lista_numerica():
    assert calcular_dobro_lista_lambda([1, 2, 3]) == [2, 4, 6]
    assert calcular_dobro_lista_lambda([-1, -2, -3]) == [-2, -4, -6]
    assert calcular_dobro_lista_lambda([0, 0.5, -0.5]) == [0, 1.0, -1.0]

