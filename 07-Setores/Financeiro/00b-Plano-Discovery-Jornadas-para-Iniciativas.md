---
tipo: plano
setor: financeiro
fase: 1
camada: discovery-iniciativa
status: ativo
data: 2026-07-03
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [plano, discovery, benchmarking, jornadas, maturidade, iniciativas, agentic, vivo]
---

# 🧭 Plano — Discovery de Jornadas → Funil de Iniciativas de IA

> **Camada 2 do mapeamento.** O blueprint [[00-Blueprint-Mapeamento-Produtos-Banking-BR]] responde *"o que cada player oferece"*. Este plano responde a pergunta que gera negócio: *"em quais jornadas a IA/agentic vale a pena, com que arquétipo, e qual serviço eu proponho"*. A base de produtos é o insumo; o backlog de iniciativas priorizado é o produto. **A máquina coleta e organiza; a priorização e a tese são minhas.**

---

## 0. A tese antes do método

Mapear produto é commodity — qualquer consultoria faz um comparativo de tarifas. O ativo defensável é ligar **jornada mapeada → nível de maturidade tecnológica → lacuna → arquétipo de iniciativa de IA → serviço proposto**, com dado público e leitura de governança/soberania. É a diferença entre "conheço IA" e "sei exatamente onde a IA move o ponteiro no *seu* fluxo de crédito, e por quê o seu concorrente já saiu na frente".

**O que eu diria num board:** o discovery não termina numa planilha comparativa — termina num backlog priorizado onde cada linha diz "esta jornada está em maturidade L2, o líder de mercado está em L4, o gap vale X, e é aqui que eu entro". Esse é o artefato que vira pipeline comercial, não slide de mercado.

---

## 1. Como esta camada se encaixa no que já existe

| Já existe (blueprint 00) | Esta camada adiciona |
|---|---|
| Ficha de **produto** por player (`02-Produtos/`) | De-para de **jornada** cruzando players ([[TPL-Jornada-DePara]]) |
| Campo `maturidade: 1-5` solto | Escala nomeada e auditável [[EMA-J — Escala de Maturidade Agentica de Jornada]] |
| Tarifas com fonte+data | Disciplina de **ganhos de negócio públicos** (ROI, fraude evitada, NPS) com fonte+página |
| "Lacuna vendável → oferta" (informal) | Funil formal: [[Placar VALE — Priorizacao de Iniciativa de IA]] + backlog `06-Iniciativas/` |
| Telas linkadas na ficha | **Spec funcional/negócio/técnica** a partir da tela ([[TPL-Spec-Tela]]) |
| Cadência diária/semanal genérica | **Sprint de discovery** + prompts prontos de Cowork + tarefa agendada |

Nada é substituído. Este doc referencia o blueprint e os templates existentes.

---

## 2. Unidade de análise: a JORNADA (não o produto)

Você escolheu comparar **por jornada, cruzando incumbentes e fintechs**. A jornada é o corte certo porque é onde a IA reimagina de verdade — e onde o gap entre bancão e fintech fica visível.

**Jornadas-alvo da Fase 1 (financeiro), em ordem de prioridade editorial:**

1. **Originação e concessão de crédito** — risco/fraude/crédito, o núcleo da fase.
2. **Onboarding & KYC** (PF e PJ) — atrito mensurável em nº de passos; alta densidade de IA.
3. **Pagamentos & Pix / agentic commerce** — trilho, autorização, Pix Automático, comércio agêntico.
4. **Prevenção a fraude & disputas** — score, contestação, chargeback.
5. **Atendimento & cobrança** — copiloto/agente, deflexão, régua de cobrança.
6. **Investimentos & advisor** — copiloto financeiro, recomendação, suitability.

Cada jornada vira uma nota de de-para em `03-Comparativos/Jornadas/` (jornada × players), não uma por produto.

**Players-farol (ambos os lados):**
- *Incumbentes:* Itaú, Bradesco, Banco do Brasil, Santander, Caixa.
- *Fintechs/neo:* Nubank, Inter, C6, Mercado Pago, PicPay, PagBank/Stone.
- *Piloto (6):* Itaú · Bradesco · BB  ×  Nubank · Inter · Mercado Pago.

---

## 3. O fluxo de discovery (5 estágios)

```
[1] MAPEAR player        → perfil, portfólio, base de clientes (nº, segmento) — com fonte
        ↓
[2] DECOMPOR a jornada   → etapas, telas públicas, nº de passos/atrito por player
        ↓
[3] MEDIR maturidade     → EMA-J (L0–L5) por player naquela jornada + ganhos públicos citáveis
        ↓
[4] DE-PARA + gap        → matriz jornada×player; onde o líder está e onde está o vale
        ↓
[5] PRIORIZAR iniciativa → arquétipo (agêntico/copiloto/modernização/insight) + Placar VALE → serviço
```

