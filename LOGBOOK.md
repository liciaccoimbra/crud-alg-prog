# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Lícia Cruz Coimbra|
| **Curso / Módulo** | Engenharia de Software · 2º período |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Sistema de agendamento de quadras de vôlei/futevôlei — MARÉ |
| **Link do meu repositório** | https://github.com/liciaccoimbra/crud-alg-prog |
| **Dupla de revisão (Campo 05)** | Júlia Ferreira |
| **Função neste ciclo** | Autora do meu CRUD · Revisora do CRUD de um colega |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ✅ | ✅ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ✅ | ✅ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ✅ | ✅ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ✅ | ✅ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ✅ | ✅ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ✅ | ✅ |
| 2 | Campo 04 — Interação com IA | 21/11 | ✅ | ✅ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [✅] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [✅] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [✅] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [✅] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [✅] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Conhecer as ferramentas que seriam utilizadas na disciplina e escolher um projeto para desenvolver o CRUD ao longo do semestre.
2. **O que implementei (commits / arquivos / links):** Escolhi o MARÉ, um sistema de agendamento de quadras de vôlei e futevôlei. Também fui aprendendo e começando a trabalhar com Git e GitHub durante as aulas. Já tinha familiaridade com o VS Code, mas ainda estava aprendendo a utilizar as ferramentas de controle de versão.
3. **Objeto(s) de conhecimento mobilizado(s):** Utilização do VS Code como ambiente de desenvolvimento, noções iniciais de Git e GitHub e organização de um projeto de programação.
4. **Desvio ou erro encontrado + causa técnica:** No início, tive dificuldade para entender como funcionava um CRUD e qual era a sequência das operações. Também tinha pouca familiaridade com Python e com a lógica necessária para desenvolver um sistema, já que comecei a programar recentemente. Ao longo do semestre, fui compreendendo melhor como funcionam o cadastro, a consulta, a atualização e a exclusão de informações.
5. **Decisão de ajuste + fonte:** Escolhi desenvolver o MARÉ por ser um tema do meu interesse pessoal, já que jogo vôlei e conheço a realidade das reservas de quadras. Percebi que muitos agendamentos são feitos por WhatsApp ou pessoalmente, o que pode dificultar a organização das reservas. Essa experiência me motivou a pensar em um sistema que pudesse facilitar esse processo.
6. **Feedback recebido e o que mudei:** Não recebi um feedback específico.
7. **Próximo passo:** Continuar estudando a lógica de programação e entender melhor como desenvolver as operações do CRUD, começando pela implementação do sistema de agendamento.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Lógica 
2. Utilização de condicionais
3. Declaração e utilização de variáveis
4. Tipos de dados, por conta do uso de aspas

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Dificuldade para organizar o passo a passo de uma solução
2. Separar o que é realmente importante para resolver um problema, deixando excessos de informações
3. Transformar o raciocínio em comandos Python, organizar o código e saber como continuar quando trava

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> Creio que algumas das falhas do CRUD podem estar associadas à organização da lógica e à escrita dos comandos em Python. Quando essas partes não estão bem organizadas, o sistema pode não interpretar as informações corretamente e realizar operações diferentes do que foi planejado

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:**  DOWNEY, Allen B. Pense em Python: pense como um cientista da computação. 2ª edição, capítulos 1 — A jornada do programa, 2 — Variáveis, expressões e instruções, e 5 — Condicionais e recursividade
— **Contribuição:** Durante meus estudos e pesquisas, encontrei esse livro, na qual a leitura permite aprofundar a maneira de organizar um problema em etapas e transformar uma solução em instruções. Também aborda o uso de variáveis, expressões e estruturas condicionais. Esses conteúdos estão relacionados ao desenvolvimento do MARÉ, pois ajudam a compreender como organizar as informações das reservas e definir as ações que o programa deve executar de acordo com cada situação.
- **Referência 2:** PYTHON SOFTWARE FOUNDATION. Documentação oficial do Python — Funções embutidas e tipos embutidos. Funções embutidas · Tipos embutidos 
— **Contribuição:** A documentação ajuda a consultar o funcionamento de recursos utilizados na programação, como input(), print() e int(), além dos diferentes tipos de dados do Python. Um ponto importante é compreender que o input() recebe as informações como texto, mesmo quando o usuário digita um número, e isso ajuda a entender melhor a diferença entre textos e números, o uso de aspas e como as informações podem ser utilizadas no programa.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> Depois do aprofundamento, continuei considerando que algumas falhas do CRUD podem estar relacionadas à organização da lógica e à escrita dos comandos em Python, como mencionei na hipótese inicial. A pesquisa também ajudou a perceber a importância de organizar um problema em etapas, utilizar corretamente as variáveis e compreender as condições e os tipos de dados envolvidos. Com isso, minha hipótese inicial foi ampliada, pois passei a considerar que esses conhecimentos também podem influenciar o funcionamento do sistema.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Referências de estudo | 2 | Consultar o livro e a documentação oficial para aprofundar os conhecimentos sobre lógica, condicionais, variáveis e tipos de dados |
| Tempo de estudo | 2 horas | Reservar um período para leitura, pesquisa e revisão dos conceitos estudados |
| Casos de teste para entrada de dados (4 cenários: texto válido, número inteiro, entrada vazia e tipo inválido no input()) | 4 | Praticar a organização de instruções, a utilização de variáveis, os tipos de dados e as estruturas condicionais |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Compreender a utilização de variáveis, tipos de dados e operações matemáticas, aplicando esses conceitos em pequenos exercícios de programação
2. **O que implementei (commits / arquivos / links):** Desenvolvi exercícios em Python envolvendo uma calculadora simples, a identificação de números pares e ímpares e o cálculo das raízes de uma equação utilizando a fórmula de Bhaskara. Nos exercícios, utilizei variáveis para armazenar valores, operações matemáticas e a função print() para exibir os resultados / https://github.com/liciaccoimbra/aulas/blob/main/aula1908pa.py
3. **Objeto(s) de conhecimento mobilizado(s):** Declaração e utilização de variáveis, tipos de dados (int, float e str), operadores aritméticos (+, -, *, /, % e **), operadores relacionais, estruturas condicionais (if, elif e else) e saída de dados com print()
4. **Desvio ou erro encontrado + causa técnica:** Durante a execução dos exercícios, não identifiquei erros que impedissem o funcionamento dos códigos. Os resultados foram apresentados corretamente para os valores utilizados. Ao revisar a atividade, percebi que os testes foram realizados com valores específicos, sem explorar todas as possibilidades das estruturas condicionais. Por exemplo, na calculadora, foi utilizada a operação de soma, e no exercício de Bhaskara foi trabalhado um caso em que o delta era maior que zero
5. **Decisão de ajuste + fonte:** Organizei os exercícios em partes separadas e utilizei estruturas condicionais para direcionar as operações de acordo com cada situação. Na calculadora, utilizei uma verificação com if para impedir a divisão por zero antes de realizar a operação. Essa decisão ajudou a compreender a importância das condições na prevenção de erros durante a execução do programa. Fonte: atividade prática desenvolvida na aula de 19/08
6. **Feedback recebido e o que mudei:** Não me recordo de um feedback específico recebido neste ciclo
7. **Próximo passo:** Continuar praticando a utilização de variáveis e operadores, aprofundar o conhecimento sobre entrada de dados com input() e compreender melhor como validar as informações recebidas antes de utilizá-las nos cálculos

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Aplicar operadores aritméticos e relacionais, entrada e conversão de dados e estruturas condicionais na resolução de um exercício em Python
2. **O que implementei (commits / arquivos / links):** Desenvolvi um programa em Python para receber três notas, calcular a média, identificar a maior nota e apresentar a situação do estudante. Para isso, utilizei input() para receber os valores, float() para convertê-los em números decimais, max() para identificar a maior nota e print() para apresentar os resultados
3. **Objeto(s) de conhecimento mobilizado(s):**  Variáveis, entrada e saída de dados, conversão de tipos (str para float), operadores aritméticos (+ e /), operadores relacionais (>= e <), estruturas condicionais (if, elif e else) e funções embutidas, como max(). Também foram abordados os fluxogramas e a organização das etapas de um algoritmo, acompanhando a explicação do professor sobre a sequência de execução de um programa
4. **Desvio ou erro encontrado + causa técnica:** Durante a execução, não identifiquei erros que impedissem o funcionamento do programa. Os resultados foram apresentados corretamente para as notas informadas e, depois ao revisar o código, percebi que não foi incluída uma validação para verificar se as notas estavam dentro da escala permitida. Também não há tratamento para entradas que não representem números, o que poderia gerar um erro durante a conversão com float()
5. **Decisão de ajuste + fonte:** Utilizei estruturas condicionais para classificar a situação do estudante de acordo com a média calculada. A combinação de if, elif e else permitiu estabelecer diferentes resultados conforme as condições definidas. Também utilizei max() para identificar a maior nota sem precisar realizar comparações manualmente entre os valores. Fonte: atividade prática desenvolvida na aula de 26/08 e explicação do professor sobre operadores e fluxogramas
6. **Feedback recebido e o que mudei:** Não me recordo de um feedback específico recebido neste ciclo
7. **Próximo passo:** Continuar praticando operadores e estruturas condicionais, aprofundando a compreensão sobre a organização da lógica dos algoritmos e a validação dos dados recebidos pelo programa

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Compreender como documentar uma aplicação e iniciar a construção do CRUD, utilizando variáveis e estruturas condicionais para organizar sua lógica de funcionamento
2. **O que implementei (commits / arquivos / links):** Durante a aula, trabalhamos na documentação da aplicação a partir de três questões: onde o aplicativo armazenaria os dados, como tomaria decisões durante sua execução e como seu fluxo poderia ser representado. Também começamos a desenvolver a primeira aplicação do CRUD, utilizando variáveis para armazenar informações e estruturas condicionais para definir o comportamento do programa
3. **Objeto(s) de conhecimento mobilizado(s):** Declaração e utilização de variáveis, tipos de dados, estruturas condicionais (if, elif e else), fluxo de execução e documentação de software. Esses conhecimentos foram utilizados para começar a estruturar a lógica da aplicação
4. **Desvio ou erro encontrado + causa técnica:** Não me recordo de um erro específico que tenha impedido a execução da atividade. Nesse primeiro contato com a aplicação, o desafio foi compreender como transformar as ideias do planejamento em instruções de código e organizar as decisões que o programa deveria executar
5. **Decisão de ajuste + fonte:** Utilizei variáveis para armazenar as informações e estruturas condicionais para direcionar a execução do programa conforme as situações definidas. Essa foi uma forma inicial de construir a lógica da aplicação, relacionando o conteúdo estudado ao funcionamento do MARÉ. Fonte: atividade prática e explicação do professor em aula, em 02/09
6. **Feedback recebido e o que mudei:** Não me recordo de um feedback específico recebido neste ciclo
7. **Próximo passo:** Continuar praticando a utilização de variáveis e estruturas condicionais, buscando compreender melhor como organizar a lógica do programa e desenvolver as funcionalidades do CRUD

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ ] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [ ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ ] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [ ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _…_ |
| **Data de realização** | _…_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

As questões do Checkpoint Conceitual não foram disponibilizadas pelo professor até o momento. Por esse motivo, o campo não foi preenchido.

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. Percebi que utilizar variáveis separadas para armazenar cada reserva não seria uma forma prática de organizar os dados do sistema. O uso de listas permitiu reunir vários agendamentos em uma única estrutura, facilitando a organização, a consulta e a manipulação dos registros. — *Objeto de conhecimento:* Estruturas de dados (listas).
2. Entendi que os dicionários permitem organizar as informações de cada reserva por meio de pares de chave e valor. Desse modo, dados como identificador, nome do cliente, modalidade, data e horário podem ser armazenados e acessados individualmente, tornando a estrutura do sistema mais organizada. — *Objeto de conhecimento:* Dicionários e pares chave-valor.
3. Identifiquei que não basta permitir o preenchimento das informações: também é necessário verificar se os campos obrigatórios foram preenchidos antes de cadastrar uma reserva. Essa validação evita registros incompletos e contribui para a confiabilidade do sistema. — *Objeto de conhecimento:* Estruturas condicionais e validação de dados.

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** O planejamento inicial previa quatro cenários de teste para a entrada de dados: texto válido, número inteiro, entrada vazia e tipo inválido no input(). Entretanto, durante a implementação do MARÉ, concentrei as verificações no preenchimento dos campos obrigatórios e na escolha da modalidade, sem contemplar todos os cenários de teste inicialmente planejados.
- **Causa técnica:** A lógica de validação implementada priorizou a verificação da presença das informações e da modalidade escolhida. O tratamento de entradas incompatíveis com os tipos esperados ainda não foi desenvolvido de maneira abrangente.

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** Organizar os agendamentos em uma lista de dicionários, utilizando uma estrutura para armazenar várias reservas e outra para agrupar as informações de cada reserva. Também foram utilizadas estruturas condicionais para verificar o preenchimento dos campos obrigatórios antes de realizar o cadastro. Essa organização facilita o armazenamento e o acesso às informações de cada reserva, enquanto as condições permitem verificar os dados informados antes de concluir o cadastro.
- **Fonte:** Python Software Foundation. The Python Tutorial. Capítulo 5 — Data Structures (Estruturas de Dados) e capítulo 4 — More Control Flow Tools (Estruturas de Controle de Fluxo).
**Objeto de conhecimento mobilizado nesta decisão:** Estruturas de dados (listas e dicionários), estruturas condicionais e validação de entrada.

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** CHATGPT **Data:** 20/11/2026
**Evidências da interação:**

- [Pergunta enviada à IA](evidencias/campo-04-pergunta.png)
- [Resposta da IA — Parte 1](evidencias/campo-04-resposta-1.png)
- [Resposta da IA — Parte 2](evidencias/campo-04-resposta-2.png)

**4b. Pergunta formulada (transcrita integralmente):**

> Analise o código atual do meu CRUD MARÉ, um sistema de agendamento de quadras de vôlei e futevôlei. Os agendamentos são armazenados em uma lista chamada agendamentos, e cada reserva é representada por um dicionário. No cadastro, o programa verifica se a modalidade escolhida é válida e se o nome do cliente, a data e o horário não estão vazios. Essa validação é suficiente para garantir que os dados estejam corretos? Identifique o que o código já valida e quais limitações ainda existem, considerando também a atualização de uma reserva. Não reescreva o código; explique de forma simples e aponte os trechos que justificam sua análise.

**4c. Resposta da IA (resumida em parágrafo):**

> A IA analisou as etapas de cadastro e atualização das reservas e identificou que o sistema já possui algumas validações, como a escolha de uma modalidade válida e o preenchimento dos campos obrigatórios durante o cadastro. Entretanto, essas verificações ainda são limitadas, pois não conferem se a data e o horário estão em formatos válidos, nem impedem o preenchimento do nome apenas com espaços em branco. Na atualização, a IA identificou que a modalidade possui validação, mas os campos de nome, data e horário recebem novos valores sem as mesmas verificações utilizadas no cadastro. Dessa forma, concluiu que as validações precisam ser aprimoradas para garantir maior consistência nas informações armazenadas.

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> Aceitei a análise de que as validações implementadas no MARÉ são parciais e não acontecem da mesma maneira nas operações de cadastro e atualização. Ao conferir o código, percebi que as estruturas condicionais e o operador lógico and são utilizados para verificar o preenchimento dos campos durante o cadastro. Também identifiquei que, na atualização, a modalidade possui verificações específicas, enquanto os demais campos recebem os novos valores diretamente. Essa análise me ajudou a compreender melhor a importância de aplicar validações consistentes nas diferentes operações do CRUD, evitando que informações incompletas ou inadequadas sejam armazenadas.

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> Questionei a observação da IA sobre a ausência de verificação de conflitos de horário, pois entendo que essa situação depende também das regras de funcionamento estabelecidas para o sistema. Embora o código atual não verifique se duas reservas ocupam o mesmo horário, considero necessário confirmar se essa restrição faz parte dos requisitos do MARÉ antes de classificá-la como uma falha. Também comparei as observações da IA com o código-fonte e confirmei que o cadastro verifica se os campos são diferentes de uma string vazia (""), mas não trata entradas preenchidas somente com espaços. Portanto, percebi que essa condição, embora impeça o cadastro de campos totalmente vazios, ainda permite algumas entradas inadequadas. Concluí que a resposta da IA foi útil para identificar limitações da implementação, mas que suas sugestões precisam ser analisadas considerando as regras do sistema e o comportamento real do código. 

Fonte de verificação: Código-fonte do MARÉ — arquivo crud_agendamento_quadras.py, especialmente os trechos de cadastro e atualização de reservas.

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** Compreender como funcionam as condicionais aninhadas e os operadores lógicos em Python, aprendendo a combinar diferentes condições para controlar o fluxo de execução de um programa.
2. **O que implementei (commits / arquivos / links):** Durante a aula, acompanhei a explicação do professor sobre condicionais aninhadas e operadores lógicos. Não desenvolvi uma nova funcionalidade nesse encontro, mas, ao relacionar o conteúdo com o MARÉ, percebi que já utilizava condicionais aninhadas na estrutura inicial do cadastro de reservas.
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas condicionais aninhadas (if dentro de outro if), operadores lógicos (and, or e not), operadores relacionais, expressões booleanas e controle do fluxo de execução.
4. **Desvio ou erro encontrado + causa técnica:** Não me recordo de um erro específico durante essa aula. Ao analisar a estrutura inicial do MARÉ, percebi que a utilização de vários níveis de condicionais exige atenção à organização e à indentação do código, pois cada condição interna depende da condição anterior para ser executada.
5. **Decisão de ajuste + fonte:** Ao revisar o código do MARÉ, compreendi melhor a escolha de utilizar condicionais aninhadas no cadastro das reservas. Primeiro, o programa verifica se o usuário escolheu a opção de cadastro; depois, verifica a modalidade e, em seguida, o preenchimento dos campos obrigatórios. Também identifiquei a utilização do operador lógico and para verificar se o nome do cliente, a data e o horário foram preenchidos simultaneamente. Essa combinação é adequada porque o cadastro só deve prosseguir quando todas essas condições forem verdadeiras.

Fonte: Explicação do professor durante a aula de 09/09 e código-fonte do projeto MARÉ (crud_agendamento_quadras.py).

Caso de teste complementar — verificação do operador lógico and:

Entrada: Nome = Ana; Data = 20/11/2026; Horário = 18:00.

Resultado esperado: O cadastro deve ser permitido, pois os três campos estão preenchidos.

Resultado obtido: Na simulação manual da condição lógica, todas as verificações são verdadeiras, permitindo que o fluxo alcance o bloco de cadastro.
- Objeto de conhecimento: Condicionais aninhadas, operadores lógicos e validação de entrada.

6. **Feedback recebido e o que mudei:** Não me recordo de um feedback individual específico recebido neste ciclo. A explicação do conteúdo ajudou a compreender melhor as estruturas condicionais que já estavam presentes no código do MARÉ.
7. **Próximo passo:** Continuar praticando condicionais aninhadas e operadores lógicos, buscando compreender melhor como combinar diferentes condições e aplicar esses conhecimentos às regras de cadastro e validação das reservas do MARÉ.

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** Entender como os programas armazenam e manipulam informações, conhecendo as estruturas de dados do tipo vetor e lista e suas diferenças em relação à organização e ao armazenamento na memória.
2. **O que implementei (commits / arquivos / links):** Durante a aula, acompanhei a explicação do professor sobre estruturas de dados, armazenamento na memória RAM, vetores e listas. Também foram apresentados conceitos relacionados à organização dos elementos, à utilização de listas em Python e às funções len() e type(). Não desenvolvi uma nova funcionalidade no MARÉ durante esse encontro.
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas de dados, vetores, listas, armazenamento e organização de dados na memória, estruturas estáticas e dinâmicas, além das funções embutidas len() e type().
4. **Desvio ou erro encontrado + causa técnica:** Não me recordo de um erro específico de execução neste ciclo, pois a aula foi voltada à explicação dos conceitos. Um ponto importante apresentado foi a diferença entre estruturas estáticas e dinâmicas, considerando a organização dos elementos na memória e a possibilidade de alteração do tamanho de uma lista.
5. **Decisão de ajuste + fonte:** A partir do conteúdo estudado, compreendi melhor a importância de utilizar listas para organizar os agendamentos do MARÉ. Como o sistema pode armazenar várias reservas, essa estrutura permite reunir diferentes registros e trabalhar com uma quantidade variável de elementos, sem depender de uma quantidade fixa previamente definida. Também conheci a função len(), que permite consultar a quantidade de elementos armazenados em uma lista, e type(), que identifica o tipo de dado utilizado.

Fonte: Explicação do professor durante a aula de 30/09 e anotações pessoais sobre estruturas de dados, vetores e listas.

6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** Não houve devolutiva individual da P1 neste encontro. A aula foi direcionada à explicação de estruturas de dados, listas e vetores, contribuindo para ampliar minha compreensão sobre como os programas armazenam e manipulam informações.
7. **Próximo passo:** Continuar estudando estruturas de dados e praticando a utilização de listas em Python, compreendendo melhor como armazenar, consultar e manipular os registros do MARÉ.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** Compreender como utilizar listas em Python para armazenar, organizar e manipular informações, conhecendo diferentes operações e formas de percorrer seus elementos.
2. **O que implementei (commits / arquivos / links):** Durante a aula, acompanhei a explicação sobre a continuação do conteúdo de listas e suas operações. Foram apresentados métodos como append(), insert(), extend(), pop(), remove() e count(), além de conceitos de ordenação, list comprehension, slicing, matrizes, dicionários, mapas, pilhas e filas. Também foram discutidas as etapas de desenvolvimento e evolução do CRUD.
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas de dados dinâmicas, listas, iteração, operações de inserção e remoção de elementos, ordenação, concatenação, fatiamento e list comprehension. No MARÉ, utilizei principalmente os métodos append() e remove(). O append() permite adicionar uma nova reserva à lista agendamentos, enquanto o remove() permite excluir uma reserva pelo seu valor.
4. **Desvio ou erro encontrado + causa técnica:** Durante o desenvolvimento do MARÉ, tive dificuldade em compreender como localizar e remover uma reserva específica da lista de agendamentos. A operação exigia percorrer os registros, comparar o identificador da reserva e utilizar o remove() para excluir o elemento correspondente. A dificuldade estava em compreender como realizar a remoção durante a iteração da lista e controlar a continuidade do laço. Para evitar que o programa continuasse percorrendo a lista após a exclusão, foi utilizado o comando break.
5. **Decisão de ajuste + fonte:** Durante o desenvolvimento do MARÉ, utilizei uma lista para armazenar os agendamentos, pois essa estrutura permite reunir vários registros e adicionar ou remover elementos conforme a necessidade do sistema. Para realizar o cadastro de uma reserva, utilizei o método append(), que adiciona um novo elemento ao final da lista. Já para cancelar uma reserva, utilizei o método remove(), após localizar o agendamento correspondente pelo identificador. Essa organização permite manipular os registros sem precisar criar variáveis separadas para cada reserva.

Fonte: Explicação do professor e anotações da aula de 07/10; Python Software Foundation — documentação oficial, capítulo 5: Data Structures, seção 5.1 — More on Lists (https://docs.python.org/3/tutorial/datastructures.html).

6. **Feedback recebido e o que mudei:** Não recebi um feedback específico do professor neste ciclo. As atividades e explicações da aula contribuíram para ampliar minha compreensão sobre a utilização de listas e suas operações no desenvolvimento do MARÉ.
7. **Próximo passo:** Continuar praticando as operações com listas, aprofundando a compreensão sobre inserção, remoção e iteração dos elementos, além de melhorar a organização dos agendamentos e a manipulação dos registros no MARÉ.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** Entender como funcionam os algoritmos de busca e ordenação, além de aprender a utilizar dicionários para organizar informações e facilitar a localização de dados em Python.
2. **O que implementei (commits / arquivos / links):** DDurante a aula, acompanhei a explicação sobre algoritmos de busca linear, binária e por interpolação, além de diferentes métodos de ordenação, como insertion sort, bubble sort, quick sort e merge sort. Também foram apresentados os dicionários, suas características, o acesso por chaves e operações como get(), len() e count(). Após a aula, apliquei o conteúdo no MARÉ, modificando a organização dos agendamentos para utilizar dicionários, nos quais cada reserva passou a armazenar suas informações por meio de pares de chave e valor.
3. **Objeto(s) de conhecimento mobilizado(s):** Algoritmos de busca e ordenação, estruturas de dados, dicionários, pares chave-valor, chaves únicas, acesso a elementos, complexidade de algoritmos, notação Big O e controle de fluxo com flag e break.
4. **Desvio ou erro encontrado + causa técnica:** Não me recordo de uma busca específica que tenha falhado durante esse ciclo. Entretanto, ao relacionar o conteúdo da aula com o MARÉ, percebi a importância de comparar corretamente o identificador informado pelo usuário com o ID armazenado no dicionário de cada reserva. Como o input() recebe os dados como texto, é necessário considerar os tipos de dados envolvidos na comparação. Outro cuidado é tratar a situação em que o identificador informado não corresponde a nenhuma reserva cadastrada, permitindo que o programa informe que o registro não foi encontrado.
5. **Decisão de ajuste + fonte:** Após estudar os dicionários, decidi utilizá-los para organizar as informações individuais de cada reserva no MARÉ. Em vez de manter os dados de cada agendamento separados, passei a agrupá-los em um dicionário, utilizando chaves para identificar informações como ID, nome do cliente, modalidade, data e horário. Esses dicionários são armazenados em uma lista chamada agendamentos, permitindo reunir várias reservas e acessar suas informações individualmente. Essa decisão tornou a organização dos dados mais estruturada e facilitou a localização e a manipulação das informações durante as operações do CRUD.

Fonte: Anotações pessoais e explicação do professor durante a aula de 14/10/2026; Python Software Foundation — documentação oficial, capítulo 5: Data Structures, seção 5.5 — Dictionaries (https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

6. **Feedback recebido e o que mudei:** Não recebi um feedback específico do professor neste ciclo. Após a aula, utilizei o conteúdo apresentado para aprimorar a organização dos agendamentos no MARÉ, passando a utilizar dicionários para agrupar as informações de cada reserva.
7. **Próximo passo:** Continuar praticando a utilização de dicionários e algoritmos de busca, aprofundando a compreensão sobre o acesso por chaves e a localização de registros. Também pretendo aprimorar a organização dos agendamentos e as consultas realizadas no MARÉ.

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** Implementar as operações de atualização e exclusão de agendamentos, completando as funcionalidades do CRUD no sistema MARÉ.
2. **O que implementei (commits / arquivos / links):** Implementei as funcionalidades de atualização e cancelamento de reservas no sistema MARÉ, utilizando Python. Também desenvolvi a busca de agendamentos pelo ID, permitindo localizar um registro específico antes de realizar uma alteração ou exclusão.
3. **Objeto(s) de conhecimento mobilizado(s):** Listas, dicionários, estruturas condicionais, laços de repetição (for), variáveis booleanas, identificadores e manipulação de elementos de uma lista.
4. **Desvio ou erro encontrado + causa técnica:** Uma das dificuldades durante o desenvolvimento foi organizar a sequência lógica necessária para realizar as operações de atualização e exclusão. Embora compreendesse a função de cada estrutura individualmente, tive dificuldade em combiná-las para percorrer a lista, localizar o registro pelo ID e executar a ação correspondente.
5. **Decisão de ajuste + fonte:** Para organizar essa lógica, utilizei um laço de repetição for para percorrer os registros, uma comparação para verificar o ID informado e uma variável booleana (reserva_encontrada) para controlar se a reserva havia sido localizada. Essa decisão foi fundamentada nos conteúdos de listas, estruturas condicionais, laços de repetição e variáveis booleanas trabalhados na disciplina.
6. **Feedback recebido e o que mudei:** Não recebi um feedback específico do professor ou de colegas durante esse ciclo. Os ajustes realizados foram resultado da minha própria análise das dificuldades encontradas durante o desenvolvimento, principalmente em relação à organização da lógica das operações de atualização e exclusão.
7. **Próximo passo:** Continuar desenvolvendo minha capacidade de organizar a lógica dos algoritmos e avançar no estudo de funções, buscando dividir o código em partes menores e tornar sua estrutura mais organizada.

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | Júlia Ferreira |
| **Repositório revisado** | _link_ |
| **Revisor** | Lícia Coimbra |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 21/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Acessar o repositório e analisar os arquivos | Revisor | _05/11_ | ✅ Concluída ☐ Em andamento ☐ Com desvio | Sem dificuldades de acesso. |
| 2. Executar o CRUD revisado | Revisor | _05/11_ | ✅ Concluída ☐ Em andamento ☐ Com desvio | O sistema foi executado corretamente. |
| 3. Testar as operações do CRUD | Revisor | _05/11_ | ✅ Concluída ☐ Em andamento ☐ Com desvio | Foram identificados pequenos pontos que precisavam de ajustes. |
| 4. Analisar o código e registrar observações | Revisor | _05/11_ | ✅ Concluída ☐ Em andamento ☐ Com desvio | As observações foram discutidas com a autora. |
| 5. Realizar os ajustes e verificar o funcionamento | Revisor / Autor | _05/11_ | ✅ Concluída ☐ Em andamento ☐ Com desvio | Os pontos identificados foram corrigidos e o funcionamento ficou adequado. |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Repositório e código-fonte | 1 | 1 | 0 | Utilizado para analisar a estrutura do projeto. |
| Operações do CRUD | 4 | 4 | 0 | Utilizadas para verificar cadastro, consulta, atualização e exclusão. |
| Ambiente de execução | 1 | 1 | 0 | Utilizado para executar e testar o sistema. |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** Verificar se as operações de cadastro, consulta, atualização e exclusão funcionam corretamente e se as informações são manipuladas conforme o comportamento esperado do sistema.
- **A solução atende?** ✅ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** Pequenos erros na implementação poderiam comprometer o funcionamento de alguma operação ou passar despercebidos durante uma análise superficial.
- **Estratégia de mitigação:** Executar o sistema, testar suas funcionalidades, registrar os pontos identificados e acompanhar as correções junto à autora.

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _05/11/26_ | Executar o sistema antes de avaliar seu funcionamento, verificando o comportamento das funcionalidades. | Revisor | Testes de software e operações CRUD | Execução prática do código-fonte do projeto revisado. |
| _05/11/26_ | Identificar e discutir pequenos pontos que precisavam de ajustes durante a execução do sistema. | Revisor / Autora | Depuração e análise de código | Observação do comportamento do programa durante os testes. |
| _05/11/26_ | Realizar correções nos pontos identificados e verificar novamente o funcionamento do sistema. | Revisor / Autora | Correção de erros e validação funcional | Código-fonte e repetição dos testes após os ajustes. |


> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> _…_

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** _…_
- **Plano de ação (passos e datas):** _…_

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** _…_
- **Resposta:**

> _…_

**Objeto de conhecimento mobilizado:** _…_
**Fonte:** _…_

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> _…_

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_
2. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> _…_

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> _…_

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _…_ |
| **Curso / Time / Função** | _…_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** _…_
2. **Objeto(s) de conhecimento que a banca mais explorou:** _…_
3. **Pergunta que mais me desafiou e como respondi:** _…_
4. **O que levo deste semestre para o próximo módulo:** _…_

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
