"""
Docstring para src.projetos.sistema_seguranca
Descrição do módulo: Módulo de sistema de portaria para controle de acesso em um condomínio.

REGRA DE NEGÓCIO:
Usar loops diferentes de "for" para implementar as funcionalidades do sistema de portaria, como "loop aninhado", "while", "do-while", "break e continue".
1. O sistema deve permitir o cadastro de moradores, visitantes e funcionários.
2. O sistema deve solicitar a identificação do visitante ou funcionário na entrada e saída do condomínio.
4. O sistema deve continuar solicitando a senha de acesso até que a senha correta seja fornecida. "Acesso Permitido 🔓"
5. O sistema deve bloquear o acesso após 3 tentativas de senha incorreta."Acesso Bloqueado 🔒"
6. O prédio tem 3 Andares (1 a 3) e cada andar tem 4 Salas (1 a 4).
7. O sistema tem a seguinte pre-lista de mensagens:
- "Sistema de Segurança do Condomínio XPTO Iniciado!"
- "Bem-vindo ao Condomínio XPTO!"
- "Sistema verificando Camera da Sala "numero da sala" no Andar "numero do andar"..."
- "Acesso Negado! Você não tem permissão para acessar esta sala."
- "Acesso Permitido! Você tem permissão para acessar esta sala."
- "A sala 1 do andar 2 está com a câmera desligada. Acesso Negado!"
- "A sala 3 do andar 2 está em reforma. Acesso Negado!"
- "A sala 4 do andar 3 está reservada para eventos. Acesso Negado!"
- "A sala 4 do andar 1 tem um intruso detectado. 🚨 ALERTA: Intruso detectado! Parando varredura."
- "A sala 3 do andar 3 tem um intruso detectado. 🚨 ALERTA: Intruso detectado! Parando varredura."
- "Por favor, identifique-se: (1) Morador, (2) Visitante, (3) Funcionário"
- "Digite sua senha de acesso:"
- "Acesso Permitido 🔓"
- "Acesso Bloqueado 🔒"
- "Cadastro de Morador, Visitante ou Funcionário"
- "Digite o número do andar (1-3):"
- "Digite o número da sala (1-4):"
- "Cadastro realizado com sucesso!"
- "Encerrando o sistema de segurança do condomínio. Até logo!"
8. O Sistema deve imprimir antes de cada menagem a data e hora atual no formato "dd/mm/yyyy HH:MM:SS".

Autora: Tina de Almeida
Data: 2026-02-09
Task: CDD-15: [CDD] [PYTHON] Sistema de Segurança com Loops
"""
import datetime
import time

def cadastrar_usuario():
    """
    Docstring para cadastrar_usuario
    Descrição: Função para cadastrar moradores, visitantes e funcionários no sistema de segurança do condomínio.
    Deve chamar as funções:
        obter tipo de usuário,
        cadastrar senha,
        obter apto/sala,
    e retornar um dicionário com as informações do usuário.

    Args:
        None

    Retorna:
        dict: Um dicionário contendo as informações do usuário cadastrado.
    """
    print("Cadastro de Morador, Visitante ou Funcionário")
    # Obter o tipo de usuário (Morador, Visitante ou Funcionário)
    tipo_usuario = obter_tipo_usuario()

    # Obter nome do usuário
    nome_usuario = input("Digite seu primeiro nome: ").title()  # Formata o nome para ter a primeira letra maiúscula
    while not nome_usuario.isalpha():
        print("🔴 Nome inválido. Por favor, digite apenas letras.")
        nome_usuario = input("Digite seu primeiro nome: ").title()

    # Obter a senha de acesso do usuário
    senha = cadastrar_senha()
    # Obter o número do apartamento e sala do usuário
    andar_sala = obter_andar_sala()

    # Criar um dicionário para armazenar as informações do usuário
    usuario = {
        "tipo": tipo_usuario,
        "nome": nome_usuario,
        "senha": senha,
        "andar_sala": andar_sala
    }
    return usuario

