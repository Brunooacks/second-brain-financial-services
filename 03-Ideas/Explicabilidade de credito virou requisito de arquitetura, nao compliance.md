---
tipo: ideia
data: 2026-08-14
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-14]]"
eixos: [governanca, financeiro]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Explicabilidade de crédito virou requisito de arquitetura, não relatório de compliance

## A tese
A explicabilidade de uma negativa de crédito deixou de ser relatório que se produz depois e virou requisito que se projeta antes — porque quem regula IA no Brasil hoje é a **ANPD**, com a **LGPD que já está em vigor**, não o PL 2338 que ainda espera relator. Quem trata explicação como entregável de compliance está construindo o passivo que o regulador vai cobrar.

## Por que eu acredito nisso
O número que fecha o argumento é o **delta de 29 pontos**: **79%** dos reguladores classificam explicabilidade como crítica ou importante, mas só **50%** da indústria adotou métodos de XAI e cerca de **dois terços não monitoram viés** (relatório Cambridge/BIS/IMF, **pág. 10**, biblioteca interna). Esse gap é exatamente onde a ANPD vai encostar: o **Mapa de Temas Prioritários 2026–2027** coloca IA + serviços financeiros entre os quatro eixos de fiscalização ativa, com alvo declarado no **scoring automatizado que nega crédito sem explicação clara** e exigência de explicabilidade **real, não meramente formal** — 10 ações programadas sobre dado biométrico, de saúde ou financeiro no 2º semestre (ANPD / Daniel Law). E ela chega **antes** do PL 2338 porque não precisa de lei nova. Se explicabilidade é relatório, você reconstrói a decisão depois — e o tempo pra reconstruir as últimas 10 negativas automáticas é a sua distância até a ANPD. Se é arquitetura, cada negativa já carrega no log o modelo, a versão, as features determinantes e o humano responsável.

## Quem discordaria — e por quê
Quem lembra que **XAI em modelo de fronteira é aproximação, não prova** — prometer explicação perfeita ao regulador cria passivo maior do que o que resolve. Ponto válido, e por isso a defesa não é "explicação perfeita", é **trilha reconstrutível + humano nomeado**. Também discordaria quem aposta que o marco a esperar é o PL 2338 (com classificação de alto risco e multa de até R$ 50 mi) — mas esperar lei nova ignora que a LGPD já basta para a ANPD agir hoje.

## O que eu faria / recomendaria
Tratar explicabilidade como **requisito de arquitetura da decisão de crédito**, não item de relatório: cada negativa gravando modelo, versão, features determinantes e responsável no próprio log. Conecta ao **Cohort** (trilha e mandato por decisão de agente) e ao **Veltrix** (o roteamento registra qual modelo/versão decidiu). O investimento vale duas vezes: atende a LGPD hoje e antecipa o PL 2338 amanhã — mesma raiz (transparência, explicação, contestação). É o argumento pra destravar orçamento: não é compliance de uma lei futura, é compliance de uma lei presente com opção grátis sobre a futura.

## Lastro
- ANPD — Mapa de Temas Prioritários 2026–2027 (via Daniel Law)
- Relatório Cambridge/BIS/IMF, pág. 10 (biblioteca interna, `02-Sources/Reports/`)
- InfoWorld, 14/08
- Relacionadas: [[Credito preditivo em Open Finance vira risco de explicabilidade - testar no sandbox da ANPD]] · [[Aconselhamento financeiro por IA em massa encontra o art 20 da LGPD]] · [[MRR - Matriz de Rastreabilidade da Recomendacao]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança  ·  **Setor:** financeiro
