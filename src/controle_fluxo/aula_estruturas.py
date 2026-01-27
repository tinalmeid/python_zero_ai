"""
Docstring para src.controle_fluxo.aula_estruturas
Descrição: Este módulo contém exemplos de estruturas de controle de fluxo em Python,
incluindo condicionais e loops.

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-6: [CDD] [PYTHON] Estruturas de Controle (If, For, While)
"""

def demonstrar_condicionais(idade: int, possui_cnh: bool) -> str:
    """
    Demonstra o uso de if, elif e else e operadores lógicos.

    Args:
    idade (int): A idade da pessoa.
    possui_cnh (bool): Indica se a pessoa possui CNH.

    Returns:
    str: Mensagem indicando se a pessoa pode dirigir.
    """

    print(f"\n--- Analisando perfil: {idade} anos, CNH: {possui_cnh} ---")

    # Estrutura condicional composta (if-elif-else)
    if idade >= 18 and possui_cnh:
        print("✅ Pode dirigir.")
        return "Pode dirigir."
    elif idade >= 18 and not possui_cnh:
        print("⚠️ Maior de idade, mas precisa tirar a CNH.")
        return "Maior de idade, mas precisa tirar a CNH."
    else:
        print("⛔ Não pode dirigir.")
        return "Não pode dirigir."

def demonstrar_loops():
    """
    Demonstra For Loops, Nested Loops e Interação de Strings.

    Args: N/A

    Returns: N/A
    """

    print("\n--- 1. Loop Simples (Range) ---")
    # Range(1, 4) vai gerar: 1, 2, 3 (4 não incluso, por ser exclusivo)
    for numero in range(1, 4):
        print(f"Número atual: {numero}")

    print("\n--- 2. Iterando Strings ---")
    palavra = "Python"
    for letra in palavra:
        #end= "" evita a quebra de linha automática
        print(f"Letra atual: {letra}")
    print()  # Quebra de linha após o loop

    print("\n--- 3. Nested Loops (Loops Aninhados) ---")
    # Matriz de coordenadas (x, y)
    for x in range(1, 4): # Loop externo
        for y in range(1, 4): # Loop interno
            print(f"Coordenada: ({x}, {y})")

def demonstrar_while_e_ternario(bateria: int):
    """
    Demonstra While Loop e Operador Ternário.

    Args:
    bateria (int): Nível inicial da bateria.

    Returns: N/A
    """

    # Demonstração do While Loop e Operador Ternário
    print(f"\n--- Iniciando Sistema com {bateria}% de bateria ---")

    #While: Executa ENQUANTO a condição for verdadeira
    while bateria > 0:
        # Operador Ternário: [valor se verdadeiro] if [condição] else [valor se falso]
        status = "🟢 Crítico" if bateria <= 20 else "🔵 Normal"

        print(f"Nível: {bateria}%, Status: {status}")
        bateria -= 20  # Decrementa para simular o consumo de bateria

    print("🔴 Bateria esgotada!")

    # --- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Testando estruturas condicionais
    demonstrar_condicionais(20, True)
    demonstrar_condicionais(25, False)
    demonstrar_condicionais(16, False)

    # Testando loops
    demonstrar_loops()

    # Testando while loop e operador ternário
    demonstrar_while_e_ternario(50)
