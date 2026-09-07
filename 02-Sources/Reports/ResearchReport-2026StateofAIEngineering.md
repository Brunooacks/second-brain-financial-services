---
tipo: source
classe: report
titulo: "State of AI Engineering 2026"
autor: Datadog
data_publicacao: 2026
data_captura: 2026-06-08
setor: [multissetor]
eixos: [economia-ia, agentes, risco, fronteira]
tags: [source]
---

**Fonte/autor/data** · Datadog, "State of AI Engineering 2026". Baseado em telemetria de LLM de **mais de mil clientes** Datadog — dado de produção real, não survey. (Token estimado por contagem de caracteres /4 para evitar ingerir dado sensível, pág 17.)

**Tese central**
A IA em produção virou um problema clássico de sistemas distribuídos — roteamento, capacity planning, controle de custo, debugging — com um agravante: mudar modelo, prompt ou retrieval altera latência, gasto e taxa de falha **sem mudança óbvia de código**. O gargalo entre demo e sistema confiável é evaluation + disciplina operacional. "Model churn vira problema de governança."

**Achados-chave (Veltrix-relevante)**
- Stacks são multi-provider: OpenAI tem **63%** de share (caiu de 75% há um ano, mas uso absoluto mais que dobrou); Gemini e Claude ganharam **+20 e +23 pontos** no ano (pág 3).
- **Mais de 70%** das organizações usam **3+ modelos**; share usando 6+ quase dobrou. Times montam portfólios de modelo por latência/custo/risco/tarefa (pág 4) — o caso de uso exato de um proxy de roteamento.
- Falha dominante em produção é **capacidade, não código**: fev/2026, 5% dos spans com erro, **60% deles por rate limit**; mar/2026, rate limits = ~1/3 dos erros, **~8,4 milhões de erros de rate limit** no total (pág 13). Exige budgeting + backpressure.
- Caching subutilizado: **69%** dos input tokens são prompt de sistema (reutilizável), mas só **28%** das chamadas (mesmo entre modelos que suportam cache) mostram cached-read tokens (pág 9-10). Dinheiro deixado na mesa.
- Janelas de contexto explodiram (128k → até 2 milhões de tokens), e tokens médios por request **mais que dobraram** na mediana — o problema migra de "gerenciar tokens" para "saber qual informação realmente move o modelo" (pág 11).
- Agentes ainda são monolíticos: **59%** dos requests agênticos fazem uma única service call; só **18%** fazem 3+ (pág 14). A migração para multi-agente está só começando.

**Conexão (Veltrix + governança)**
Este relatório é praticamente o briefing de produto do Veltrix. Três dores mapeiam 1:1: (1) 70% multi-modelo → necessidade de proxy/roteamento por custo-latência-risco; (2) rate limit como falha nº1 → o proxy é o lugar natural para budgeting, backpressure e failover entre provedores; (3) caching em 28% → ganho de FinOps imediato observável no proxy. E "model churn vira governança" é a ponte para o Cohort. Em banco, onde custo de LLM e confiabilidade são auditáveis, ter esse plano de observabilidade+FinOps centralizado deixa de ser conforto e vira controle.

**O que eu diria sobre isso num board**
Este é o report técnico que justifica por que não basta "contratar a OpenAI". Os três números que eu levaria: 70% das empresas já são multi-modelo, rate limit é a falha nº1 de produção, e caching é usado em apenas 28% dos casos onde caberia. Traduzindo para finanças: temos uma alavanca de FinOps não explorada (cache) e um risco de confiabilidade (capacidade do provedor) que só um plano de proxy/observabilidade centralizado resolve — exatamente onde o Veltrix se posiciona. É dado de telemetria real de mil empresas, então tem peso de evidência; a única ressalva é viés de base (clientes Datadog tendem a ser mais maduros em observabilidade que a média do mercado).