def obter_tipo_usuario():
    """
    Docstring para obter_tipo_usuario
    Descrição: Função para obter o tipo de usuário (Morador, Visitante ou Funcionário) a partir da entrada do usuário.

    Args:
        None

    Retorna:
        str: O tipo de usuário selecionado
        (1) 🏠 Morador,
        (2) 🙂 Visitante,
        (3) 🤓 Funcionário"
    """
    mapeamento_tipos = {
        '1': "🏠 Morador",
        '2': "🙂 Visitante",
        '3': "🤓 Funcionário"
    }

    print("Por favor, identifique-se: (1) 🏠 Morador, (2) 🙂 Visitante, (3) 🤓 Funcionário")
    tipo = input("Digite o número correspondente ao seu tipo de usuário: ")
    # Validar a entrada do usuário para garantir que seja uma opção válida
    while tipo not in ['1', '2', '3']:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")
        tipo = input("Digite o número correspondente ao seu tipo de usuário: ")

    print(f"Foi selecionado o tipo de usuário: " + mapeamento_tipos[tipo])
    return mapeamento_tipos[tipo]

def cadastrar_senha():
    """
    Docstring para cadastrar_senha
    Descrição: Função para cadastrar a senha de acesso do usuário. Deve solicitar ao usuário que digite uma senha e confirmá-la.
    A senha deve ter 6 caracteres do tipo numérico.
    Enquanto a senha não for validada pela regra de negócio, a função deve continuar solicitando a senha e a confirmação.

    Args:
        None

    Retorna:
        str: A senha de acesso cadastrada pelo usuário.
    """
    print("Por favor, digite a senha de 6 caracteres numéricos")
    senha = input("🔑 Digite a senha: ")
    # Validar a senha para garantir que tenha 6 caracteres numéricos
    while not (senha.isnumeric() and len(senha) == 6):
        print("🔴 Senha inválida. A senha deve conter exatamente 6 caracteres numéricos.")
        senha = input("🔑 Digite a senha: ")

    confirmacao = input("🔑 Confirme a senha: ")

    # Validar a confirmação da senha para garantir que coincida com a senha digitada
    while senha != confirmacao:
        print("🔴 As senhas não coincidem. Por favor, tente novamente.")
        confirmacao = input("🔑 Confirme a senha: ")
    print("✅ Senha cadastrada com sucesso!")
    return senha

def obter_andar_sala():
    """
    Docstring para obter_andar_sala
    Descrição: Função para obter o número do andar e da sala do usuário. Deve solicitar ao usuário que digite o número do andar e da sala.
    O número do andar deve ser entre 1 e 3, e o número da sala deve ser entre 1 e 4.
    Enquanto os números não forem válidos, a função deve continuar solicitando as informações.

    Args:
        None

    Retorna:
        tuple: Uma tupla contendo o número do andar e da sala (andar, sala).
    """
    print("Por favor, informe o número do andar (1-3) e da sala (1-4)")
    andar = input("Digite o número do andar (1-3): ")
    # Validar a entrada do usuário para garantir que o número do andar seja entre 1 e 3
    while andar not in ['1', '2', '3']:
        print("Número de andar inválido. Por favor, digite um número entre 1 e 3.")
        andar = input("Digite o número do andar (1-3): ")
    sala = input("Digite o número da sala (1-4): ")
    # Validar a entrada do usuário para garantir que o número da sala seja entre 1 e 4
    while sala not in ['1', '2', '3', '4']:
        print("Número de sala inválido. Por favor, digite um número entre 1 e 4.")
        sala = input("Digite o número da sala (1-4): ")

    print(f"Foi selecionado o apartamento/sala: Andar {andar}, Sala {sala}")
    return (andar, sala)

