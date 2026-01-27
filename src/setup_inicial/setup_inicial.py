"""
Docstring para src.setup_inicial.setup_inicial
Este módulo pode conter funções e classes relacionadas à configuração inicial do projeto.
Servindo como ponto de partida para outras funcionalidades.

Autor: Tina de Almeida
Data: 2026-01-26
Versão: 1.0.0
Task: CDD-5 : [CDD] [PYTHON] Setup: Ambiente, CI/CD e Quality Gate
"""

def formatar_hostname(nome_do_host: str, nome_do_dominio: str) -> str:
    """
    Docstring para formatar_hostname
    Formata o nome do host e anexa o domínio, garantindo o formato correto.
    Aplica o Princípio da Responsabilidade Única (SRP) ao focar apenas na formatação do hostname.
    Apenas forma o hostname, sem realizar validações adicionais.

    Args:
        nome_do_host (str): O nome do host a ser formatado.
        nome_do_dominio (str): O domínio a ser anexado ao nome_do_host.

    Returns:
        str: O nome_do_host formatado com o domínio anexado. Exemplo: 'router1.exemplo.com'
        Retorna string vazia se o nome_do_host fornecido for inválido.
    """
    if not nome_do_host or not nome_do_host.strip():
        return ""

    if not nome_do_dominio or not nome_do_dominio.strip():
        return ""

    nome_limpo = nome_do_host.strip().lower()
    dominio_limpo = nome_do_dominio.strip().lower()

    #Garante que não duplique o ponto se o usuário já incluiu o ponto
    if dominio_limpo.startswith('.'):
        dominio_limpo = dominio_limpo[1:]

    return f"{nome_limpo}.{dominio_limpo}"


def construir_fqdn(nome_do_host: str, nome_do_dominio: str) -> str:
    """
    Constrói um FQDN (Fully Qualified Domain Name) reutilizando a lógica de formatação.

    Retorna string vazia se host ou domínio forem inválidos.

    Args:
        nome_do_host (str): Parte do hostname.
        nome_do_dominio (str): Domínio a ser anexado.

    Returns:
        str: FQDN em minúsculas ou string vazia se inválido.
    """
    return formatar_hostname(nome_do_host, nome_do_dominio)

def validar_porta_rede(num_porta: int) -> bool:
    """
    Docstring para validar_porta_rede
    Verifica se o número da porta está dentro do intervalo padrão TCP/UDP (1-65535).
    Aplica o Princípio da Responsabilidade Única (SRP) ao focar apenas na validação do número da porta.

    Args:
        num_porta (int): O número da porta a ser validado.

    Returns:
        bool: True se a porta for válida, False caso contrário.

    :PORTA_MAXIMA: Constante representando a porta máxima permitida (65535).
    :PORTA_MINIMA: Constante representando a porta mínima permitida (1).
    """
    PORTA_MAXIMA = 65535
    PORTA_MINIMA = 1

    if not isinstance(num_porta, int):
        return False

    return PORTA_MINIMA <= num_porta <= PORTA_MAXIMA

def categorizar_latencia(latencia_ms: float) -> str:
    """
    Docstring para categorizar_latencia
    Classifica a latência em categorias: '👆🏾 Excelente', '👍🏾 Alta Latência', '🤞🏾 Normal' ou '🔴 Erro: Latência negativa'

    Regra de Negócio:
    Em latência, quanto menor o valor, melhor a qualidade da conexão.
    - <= 20ms: Muito rápido (Excelente)
    - Entre 21ms e <= 100ms: Aceitável (Normal)
    - Maior que 101ms: Lento (Alta Latência)

    Aplica o Princípio da Responsabilidade Única (SRP) ao focar apenas na categorização da latência.

    Args:
        latencia_ms (float): A latência em milissegundos.

    Returns:
        str: A categoria da latência ('👆🏾 Excelente', '👍🏾 Alta Latência', '🤞🏾 Normal' ou '🔴 Erro: Latência negativa').
    """
    if latencia_ms < 0:
        return "🔴 Erro: Latência negativa."

    elif latencia_ms <= 20.0:
        return "👆🏾 Excelente"

    elif latencia_ms <= 100.00:
        return "🤞🏾 Normal"

    else:
        return "👍🏾 Alta Latência"
