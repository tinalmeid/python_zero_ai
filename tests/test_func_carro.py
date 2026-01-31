"""
Docstring for tests/test_funcionarios_carro.py
Este módulo contém testes unitários para as funções de gerenciamento de funcionários e seus carros.

Autora: Tina Almeida
Data: 2026-01-30
Task: Tasks:CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import pytest
from src.projetos.func_carro_sets import (
    funcionarios_sem_carro,
    funcionarios_com_carro_e_trabalha_noite,
    funcionarios_com_carro_e_trabalha_dia,
    funcionarios_com_carro
)

@pytest.fixture
def dados_funcionarios():
    return {
        'funcionarios': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda'],
        'funcionarios_com_carro': ['Bruno', 'Diana', 'Fernanda'],
        'funcionarios_trabalha_noite': ['Carlos', 'Diana', 'Eduardo'],
        'funcionarios_trabalha_dia': ['Ana', 'Bruno', 'Fernanda']
    }

def test_funcionarios_sem_carro(dados_funcionarios):
    # Verifica se a função retorna corretamente os funcionários sem carro
    resultado = funcionarios_sem_carro(
        dados_funcionarios['funcionarios'],
        dados_funcionarios['funcionarios_com_carro']
    )
    esperado = {'Ana', 'Carlos', 'Eduardo'}
    assert resultado == esperado

def test_funcionarios_com_carro_e_trabalha_noite(dados_funcionarios):
    # Verifica se a função retorna corretamente os funcionários com carro que trabalham à noite
    resultado = funcionarios_com_carro_e_trabalha_noite(
        dados_funcionarios['funcionarios_com_carro'],
        dados_funcionarios['funcionarios_trabalha_noite']
    )
    esperado = {'Diana'}
    assert resultado == esperado

def test_funcionarios_com_carro_e_trabalha_dia(dados_funcionarios):
    # Verifica se a função retorna corretamente os funcionários com carro que trabalham durante o dia
    resultado = funcionarios_com_carro_e_trabalha_dia(
        dados_funcionarios['funcionarios_com_carro'],
        dados_funcionarios['funcionarios_trabalha_dia']
    )
    esperado = {'Bruno', 'Fernanda'}
    assert resultado == esperado

def test_funcionarios_com_carro(dados_funcionarios):
    # Verifica se a função retorna corretamente os funcionários com carro
    resultado = funcionarios_com_carro(
        dados_funcionarios['funcionarios'],
        dados_funcionarios['funcionarios_com_carro']
    )
    esperado = {'Bruno', 'Diana', 'Fernanda'}
    assert resultado == esperado

# Fim
