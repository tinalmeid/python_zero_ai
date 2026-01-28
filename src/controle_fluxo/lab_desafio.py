"""
Docstring para src.controle_fluxo.lab_desafio
Descrição: Este módulo contém desafios práticos para aplicar estruturas de controle de fluxo em Python,
incluindo condicionais e loops.
Objetivo: Receber uma string mista e separar números e letras.

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-6: [CDD] [PYTHON] Estruturas de Controle (If, For, While)
"""

def filtrar_dados_sujos(texto_baguncado: str) -> tuple:
    """
    Recebe uma string mista e separa números e letras.

    Args:
    texto_baguncado (str): String contendo letras e números misturados.

    Returns:
    tuple: Uma tupla contendo duas strings - a primeira com os números e a segunda com as letras.
    """

    numeros = []
    letras = []

    print(f"\n📥 Processando: {texto_baguncado} ")

    for caractere in texto_baguncado:
        if caractere.isdigit():
            # Se for número, adiciona à lista de números
            numeros.append(caractere)
        elif caractere.isalpha():
            # Se for letra, adiciona à lista de letras
            letras.append(caractere)
        else:
            # Ignora outros caracteres especiais
            print(f"⚠️ Ignorando caractere não alfanumérico: {caractere}")

    # Join junta a lista em uma string única
    print(f"🔢 Números encontrados: {''.join(numeros)}")
    print(f"📝 Letras encontradas: {''.join(letras)}")

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Simulação de dado enviado vindo de um sistema legado
    dado_bruto = "C4r1s7in4_2026_T3ch"
    filtrar_dados_sujos(dado_bruto)
