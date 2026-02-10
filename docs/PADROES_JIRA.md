# 📝Padrão Jira

## 🎯 Objetivo

Implementar **[FUNCIONALIDADE]** para permitir que **[USUÁRIO/SISTEMA]** consiga **[RESULTADO_ESPERADO]**.

---

## 🛠️ Especificações Técnicas & Critérios de Aceite

- [ ] Criar função/classe X.
- [ ] O sistema deve aceitar a entrada Y.
- [ ] O sistema deve tratar o erro Z (Try/Except).
- [ ] **Dataset/Arquivo a utilizar:** [NOME DO ARQUIVO.csv] (se aplicável).

---

## 🌳 Gestão da Configuração (Git)

**Nome da Branch:** `CDD-XX-tipo/nome-da-tarefa`

---

## ✅ Definition of Done (DoD) - Checklist de Finalização

### Qualidade & Testes

- [ ] **Testes Unitários:** Criados e passando (pytest).
- [ ] **Cobertura:** Mínimo de 80% (ou 100% dependendo da regra).
- [ ] **SonarQube:** Análise rodada localmente ou via CI/CD (Sem "New Code Smells").
- [ ] **Sonar Config:** Arquivo `sonar-project.properties` atualizado (se houver novas pastas).

### Documentação

- [ ] **Código:** Comentários explicativos em funções complexas (Docstrings).
- [ ] **README.md:** Atualizado com instruções de como rodar essa nova feature.
- [ ] **Requisitos:** `requirements.txt` atualizado (se instalou nova lib).

### Entrega

- [ ] Pull Request (PR) aberto seguindo o template.
- [ ] Merge realizado na `main` sem conflitos.
- [ ] Tag de versão criada (se for fim de ciclo).
