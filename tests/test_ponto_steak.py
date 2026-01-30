"""
Docstring for test_ponto_steak.py
Descrição: Testes unitários para a função ponto_steak no módulo projetos.ponto_steak.

Autora: Tina Almeida
Data: 2026-01-29
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import pytest
from src.projetos.executar_ponto_steak import executar_ponto_steak
from src.projetos.ponto_steak import ponto_steak

#Mock para cada ponto de cozimento
@pytest.mark.parametrize("temperatura, esperado", [
    (45, "🥩 Precisa de mais cozimento"),
    (50, "🥩 Mal passado"),
    (57, "🥩 Ao ponto para mal"),
    (63, "🥩 Ao ponto"),
    (68, "🥩 Ao ponto para bem"),
    (71, "🥩 Bem passado"),
    (75, "🥩 Passou do ponto"),
])

def test_ponto_steak(temperatura, esperado):
    # Testa temperaturas para cada ponto de cozimento
    resultado = ponto_steak(temperatura)
    assert resultado == esperado

@pytest.mark.parametrize("temperatura, esperado_borda", [
    (48, "🥩 Mal passado"),
    (54, "🥩 Mal passado"),
    (55, "🥩 Ao ponto para mal"),
    (60, "🥩 Ao ponto para mal"),
    (61, "🥩 Ao ponto"),
    (65, "🥩 Ao ponto"),
    (66, "🥩 Ao ponto para bem"),
    (70, "🥩 Ao ponto para bem"),
    (71, "🥩 Bem passado"),
    (72, "🥩 Passou do ponto"),

])
def test_ponto_steak_bordas(temperatura, esperado_borda):
   # Testa valores de borda
    resultado = ponto_steak(temperatura)
    assert resultado == esperado_borda

# Mock para entradas inválidas
@pytest.mark.parametrize("temperatura_invalida, mensagem", [
    ("abc", "⛔ Erro: Por favor, insira um valor numérico válido para a temperatura."),
    (None, "⛔ Erro: Por favor, insira um valor numérico válido para a temperatura."),
    (";", "⛔ Erro: Por favor, insira um valor numérico válido para a temperatura."),
    ({}, "⛔ Erro: Por favor, insira um valor numérico válido para a temperatura."),
])
def test_ponto_steak_invalidos(temperatura_invalida, mensagem):
    # Testa entradas inválidas
    resultado = ponto_steak(temperatura_invalida)
    assert resultado == mensagem
