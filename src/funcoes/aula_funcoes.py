"""
Docstring do módulo funcoes.py
Descrição: Este módulo implementa funções simples, argumentos padrão e *args em Python.

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-8: [CDD] [PYTHON] Funções, Argumentos Dinâmicos e Módulos
"""

def saudacao(nome: str, mensagem: str = "Bem-vinda(o) ao sistema!"):
    """
    Docstring para saudacao
    Demonstra Argumentos Default em funções Python.

    Args:
        nome (str): Nome da pessoa a ser saudada.
        mensagem (str, optional): Mensagem de saudação. Padrão é "Bem-vinda(o) ao sistema!".

    Returns:
        N/A
    """
    return f"{mensagem}, {nome}!"

def soma_numeros(num1:int, num2: int):
    """
    Docstring para soma_numeros
    Demonstra o uso de função simples.

    Args:
        num1 (int): Primeiro número.
        num2 (int): Segundo número.

    Returns:
        resultado: A soma dos dois números.
    """
    resultado = num1 + num2
    return resultado

def funcao_com_print(texto):
    """
    Docstring para funcao_com_print
    Demonstra função que apenas EXIBE( não RETORNA) um valor.

    Args:
        texto (str): Texto a ser exibido.

    Returns:
        N/A
    """
    print(f"📢 AVISO -> Função exibindo: {texto}")

def somar_varios_numeros(*args):
    """
    Docstring para somar_varios_numeros
    Demonstra o uso de *args para aceitar número variável de argumentos.

    Args:
        *args: Números inteiros a serem somados.

    Returns:
        soma_total: A soma de todos os números fornecidos.
    """
    soma_total = 0
    for numero in args:
        soma_total += numero
    return soma_total

    #---- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Testando a função de saudação
    saudacao("Tina")
    saudacao("Carlos", "Seja bem-vindo ao nosso portal!")
    print("-----")

    # Testando a função de soma simples
    resultado_soma = soma_numeros(10, 25)
    print(f"A soma de 10 e 25 é: {resultado_soma}")
    print("-----")

    # Testando a função com print
    funcao_com_print("Este é um teste de função com print.")

    print("-----")

    # Testando a função com *args
    soma_varios = somar_varios_numeros(5, 10, 15, 20)
    print(f"A soma de vários números (5, 10, 15, 20) é: {soma_varios}")
