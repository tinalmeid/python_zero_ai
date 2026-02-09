"""
Docstring para tests.test_sistema_seguranca
Descrição: Testes unitários para o sistema de segurança do condomínio, cobrindo cadastro de usuários, autenticação e varredura das câmeras.

Autora: Tina de Almeida
Data: 2026-02-09
Task: CDD-15: [CDD] [PYTHON] Sistema de Segurança com Loops - Testes Unitários
"""
import pytest
from src.projetos.sistema_seguranca import (
    cadastrar_usuario,
    obter_andar_sala,
    obter_tipo_usuario,
    cadastrar_senha,
    autenticar_usuario,
    robo_varredura
)
# Testes para cadastro de usuário
@pytest.mark.parametrize("entrada_usuario, espera_dict_usuario",
[   (["1", "Tina", "123456", "123456", "2", "3"], {'tipo': '🏠 Morador', 'nome': 'Tina', 'senha': '123456', 'andar_sala': ('2', '3')}),
    (["2", "Carlos", "123456", "123456", "1", "1"], {'tipo': '🙂 Visitante', 'nome': 'Carlos', 'senha': '123456', 'andar_sala': ('1', '1')}),
    (["3", "Ana", "123456", "123456", "3", "4"], {'tipo': '🤓 Funcionário', 'nome': 'Ana', 'senha': '123456', 'andar_sala': ('3', '4')}),
                         ])
def test_cadastrar_usuario_sucesso(entrada_usuario, espera_dict_usuario, monkeypatch):
    # Simula as entradas do usuário para o cadastro
    inputs = iter(entrada_usuario)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    usuario = cadastrar_usuario()
    assert usuario == espera_dict_usuario

# Testes nome de usuário inválido
@pytest.mark.parametrize("tipo, nome_invalido, nome_corrigido, senha, andar_sala, usuario_esperado", [
    ("1", "Tina123", "Tina", "123456", ('2', '3'), {'tipo': '🏠 Morador', 'nome': 'Tina', 'senha': '123456', 'andar_sala': ('2', '3')}), # Caso 1: Números
    ("2", "Carlos!", "Carlos", "123456", ('1', '1'), {'tipo': '🙂 Visitante', 'nome': 'Carlos', 'senha': '123456', 'andar_sala': ('1', '1')}), # Caso 2: Caracteres especiais
    ("3", "Ana_456", "Ana", "123456", ('3', '4'), {'tipo': '🤓 Funcionário', 'nome': 'Ana', 'senha': '123456', 'andar_sala': ('3', '4')}), # Caso 3: Caracteres especiais e números
])
def test_cadastrar_usuario_nome_invalido(tipo, nome_invalido, nome_corrigido, senha, andar_sala, usuario_esperado, monkeypatch):
    # Simula as entradas do usuário para o cadastro com nome inválido (isAlpha) e gera um dicionário esperado para comparação
    inputs = iter([tipo, nome_invalido, nome_corrigido, senha, senha, andar_sala[0], andar_sala[1]])  # Simula as entradas do usuário

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    usuario = cadastrar_usuario()
    assert usuario == usuario_esperado

# Testes para validar tipo de usuário
@pytest.mark.parametrize("entrada_tipo, tipo_esperado", [
    ("1", "🏠 Morador"),
    ("2", "🙂 Visitante"),
    ("3", "🤓 Funcionário"),
])
def test_obter_tipo_usuario(entrada_tipo, tipo_esperado, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: entrada_tipo)
    tipo = obter_tipo_usuario()
    assert tipo == tipo_esperado

# Testes para validar tipo de usuário inválido
@pytest.mark.parametrize("entrada_tipo, tipo_esperado", [
    ("4", "1"),  # Entrada inválida seguida de uma entrada válida
    ("0", "2"),  # Entrada inválida seguida de uma entrada válida
    ("abc", "3"),  # Entrada inválida seguida de uma entrada válida
])
def test_obter_tipo_usuario_invalido(entrada_tipo, tipo_esperado, monkeypatch):
    # Simula a entrada inválida seguida da entrada válida
    inputs = iter([entrada_tipo, tipo_esperado])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    tipo = obter_tipo_usuario()
    assert tipo == ("🏠 Morador" if tipo_esperado == "1" else "🙂 Visitante" if tipo_esperado == "2" else "🤓 Funcionário")

# Testes cadastrar senha de acesso
@pytest.mark.parametrize("senha, confirmacao, senha_esperada", [
    ("123456", "123456", "123456"),
    ("111111", "111111", "111111"),
    ("101010", "101010", "101010"),
])
def test_cadastrar_senha_sucesso(senha, confirmacao, senha_esperada, monkeypatch):
    # Simula as entradas do usuário para a senha e sua confirmação
    inputs = iter([senha, confirmacao])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    senha_cadastrada = cadastrar_senha()
    assert senha_cadastrada == senha_esperada

