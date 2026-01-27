# 📘 Padrões de Git e Code Review

Este documento define os padrões de qualidade, versionamento e revisão de código do projeto **Python Zero a AI**.

---

## 1. ⚡ Cheatsheet (Fluxo de Trabalho)
Siga esta ordem para executar suas tarefas sem erros.

### 1. Volte para a main e atualize
Sempre atualize a main antes de criar sua branch.
```Bash
git checkout main # Volte para a main
git pull origin main # Pegue as novidades (seu código mergeado)
```

### 2. Crie a branch da sua tarefa (Ex: Task CDD-586)
```Bash
git checkout -b ID-JIRA-tipo/nome-da-tarefa
git checkout -b CDD-5-chore/setup-ambiente
```

### 3. Salvar o Código (Commit)
O padrão de mensagem é: CDD-ID tipo(escopo): descrição.

```Bash
git cd .. # Volta a raiz do projeto, se necessário
git status # Mostra os arquivos modificados
git add . # Adicione os arquivos modificados
git commit -m "CDD-5 chore(setup): configura ambiente e ci/cd" # Faça o commit seguindo o padrão
```
### 4. Enviar para o Repositório Remoto (Github)
Na primeira vez que subir a branch, você precisa ligar ela ao remoto (-u).

```Bash
git push -u origin CDD-5-chore/setup-ambiente
```
Próximas Vezes (Só atualizar): Como o vínculo já existe, basta rodar:
```Bash
git push
```
### 5: Limpeza (Pós-Merge no GitHub)
Depois que seu PR for aprovado e mergeado na `main`, apague a branch velha para manter a casa limpa.

```bash
git checkout main # Volte para a main
git pull origin main # Pegue as novidades (seu código mergeado)
git branch # Exibe as branch existentes, a main deve ter um *
git branch -d CDD-5-chore/setup-ambiente # Apague a branch local
git push origin --delete CDD-5-chore/setup-ambiente # Apague a branch remota (no GitHub)
```

## 1. 🛡️ Auto Code Review (Checklist)
*Copie e cole este checklist no **primeiro comentário** do seu Pull Request logo após abri-lo. Isso confirma para o revisor que você garantiu a qualidade básica.*

### Checklist de Qualidade (Cristina)
- [ ] **SOLID:** O código respeita o princípio de responsabilidade única (SRP)?
        Ver SOLID.md
- [ ] **Clean Code:**  Variáveis têm nomes descritivos?
        Ver CLEAN_CODE.md
- [ ] **Docstrings:** Todas as funções/classes novas possuem documentação explicativa (Google Style)?
        Resumo: A primeira linha explicando o que a função faz.
        Args: Lista os argumentos (parâmetros) que a função recebe.
        Returns: Explica o que a função devolve.
        Raises: (Opcional) Avisa se a função pode dar algum erro específico (ex: ValueError).
- [ ] **Tipagem:** Os tipos de entrada e saída estão definidos (ex: `def func(x: int) -> str`)?
- [ ] **Limpeza:** Removi `print()` de debug, código comentado morto e importações não usadas?
- [ ] **Segurança:** Garanti que **NENHUMA** senha, token ou chave de API foi commitada?
- [ ] **Testes:**
    - [ ] A cobertura está em **100%** (ou acima de 80% conforme regra)?
    - [ ] Os testes passam localmente (`pytest`)?
- [ ] **SonarCloud:** O Quality Gate passou (Verde ✅)?

---

## 2. 🔀 Padrão de Merge (Squash & Merge)
*Ao finalizar um PR no GitHub, utilize a opção **"Squash and Merge"** e edite a mensagem final seguindo este padrão.*

### Estrutura do Título
`[CDD-XXX] tipo(escopo): descrição curta e imperativa`

**Tipos Permitidos:**
- `chore`: Configuração, infra, CI/CD (não altera código de produção).
- `docs`: Alteração apenas em documentação.
- `feat`: Nova funcionalidade.
- `test`: Criação ou correção de testes.
- `refactor`: Melhoria de código sem alterar comportamento.
- `fix`: Correção de bug.

**Exemplos de Título:**
- `[CDD-5] feat(auth): implementa login com google`
- `[CDD-254] chore(setup): configura pipeline de ci e sonarcloud`
- `[CDD-16] fix(pandas): corrige erro de tipagem na coluna data`
- `[CDD-765] docs(readme): adiciona badges de status e cobertura`

### Estrutura do Corpo da Mensagem
*Liste as alterações técnicas em tópicos e vincule a tarefa do Jira no final.*

```text
Implementa a estrutura inicial do projeto e configurações de qualidade.

Alterações realizadas:
* Configura ambiente virtual e dependências (requirements.txt).
* Adiciona pipeline do GitHub Actions para testes e SonarCloud.
* Cria módulo `src/setup_inicial` com exemplos de Clean Code.
* Documenta padrões de projeto no README e docs/.

Relacionado a: [CDD-586]
