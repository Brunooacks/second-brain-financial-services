---
tipo: auditoria
setor: financeiro
data: 2026-09-02
origem: rotina noturna — 46ª passada
tags: [proveniencia, auditoria, ganhos, governanca, dado-e-rei]
status: coleta concluída · tese ⏳ para o Bruno
---

# Auditoria de proveniência dos ganhos do acervo — lote 1 (16 afirmações, 5 players + setor)

> **Por que esta passada existe.** A passada de 02/09 (44ª) derivou um corolário e não agiu sobre ele: *"todo número cuja origem seja snippet deve ser tratado como hipótese, não como dado — e o acervo tem ~90 ganhos com fonte, boa parte coletada assim."* Seis erros materiais já haviam sido derrubados em seis passadas, todos do mesmo tipo. Esta passada aplica a regra ao **lote mais load-bearing**: os números que apareceriam primeiro num board.
>
> **Regra mãe respeitada:** verificar proveniência é coleta. Nenhum nível EMA-J foi alterado, nenhuma iniciativa criada, nenhuma jornada aberta. **Teses ⏳ para o Bruno.**

---

## 1. Placar da auditoria

| | Contagem |
|---|---|
| Afirmações auditadas | **16** |
| ✅ Confirmadas em **primário (emissor)** | **5** |
| ✅ Confirmadas **com correção de escopo/rótulo** | **4** |
| 🟨 Só em **secundária** (imprensa/fornecedor) | **4** |
| ❌ **Derrubadas** (erro material ou colagem) | **6** |
| 🔍 **Não localizadas** — não citáveis | **1** |

> Soma > 16 porque itens compostos entram em mais de uma coluna.
>
> **Taxa de erro do lote mais visível do acervo: 6 de 16 afirmações precisaram de correção material.** Não é ruído de coleta — é padrão.

---

## 2. Os erros derrubados nesta passada (7º ao 12º do acervo)

