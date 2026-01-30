"""
Docstring for projetos/executar_calculadora_tinta.py
Descrição: Módulo que espera o input dos valores informados pelo usuário, para realizar o calculo e retornar

Autora: Tina Almeida
Data: 2026-01-30
Tasks:CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.projetos.calculo_area_parede import (
     calcular_area_parede,
     calcular_rendimento_tinta,
     obter_valor_float
    )

def executar_calculadora_tinta():
    # Execução interativa da função calcular_rendimento_tinta
    print(" ")
    print("\n" + "="*10 + " Calculadora de Tinta " + "="*10)
    print("        🖌️ Cálculo de Tinta Necessária para Pintura")
    print(" ")

    largura = obter_valor_float("➡️  Informe a largura da parede (em metros): ")
    altura = obter_valor_float("➡️  Informe a altura da parede (em metros): ")
    if largura is None or altura is None:
        print("🚫 Largura e altura não podem ser None.")
        return
    if not isinstance(largura, (int, float)) or not isinstance(altura, (int, float)):
        print("🚫 Largura e altura devem ser números (int ou float).")
        return
    if largura < 0 or altura < 0:
        print("🚫 Largura e altura devem ser valores não negativos.")
        return
    area = calcular_area_parede(largura, altura)
    if area == 0:
        print("🚫 A área calculada é zero. Verifique os valores informados.")
        return
    else:
        print(f"📐 A área da parede é: {area} m²")
    print(" ")

    rendimento_litro = obter_valor_float("➡️  Informe o rendimento da tinta (m² por litro): ")
    if rendimento_litro is None:
        print("🚫 Rendimento por litro não podem ser None.")
        return
    if not isinstance(rendimento_litro, (int, float)):
        print("🚫 Rendimento por litro deve ser um número (int ou float).")
        return
    if rendimento_litro <= 0:
        print("🚫 Rendimento por litro deve ser um valor positivo.")
        return

    tinta_necessaria = calcular_rendimento_tinta(area, rendimento_litro)
    if tinta_necessaria == 0:
        print("🚫 A quantidade de tinta necessária é zero. Verifique os valores informados.")
        return
    else:
        print(f"🖌️ Quantidade de tinta necessária: {tinta_necessaria:.2f} litros")

    print("\n" + "="*40)
    print("🏁 FIM DA CALCULADORA DE TINTA")
    print("="*40)

#===== Execução Do Script ====
if __name__ == "__main__":
    executar_calculadora_tinta()

# Fim do arquivo executar_calculadora_tinta.py
