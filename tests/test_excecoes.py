import pytest
from src.tratamentos_erros.gerenciador import (
     dividir_seguro,
     acessar_banco_dados_fake)
"""
Docstring for tests/test_excecoes.py
Descrição: Este módulo contém testes unitários para o gerenciador de exceções definido em src

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-10 : [CDD] [PYTHON] Tratamento de Exceções (Try, Except, Finally)

"""

def test_divisao_sucesso():
    # Testa o caso de divisão bem-sucedida
    assert dividir_seguro(10, 2) == 5

def test_divisao_por_zero():
    # Testa se a função retorna None (e não explode) ao dividir por zero
    resultado = dividir_seguro(10, 0)
    assert resultado is None

def test_divisao_tipo_invalido():
    # Testa se a função retorna None ao receber um tipo inválido
    resultado = dividir_seguro(10, "a") #type: ignore
    assert resultado is None

def test_acesso_lista_valido():
    # Testa o acesso válido a um índice da lista
    dados = ["Cliente A", "Cliente B", "Cliente C"]
    assert acessar_banco_dados_fake(dados, 1) == "Cliente B"

def test_acesso_lista_indice_invalido():
    # Testa o acesso a um índice inválido da lista, tenta acessar 99 em uma lista de 3 itens
    dados = ["Cliente A", "Cliente B", "Cliente C"]
    resultado = acessar_banco_dados_fake(dados, 99)
    assert resultado is None

def test_erro_generico_inesperado():
    # Testa se a função lida com um erro genérico inesperado
    dados = None  # Isso causará um TypeError ao tentar acessar um índice
    resultado = acessar_banco_dados_fake(dados, 0)
    assert resultado is None