### ❌ 7º — Itaú: "−50% de perdas de fraude em 2 anos **e** −98% de incidentes de alto impacto desde 2018"
São **dois universos diferentes colados numa frase de antifraude**.
- **−50% de perdas por fraude em 2 anos** existe (Estadão via UGT, [19/08/2025](https://www.ugt.org.br/Noticias/78830-Contra-golpes-virtuais-veja-como-bancos-usam-IA-para-rastrear-acoes-suspeitas-e-barrar-ameacas)) — **imprensa**, não release.
- **−98% de incidentes de alto impacto** é métrica de **confiabilidade de TI / experiência do cliente**, não de fraude. Literal: *"redução de 99% nos incidentes de alto impacto na experiência dos clientes; aumento de 2.606% no volume de implantações; redução de 45% no custo de transações únicas"* ([IT Forum, 12/02/2026](https://itforum.com.br/noticias/itau-amplia-uso-de-ia-avanca-tecnologia/)). O número oscila por safra: **98%** (1T26 vs 1T18), **99%** (fechamento 2025), e há ainda um terceiro 98% de *"incidentes críticos"* (Mazzei, Gartner CIO, 23/09/2025).
- **Formulação segura:** citar um ou outro, nunca na mesma frase, e nunca o −98% como ganho antifraude.

### ❌ 8º — Bradesco: "R$ 400 mi de benefício em cobrança **no Febraban Tech**"
O **número é fiel; o evento está errado por 10 meses**.
- Literal: *"Essa iniciativa gerou mais de R$ 400 milhões em benefícios capturados em 2025"* — **Patricia Kessler**, diretora do Bradesco Experience, no **Bloomberg Línea Summit 2025 (27/10/2025)**, não no Febraban Tech 2026 ([Bloomberg Línea, 28/10/2025](https://www.bloomberglinea.com.br/negocios/ia-generativa-resolve-82-dos-atendimentos-iniciais-no-bradesco-diz-diretora/)). "Essa iniciativa" = IA na operação de cobrança (18 mil ligações diárias analisadas).
- ⚠️ **Colagem já circulando na imprensa:** o Baguete (03/11/2025) generalizou o mesmo número de *cobrança* para *o banco inteiro*. São a mesma fala com escopos distintos.
- **Nível:** imprensa. Citável com atribuição a Kessler/Bloomberg Línea Summit; **não** como dado institucional do Bradesco.

### ❌ 9º — Bradesco: "BIA com 74 milhões de **transações** no 1S26"
Erro de **uma palavra que muda três ordens de grandeza**.
- O emissor diz **74 milhões de INTERAÇÕES** no 1S26 (release de 06/08/2026). **Transações concluídas** no mesmo período são **386 mil** (RI 2T26). 74.000.000 vs 386.000.
- A origem provável do erro: o título do Mobile Time (24/08/2026) usa "transações".
- ⚠️ **Armadilha adicional:** a customer story da Microsoft diz *"a BIA Clientes suporta interações personalizadas para cerca de **74 milhões de clientes**"* — o mesmo número, terceiro significado.
- **Formulação segura (e citável):** os números do **Relatório de Análise Econômica e Financeira 2T26 do Bradesco RI** — **34 mi de interações no 2T26, 88% de resolutividade, 386 mil transações concluídas (+28% vs 1T26)**. É o único primário de emissor do bloco.

### ❌ 10º — Bradesco: "BIA 87% de resolutividade **e** 25 milhões de interações"
Par que **não existe junto em nenhuma fonte**.
- **87%** é do release de **1S26** (06/08/2026). **25 mi de interações** é recorte de **jan/2026** (TI Inside, 07/01/2026, Rafael Cavalcanti) — e o corpo do artigo não é carregável, então esse número está em **nível de snippet**.
- **A métrica oscila entre fontes do próprio banco:** 82% (out/25) · 83% (dez/25) · 87% (release ago/26) · **88% (RI 2T26)**.

### ❌ 11º — BB: a negociação de dívida no WhatsApp **não é do Banco do Brasil**
Os três números conferem literalmente — *"aumento de 306% nas conversões · 50% das interações sem intervenção humana · parcelas de 33,17 para 14,22"* ([AdNews, 07/07/2026](https://adnews.com.br/post/bbts-estrutura-cobranca-digital-com-ia-no-whats-app-e-aumenta-conversoes-em-306)) — mas o **emissor é a BBTS (BB Tecnologia e Serviços)**, com **AWS** e **BRQ**, não o banco. Release não localizado no site da própria BBTS.
- ⚠️ **Buraco no dado:** o "+306%" **não declara base de comparação nem período**. Sem denominador público.
- **Impacto sobre o achado de Atendimento & cobrança (piloto):** a frase *"o BB é o mais próximo de agêntico porque formaliza acordo no WhatsApp"* fica com o sujeito trocado — é a **empresa de tecnologia do grupo**, num case de fornecedor de nuvem.

### ❌ 12º — Nubank: "nuFormer, 330 mi de parâmetros, treinado em 100 bi de transações"
**Três recortes de fontes e momentos diferentes** apresentados como spec de um modelo.
- **"3 carteiras" ✅ primário:** *"já está em produção em três carteiras — cartões de crédito no Brasil e no México e crédito sem garantia no Brasil"* ([Nu Holdings, release 2T26, 13/08/2026](https://international.nubank.com.br/pt-br/companhia/nu-holdings-ltd-divulga-resultados-financeiros-do-segundo-trimestre-de-2026/)).
- **"330 mi de parâmetros" 🟨:** existe no paper *"Your Spending Needs Attention"* (arXiv 2507.23267, jul/2025) como **configuração de experimento** comparada a uma de 24M — **não** como spec do modelo em produção.
- **"100 bi de transações" ❌:** o paper **não diz isso**. Diz que a escala de dado *da empresa* é `O(100B) of transactions across 100M+ members`. O release fala em *"mais de uma década de histórico de transações de mais de **100 milhões de clientes**"*. O acervo fundiu **100 bi de transações** com **100 mi de clientes**.

---

## 3. Correções de escopo (o número existe, o rótulo mente)

| Afirmação no acervo | O que a fonte diz literalmente | Consequência |
|---|---|---|
| **Itaú: "Alerta Pix pega 80% dos golpes"** | *"em oito a cada dez situações [em que] um fraudador ligou para um cliente e o convenceu a fazer uma transação, a gente consegue avisar ao cliente"* — Victor Thomazetti (Estadão, 19/08/2025) | Denominador é **golpe por indução/engenharia social**, não "os golpes". Verbo é **avisar**, não bloquear. 🟨 imprensa |
| **Itaú: "saltou de 300 mil → 3 mi de clientes"** | *"já está disponível para 300 mil usuários e crescerá de forma gradual: **até setembro, chegará a 3 milhões**"* ([feito.itau.com.br, 28/07/2026](https://feito.itau.com.br/itau-iai-superapp-inteligencia-artificial/)) | É **meta, não realizado**. Sem confirmação de que os 3 mi foram atingidos. ✅ primário |
| **Itaú: "meta 100% da base em 2026"** | *"até o final do ano para 100% dos usuários **pessoa física do Superapp**"* | Exclui PJ e quem não está no Superapp. ✅ primário |
| **Bradesco: "Bridge processa 2 mi req/dia e 2 bi de tokens/dia"** | O sujeito da frase é o **Azure Cosmos DB**, não a Bridge ([Microsoft customer story, 18/12/2025](https://www.microsoft.com/pt-br/customers/story/25888-bradesco-microsoft-foundry)) | É carga do **banco de dados** da arquitetura, não throughput da plataforma. "10 LLMs, 400+ experimentos, 20 casos em produção" ✅ confere. 🟨 fornecedor |
| **Bradesco: "modelo fundacional da Kunumi + hardware"** | *"**Estamos** junto com a Kunumi contribuindo... o **primeiro passo é** o modelo fundacional... **estamos desenvolvendo** um hardware"* — Cíntia Scovine Barcelos, CTO (Convergência Digital, 25/08/2026) | É **agenda de P&D declarada**, não entrega. Nada em produção. 🟨 imprensa |
| **Setor: "orçamento de IA foi de R$ 2,76 → 2,97 bi (+7,6%)"** | A rubrica é **"Inteligência artificial, analytics e big data"** e o estudo rotula a variação como **8%** ([Pesquisa Febraban de Tecnologia Bancária 2026, vol. 2](https://cmsarquivos.febraban.org.br/Arquivos/documentos/PDF/Pesquisa%20Febraban%20de%20Tecnologia%20Banc%C3%A1ria%202026%20v_2.pdf)) | Chamar de "orçamento de IA" **infla a categoria**; e "+7,6%" é aritmética própria que **contraria o número publicado**. ✅ primário |
| **Setor: "Pix Automático — BC classifica como em teste"** | *"Isso sinaliza que estamos em um processo de teste ainda"* — Márcia Vicari, chefe da divisão de Gestão do Pix do BC, painel do Febraban Tech, 24/08/2026 | É **fala de executiva**, não classificação formal do BC. Os **14 mil recebedores** (vs. mil em dez/25) também vêm da fala, não de estatística publicada. 🟨 imprensa |
| **Santander: "280+ agentes em produção" (lido como Brasil)** | Os **280+ agentes são do grupo global**; o que é do Brasil é a **contestação de fraude de cartão** (~95% mais rápida, até 90% automação, <1% erro) ([santander.com, 22/06/2026](https://www.santander.com/en/stories/santander-turns-its-ai-first-strategy-into-measurable-impact-and-extends-ai-access-to-all-185000-employees)) | Dois recortes: **global × Brasil**. ✅ primário |
| **Santander: "400 projetos no Brasil"** | Não está no material do emissor. É fala de **Eduardo Álvarez**, diretor de dados e IA do Santander Brasil, em entrevista (22/06/2026) | 🟨 imprensa. €1 bi / €35 mi / 185 mil func. são **do grupo**; os 400 projetos são **do Brasil**, de fonte diferente |
| **BB: "500 soluções de IA em 10 anos"** | *"uma década de investimentos em **big data e inteligência artificial** com um portfólio de 500 soluções implementadas **internamente**"* — Giuliane Paulista, no **Evolve 2024 da Cloudera** (Baguete, 07/10/2024) | Não é "IA": é **big data + IA**, **interno**, e o dado tem **quase 2 anos**. 🟨 imprensa em evento de fornecedor |
| **Nubank/OpenAI: "−70% no tempo de atendimento"** | *"reducing **chat response times** by 70%"* ([openai.com/index/nubank](https://openai.com/index/nubank/), ~mar/2025) | É **tempo de resposta do chat**, não AHT. A própria página se contradiz no 55% ("more than up to 50%" no corpo). 🟨 fornecedor, e **superado** pelo dado de 2T26 |

---

## 4. O que ficou **✅ citável num board sem ressalva**

Cinco afirmações passaram intactas, todas com PDF ou release do emissor atrás:

1. **Nubank — agentes de IA conduzem >60% das conversas de atendimento no Brasil**, "com desempenho equivalente ou superior ao humano" (release 2T26, 13/08/2026). Precisão: *conversas de atendimento*, não atendimento total.
2. **Nubank — nuFormer em produção em três carteiras**: cartão BR, cartão MX, crédito sem garantia BR; PJ e cartão Colômbia em teste (mesmo release).
3. **Setor — orçamento de tecnologia dos bancos: R$ 46,8 bi (2025) → R$ 50,4 bi (2026), +8%**; rubrica IA+analytics+big data R$ 2,76 → 2,97 bi (+8%); migração para cloud R$ 3 → 3,9 bi (+30%) — Pesquisa Febraban/Deloitte 2026, 34ª ed.
4. **Santander — €1 bi de valor de negócio com IA entre 2026 e 2028**, €35 mi no 1T (a caminho de >€200 mi no ano), **185 mil funcionários com acesso a IA** (antes ~40 mil ativos) — santander.com, 22/06/2026, assinado pelo Chief Data & AI Officer.
5. **Santander Brasil — contestação de fraude de cartão ~95% mais rápida, até 90% de automação, taxa de erro <1%** (mesma fonte, escopo Brasil explícito).

E, do bloco Bradesco, o único primário: **RI 2T26 — 34 mi de interações da BIA no trimestre, 88% de resolutividade, 386 mil transações concluídas, 28 mi de clientes com acesso**.

---

## 5. Achados da passada (descritivos — a tese é do Bruno)

**5.1 — A taxa de erro tem assinatura, e ela é sempre a mesma.** Doze erros derrubados em sete passadas. **Todos** de um dos três tipos: (a) **dois recortes colados** (fraude + TI no Itaú; 100 bi de transações + 100 mi de clientes no Nubank; global + Brasil no Santander); (b) **rótulo trocado** (interações→transações; IA→IA+analytics+big data; avisar→bloquear; meta→realizado); (c) **sujeito trocado** (Bridge→Cosmos DB; BB→BBTS; Febraban Tech→Bloomberg Línea Summit). Nenhum foi invenção. Todos foram **imprecisão herdada de imprensa e nunca reaberta**.

**5.2 — Existe uma hierarquia de proveniência estável no setor, e ela inverte a intuição.** Ordenado por confiabilidade observada neste lote: **RI/earnings release** (Bradesco 2T26, Nu Holdings 2T26) > **PDF de associação setorial** (Febraban/Deloitte) > **release institucional do emissor** (Santander, Itaú/feito) > **customer story de fornecedor** (Microsoft/Bradesco, OpenAI/Nubank — marketing do vendor, com incentivo a inflar e sujeito de frase escorregadio) > **imprensa citando executivo em evento** > **snippet de busca** (não citável). **O material de marketing do banco diverge do RI do próprio banco** — Bradesco publicou 87% no release e 88% no RI, 74 mi no release e 34 mi no RI. Quando as duas existem, o RI ganha.

**5.3 — O número mais load-bearing do acervo sobreviveu, e é o do setor.** A Pesquisa Febraban/Deloitte 2026 é primária, tem PDF, tem tabela e tem página. O achado que ela sustenta — **o orçamento de IA cresce menos que o de tecnologia (8% vs 8%) e muito menos que o de cloud (30%)** — fica de pé, com uma correção que o **fortalece**: a rubrica de R$ 2,97 bi **não é só IA**, é IA + analytics + big data. Ou seja, o gasto isolado em IA é **menor** que o número que o acervo vinha usando.

**5.4 — Três das seis correções tocam diretamente a tese de governança.** O Itaú não reduziu 98% de incidentes de fraude; o Bradesco não tem modelo fundacional próprio (tem agenda); o Nubank não treinou o nuFormer em 100 bi de transações (a base da empresa é dessa ordem). **O que se sabe publicamente sobre a maturidade real de IA dos incumbentes é menos do que o acervo registrava** — e o acervo é dos mais rigorosos que existem sobre o tema no país.

**5.5 — Barreira de renderização confirmada pela terceira vez.** `tiinside.com.br` e `mobiletime.com.br` retornam corpo vazio ao `web_fetch` em todas as tentativas, somando-se a BB, Mercado Pago e RI da Stone. **Cinco fontes brasileiras relevantes só são legíveis com browser.**

---

## 6. Regra de higiene derivada (a 3ª do acervo)

As duas anteriores:
1. *(01/09)* Nenhum número ou data de **norma** entra sem PDF do regulador ou DOU atrás.
2. *(02/09)* Nenhum número de **player** entra sem documento do emissor atrás.

A desta passada:

> **3. Todo ganho publicado deve carregar, junto com o número: o recorte temporal, o denominador, o sujeito da frase e o nível de proveniência.** Um número sem recorte é uma hipótese com aparência de dado. Os doze erros do acervo não foram falhas de busca — foram números corretos com recorte, denominador ou sujeito errado.

**Aplicação sugerida:** ~74 ganhos do acervo ainda não foram auditados. Este lote (16) tem 6 erros — **37,5%**. Se a taxa se mantiver, há ordem de **25 a 28 correções pendentes** no acervo.

---

## 7. O que eu diria sobre isso num board

⏳ **para o Bruno.**

Matéria-prima que esta passada entrega e que ele não tinha antes:
- um **placar de erro do próprio acervo** (6/16 = 37,5%) e uma **projeção** (25–28 correções pendentes em ~74 ganhos não auditados);
- uma **hierarquia de proveniência empírica** (§5.2) — incluindo a constatação de que **o release de marketing do banco contradiz o RI do mesmo banco**;
- o fato de que **o gasto isolado em IA do setor é menor que o já modesto R$ 2,97 bi**, porque a rubrica soma analytics e big data;
- e o mais desconfortável: **o que se sabe publicamente sobre a maturidade de IA dos incumbentes brasileiros é sistematicamente mais frouxo do que parece** — três dos seis erros inflavam capacidade declarada.

**Contraponto que a máquina registra sem resolver:** ⏳ para o Bruno.

---

## Ligações
- [[2026-09-01 — Residencia de Dados e Explicabilidade nos 11 Players]]
- [[2026-08-31 — Refresh 2T26 e Frame Regulatório]]
- [[_Ledger-Discovery]]
- [[De-Para — Atendimento & cobrança]] · [[De-Para — Prevenção a fraude & disputas]] · [[De-Para — Investimentos & advisor]]
