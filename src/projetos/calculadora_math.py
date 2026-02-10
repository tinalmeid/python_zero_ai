"""
Docstring for calculadora_math.py
Descrição: Este módulo contém a implementação da classe Calculadora Math, que oferece uma variedade de operações matemáticas avançadas,
incluindo funções exponenciais, fatorial, recursividade e funções lambda.

REGRA DE NEGÓCIO:
- O Sistema deve receber os numeros do usuário e realizar as operações matemáticas solicitadas, retornando os resultados de forma clara e precisa.
- O Sistema deve validar as entradas do usuário, garantindo que sejam números válidos e que as operações solicitadas sejam suportadas.
- O Sistema deve lidar com casos de erro, como divisão por zero ou entrada de dados inválidos, fornecendo mensagens de erro apropriadas.
- O Sistema terá:
        Função Quadrado: Recebe um número, retorna o quadrado.
        Função Soma: Recebe dois números, retorna a soma.
        Função Potência (Default): Recebe base e expoente. Se o expoente não for informado, assume 2 (ao quadrado).
        Função Fatorial (Recursiva): Calcula o fatorial (ex: 5! = 54321) chamando a si mesma.
        Função Aninhada: Uma função principal que calcula o dobro, a outra usa esse resultado para calcular o quadrado
        Lambda Cubo: Calcula o cubo de um número.
        Lambda Multiplicação: Multiplica dois números.
        Lambda Par/Ímpar: Retorna "Par" ou "Ímpar".
        Lambda Lista: Recebe uma lista numérica e retorna o dobro de cada item (usando map).

Autora: Tina Almeida
Data: 2024-02_09
Task: [CDD-17] [CDD] [PYTHON] Implementação de Calculadora com Funções Avançadas, Recursividade e Lambdas.
"""
# Função Validar Número: Valida se a entrada é um número válido, lançando um erro caso contrário.
def validar_numero(numero):
    """Valida se a entrada é um número válido."""
    try:
        return float(numero)
    except ValueError:
        raise ValueError(f"Entrada inválida: '{numero}' não é um número.")

# Função Quadrado: Recebe um número, retorna o quadrado.
def calcular_quadrado(numero):
    """Calcula o quadrado de um número."""
    return numero ** 2

# Função Soma: Recebe dois números, retorna a soma.
def calcular_soma(num1, num2):
    """Calcula a soma de dois números."""
    return num1 + num2

# Função Potência (Default): Recebe base e expoente. Se o expoente não for informado, assume 2 (ao quadrado).
def calcular_potencia(base, expoente=2):
    """Calcula a potência de um número, com expoente padrão 2."""
    return base ** expoente

# Função Fatorial (Recursiva): Calcula o fatorial (ex: 5! = 54321) chamando a si mesma.
def calcular_fatorial(numero):
    """Calcula o fatorial de um número usando recursão."""
    if numero < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

# Função Aninhada: Uma função principal que calcula o dobro, a outra usa esse resultado para calcular o quadrado
def calcular_dobro_e_quadrado(numero):
    """Calcula o dobro de um número e depois o quadrado do resultado."""
    def calcular_dobro(n):
        return n * 2
    dobro = calcular_dobro(numero)
    print(f"O dobro de {numero} é {dobro}.")
    return calcular_quadrado(dobro)

# Lambda Cubo: Calcula o cubo de um número.
calcular_cubo_lambda = lambda x: x ** 3

# Lambda Multiplicação: Multiplica dois números.
calcular_multiplicacao_lambda = lambda x, y: x * y

# Lambda Par/Ímpar: Retorna "Par" ou "Ímpar".
calcular_par_impar_lambda = lambda x: "Par" if x % 2 == 0 else "Ímpar"

# Lambda Lista: Recebe uma lista numérica e retorna o dobro de cada item (usando map).
calcular_dobro_lista_lambda = lambda lst: list(map(lambda x: x * 2, lst))

# Fim do módulo calculadora_math.py
