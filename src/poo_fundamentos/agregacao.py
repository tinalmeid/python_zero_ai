"""
Docstring do módulo sistema_escola.py
Descrição: Este módulo implementa exemplo de agregação em Python,
dentro do contexto de carros e motores.

Autora: Tina Almeida
Data: 2026-01-27
Task: CDD-8: [CDD] [PYTHON] Programação Orientada a Objetos (Agregação)
"""

class Motor:
    """
    Docstring para Motor
    Exemplifica a classe Motor que pode ser agregada a um Carro.
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um motor.

    Args:
        potencia (str): Potência do motor (e.g., '150cv').

    Methods:
        __init__(self, potencia: str, modelo: str): Inicializa os atributos do motor.
        roncar(self): Simula o som do motor.
    """
    def __init__(self, potencia: str):
        self.potencia = potencia

    def roncar(self):
        return "Vroom Vroom!"

class Carro:
    """
    Docstring para Carro
    Exemplifica a classe Carro que agrega um Motor.
    Aplica o Princípio da Responsabilidade Única (SRP) ao encapsular atributos e comportamentos específicos de um carro.

    Args:
        modelo (str): Modelo do carro.
        motor (Motor): Instância da classe Motor associada ao carro.
    """
    def __init__(self, modelo: str, motor: Motor):
        self.modelo = modelo
        self.motor = motor  # Agregação: Carro "tem um" Motor

    def ligar(self):
        print(f"O {self.modelo} está ligado: {self.motor.roncar()} ({self.motor.potencia})")

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    motor_forte = Motor("200cv")
    meu_carro = Carro("Esportivo Volvo", motor_forte)
    meu_carro.ligar()
    print("-----")
