# 🧹 Clean Code & Boas Práticas

> *"Código é lido muito mais vezes do que é escrito."*

Este guia define como manter o código legível e profissional.

---

## 1. Nomenclatura (Naming)
Nomes devem revelar intenção. Não tenha medo de nomes grandes se eles forem claros.

| Tipo | ❌ Ruim | ✅ Bom | Por quê? |
| :--- | :--- | :--- | :--- |
| **Variáveis** | `x`, `d`, `aux`, `lista` | `dias_restantes`, `lista_usuarios` | `d` poderia ser dia, dado ou distância. Seja explícito. |
| **Funções** | `processar()`, `fazer()` | `calcular_imposto_renda()`, `buscar_usuario_id()` | O verbo deve dizer exatamente o que a função faz. |
| **Booleanos** | `flag`, `status` | `is_ativo`, `tem_permissao`, `user_has_access` | Deve soar como uma pergunta de Sim/Não. |

---

## 2. Docstrings (Google Style)
Usamos o padrão do Google para documentar funções. É limpo e legível.

**Exemplo:**
```python
def calcular_media(notas: list) -> float:
    """
    Calcula a média aritmética simples das notas. <-- RESUMO

    Args:                                     <-- ENTRADAS
        notas (list): Uma lista contendo números (int ou float).

    Returns:                                  <-- SAÍDA
        float: A média calculada. Retorna 0.0 se a lista for vazia.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
```

## 3. Limpeza Geral
Antes de comitar, faça a "faxina":

💀 Dead Code: Apague códigos comentados. Se precisar do histórico, o Git já guardou para você.

🖨️ Prints: Remova todos os print("TESTE") usados para debug. Use logs se for necessário.

🍝 Importações: Remova imports que não estão sendo usados (o topo do arquivo deve estar limpo).

## 4. Tipagem (Type Hinting)
Python é dinâmico, mas em projetos profissionais usamos tipagem explícita para evitar erros bobos.

❌ Ruim: def soma(a, b): (O que é a? Número? Texto?)

✅ Bom: def soma(a: int, b: int) -> int: (Fica claro que entra número e sai número).

---