Estágios 1–4 são coleta e estruturação (**automatizáveis** via Cowork + Claude in Chrome). Estágio 5 é onde eu penso: escolher o arquétipo, dar a tese e propor o serviço. Atrito zero de coleta, pensamento 100% meu.

---

## 4. Escala de maturidade (resumo — detalhe no framework)

Todo player, em toda jornada, recebe um nível [[EMA-J — Escala de Maturidade Agentica de Jornada]]:

| Nível | Rótulo | Sinal observável na jornada |
|---|---|---|
| **L0** | Manual/analógico | agência, papel, humano em todo passo |
| **L1** | Digitalizado | self-service no app, mas fluxo estático |
| **L2** | Automatizado (regras) | decisão por regra fixa, STP parcial |
| **L3** | Preditivo (ML) | score/modelo pontual (crédito, fraude) |
| **L4** | Assistido por IA (GenAI) | copiloto, atendimento generativo, human-in-the-loop |
| **L5** | Agêntico | agente executa a jornada ponta-a-ponta sob mandato/governança |

O **gap** (nível do líder − nível do alvo) é o combustível do backlog. Salto de nível define o **arquétipo de iniciativa** (§5).

---

## 5. Do gap ao serviço: arquétipos de iniciativa

O de-para revela em que nível cada jornada está. O salto pretendido define o tipo de iniciativa que eu proponho:

- **Reimaginação agêntica** (→ L5): agente autônomo sob mandato executa a jornada. *Laboratório: [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] / Cohort.*
- **Copiloto/assistência** (→ L4): GenAI com human-in-the-loop reduz tempo/erro.
- **Modernização** (L1→L2/L3): automação e preditivo onde ainda há regra manual.
- **Insight & feedback** (transversal): melhoria incremental baseada em atrito medido (passos, campos, abandono).

Cada iniciativa candidata vira nota em `06-Iniciativas/` ([[TPL-Iniciativa-IA]]) e recebe [[Placar VALE — Priorizacao de Iniciativa de IA]]: **V**alor de negócio · **A**derência a governança/soberania · **L**astro técnico/viabilidade · **E**ncaixe com Veltrix/Cohort. Governança pesa mais — é o núcleo defensável.

---

## 6. Ritmo operacional

### Sprint de discovery — 6 semanas (uma jornada por semana)

| Semana | Jornada | Entrega ao fim da semana |
|---|---|---|
| 1 | Onboarding & KYC | de-para + maturidade dos 6 players + 2 iniciativas priorizadas |
| 2 | Originação de crédito | idem |
| 3 | Pagamentos & Pix / agentic | idem |
| 4 | Prevenção a fraude & disputas | idem |
| 5 | Atendimento & cobrança | idem |
| 6 | Investimentos & advisor | idem + consolidação do backlog VALE |

Fim da Semana 6: **1 backlog priorizado de ~12 iniciativas** e a escolha de 1–2 para virar proposta de serviço.

### Rotina diária (~60–90 min, encaixa no loop que você já tem)

1. **Coletar (auto, ~30 min):** rodar o *Prompt 1 (mapear player)* ou *Prompt 2 (de-para de jornada)* do dia. Cruzar com a biblioteca de reports.
2. **Capturar telas (~15 min):** *Prompt 3* via Claude in Chrome nas telas públicas da jornada do dia → gera spec.
3. **Pensar (~15–30 min, eu):** revisar o de-para, marcar maturidade, escrever a tese e o arquétipo de iniciativa. **Só eu faço isto.**

### Rotina semanal (sexta, junto da Weekly Review)

Rodar *Prompt 4 (priorização)* sobre as jornadas da semana → atualizar backlog VALE → escolher **uma** iniciativa que vira post/oferta. Fecha o loop com [[TPL-Weekly-Review]].

---

## 7. Prompts prontos de Cowork

> Colar no Cowork. Todos respeitam: **só conteúdo público**, dado com **fonte+data**, e fecho **"o que eu diria num board"**. Nenhum burla login/ToS (governança que eu mesmo vendo).

