"""
Docstring do arquivo funcionario.py
Descrição: Este módulo estrutura exemplos de Classes e Objetos em Python,
dentro do contexto de funcionários em uma empresa.

Autora: Tina Almeida
Data: 2026-01-28
Task: CDD-11: [CDD] [PYTHON] Programação Orientada a Objetos (Classes e Objetos)
"""

class Funcionario:
    """
    Docstring para Funcionario
    Classe que representa (é um molde) um funcionário em uma empresa.
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um funcionário.

    Uma classe define:
    1. Atributos (características/propriedades): Nome, Cargo, Ano de nascimento.
    2. Métodos (comportamentos/funções): Apresentar, Calcular idade.

    Args:
        nome (str): Nome do funcionário.
        cargo (str): Cargo do funcionário.
        ano_nascimento (int): Ano de nascimento do funcionário.

    Methods:
        Construtor: __init__(self, nome: str, cargo: str, ano_nascimento: int): Inicializa os atributos do funcionário.
        apresentar(self): Apresenta o nome e cargo do funcionário.
        calcular_idade(self, ano_atual: int) -> int: Calcula e retorna a idade do funcionário com base no ano atual.
    """

    def __init__(self, nome: str, sobrenome: str, cargo: str, ano_nascimento: int):
        """
        O CONSTRUTOR (__INIT__)
        Ele roda automaticamente sempre que criamos um novo objeto(new)

        O 'self' é obrigatório: Ele serve para o objeto saber que os dados estão sendo atribuídos a ele mesmo.

        Args:
            nome (str): Nome do funcionário.
            sobrenome (str): Sobrenome do funcionário.
            cargo (str): Cargo do funcionário.
            ano_nascimento (int): Ano de nascimento do funcionário.

        Returns:
            None
        """

        # Atributos de instância (Cada objeto tem o seu próprio conjunto de dados)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.ano_nascimento = ano_nascimento
        self.email = f"{nome.lower()}.{sobrenome.lower()}@empresa.com"

    def apresentar(self):
        # Método para o funcionário se apresentar
        print(f"Olá, meu nome é {self.nome} {self.sobrenome}.")
        return f"Olá, meu nome é {self.nome} {self.sobrenome} e eu sou {self.cargo}."

    def calcular_idade(self, ano_atual: int) -> int:
        # Método para calcular a idade do funcionário baseado no ano atual
        idade = ano_atual - self.ano_nascimento
        return idade

# --- Bloco de Execução Principal ---
if __name__ == "__main__":

    print("\n" + "="*50)
    print("📢 Executando o módulo funcionario.py diretamente.")
    print("  ")
    print("            🚛 FÁBRICA DE OBJETOS (POO)")
    print("="*50 + "\n")

    # Funcionario 1: Criando um objeto da classe Funcionario
    funcionario1 = Funcionario("Cristina", "Almeida", "Manager Tech ", 1990)
    print(f"     Funcionário 1 Criado 👩🏽‍💻: {funcionario1.nome} {funcionario1.sobrenome}")
    print(f"     Cargo: {funcionario1.cargo}")
    print(f"     E-mail Corporativo: {funcionario1.email}")
    print(f"     Idade em 2026: {funcionario1.calcular_idade(2026)} anos")

    print("\n" + "-"*50 + "\n")

    # Funcionario 2: Criando outro objeto da classe Funcionario
    funcionario2 = Funcionario("João", "Silva", "Médico", 1985)
    print(f"     Funcionário 2 Criado 👨🏽‍⚕️: {funcionario2.nome} {funcionario2.sobrenome}")
    print(f"     Cargo: {funcionario2.cargo}")
    print(f"     E-mail Corporativo: {funcionario2.email}")
    print(f"     Idade em 2026: {funcionario2.calcular_idade(2026)} anos")

    print("\n" + "="*50)
    print("🏁 Fim da execução do módulo funcionario.py"
          "\n" + "="*50 + "\n")
