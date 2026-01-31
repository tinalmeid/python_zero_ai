"""
Docstring for src/projetos/ponto_steak.py
Descrição: Implementa a função que retorna para o usuário qual é o ponto da carne,
de acordo com a temperatura que ele informa.
Usando estruturas condicionais para determinar o ponto da carne.(if, elif, else).

REGRA DE NEGÓCIO:
Usaremos celsius como unidade de medida da temperatura.
- Abaixo de 48°C: Precisa de mais cozimento
- Entre 48°C e 54°C (inclusive ): Mal passado
- Entre 55°C e 60°C (inclusive): Ao ponto para mal
- Entre 61°C e 65°C (inclusive): Ao ponto
- Entre 66°C e 70°C (inclusive): Ao ponto para bem
- 71°C : Bem passado
- Acima de 71°C: Passou do ponto

Autora: Tina Almeida
Data: 2026-01-29
Task: CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""

def ponto_steak(temperatura_celsius):
    """
    Retorna o ponto de cozimento da carne com base na temperatura em Celsius

    Args:
        temperatura_celsius (float): Temperatura da carne em graus Celsius.


    Returns:
        str: Descrição do ponto de cozimento da carne.
    """

    try:
        # Converte a entrada para float
        if temperatura_celsius is None or isinstance(temperatura_celsius, dict):
            raise ValueError ("⛔ Erro: Por favor, insira um valor numérico válido para a temperatura.")

        temperatura = float(temperatura_celsius)
    except (ValueError, TypeError):
        return "⛔ Erro: Por favor, insira um valor numérico válido para a temperatura."

    if temperatura < 48:
        return "🥩 Precisa de mais cozimento"

    elif 48 <= temperatura <= 54:
        return "🥩 Mal passado"

    elif 55 <= temperatura <= 60:
        return "🥩 Ao ponto para mal"

    elif 61 <= temperatura <= 65:
        return "🥩 Ao ponto"

    elif 66 <= temperatura <= 70:
        return "🥩 Ao ponto para bem"

    elif temperatura == 71:
        return "🥩 Bem passado"

    else:
        return "🥩 Passou do ponto"

# Fim do arquivo ponto_steak.py
