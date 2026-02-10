"""
Docstring para src.projetos.executar_estados_brasil
Descrição: Executa a função informar_sigla_estado e interage com o usuário para exibir os estados do Brasil e suas capitais.
Utiliza a função informar_sigla_estado do módulo projetos.estados_brasil para solicitar ao usuário a sigla de um estado do Brasil e exibir sua capital.

Autora: Tina Almeida
Data: 2026-02-09
Task: CDD-16: [CDD] [PYTHON] Manipulação de Estados Brasileiros com Dicionários e Operações de Conjuntos (Sistema de Geografia de Viagens)
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.projetos.estados_brasil import (
    informar_sigla_estado,
    analisar_viagens
)

def executar_estados_brasil():
    # Execução interativa da função informar_sigla_estado
    print(" ")
    print("\n" + "="*10+ " 🌎 Estados do Brasil 🌎 " + "="*10)
    informar_sigla_estado()

    print(" ")
    print("\n" + "="*10+ " 🛫 Analisar Viagens 🛫 " + "="*10)
    resultados = analisar_viagens()
    print(" ↔️  Interseção:", resultados["interseccao"])
    print(" ↗️  Diferença do Usuário 1:", resultados["diferenca_usuario1"])
    print(" ↘️  Diferença do Usuário 2:", resultados["diferenca_usuario2"])
    print(" ➕  União:", resultados["uniao"])
    print("\n" + "="*40)

    print("🏁 FIM DO PROJETO ESTADOS DO BRASIL")
    print(" ")

#====== Execução Do Script ======
if __name__ == "__main__":
    executar_estados_brasil()

# Fim do arquivo src.projetos.executar_estados_brasil.py
