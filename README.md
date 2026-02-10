# 📊 PYTHON do ZERO -> AI Programação PYTHON do Zero a Inteligência Artificial 2026

![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-analise-de-dados-financeiros&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-analise-de-dados-financeiros&metric=coverage)
![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-analise-de-dados-financeiros&metric=duplicated_lines_density)
![Build Status](https://github.com/tinalmeid/PYTHON-analise-de-dados-financeiros/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Desenvolvimento

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testes-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Pandas](https://img.shields.io/badge/Dados-Pandas-150458?style=flat&logo=pandas&logoColor=white)
![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white")
![Github Copilot](https://img.shields.io/badge/AI-Copilot-000000?style=flat&logo=githubcopilot&logoColor=white)

## Gestão & DevOps

![Jira](https://img.shields.io/badge/Gestão-Jira-0052CC?style=flat&logo=jira&logoColor=white)
![Azure](https://img.shields.io/badge/DevOps-Azure-0078D7?style=flat&logo=azuredevops&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![SonarCloud](https://img.shields.io/badge/Quality-SonarCloud-F3702A?style=flat&logo=sonarcloud&logoColor=white)
![Clean Code](https://img.shields.io/badge/Prática-Clean_Code-green?style=flat&logo=geocaching&logoColor=white)
![Code Style](https://img.shields.io/badge/Code_Style-PEP8-brightgreen?style=flat)

### Produtividade & Aprendizado

![WakaTime](https://img.shields.io/badge/Produtividade-Wakatime-000000?style=flat&logo=wakatime&logoColor=white)
![Udemy](https://img.shields.io/badge/Plataforma-Udemy-EC5252?style=flat&logo=udemy&logoColor=white)

Este repositório hospeda o desenvolvimento do **Aprendizado do Uso de Python para AI**, um monólito com diversos exemplo de aplicação do Python para análise de dados.

Aqui o foco é **Engenharia de Software aplicada a Dados**. O projeto recursos avançados da linguagem (List Comprehensions, Map/Reduce, File I/O) com uma arquitetura blindada por testes automatizados e análise estática.

## 📚 Curso de Referência

Udemy: [Introdução à linguagem Python](https://www.udemy.com/course/programacao-python-do-basico-ao-avancado/learn/lecture/51564387#overview)

## 🚀 Como Rodar (Quick Start)

### Pre-requisitos

- Python 3.8 or higher
- pip (Python package manager)

### Instalação

1. 📥**Clone o repositório:**

   ```bash
   git clone https://github.com/tinalmeid/python_zero__ai
   ```

2. 🐍**Crie o ambiente virtual:**

   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. 📦**Instale as dependências:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. 🔬**Rode os Testes:**

   ```bash
   pytest tests/ -v
   ```

## 🧪 Padrões de Qualidade (QA Engineering)

Para garantir a excelência do código, este projeto utiliza um Quality Gate rigoroso:

1. Linting (Pylint): O código deve seguir a PEP8.

2. Testes (Pytest): Cobertura mínima exigida pelo SonarCloud.

3. Clean Code: Funções pequenas, nomes descritivos e princípios SOLID.

4. Code Review: Nenhum código entra na main sem passar pela pipeline de CI.

## 📝 Development Guidelines

Para manter a qualidade e a rastreabilidade do projeto, seguimos estritamente:

1. **🌿 Branching Strategy:**

    - Toda branch deve começar com a chave do Jira: `CDD-XXX-nome-da-tarefa`.
    - Ex: `CDD-577-setup-ambiente`.

2. **💾 Padrão de Commit (Conventional Commits):**

    - Formato: `CDD-XXX tipo: Descrição breve`.
    - Tipos permitidos:
      - `chore`: Configurações e manutenção.
      - `docs`: Documentação.
      - `feat`: Nova funcionalidade.
      - `test`: Testes.
      - `refactor`: Melhoria de código sem alterar funcionalidade.
      - `fix`: Correção de bug.
    - Ex: `CDD-586 chore: Configura pipeline inicial`.

3. **🧪 Testes & TDD:**

    - Toda nova funcionalidade em `src/` deve ter um teste correspondente em `tests/`.
    - Rode `pytest` localmente antes de subir o código.
    - Toda lógica de negócio deve ter teste unitário (.test.js).
    - O Pipeline falha se a cobertura for inferior a 80%.
    - Cobertura de testes

     ```text
    | Arquivo                                | Stmts | Miss | Cover | Missing | Status |
    |----------------------------------------------------------------------------------|
    |src\controle_fluxo\aula_estruturas.py      30      0      100%              ✅
    |src\controle_fluxo\lab_desafio.py          12      0      100%              ✅
    |src\estrutura_dados\analise_avancada.py    10      0      100%              ✅
    |src\estrutura_dados\dicionarios_sets.py     6      0      100%              ✅
    |src\estrutura_dados\fila_processamento.py   9      0      100%              ✅
    |src\estrutura_dados\listas_tuplas.py       11      0      100%              ✅
    |src\funcoes\aula_funcoes.py                12      0      100%              ✅
    |src\funcoes\calculadora.py                 14      0      100%              ✅
    |src\orientacao_objetos\funcionario.py      13      0      100%              ✅
    |src\poo_fundamentos\agregacao.py           11      0      100%              ✅
    |src\poo_fundamentos\sistema_escola.py      31      0      100%              ✅
    |src\projetos\ponto_steak.py                20      0      100%              ✅
    |src\projetos\calculo_area_parede.py        32      0      100%              ✅
    |src\projetos\funcionarios_carro_sets.py    20      0      100%              ✅
    |src\projetos\calculo_imc.py                29      0      100%              ✅
    |src\projetos\analisa_lista_frutas.py       30      0      100%              ✅
    |src\projetos\sistema_seguranca             79      0      100%              ✅
    |src\projetos\estados_brasil                24      0      100%              ✅
    |src\setup_inicial\setup_inicial.py         24      0      100%              ✅
    |src\tratamento-de-erros\gerenciador        24      0      100%              ✅
    |src\estatistica\estatistica.py              7      0      100%              ✅
    |src\estatistica\main.py                    20      0      100%              ✅
    ----------------------------------------------------------------------------------|
    | TOTAL                                    468      0      100%              ✅
    🔢 Stmts (Statements) : Linhas executáveis
    ❌ Miss (Missed) : Linhas que o teste não conseguiu cobrir
    🎯 Cover (Coverage) : Porcentagem de cobertura
    🔍 Missing (Linhas Faltantes) : Linhas que não foram cobertas por teste
    ```

4.**🛡️ Quality Gate:**

- Para aceite de Pull Requests será necessário aprovação do checklist de QA (Sonar + W3C).
- Código sem Docstrings (documentação de função) será reprovado no Code Review.
- Mantenha o **SonarCloud** feliz: Zero "Bugs", Zero "Vulnerabilities" e Cobertura aceitável.

1. **🧹 Clean Code:**
    - Variáveis descritivas (nada de `x`, `y`, `aux`).
    - Respeite o **PEP8** (o `pylint` vai reclamar se não fizer!).

## 🏗️ Estrutura do Projeto

```text
python_zero_a_ai/
├── .github/
│   ├── workflows/                          # 🤖 Automação (GitHub Actions)
|   └── PULL_REQUEST_TEMPLATE.md            # 📋 Template de Descrição Automática
├── docs/                                   # 📘 Documentação de Padrões
│   ├── PADROES_GIT.md                      # 🔀 Processos (Review, Merge)
│   ├── SOLID.md                            # 🧱 Arquitetura (SRP)
│   └── CLEAN_CODE.md                       # 🧹 Estilo (Nomes, Docs)
├── src/                                    # 🧠 Código Fonte (Módulos do Curso)
│   ├── __init__.py
│   ├── setup_inicial/                      # 🏗️ Módulo 01: Setup e Boas Práticas
│   │   └── 🐍 setup_inicial.py
|   ├── controle_fluxo/                     # 🔀 Módulo 02: Lógica de Programação
│   │   ├── 📘 aula_estruturas.py          (If, For, While)
│   │   └── 🧩 lab_desafio.py              (Algoritmo de Separação)
|   ├── poo-fundamentos/                    # 🧬 Módulo 03: Orientação a Objetos
|   │   ├── 🏫 sistema_escola.py           (Herança e Polimorfismo)
|   │   └── 🚗 agregacao.py                (Relação entre Objetos)
|   ├── funcoes                             # 🧩 Módulo 04: Funções e Modularização
|   |   ├── 🛠️ aula_funcoes.py             (Def, Return, *Args)
|   │   └── 🧮 calculadora.py              (Módulo de cálculos para importação)
|   ├── estrutura_dados                     # 🗃️ Estruturas de Dados
|   |   ├── 📜 listas_tuplas.py            (Sequências e Imutabilidade)
|   |   ├── 🔑 dicionarios_sets.py         (Chave-Valor e Unicidade)
|   │   └── ⚙️ fila_processamento.py       (Algoritmo de Priorização)
|   ├── tratamentos_erros                   # 🛡️ Tratamento de Exceções
|   │   └── 💊 gerenciador.py              (Try, Except, Finally)
|   ├── orientacao_objetos                  # 🏭 Classes, Construtores e Métodos  (OOP)
|   │   └── 👷🏾funcionario.py               (Classe e Objetos)
|   ├── estatistica                         # 📦 Modularização, Imports e Package
|   │   └─ 📊 basica.py                    (Módulos, importação e pacotes)
|   ├── projetos                            # 🫥 Desafios de Lógica
|   |   ├── 🥩 ponto_steak.py              (Calcula o Ponto da carne de acordo com a temperatura informada)
|   |   ├── 🎨 calculadora_area_parede.py  (Calcula a área de acordo com a hxl, calcula a quantidade de lata como rendimento da tinta)
|   |   ├── 🏭 func_carro_sets.py          (Sets de funcionários: Não tem carro, tem e trabalha a noite e tem e trabalha de dia)
|   |   ├── 📏 calculo_imc.py              (Realiza calculo IMC de acordo com peso e altura do usuário)
|   |   ├── 📋 analisa_lista_frutas        (Cria uma lista com 6 itens de frutas e gerencia CRUD)
|   |   ├── 🔐 sistema_seguranca           (Lógica de portão eletrônico usando while, break e continue)
|   |   ├── 🇧🇷  estados_brasil              (Lógica para consultar as capitais dos estados do Brasil)
├── tests/                                  # 🧪 Testes Unitários (Pytest)
│   ├── 🩺 test_controle_fluxo.py
│   ├── 🩺 test_estatistica.py
│   ├── 🩺 test_estrutura.py
│   ├── 🩺 test_excecoes.py
|   ├── 🩺 test_funcoes.py
|   ├── 🩺 test_ponto_steak.py
|   ├── 🩺 test_poo_basico.py
|   ├── 🩺 test_poo_fundamentos.py
|   ├── 🩺 test_rendimento_tinta.py
|   ├── 🩺 test_setup.py
|   ├── 🩺 test_lista_frutas.py
|   ├── 🩺 test_sistema_seguranca.py
|   ├── 🩺 test_estados_brasil.py
├── .gitignore                             # 🙈 Arquivos ignorados pelo Git
├── README.md                              # 📘 Documentação do Projeto
├── requirements.txt                       # 📦 Lista de Dependências
└── sonar-project.properties               # 📡 Configuração do SonarCloud
```

## 🗺️ Roadmap & Entregas (Jira)

Monitoramento de tarefas de desenvolvimento com base no fluxo de trabalho de Engenharia.

| ID Jira     | 📚 Módulo / Tarefa                                      | Branch                                | Status          |
| :---------- | :-------------------------------------------------------| :------------------------------------ | :---------------|
| **CDD-5**   | 🏗️ Setup: Ambiente, CI/CD e Quality Gate                | CDD-5-chore/setup-ambiente            | ✅ Concluído    |
| **CDD-6**   | 🔀 Estruturas de Controle (If, For, While)              | CDD-6-feat/loops-e-condicionais       | ✅ Concluído    |
| **CDD-7**   | 🧬 Programação Orientada a Objetos (Classes e Herança)  | CDD-7-feat/poo-fundamentos            | ✅ Concluído    |
| **CDD-8**   | 🧩 Funções, Argumentos Dinâmicos e Módulos              | CDD-8-feat/funcoes-e-modulos          | ✅ Concluído    |
| **CDD-9**   | 🗃️ Estruturas de Dados (Listas, Sets, Dicts) e Lambda   | CDD-9-feat/estruturas-de-dados        | ✅ Concluído    |
| **CDD-10**  | 🛡️ Tratamento de Exceções (Try, Except, Finally)        | CDD-10-feat/tratamento-de-erros       | ✅ Concluído    |
| **CDD-11**  | 🏭 Classes, Construtores e Métodos (OOP)                | CDD-11-feat/poo-classes-objetos       | ✅ Concluído    |
| **CDD-12**  | 📦 Modularização, Imports e Packages                    | CDD-12-feat/modulos-e-pacotes         | ✅ Concluído    |
| **CDD-13**  | 🫥 Desafios: Ponto do Steak, Calculadora e mais..       | CDD-13-projetos/desafios              | ✅ Concluído    |
| **CDD-14**  | 🫥 Desafios: Gerenciador de lista de frutas             | CDD-14-feat/manipulacao-listas        | ✅ Concluído    |
| **CDD-14**  | 🫥 Desafios: Sistema de Segurança                       | CDD-15-feat/sistema-seguranca-loops   | ✅ Concluído    |

> **Legenda:** ✅ Concluído | 🔄 Em Andamento | 📝 A Fazer

## 📄 Licença

Este projeto faz parte de um curso de aprendizagem. Sinta-se à vontade para utilizá-lo para fins educacionais.

👩🏽‍💻 Desenvolvido por **Cristina de Almeida** como parte do plano de desenvolvimento técnico.
