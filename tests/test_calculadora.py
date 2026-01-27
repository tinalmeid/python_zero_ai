import pytest
from src.matematica.calculadora import somar_numeros

def test_deve_somar_dois_numeros_positivos():
    """Testa a soma básica de 2 + 2"""
    resultado = somar_numeros(2, 2)
    assert resultado == 4

def test_deve_somar_numeros_negativos():
    """Testa soma de negativos"""
    resultado = somar_numeros(-1, -1)
    assert resultado == -2
