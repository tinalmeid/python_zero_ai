"""
Docstring do arquivo sistema_escola.py
Descrição: Este módulo implementa exemplos de Herança, Polimorfismo e uso  de super() em Python,
dentro do contexto de um sistema escolar.

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-7: [CDD] [PYTHON] Programação Orientada a Objetos (Classes e Herança)
"""

class MembroEscola:
    """
    Docstring para MembroEscola
    Classe Base(Pai) que define atributos comuns a todos os membros da escola.
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos básicos de um membro da escola.

    Args:
        nome (str): Nome do membro.
        idade (int): Idade do membro.
        status (Operador Ternário): Status ativo/inativo do membro.

    Methods:
        __init__(self, nome: str, idade: int, status: bool): Inicializa os atributos do membro da escola.
        apresentar(self): Apresenta o nome e idade do membro da escola.
        verificar_status(self): Retorna o status do membro da escola.
    """
    def __init__(self, nome: str, idade: int, status: bool):
        self.nome = nome
        self.idade = idade
        self.status = status

    def apresentar(self):
        # Método base que será estendido pelas subclasses filhas.
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def verificar_status(self):
        # Mostra se o membro está ativo ou inativo usando Operador Ternário
        estado = "ATIVO" if self.status else "INATIVO"
        print(f"Status: {estado}")

class Aluno(MembroEscola):
    """
    Docstring para Aluno
    Classe Filha: Herda de MembroEscola, representando um aluno específico e adicionando atributos e comportamentos próprios, no caso 'ano'
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um aluno.

    Args:
        nome (str): Nome do aluno.
        idade (int): Idade do aluno.
        status (Operador Ternário): Status ativo/inativo do aluno.
        ano (int): Ano escolar do aluno.

    Methods:
        __init__(self, nome: str, idade: int, status: bool, ano: int): Inicializa os atributos do aluno.
        apresentar(self): Apresenta o nome, idade e ano do aluno (sobrescreve o método da classe base).
    """
    def __init__(self, nome: str, idade: int, status: bool, ano: int):
        # super()  chama o construtor da classe Pai para não repetir código
        super().__init__(nome, idade, status)
        self.ano = ano

    def apresentar(self):
        # Chama a apresentação padrão (nome e idade)
        super().apresentar()
        # Adiciona a especificidade do Aluno (ano)
        print(f"Estou no {self.ano}º ano.")

class Professor(MembroEscola):
    """
    Docstring para Professor
    Classe Filha: Herda de MembroEscola, representando um professor específico e adicionando atributos e comportamentos próprios, no caso 'disciplina'
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um professor.

    Args:
        nome (str): Nome do professor.
        idade (int): Idade do professor.
        status (Operador Ternário): Status ativo/inativo do professor.
        disciplina (str): Disciplina que o professor leciona.

    Methods:
        __init__(self, nome: str, idade: int, status: bool, disciplina: str): Inicializa os atributos do professor.
        apresentar(self): Apresenta o nome, idade e disciplina do professor (sobrescreve o método da classe base).
    """
    def __init__(self, nome: str, idade: int, status: bool, disciplina: str):
        # super()  chama o construtor da classe Pai para não repetir código
        super().__init__(nome, idade, status)
        self.disciplina = disciplina

    def apresentar(self):
        # Chama a apresentação padrão (nome e idade)
        super().apresentar()
        # Adiciona a especificidade do Professor (disciplina)
        print(f"Eu sou professor de {self.disciplina}.")

class Assistente(MembroEscola):
    """
    Docstring para Assistente
    Classe Filha: Herda de MembroEscola, representando um assistente específico e adicionando atributos e comportamentos próprios, no caso 'departamento'
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um assistente.

    Args:
        nome (str): Nome do assistente.
        idade (int): Idade do assistente.
        status (Operador Ternário): Status ativo/inativo do assistente.
        departamento (str): Departamento onde o assistente trabalha.

    Methods:
        __init__(self, nome: str, idade: int, status: bool, departamento: str): Inicializa os atributos do assistente.
        apresentar(self): Apresenta o nome, idade e departamento do assistente (sobrescreve o método da classe base).
    """
    def __init__(self, nome: str, idade: int, status: bool, departamento: str):
        # super()  chama o construtor da classe Pai para não repetir código
        super().__init__(nome, idade, status)
        self.departamento = departamento

    def apresentar(self):
        # Chama a apresentação padrão (nome e idade)
        super().apresentar()
        # Adiciona a especificidade do Assistente (departamento)
        print(f"Eu trabalho no departamento de {self.departamento}.")

# ---- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Simulando a criação de objetos para cada tipo de membro da escola
    aluno = Aluno("Ana Silva", 16, True, 2)
    aluno.apresentar()
    aluno.verificar_status()
    print("-----")

    professor = Professor("Carlos Souza", 45, True, "Matemática")
    professor.apresentar()
    professor.verificar_status()
    print("-----")

    assistente = Assistente("Mariana Lima", 30, False, "Biblioteca")
    assistente.apresentar()
    assistente.verificar_status()
    print("-----")
