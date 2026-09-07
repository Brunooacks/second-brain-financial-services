---
tipo: ideia
data: 2026-07-03
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-03]]"
eixos: [financeiro, governanca, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 No agente de investimento, o motor determinístico decide e o LLM só conversa — quem inverter troca suitability por alucinação

## A tese
A arquitetura que o Itaú colocou em produção é a divisão certa e vai virar o padrão de referência: as **22 mil simulações fazem o trabalho quantitativo (a decisão), o LLM só traduz em conversa**. Isso não é detalhe de engenharia — é o que torna o sistema **auditável**. A tese defensável: qualquer banco que inverter a ordem, deixando o LLM *decidir* a alocação em vez de só *conversar* sobre ela, troca suitability (dever de adequação) demonstrável por alucinação não-rastreável. A camada de conversa nunca pode ser a camada de decisão num produto regulado.

## Por que eu acredito nisso
A **Inteligência de Investimentos Itaú** consulta **50 bases de dados** e roda **22 mil simulações antes de sugerir** — teste com 10 mil clientes Uniclass/Personnalité sem assessor humano, expandindo a 30 mil no ano (NeoFeed; Consumidor Moderno; Mobile Time, jul/2026). O ponto de arquitetura: a GenAI é a **camada de conversa, não a de decisão**. Um motor determinístico produz um rastro reproduzível ("rodei estas simulações, apliquei este perfil"); um LLM decisor produz uma saída que ninguém consegue reconstruir depois. Quando o regulador (CVM/Bacen) perguntar *"por que o agente recomendou isto a este cliente?"*, só a primeira arquitetura tem resposta.

## Quem discordaria — e por quê
O defensor do agente end-to-end: modelos de fronteira já raciocinam bem o suficiente para decidir com tool-use, e separar motor determinístico de LLM é muleta transitória que trava flexibilidade — a trajetória é o agente que decide e explica sozinho. Contraponto real para domínios de baixo risco. Cai por terra em decisão regulada: "explicação gerada pelo próprio LLM" é narrativa plausível, não trilha auditável — o modelo pode racionalizar *post hoc* uma decisão que não foi a que ele de fato tomou. Adequação demonstrável exige que a decisão nasça de um processo reproduzível, não de uma caixa que também escreve a própria justificativa.

## O que eu faria / recomendaria
Adotar a arquitetura do Itaú (motor determinístico decide, LLM só conversa) como **padrão de referência interno** para todo agente que toque recomendação regulada — e transformá-la em critério de aprovação de agente no **Cohort**: o mandato separa explicitamente "pode conversar" de "pode decidir", e a promoção a produção exige que a camada de decisão seja auditável fora do LLM. No **Veltrix**, a conta importa: 22 mil simulações por sugestão × 30 mil clientes é volume de inferência que vira linha de custo material — instrumentar por caso de uso agora. Conecta a [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] e complementa [[Agente de investimento sem assessor humano e alto risco em producao antes da regua]] pelo ângulo de *como* construir, não só *que risco* corre.

## Lastro
- [[2026-07-03]] — clusters 💰 IA em Serviços Financeiros e 🎓 Aprendizado do dia (suitability)
- Itaú Inteligência de Investimentos — 50 bases, 22 mil simulações, 10 mil → 30 mil clientes (NeoFeed · Consumidor Moderno · Mobile Time, jul/2026)
- Nubank nuFormer / AI Private Banker — 15 mi de MAU em teste (Finsiders · Nu International, jun/2026)

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança  ·  **Setor:** Financeiro
