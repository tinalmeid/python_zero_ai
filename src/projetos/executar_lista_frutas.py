"""
Docstring para src.projetos.executar_lista_frutas
Descrição: Executa a função de análise de lista de frutas e interage com o usuário.

Autora: Tina Almeida
Data: 2026-02-06
Task: CDD-14: [CDD] [PYTHON] Gerenciador de Lista de Frutas (CRUD e Iteração)
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.projetos.analisa_lista_frutas import (
    inicializar_lista_frutas,
    substituir_fruta,
    remover_fruta,
    excluir_ultima_fruta,
    exibir_lista_frutas
)

def executar_lista_frutas():
    # Execução interativa com o usuário para criar e manipular uma lista de frutas
    print(" ")
    print("\n" + "="*10+ " 🍅 Gerenciador de Lista de Frutas 🍅 " + "="*10)

    #Solicitar ao usuário que informe uma lista de frutas, separadas por vírgula
    lista_frutas = input("Informe 6 frutas para sua lista, separadas por vírgula: ")
    frutas = inicializar_lista_frutas(lista_frutas)
    # Exibir a lista de frutas informada pelo usuário
    print(f"\n📜 Lista de frutas informada pelo usuário: {frutas}")
    print ("")

    #Exibe o primeiro item da lista
    print(f"\n🍓 Primeira fruta da lista: {frutas[0]}")
    print("")

    # Exibe o ultimo item da lista
    print(f"\n🍓 Última fruta da lista: {frutas[-1]}")
    print("")

    #Exibe o segundo item da lista e pede para o usuário substituir por uma nova fruta
    print(f"\n🍓 Segunda fruta da lista: {frutas[1]}")
    nova_fruta = input("\n🔄 Informe uma nova fruta para substituir a segunda fruta da lista: ")
    frutas = substituir_fruta(frutas, nova_fruta)
    # Exibe a lista atualizada de frutas
    print(f"\n📜 Lista de frutas atualizada: {frutas}")
    print("")

    #Pede ao usuário uma fruta para remover da lista
    fruta_para_remover = input("\n🗑️  Informe uma fruta para remover da lista: ")
    remover_fruta(frutas, fruta_para_remover)
    print("")

    #Exclui a última fruta da lista
    print(f"\n🍓 Última fruta da lista antes de excluir: {frutas[-1]}")
    frutas = excluir_ultima_fruta(frutas)
    print(f"\n📜 Lista de frutas após excluir a última fruta: {frutas}")
    print("")

    # Loop para exibir a mensagem para cada fruta na lista
    exibir_lista_frutas(frutas)

    print("\n" + "="*50)
    print("🏁 FIM DO PROJETO PONTO DO STEAK")
    print(" ")

#===== Execução Do Script ====
if __name__ == "__main__":
    executar_lista_frutas()

# Fim do arquivo src/projetos/executar_lista_frutas.py
