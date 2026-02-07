"""
Docstring para tests.test_lista_frutas
Descrição: Testes unitários para as funções do módulo de análise de lista de frutas.

Autora: Tina Almeida
Data: 2026-02-06
Task: CDD-14: [CDD] [PYTHON] Gerenciador de Lista de Frutas (CRUD e Iteração)
"""
import pytest
from src.projetos.analisa_lista_frutas import (
    inicializar_lista_frutas,
    substituir_fruta,
    remover_fruta,
    excluir_ultima_fruta,
    exibir_lista_frutas
)

@pytest.mark.parametrize("entrada_usuario, esperado_lista_frutas", [
    ("maçã, banana, laranja", ["maçã", "banana", "laranja"]),
])

# Teste para a função inicializar_lista_frutas
def test_inicializar_lista_frutas(entrada_usuario, esperado_lista_frutas, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: entrada_usuario)
    lista_frutas = inicializar_lista_frutas(entrada_usuario)
    assert lista_frutas == esperado_lista_frutas

@pytest.mark.parametrize("frutas, nova_fruta, esperado_lista_substituta", [
    (["maçã", "banana", "laranja"], "uva", ["maçã", "uva", "laranja"]),
])
# Teste para a função substituir_fruta
def test_substituir_fruta(frutas, nova_fruta, esperado_lista_substituta, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: nova_fruta)
    lista_atualizada = substituir_fruta(frutas, nova_fruta)
    assert lista_atualizada == esperado_lista_substituta

@pytest.mark.parametrize("frutas, fruta_para_remover, esperado_lista_remove", [
    (["maçã", "banana", "laranja"], "banana", ["maçã", "laranja"]),
])
# Teste para a função remover_fruta
def test_remover_fruta(frutas, fruta_para_remover, esperado_lista_remove, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: fruta_para_remover)
    lista_atualizada = remover_fruta(frutas, fruta_para_remover)
    assert lista_atualizada == esperado_lista_remove

@pytest.mark.parametrize("frutas, esperado_lista_ultima", [
    (["maçã", "banana", "laranja"], ["maçã", "banana"]),
])
# Teste para a função excluir_ultima_fruta
def test_excluir_ultima_fruta(frutas, esperado_lista_ultima):
    lista_atualizada = excluir_ultima_fruta(frutas)
    assert lista_atualizada == esperado_lista_ultima

@pytest.mark.parametrize("frutas, esperado_output", [
    (["maçã"], ["🍓 Eu gosto de comer maçã no café da manhã."]),
])
# Teste para a função exibir_lista_frutas
def test_exibir_lista_frutas(frutas, esperado_output, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: frutas)
    exibir_lista_frutas(frutas)
    captured = capsys.readouterr()
    assert captured.out.strip() == "\n".join(esperado_output)


@pytest.mark.parametrize("frutas, fruta_para_remover, esperado_lista_remove", [
    (["maçã", "banana", "laranja"], "uva", ["maçã", "banana", "laranja"]),
])
# Testa quando a fruta para remover não está na lista
def test_remover_fruta_nao_encontrada(frutas, fruta_para_remover, esperado_lista_remove, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: fruta_para_remover)
    lista_atualizada = remover_fruta(frutas, fruta_para_remover)
    assert lista_atualizada == esperado_lista_remove

# Testa lista de frutas vazia
@pytest.mark.parametrize("frutas, esperado_output", [
    ([], "A lista de frutas está vazia."),
])
def test_exibir_lista_frutas_vazia(frutas, esperado_output, capsys):
    exibir_lista_frutas(frutas)
    captured = capsys.readouterr()
    assert captured.out.strip() == esperado_output


