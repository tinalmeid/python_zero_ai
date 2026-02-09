"""
Docstring para src.projetos.executar_sistema_seguranca
Descrição: Script principal para executar o sistema de segurança do condomínio.
O sistema permite o cadastro de moradores, visitantes e funcionários, além de controlar o acesso às salas
do condomínio com base em permissões e status das câmeras.

Autora: Tina de Almeida
Data: 2026-02-09
Task: CDD-15: [CDD] [PYTHON] Sistema de Segurança com Loops
"""
import datetime
import time
import sys
import os
from sistema_seguranca import (
    cadastrar_usuario,
    autenticar_usuario,
    robo_varredura
)

def executar_sistema_seguranca():
    print("")
    print("\n" + "="*10+ " 🏢 Sistema de Segurança do Condomínio XPTO Iniciado! 🏢")
    print("Bem-vindo ao Condomínio XPTO!")
    print("Data e hora atual: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(" ")

    # Cadastro de usuário
    usuario = cadastrar_usuario()
    if usuario is None:
        print("🔴 Cadastro falhou. Encerrando o sistema.")
        return
    print(f"\n✅ Usuário cadastrado com sucesso: {usuario['nome']} que é um ({usuario['tipo']}) para o Apto/Sala: {usuario['andar_sala']}")
    print(" ")

    # Simulação de autenticação do usuário
    autenticar_usuario(usuario)

    # Simulação de varredura das câmeras
    robo_varredura()
    print(" ")

    # Simulação de acesso a salas (a ser implementada)
    # Aqui você pode adicionar a lógica para verificar o acesso às salas com base no tipo de usuário e status das câmeras

    print("Encerrando o sistema de segurança do condomínio. Até logo 👋🏾!")
    print("Data e hora de encerramento: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(" ")

#===== Execução Do Script ====
if __name__ == "__main__":
    executar_sistema_seguranca()

# Fim do arquivo src.projetos.executar_sistema_seguranca.py