# Testes senhas inválidas (> 6 caracteres e não numéricas)
@pytest.mark.parametrize("senha, confirmacao, senha_esperada", [
    ("12345", "123456", "123456"),  # Menos de 6 caracteres
    ("abcdef", "678900", "678900"),  # Não numérica
    ("1234567", "234567", "234567"),  # Mais de 6 caracteres
])
def test_cadastrar_senha_invalida(senha, senha_esperada, confirmacao, monkeypatch):
    # Simula a entrada da senha inválida, a confirmação e depois a entrada correta
    inputs = iter([senha, senha_esperada, confirmacao])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    senha_cadastrada = cadastrar_senha()
    assert senha_cadastrada == senha_esperada  # A senha correta deve ser cadastrada após a tentativa inválida

# Testes senhas não coincidem
@pytest.mark.parametrize("senha, confirmacao, senha_esperada", [
    ("123456", "654321", "123456"),
    ("111111", "222222", "111111"),
    ("101010", "010101", "101010"),
])
def test_cadastrar_senha_nao_coincide(senha, confirmacao, senha_esperada, monkeypatch):
    # Simula a entrada da senha e uma confirmação diferente, seguida da entrada correta
    inputs = iter([senha, confirmacao, senha])  # Simula a entrada da senha, a confirmação incorreta e depois a entrada correta
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    senha_cadastrada = cadastrar_senha()
    assert senha_cadastrada == senha_esperada

# Testes para obter apartamento/sala
@pytest.mark.parametrize("andar, sala, andar_sala_esperado", [
    ("1", "1", ('1', '1')),
    ("2", "3", ('2', '3')),
    ("3", "4", ('3', '4')),
])
def test_obter_apartamento_sala_sucesso(andar, sala, andar_sala_esperado, monkeypatch):
    inputs = iter([andar, sala])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    andar_sala = obter_andar_sala()
    assert andar_sala == andar_sala_esperado

# Testes para obter apartamento/sala com entradas inválidas
@pytest.mark.parametrize("andar_sala_incorreto, andar_sala_esperado", [
    # Cenários 1: Andar inválido "0" seguido de entrada válida "1"
    (["0", "1", "1"], ('1', '1')),
    # Cenários 2: Andar inválido "4" seguida de entrada válida "2"
    (["4", "2", "2"], ('2', '2')),
    # Cenários 3: Andar válido "1" e Sala inválida "0" seguida de entrada válida "1"
    (["1", "0", "1"], ('1', '1')),
    # Cenários 4: Andar válido "2" e Sala inválida "5" seguida de entrada válida "3"
    (["2", "5", "3"], ('2', '3')),
    # Cenários 5: Andar inválido "abc" seguida de entrada válida "3" e Sala valida "4"
    (["abc", "3", "4"], ('3', '4')),
     # Cenários 6: Andar válido "3" e Sala inválida "xyz" seguida de entrada válida "4"
    (["3", "xyz", "4"], ('3', '4')),
])

def test_obter_apto_sala_invalida(andar_sala_incorreto, andar_sala_esperado, monkeypatch):
    # Simula as entradas do usuário para o andar e sala, incluindo entradas inválidas seguidas de entradas válidas
    inputs = iter(andar_sala_incorreto)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    andar_sala = obter_andar_sala()
    assert andar_sala == andar_sala_esperado

# Testes para autenticação de usuário
@pytest.mark.parametrize("tipo, nome, senha_cadastrada, tentativas, resultado_esperado", [
    ("🏠 Morador", "Tina", "123456", ["123456"], True),  # Senha correta na primeira tentativa
    ("🙂 Visitante", "Cris","111111", ["000000", "111111"], True),  # Senha incorreta seguida da senha correta
    ("🤓 Funcionário", "Marta","101010", ["000000", "222222", "101010"], True),  # Duas tentativas incorretas seguidas da senha correta
    ("🙂 Visitante", "Mara","123456", ["000000", "111111", "222222"], False),  # Três tentativas incorretas
])
def test_autenticar_usuario(tipo, nome, senha_cadastrada, tentativas, resultado_esperado, monkeypatch):
    # Simula as tentativas de autenticação do usuário, incluindo tentativas incorretas seguidas da tentativa correta
    inputs = iter(tentativas)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    usuario = {'tipo': tipo, 'nome': nome, 'senha': senha_cadastrada, 'andar_sala': ('1', '1')}  # Simula um usuário cadastrado
    resultado = autenticar_usuario(usuario)
    assert resultado == resultado_esperado

# Testes para varredura das câmeras
def test_robo_varredura(capsys):
    # Simula a varredura das câmeras e captura a saída para verificar se o status foi atualizado corretamente
    robo_varredura()
    captured = capsys.readouterr()
    assert "Varredura das câmeras concluída. Status atualizado para todas as salas." in captured.out

