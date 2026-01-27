import pytest
from src.setup_inicial.setup_inicial import (
    validar_porta_rede,
    formatar_hostname,
    categorizar_latencia)

"""
Docstring para test.test_setup
Este módulo contém testes unitários para as funções do módulo setup_inicial.

Autor: Tina de Almeida
Data: 2026-01-26
Versão: 1.0.0
Task: CDD-5 : [CDD] [PYTHON] Setup: Ambiente, CI/CD e Quality Gate
"""

# Testes: Formatação de Hostname
def test_formatar_hostname_sucesso():
    """Deve limpar espaços, converter para minúsculas e anexar domínio corretamente."""
    resultado = formatar_hostname(" SW-Core_01 ", " empresa.local ")
    assert resultado == "sw-core_01.empresa.local"

def test_formatar_hostname_remove_ponto_extra_dominio():
    """Deve tratar caso o usuário inclua um ponto no início do domínio."""
    resultado = formatar_hostname("firewall", ".empresa.local")
    assert resultado == "firewall.empresa.local"

def test_formatar_hostname_retorna_vazio_se_nome_invalido():
    """Deve retornar string vazia se o nome do host for None ou espaço."""
    assert formatar_hostname("   ", "empresa.local") == ""
    assert formatar_hostname(None, "empresa.local") == ""
    assert formatar_hostname("", "empresa.local") == ""


def test_formatar_hostname_retorna_vazio_se_dominio_invalido():
    """Deve retornar string vazia se o domínio for None ou vazio/blank."""
    assert formatar_hostname("router", None) == ""
    assert formatar_hostname("router", "   ") == ""
    assert formatar_hostname("router", "") == ""

# Testes: Validação de Porta de Rede
def test_porta_padrao_http_deve_ser_valida():
    """Deve validar a porta padrão HTTP (80)."""
    assert validar_porta_rede(80) is True

def test_limite_minimo_porta_deve_ser_valido():
    """Deve validar o limite mínimo da porta (1)."""
    assert validar_porta_rede(1) is True

def test_limite_maximo_porta_deve_ser_valido():
    """Deve validar o limite máximo da porta (65535)."""
    assert validar_porta_rede(65535) is True

def test_porta_zero_deve_ser_invalida():
    """Deve invalidar a porta 0."""
    assert validar_porta_rede(0) is False

def test_porta_acima_do_maximo_deve_ser_invalida():
    """Deve invalidar portas acima de 65535."""
    assert validar_porta_rede(70000) is False

def test_input_nao_inteiro_deve_ser_invalido():
    """Deve invalidar entradas que não são inteiros."""
    # O Type Ignore é usado aqui para forçar a passagem de tipos incorretos para teste
    assert validar_porta_rede("eighty") is False #type: ignore
    assert validar_porta_rede(22.5) is False #type: ignore
    assert validar_porta_rede(None) is False #type: ignore
    assert validar_porta_rede([]) is False #type: ignore

# Testes: Categorização de Latência
def test_categorizar_latencia_negativa_deve_ser_invalida():
    """Deve retornar 'Inválida' para latências negativas."""
    assert categorizar_latencia(-5.0) == "🔴 Erro: Latência negativa."

def test_categorizar_latencia_Excelente():
    """Deve categorizar latências <= 20ms como 'Excelente'."""
    assert categorizar_latencia(10.0) == "👆🏾 Excelente"
    assert categorizar_latencia(20.0) == "👆🏾 Excelente"

def test_categorizar_latencia_Normal():
    """Deve categorizar latências entre 21ms e 100ms como 'Normal'."""
    assert categorizar_latencia(21.0) == "🤞🏾 Normal"
    assert categorizar_latencia(50.0) == "🤞🏾 Normal"
    assert categorizar_latencia(100.0) == "🤞🏾 Normal"

def test_categorizar_latencia_Alta():
    """Deve categorizar latências > 100ms como 'Alta'."""
    assert categorizar_latencia(101.0) == "👍🏾 Alta Latência"
    assert categorizar_latencia(150.0) == "👍🏾 Alta Latência"
    assert categorizar_latencia(300.0) == "👍🏾 Alta Latência"
