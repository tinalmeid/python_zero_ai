"""
Docstring for executar_calculadora_math.py
Descrição: Este módulo é responsável por executar a classe Calculadora Math, permitindo que o usuário interaja com as operações matemáticas avançadas implementadas na classe.

Autora: Tina Almeida
Data: 2024-02_09
Task: [CDD-17] [CDD] [PYTHON] Implementação de Calculadora com Funções Avançadas, Recursividade e Lambdas.
"""
import sys
import os

# Importa a classe Calculadora Math do módulo calculadora_math
from calculadora_math import (
    validar_numero,
    calcular_quadrado,
    calcular_soma,
    calcular_potencia,
    calcular_fatorial,
    calcular_dobro_e_quadrado,
    calcular_cubo_lambda,
    calcular_multiplicacao_lambda,
    calcular_par_impar_lambda,
    calcular_dobro_lista_lambda,
)

def executar_calculadora():
    """Função principal para executar a calculadora."""

    while True:
        print("*"*50)
        print("\nCalculadora Math 🧮 - Operações Disponíveis:")
        print("1. Quadrado")
        print("2. Soma")
        print("3. Potência")
        print("4. Fatorial")
        print("5. Aninhada")
        print("6. Cubo (Lambda)")
        print("7. Multiplicação (Lambda)")
        print("8. Par/Ímpar (Lambda)")
        print("9. Lista (Lambda)")
        print("0. Sair")

        escolha = input("Escolha uma operação (0-9): ")
        print(" ")

        if not escolha.isnumeric() or escolha not in [str(i) for i in range(10)]:
            print(" 🔴  Entrada inválida. Por favor, insira um número entre 0 e 9.")
            continue
        if escolha == '0':
           print("Encerrando a calculadora. Até logo ! 👋")
           break

        try:
            if escolha == '1':
                "Chama a função para calcular o quadrado"
                quadrado = validar_numero(input("Digite um número para calcular o quadrado: "))
                resultado = calcular_quadrado(quadrado)
                print(f"O quadrado de {quadrado} é {resultado}.")

            if escolha == '2':
                "Chama a função para calcular a soma"
                num1 = validar_numero(input("Digite o primeiro número: "))
                num2 = validar_numero(input("Digite o segundo número: "))
                resultado = calcular_soma(num1, num2)
                print(f"A soma de {num1} e {num2} é {resultado}.")

            if escolha == '3':
                "Chama a função para calcular a potência"
                base = validar_numero(input("Digite a base: "))
                expoente_input = input("Digite o expoente (pressione Enter para usar o padrão 2): ")
                expoente = validar_numero(expoente_input) if expoente_input else 2
                resultado = calcular_potencia(base, expoente)
                print(f"{base} elevado a {expoente} é {resultado}.")

            if escolha == '4':
                "Chama a função para calcular o fatorial"
                numero = validar_numero(input("Digite um número para calcular o fatorial: "))
                resultado = calcular_fatorial(int(numero))
                print(f"O fatorial de {int(numero)} é {resultado}.")

            if escolha == '5':
                "Chama a função para calcular o dobro e depois o quadrado"
                numero = validar_numero(input("Digite um número para calcular o dobro e depois o quadrado: "))
                resultado = calcular_dobro_e_quadrado(numero)
                print(f"O quadrado do dobro de {numero} é {resultado}.")

            if escolha == '6':
                "Chama a função lambda para calcular o cubo"
                numero = validar_numero(input("Digite um número para calcular o cubo: "))
                resultado = calcular_cubo_lambda(numero)
                print(f"O cubo de {numero} é {resultado}.")

            if escolha == '7':
                "Chama a função lambda para multiplicar dois números"
                num1 = validar_numero(input("Digite o primeiro número: "))
                num2 = validar_numero(input("Digite o segundo número: "))
                resultado = calcular_multiplicacao_lambda(num1, num2)
                print(f"A multiplicação de {num1} e {num2} é {resultado}.")

            if escolha == '8':
                "Chama a função lambda para verificar se um número é par ou ímpar"
                numero = validar_numero(input("Digite um número para verificar se é par ou ímpar: "))
                resultado = calcular_par_impar_lambda(numero)
                print(f"O número {numero} é {resultado}.")

            if escolha == '9':
                "Chama a função lambda para calcular o dobro de cada item em uma lista"
                lista_input = input("Digite uma lista de números separados por vírgula: ")
                lista = [validar_numero(item.strip()) for item in lista_input.split(",")]
                resultado = calcular_dobro_lista_lambda(lista)
                print(f"Sua lista  é {lista}")
                print(f"O dobro de cada item na lista é {resultado}.")

        except ValueError as e:
            print(f" 🔴  Erro: {e}")
            continue


        # Aqui você pode adicionar a lógica para chamar as funções da classe Calculadora Math com base na escolha do usuário


    print("\n" + "="*40)
    print("🏁 FIM DO PROJETO CALCULADORA MATH")
    print(" ")


#====== Execução Do Script ======
if __name__ == "__main__":
    executar_calculadora()

# Fim do arquivo src.projetos.executar_calculadora_math.py

