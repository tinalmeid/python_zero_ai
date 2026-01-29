from typing import Any, Union, List

"""
Docstring for src/tratamentos_erros/gerenciador.py
Descrição: Este módulo contém exemplos de como implementar tratamentos de erros em Python, incluindo o uso de blocos try-except, criação de exceções personalizadas e boas práticas para lidar com erros em aplicações.

Autor: Tina Almeida
Data: 2026-01-28
Task: CDD-10 : [CDD] [PYTHON] Tratamento de Exceções (Try, Except, Finally)

"""

def dividir_seguro(numerador: float, denominador: float) -> Union[float, None]:
    """
    Função que realiza uma divisão segura, tratando possíveis erros de divisão por zero.
    Usando try-except-finally para gerenciar exceções.
    - Try: Tenta executar o bloco de código que pode gerar uma exceção.
    - Except: Captura e trata a exceção específica (ZeroDivisionError).
    - Else: Executa se o bloco try for bem-sucedido.
    - Finally: Executa sempre, independentemente de ocorrer uma exceção ou não.

    Args:
        numerador (float): O numerador da divisão.
        denominador (float): O denominador da divisão.

    Returns:
        float: O resultado da divisão ou uma mensagem de erro.
        None: Se ocorrer um erro.
    """
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        print(f"❌ ERRO CRÍTICO: Tentativa de divisão por zero ({numerador}/{denominador})")
        return None
    except TypeError:
        print(f"❌ ERRO DE TIPO: Por favor, envie apenas números")
        return None
    else:
        print(f"✅ Sucesso: {numerador} dividido por {denominador} é {resultado}")
        return resultado
    finally:
        print("🔄 Operação de divisão finalizada (Independente do resultado).")

def acessar_banco_dados_fake(dados: List[Any], indice: int) -> Any:
    """
    Simula um acesso a BD(lista) e trata erros de índice inválido.

    Evita o IndexErroR que travaria o programa se o usuários pedisse o item 10 de uma lista que só exista 3

    Args:
        dados (List[Any]): A lista simulando o banco de dados.
        indice (int): O índice do item a ser acessado.

    Returns:
        Any: O item acessado ou uma mensagem de erro.

    """

    try:
        valor = dados[indice]
        return valor
    except IndexError:
        print(f"❌ ERRO: Índice {indice} fora do intervalo. A lista contém {len(dados)} itens.")
        # Boas Praticas: Retornar um valor padrão ou None em vez de quebrar
        return None
    except Exception as erro_generico:
        # Má Pratica: Capturar exceções genéricas sem tratamento específico
        # Só para fins ilustrativos
        print(f"❌ ERRO GENÉRICO: Ocorreu um erro inesperado: {erro_generico}")
        return None



