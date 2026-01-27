import pytest
from src.poo_fundamentos.sistema_escola import (
    Aluno,
    Professor,
    Assistente)
from src.poo_fundamentos.agregacao import (
    Carro,
    Motor)
"""
Docstring para test.poo_fundamentos
Este módulo contém testes unitários para as classes do módulo poo_fundamentos.

Autora: Tina de Almeida
Data: 2026-01-27
Task: CDD-7: [CDD] [PYTHON] Programação Orientada a Objetos (Classes e Herança)
"""

# =================================================
# Testes: Arquivo sistema_escola.py
# =================================================

def test_aluno_apresentacao(capsys):
    # Testa o método apresentar da classe Aluno
    aluno = Aluno("Maria", 16, True, 10)
    aluno.apresentar()
    captured = capsys.readouterr()
    assert "Olá, meu nome é Maria e tenho 16 anos." in captured.out

def test_professor_apresentacao(capsys):
    # Testa o método apresentar da classe Professor
    professor = Professor("João", 35, True, "Matemática")
    professor.apresentar()
    captured = capsys.readouterr()
    assert "Olá, meu nome é João e tenho 35 anos." in captured.out

def test_assistente_apresentacao(capsys):
    # Testa o método apresentar da classe Assistente
    assistente = Assistente("Ana", 28, False, "Biblioteca")
    assistente.apresentar()
    captured = capsys.readouterr()
    assert "Olá, meu nome é Ana e tenho 28 anos." in captured.out

def test_aluno_status_ativo(capsys):
    # Testa o método verificar_status da classe Aluno para status ativo
    aluno = Aluno("Carlos", 17, True, 11)
    aluno.verificar_status()
    captured = capsys.readouterr()
    assert "Status: ATIVO" in captured.out

def test_professor_status_inativo(capsys):
    # Testa o método verificar_status da classe Professor para status inativo
    professor = Professor("Luíza", 40, False, "História")
    professor.verificar_status()
    captured = capsys.readouterr()
    assert "Status: INATIVO" in captured.out

def test_assistente_status_ativo(capsys):
    # Testa o método verificar_status da classe Assistente para status ativo
    assistente = Assistente("Pedro", 30, True, "Laboratório")
    assistente.verificar_status()
    captured = capsys.readouterr()
    assert "Status: ATIVO" in captured.out

def test_aluno_ano(capsys):
    # Testa se o atributo ano do Aluno está correto
    aluno = Aluno("Beatriz", 15, True, 9)
    assert aluno.ano == 9

def test_professor_disciplina(capsys):
    # Testa se o atributo disciplina do Professor está correto
    professor = Professor("Ricardo", 45, True, "Física")
    assert professor.disciplina == "Física"

def test_assistente_departamento(capsys):
    # Testa se o atributo setor do Assistente está correto
    assistente = Assistente("Sofia", 26, True, "Secretaria")
    assert assistente.departamento == "Secretaria"

# =================================================
# Testes: Arquivo agregacao.py
# =================================================
def test_agregacao_carro_motor(capsys):
    # Testa a agregação entre Carro e Motor
    motor_v8 = Motor(potencia="V* Turbo 300cv")
    volvo = Carro(modelo="Sedan", motor=motor_v8)

    volvo.ligar()

    captured = capsys.readouterr()
    assert "Vroom Vroom!" in captured.out
    assert "V* Turbo 300cv" in captured.out

