"""
Docstrings para projetos/funcionarios_carro_sets.py
Descrição: Este módulo demonstra o uso de conjuntos (sets) para gerenciar funcionários e seus carros e horário de trabalho.

REGRA DE NEGÓCIO:
- Lista de funcionários que não tem carro
- Lista de funcionários que tem carro e trabalha à noite
- Lista de funcionários que tem carro e trabalha durante o dia

Autora: Tina Almeida
Data: 2026-01-30
Task: Tasks:CDD-13: [CDD] [PYTHON] Desafios: Ponto do Steak, Calculadora e mais..
"""

Lista_funcionarios_ = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda']
Lista_funcionarios_com_carro_ = ['Bruno', 'Diana', 'Fernanda']
Lista_funcionarios_trabalha_noite_ = ['Carlos', 'Diana', 'Eduardo']
Lista_funcionarios_trabalha_dia_ = ['Ana', 'Bruno', 'Fernanda']

def funcionarios_sem_carro(funcionarios, funcionarios_com_carro):
    """Retorna um conjunto de funcionários que não possuem carro."""
    set_funcionarios = set(funcionarios)
    set_funcionarios_com_carro = set(funcionarios_com_carro)
    return set_funcionarios - set_funcionarios_com_carro

def funcionarios_com_carro_e_trabalha_noite(funcionarios_com_carro, funcionarios_trabalha_noite):
    """Retorna um conjunto de funcionários que possuem carro e trabalham à noite."""
    set_funcionarios_com_carro = set(funcionarios_com_carro)
    set_funcionarios_trabalha_noite = set(funcionarios_trabalha_noite)
    return set_funcionarios_com_carro & set_funcionarios_trabalha_noite

def funcionarios_com_carro_e_trabalha_dia(funcionarios_com_carro, funcionarios_trabalha_dia):
    """Retorna um conjunto de funcionários que possuem carro e trabalham durante o dia."""
    set_funcionarios_com_carro = set(funcionarios_com_carro)
    set_funcionarios_trabalha_dia = set(funcionarios_trabalha_dia)
    return set_funcionarios_com_carro & set_funcionarios_trabalha_dia

def funcionarios_com_carro(funcionarios, funcionarios_com_carro):
    """Retorna um conjunto de funcionários que possuem carro."""
    set_funcionarios = set(funcionarios)
    set_funcionarios_com_carro = set(funcionarios_com_carro)
    return set_funcionarios & set_funcionarios_com_carro

#===== Execução das funções =====#
if __name__ == "__main__":
    print("Funcionários que não possuem carro:")
    print(funcionarios_sem_carro(Lista_funcionarios_, Lista_funcionarios_com_carro_))
    print(" ")
    print("\nFuncionários que possuem carro:")
    print(funcionarios_com_carro(Lista_funcionarios_, Lista_funcionarios_com_carro_))
    print(" ")
    print("\nFuncionários que possuem carro e trabalham à noite:")
    print(funcionarios_com_carro_e_trabalha_noite(Lista_funcionarios_com_carro_, Lista_funcionarios_trabalha_noite_))
    print(" ")
    print("\nFuncionários que possuem carro e trabalham durante o dia:")
    print(funcionarios_com_carro_e_trabalha_dia(Lista_funcionarios_com_carro_, Lista_funcionarios_trabalha_dia_))
    print(" ")

#Fim do arquivo funcionarios_carro_sets.py