def autenticar_usuario(usuario):
    """
    Docstring para autenticar_usuario
    Descrição: Função para autenticar o usuário com base na senha cadastrada. Deve solicitar ao usuário que digite a senha de acesso e comparar com a senha cadastrada.
    O usuário tem 3 tentativas para digitar a senha correta.
    Se a senha for correta, a função deve retornar True. Se a senha for incorreta após 3 tentativas, a função deve retornar False.

    Args:
        usuario (dict): Um dicionário contendo as informações do usuário, incluindo a senha cadastrada.

    Retorna:
        bool: True se a autenticação for bem-sucedida, False se a autenticação falhar após 3 tentativas.
    """
    print(f"\n🔐 Autenticação do usuário {usuario['nome']} iniciada.")
    tentativas = 0
    while tentativas < 3:
        senha_input = input("Digite sua senha de acesso: ")
        if senha_input == usuario['senha']:
            print("Acesso Permitido 🔓")
            print(f"Bem-vindo, {usuario['nome']}! Você é um ({usuario['tipo']}) e tem acesso ao Apto/Sala: {usuario['andar_sala']}")
            print("Data e hora do acesso: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(" ")
            return True
        else:
            tentativas += 1
            print(f"Senha incorreta. Tentativa {tentativas} de 3.")
            print("Data e hora última tentativa: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(" ")
    print("Acesso Bloqueado 🔒")
    return False

def robo_varredura():
    """
    Docstring para robo_varredura
    Descrição: Função para simular um robô de varredura de segurança que percorre os andares e salas do condomínio.
    O robô deve imprimir mensagens pré-definidas para cada sala, indicando o status da câmera ou se há algum alerta.
    Se o robô detectar um intruso na sala 4 do andar 1, ele deve imprimir uma mensagem de alerta e parar a varredura.

    Args:
        None

    Retorna:
        None
    """
    # Pre-lista de mensagens para o robô de varredura
    mensagens = {
        "Sistema de Segurança do Condomínio XPTO Iniciado!": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - Bem-vindo ao Condomínio XPTO!",
        (1, 1): "A sala 1 do andar 1 tem um intruso detectado. 🚨 ALERTA: Intruso detectado! Parando varredura.",
        (1, 2): "A sala 2 do andar 1 está com a câmera desligada. Acesso Negado!",
        (1, 3): "A sala 3 do andar 1 está em reforma. Acesso Negado!",
        (1, 4): "A sala 4 do andar 1 tem um intruso detectado. 🚨 ALERTA: Intruso detectado! Parando varredura.",
        (2, 1): "A sala 1 do andar 2 está com a câmera desligada. Acesso Negado!",
        (2, 2): "A sala 2 do andar 2 está funcionando normalmente. Acesso Permitido!",
        (2, 3): "A sala 3 do andar 2 está em reforma. Acesso Negado!",
        (2, 4): "A sala 4 do andar 2 está funcionando normalmente. Acesso Permitido!",
        (3, 1): "A sala 1 do andar 3 está funcionando normalmente. Acesso Permitido!",
        (3, 2): "A sala 2 do andar 3 está funcionando normalmente. Acesso Permitido!",
        (3, 3): "A sala 3 do andar 3 tem um intruso detectado. 🚨 ALERTA: Intruso detectado! Parando varredura.",
        (3, 4): "A sala 4 do andar 3 está reservada para eventos. Acesso Negado!"
    }
    # Simular a varredura do robô pelos andares e salas
    # Loop aninhado para percorrer os andares e salas
    # Primeiro loop para os andares (1 a 3)
    for andar in range(1, 4):
        print(f"\n🔍 Sistema verificando Câmera da Sala no Andar {andar}...")
        time.sleep(1)  # Simular o tempo de verificação da câmera
        # Segundo loop para as salas (1 a 4)
        for sala in range(1, 5):
            print(f"Verificando a sala {sala} do andar {andar}...")
            time.sleep(1)  # Simular o tempo de verificação da sala
            # Se o robô detectar um intruso na sala 4 do andar 1 e sala 3 do andar 3, ele deve imprimir uma mensagem de alerta e parar a varredura
            if (andar, sala) == (1, 4) or (andar, sala) == (3, 3) or (andar, sala) == (1, 1):
                print(f"🚨 ALERTA: Intruso detectado na sala {sala} do andar {andar}! Parando varredura.")
                break  # Parar a varredura se um intruso for detectado
            # Se o robô detectar mensagem de sala em reforma ou câmera desligada, ele deve imprimir a mensagem e continuar a varredura (1,3 e 2,3) e (1,2 e 2,1)
            elif (andar, sala) in [(1, 2), (2, 1), (1, 3), (2, 3)]:
                print(mensagens[(andar, sala)])
                continue  # Continuar a varredura para as próximas salas

            # Para as outras salas, o robô deve imprimir a mensagem de acesso permitido
            else:
                print(mensagens[(andar, sala)])
    print("Varredura das câmeras concluída. Status atualizado para todas as salas.")