### Prompt 1 — Mapear player
```
Mapeie o player <NOME> para minha base de discovery financeiro. Use apenas fontes
públicas (site institucional, relatório de resultados/RI, tarifário Bacen, app stores,
imprensa). Traga, cada dado com fonte + data: (1) perfil e licença; (2) portfólio de
produtos por segmento; (3) base de clientes — nº de clientes/contas, segmento (PF/PJ),
market share se público; (4) estratégia de IA e estratégia de ataque/GTM. Salve como
ficha em 07-Setores/Financeiro/01-Instituicoes/<grupo>/ (Bancoes | Fintechs-e-Neobancos |
Adquirentes-e-Pagamentos | Concorrentes-Consultoria) no template TPL-Ficha-Instituicao.
Feche com "o que eu diria sobre este player num board". Se um dado não tiver fonte
pública, marque [sem fonte] em vez de estimar.
```

### Prompt 2 — De-para de jornada (o coração)
```
Monte o de-para da jornada <JORNADA> cruzando os players <A, B, C...>. Para cada player,
usando só fontes públicas: (1) decomponha a jornada em etapas e conte nº de passos/campos
até a parede de login; (2) atribua o nível de maturidade EMA-J (L0–L5) com a evidência
que justifica; (3) liste ganhos de negócio medidos e publicados (ex: redução de fraude %,
aprovação de crédito, NPS, tempo de onboarding) — cada um com fonte + página/URL. Gere a
matriz jornada×player e aponte o gap (quem lidera, onde está o vale). Salve em
07-Setores/Financeiro/03-Comparativos/Jornadas/ no template TPL-Jornada-DePara. Feche com
a minha leitura de board. Sinalize [sem tese] se não render.
```

### Prompt 3 — Capturar telas → spec (Claude in Chrome)
```
Abra as telas PÚBLICAS da jornada <JORNADA> do player <NOME> (landing, simulação,
onboarding até o login) via Claude in Chrome. Capture cada tela datada em
07-Setores/Financeiro/05-Telas/<player>/<jornada>/. Para cada tela relevante gere uma
spec no template TPL-Spec-Tela com as três lentes: FUNCIONAL (o que a tela faz, campos,
validações), NEGÓCIO (objetivo, métrica de atrito, gatilho de conversão), TÉCNICA
(padrões de UI, sinais de stack/IA embarcada, integrações visíveis). Não acesse nada
logado; pare na parede de autenticação.
```

### Prompt 4 — Priorizar iniciativas (do de-para ao backlog)
```
Leia os de-para de jornada em 07-Setores/Financeiro/03-Comparativos/Jornadas/ desta semana. Para
cada gap relevante, proponha iniciativas de IA classificadas por arquétipo (reimaginação
agêntica / copiloto / modernização / insight). Para cada uma, crie nota em
06-Iniciativas/ no template TPL-Iniciativa-IA e aplique o Placar VALE (V, A, L, E, 1–5,
governança com peso 2). Gere um ranking. NÃO escreva a tese final nem escolha a vencedora
— isso é meu. Entregue o ranking e os candidatos.
```

### Prompt 5 — Consolidação semanal
```
Consolide o discovery da semana: jornadas fechadas, cobertura (players×jornada), nº de
iniciativas no backlog por arquétipo, e as 3 de maior VALE. Cruze com a biblioteca de
reports (~/Reports) quando houver dado que reforce um gap. Prepare um rascunho de 1 tese
para post/oferta ligada a Veltrix ou Cohort. Salve em 06-Posts/ como rascunho.
```

---

## 8. Governança (herda do blueprint, reforço)

Só conteúdo público; respeito a `robots.txt`/ToS; zero scraping atrás de login; telas param na parede de autenticação; todo dado com proveniência (fonte+data). Esta base **é** demonstração da governança que vendo — coletar errado destrói o argumento. Ganhos de negócio de terceiros são reportados como autorrelato do player (com fonte), nunca como fato meu.

---

## 9. Métricas de sucesso

Não é "quantas jornadas". É: **cobertura** (jornadas × players preenchidos), **frescor** (de-para com captura < 60 dias), **densidade de tese** (% de iniciativas com leitura de board), e a que importa — **conversão comercial** (iniciativas que viraram proposta/gancho de oferta).

---

## 10. Próximos passos

1. Aprovar os dois frameworks ([[EMA-J — Escala de Maturidade Agentica de Jornada]] e [[Placar VALE — Priorizacao de Iniciativa de IA]]) e os três templates.
2. Rodar a **Semana 1 (Onboarding & KYC)** com os 6 players-piloto — usa Prompt 2 + Prompt 3.
3. Decidir se a coleta diária vira **tarefa agendada** do Cowork (recomendo 1 semana manual, depois agendar).
4. Ao fechar a Semana 1, escolher a iniciativa de maior VALE e ligar a uma oferta do catálogo consultivo.

---

**Liga com:** [[00-Blueprint-Mapeamento-Produtos-Banking-BR]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[TPL-Jornada-DePara]] · [[TPL-Iniciativa-IA]] · [[TPL-Spec-Tela]]
