# 🧱 Princípios SOLID

Guia de referência dos princípios de arquitetura utilizados no projeto.

---

## 1. SRP - Single Responsibility Principle (Responsabilidade Única)

> *"Uma classe ou função deve ter um, e apenas um, motivo para mudar."*

### 💡 O Conceito
Imagine um **Canivete Suíço** vs. um **Bisturi**.
* O canivete faz tudo (corta, abre vinho, lixa), mas não faz nada com excelência e é difícil de manusear.
* O bisturi faz apenas uma coisa (cortar), mas faz com precisão absoluta.

No código, queremos **Bisturis**. Cada função deve resolver apenas um problema pequeno.

### ❌ Como NÃO fazer (Violação do SRP)
Uma função "Faz Tudo". Se a regra de e-mail mudar, você mexe nela. Se o banco de dados mudar, você mexe nela também. Isso gera bugs.

```python
# Ruim: A função faz 3 coisas (Valida + Formata + Salva)
def registrar_host(nome):
    if not nome:
        return "Erro"                 # 1. Validação

    nome_final = nome.lower() + ".com" # 2. Lógica de Negócio (Formatação)

    database.save(nome_final)          # 3. Infraestrutura (Banco de Dados)
```

### ✅ Como FAZER (Aplicando SRP)
Quebramos em pequenas funções especialistas.

```python
# Bom: Cada função tem sua responsabilidade clara

def formatar_hostname(nome: str) -> str:
    """Responsabilidade: Apenas manipular texto (String)."""
    return f"{nome.strip().lower()}.com"

def salvar_host_banco(nome_formatado: str):
    """Responsabilidade: Apenas falar com o Banco de Dados (Infra)."""
    database.save(nome_formatado)

def registrar_host(nome: str):
    """Responsabilidade: Orquestrar o processo (Controlador)."""
    # Ela apenas delega, não põe a mão na massa
    host = formatar_hostname(nome)
    salvar_host_banco(host)
```
