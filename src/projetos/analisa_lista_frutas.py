"""
Docstring para src.projetos.analisador_lista
Descrição: Módulo para analisar listas de frutas que serão informado pelo usuário.

REGRA DE NEGÓCIO:
- O arquivo executar_lista_frutas.py deve interagir com o usuário para criar e manipular uma lista de frutas.
- O programa deve solicitar ao usuário que informe uma lista de frutas, separadas por vírgula.
- O programa deve exibir a lista de frutas informada pelo usuário.
- O programa deve pedir o usuário para substituir o segundo item da lista por uma nova fruta.
- O programa deve exibir a lista atualizada de frutas.
- O programa deve pedir ao usuário uma fruta para remover da lista.
- O programa deve exibir a lista final de frutas após a remoção.
- O programa deve excluir a ultima fruta da lista e exibir a lista final.
- O programa deve criar um loop para exibir a mensagem " 🍓 Eu gosto de comer [fruta] no café da manhã." para cada fruta na lista.

Autora: Tina Almeida
Data: 2026-02-06
Task: CDD-14: [CDD] [PYTHON] Gerenciador de Lista de Frutas (CRUD e Iteração)
"""
def inicializar_lista_frutas(lista_frutas):
    """
    Inicializa a lista de frutas a partir da entrada do usuário.

    Args:
        lista_frutas (str): String contendo as frutas separadas por vírgula.

    Returns:
        list: Lista de frutas criada a partir da entrada do usuário.
    """
    # Função que recebe e cria a lista de frutas a partir da entrada do usuário
    # Divide a string de entrada em uma lista, removendo espaços extras
    frutas = [fruta.strip() for fruta in lista_frutas.split(",")]
    return frutas

def substituir_fruta(frutas, nova_fruta):
    """
    Substitui o segundo item da lista de frutas por uma nova fruta.

    Args:
        frutas (list): Lista de frutas atual.
        nova_fruta (str): Nova fruta para substituir o segundo item da lista.

    Returns:
        list: Lista de frutas atualizada após a substituição.
    """
    # Função que substitui o segundo item da lista por uma nova fruta
    if len(frutas) >= 2:
        frutas[1] = nova_fruta.strip()
    return frutas

def remover_fruta(frutas, fruta_para_remover):
    """
    Remove uma fruta específica da lista de frutas.

    Args:
        frutas (list): Lista de frutas atual.
        fruta_para_remover (str): Fruta que o usuário deseja remover da lista.

    Returns:
        list: Lista de frutas atualizada após a remoção.
    """
    # Função que remove uma fruta específica da lista
    fruta_para_remover = fruta_para_remover.strip()
    fruta_encontrada = None  # Inicializando a variável
    for item in frutas:
        if item.lower() == fruta_para_remover.lower():
            fruta_encontrada = item
            break
    # Removendo a fruta encontrada da lista
    if fruta_encontrada:
        frutas.remove(fruta_encontrada)
        print(f"✅ A fruta '{fruta_encontrada}' foi removida da lista com sucesso.")
        print(f"📜 Lista de frutas atualizada: {frutas}")
    else:
        print(f"⚠️  A fruta '{fruta_para_remover}' não foi encontrada na lista. Nenhuma fruta foi removida.")
        print(f"📜 Lista de frutas atual: {frutas}")
    return frutas

def excluir_ultima_fruta(frutas):
    """
    Exclui a última fruta da lista de frutas.

    Args:
        frutas (list): Lista de frutas atual.

    Returns:
        list: Lista de frutas atualizada após a exclusão da última fruta.
    """
    # Função que exclui a última fruta da lista
    if frutas not in (None, []) and len(frutas) > 0:
        frutas.pop()
    return frutas

def exibir_lista_frutas(frutas):
    """
    Exibe a lista de frutas.

    Args:
        frutas (list): Lista de frutas a ser exibida.
    """
    # Função que exibe a lista de frutas
    if frutas not in (None, []):
        for fruta in frutas:
            print(f"🍓 Eu gosto de comer {fruta} no café da manhã.")
    else:
        print("A lista de frutas está vazia.")

# Fim do arquivo analisa_lista_frutas.py
