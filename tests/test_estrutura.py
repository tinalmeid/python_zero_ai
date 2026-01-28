import pytest
from src.estrutura_dados.listas_tuplas import (
    processar_fila,
    obter_coordenadas_gps)
from src.estrutura_dados.dicionarios_sets import (
    criar_relatorio_funcionario,
    limpar_lista_emails)
from src.estrutura_dados.fila_processamento import (
    organizar_tarefa)

"""
Docstring para tests.test_estrutura
Descrição: Testes unitários para o módulo estrutura_dados.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-9 [CDD] [PYTHON] Estruturas de Dados (Listas, Sets, Dicts) e Lambda
"""

# =================================================
# Testes: Arquivo listas_tuplas.py
# =================================================

def test_fila_atendimento():
    # Testa a função processar_fila
    fila_inicial = ["João", "Maria", "Pedro"]
    atendidos = processar_fila(fila_inicial)

    # Verifica se o nome atendido é o primeiro da fila inicial
    assert atendidos == ["João"]
    # Verifica se a fila inicial foi atualizada corretamente
    assert fila_inicial == ["Maria", "Pedro", "Ana é o novo nome 1", "Carlos é o novo nome 2"]
    # Verifica se "João" não está mais na fila inicial
    assert "João" not in fila_inicial

def test_fila_vazia():
    # Testa a função processar_fila com fila vazia
    fila_inicial = []
    atendidos = processar_fila(fila_inicial)

    # Verifica se a lista de atendidos está vazia
    assert atendidos == []
    # Verifica se a fila inicial permanece vazia
    assert fila_inicial == []

def test_coordenadas_imutaveis():
    # Testa a função obter_coordenadas_gps
    coordenadas = obter_coordenadas_gps()

    # Verifica se as coordenadas retornadas são uma tupla
    assert isinstance(coordenadas, tuple)
    # Verifica se a tupla contém exatamente dois elementos
    assert len(coordenadas) == 2
    # Verifica se os valores são os esperados (latitude e longitude de BH)
    assert coordenadas == (-19.916681, -43.934493)

# =================================================
# Testes: Arquivo dicionarios_sets.py
# =================================================

def test_perfil_funcionario():
    # Testa a função criar_relatorio_funcionario
    func = criar_relatorio_funcionario("Cristina", 50000, "Manager Tecnologia")
    assert func["nome"] == "Cristina"
    assert func["salario_anual"] == 600000  # 50000 * 12
    assert func["cargo"] == "Manager Tecnologia"
    assert func["ativo"] is True
    assert "cargo" in func # Verifica se a chave 'cargo' está presente no dicionário

def test_limpar_emails_duplicados():
    # Testa a função limpar_lista_emails
    emails_sujos = [
        "user@example.com",
        "a@example.com",
        "a@example.com",
        "admin@example.com",
        "contact@example.com"
    ]
    # Remove emails duplicados da lista
    emails_limpos = limpar_lista_emails(emails_sujos)

    # Verifica  a quantidade de emails únicos
    assert len(emails_limpos) == 4  # Deve conter apenas emails únicos

    # Verifica se os emails esperados estão na lista limpa
    assert emails_limpos == ["a@example.com", "admin@example.com", "contact@example.com", "user@example.com"]

# =================================================
# Testes: Arquivo fila_processamento.py
# =================================================

def test_organizar_tarefas():
    # Testa a função organizar_tarefa
    tarefas = [
        "Comprar leite",
        "Lavar o carro",
        "URGENTE: Pagar contas",
        "Estudar para prova",
        "URGENTE: Pagar contas",  # Duplicata
        "Comprar leite"           # Duplicata
    ]
    resultado = organizar_tarefa(tarefas)

    # Verifica a quantidade de tarefas em cada prioridade
    assert len(resultado["prioridade_alta"]) == 1  # Deve conter apenas uma tarefa urgente
    assert len(resultado["prioridade_baixa"]) == 3  # Deve conter tarefas não urgentes únicas

    # Verifica se as tarefas urgentes estão corretas
    assert "URGENTE: Pagar contas" in resultado["prioridade_alta"]

    # Verifica se as tarefas não urgentes estão corretas
    assert "Comprar leite" in resultado["prioridade_baixa"]

    # Verifica removeu duplicatas
    assert resultado["prioridade_baixa"].count("Comprar leite") == 1
    assert resultado["prioridade_alta"].count("URGENTE: Pagar contas") == 1
