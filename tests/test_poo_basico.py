"""
Docstring for tests/test_poo_basico.py
Descrição: Este módulo contém testes para a classe Funcionario definida em src/orientacao_objetos/funcionario.py,
verificando a correta funcionalidade dos seus métodos e atributos.

Autora: Tina Almeida
Data: 2026-01-28
Task: CDD-11: [CDD] [PYTHON] Programação Orientada a Objetos (Classes e Objetos)
"""

import pytest
from src.orientacao_objetos.funcionario import Funcionario

def test_criacao_funcionario():
    # Testa se o objeto é criado com os atributos corretos (O CONSTRUTOR)
    funcionario = Funcionario("Ana", "Silva", "Desenvolvedora", 1990)
    assert funcionario.nome == "Ana"
    assert funcionario.sobrenome == "Silva"
    assert funcionario.cargo == "Desenvolvedora"
    assert funcionario.ano_nascimento == 1990
    assert funcionario.email == "ana.silva@empresa.com"

def test_metodo_apresentar():
    # Testa se o método pega 'self' corretamente e imprime a apresentação
    funcionario = Funcionario("Bruno", "Costa", "Analista", 1985)
    mensagem = funcionario.apresentar()
    assert  mensagem == "Olá, meu nome é Bruno Costa e eu sou Analista."

def test_calcular_idade():
    # Testa o método calcular_idade
    funcionario = Funcionario("Carla", "Mendes", "Gerente", 1980)
    # Se estamos em 2026, a idade deve ser 46
    idade = funcionario.calcular_idade(2026)
    assert idade == 46
