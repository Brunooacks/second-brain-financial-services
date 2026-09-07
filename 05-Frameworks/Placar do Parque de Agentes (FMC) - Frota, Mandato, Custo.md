---
tipo: framework
data: 2026-06-29
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-06-28]]"
eixos: [agentes, governanca, economia-ia, financeiro]
tags: [framework, auto]
---

# 🧱 Placar do Parque de Agentes (FMC) — as três colunas que separam "ter IA agêntica" de "controlar IA agêntica"

## O problema que ele resolve
Itaú, Bradesco e Banco do Brasil já cruzaram a linha do piloto para o **parque de agentes (agent estate)** em produção — centenas a milhares de agentes. Mas a régua de board ainda mede **adoção** (quantos agentes, quantas iniciativas), não **controle**. Falta o painel de uma página que um conselho lê em 30 segundos e sabe se a frota está governada ou apenas grande. Sem ele, "temos IA agêntica" e "controlamos nossa IA agêntica" viram a mesma frase.

## O framework
Todo parque de agentes em produção se mede por **três colunas — FMC**:

- **F — Frota:** nº de agentes em produção. É o número que os bancos já publicam (BB: +12 mil agentes Copilot). Sozinho, é vaidade.
- **M — Mandato:** % da frota com escopo/mandato documentado e auditável (o ELJT do [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]). É o que separa frota de shadow-AI.
- **C — Custo:** custo de inferência por agente. Sem ele, ROI de IA é fé, não FinOps — e a fatura aparece no fechamento, não no planejamento.

A maturidade não está em maximizar F. Está em ter as três colunas preenchidas: frota grande com M baixo e C cego é proliferação, não maturidade.

## Quando usar / quando NÃO usar
**Usar:** como slide de board para reportar IA agêntica; como diagnóstico antes de escalar um marketplace de agentes; como critério de comparação entre bancos (quem só tem F vs quem tem F+M+C).
**Não usar:** para um time com punhado de agentes em piloto isolado — aí o placar é burocracia; basta o mandato individual. FMC é instrumento de *estate*, não de protótipo.

## Aplicado na prática
No **Cohort**, a coluna **M** é o produto: cada agente promovido a produção entra no registro com mandato ELJT, e o % governado vira métrica viva. No **Veltrix**, a coluna **C** é executável: observabilidade e custo de inferência por agente, com teto e alerta de anomalia (igual a limite de cartão corporativo). Cohort preenche M, Veltrix preenche C — o board lê F+M+C numa linha.

## Como cito isto num board
"Não me digam quantos agentes temos. Digam quantos estão sob mandato e quanto cada um custa por inferência — Frota, Mandato, Custo. É o placar que separa ter IA agêntica de controlá-la."
