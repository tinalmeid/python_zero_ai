"""
Docstring para tests.test_estados_brasil
Este módulo contém testes unitários para a função informar_sigla_estado do módulo estados_brasil.

Autora: Tina Almeida
Data: 2026-02-09
Task: CDD-16: [CDD] [PYTHON] Manipulação de Estados Brasileiros com Dicionários e Operações de Conjuntos (Sistema de Geografia de Viagens)
"""
import pytest
from src.projetos.estados_brasil import (
    informar_sigla_estado,
    analisar_viagens
)

# Teste para verificar se a função retorna a capital correta para uma sigla válida
@pytest.mark.parametrize("sigla, nome_esperado, capital_esperada", [
    ("AC", "Acre", "Rio Branco 🦕"),
    ("MA", "Maranhão", "São Luís 🦁"),
    ("MG", "Minas Gerais", "Belo Horizonte 🧀"),
    ("RJ", "Rio de Janeiro", "Rio de Janeiro 🎭"),
    ("RN", "Rio Grande do Norte", "Natal 🐪"),
    ("SE", "Sergipe", "Aracaju 🦀")
])
def test_informar_sigla_estado_valida(sigla, nome_esperado, capital_esperada, monkeypatch, capsys):
    # Simula a entrada da sigla e depois 'sair' para encerrar
    inputs = iter([sigla, 'sair'])

    # Configura o monkeypatch para simular a entrada do usuário um por vez
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Chama a função
    informar_sigla_estado()

    # Captura o que foi impresso no console
    captured = capsys.readouterr()

    # Verifica se a saída contém o nome do estado e a capital esperados
    assert capital_esperada in captured.out
    assert nome_esperado in captured.out

# Teste para verificar se a função exibe uma mensagem de erro para uma sigla inválida
@pytest.mark.parametrize("sigla_invalida", [
    "XX", "YY", "ZZ", "AAA", "123"  # Siglas que não existem
])
def test_informar_sigla_estado_invalida(sigla_invalida, monkeypatch, capsys):
    # Simula a entrada da sigla inválida e depois 'sair' para encerrar
    inputs = iter([sigla_invalida, 'sair'])

    # Configura o monkeypatch para simular a entrada do usuário um por vez
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Chama a função
    informar_sigla_estado()

    # Captura o que foi impresso no console
    captured = capsys.readouterr()

    # Verifica se a saída contém a mensagem de erro esperada
    assert "Estado não encontrado. Por favor, tente novamente." in captured.out

# Teste analisar viagens
@pytest.mark.parametrize("viagens_usuario1, viagens_usuario2, resultados_esperados", [
    ({"RJ", "SP", "MG", "BA", "CE", "MA"}, {"SE", "MG", "AM", "BA", "PE", "PI"}, {
        "interseccao": {"MG", "BA"},
        "diferenca_usuario1": {"RJ", "SP", "CE", "MA"},
        "diferenca_usuario2": {"SE", "AM", "PE", "PI"},
        "uniao": {"RJ", "SP", "MG", "BA", "CE", "MA", "SE", "AM", "PE", "PI"}
    }),
    ({"CE"}, {"CE"}, {
        "interseccao": {"CE"},
        "diferenca_usuario1": set(),
        "diferenca_usuario2": set(),
        "uniao": {"CE"}
    }),
])
def test_analisar_viagens(viagens_usuario1, viagens_usuario2, resultados_esperados):
    # Chama a função, já que não tem inputs interativos, podemos passar os sets diretamente
    resultados = analisar_viagens(viagens_usuario1, viagens_usuario2)

    # Verifica se os resultados correspondem aos resultados esperados
    assert resultados == resultados_esperados

# Testes analisar viagens com sets vazios
def test_analisar_viagens_vazios():
    # Chama a função com sets vazios, sem argumentos
    resultados = analisar_viagens()

    assert resultados["interseccao"] == {"MG", "BA"}

    # Verifica se as diferenças e a união estão corretas
    assert len(resultados["diferenca_usuario1"]) == 4
    assert len(resultados["diferenca_usuario2"]) == 4
    assert len(resultados["uniao"]) == 10

# Fim do arquivo tests.test_estados_brasil.py
