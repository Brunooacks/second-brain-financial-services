---
tipo: framework
data: 2026-07-09
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-09]]"
eixos: [soberania, economia-ia, financeiro, governanca]
tags: [framework, auto]
---

# 🧱 Matriz Construir-Comprar-Parcear do Ativo de IA (DCS) — Dado, Custo, Soberania

## O problema que ele resolve
Quando o líder de mercado internaliza o ativo de IA (Nubank construindo o NuFormer, BB parceirando com a UnB), o board dos outros bancos reage com fé — "vamos ter nosso modelo também" — sem o número que justifica. A decisão de **construir, comprar ou parcear** cada capacidade de IA vira vaidade em vez de estratégia. Faltava um one-pager que transformasse essa decisão numa conta auditável, capacidade por capacidade.

## O framework
Para cada capacidade de IA (crédito, atendimento, private banking, cobrança...), pontue três eixos — **DCS** — e deixe a nota apontar a decisão:

- **D — Dado proprietário.** Tenho volume e exclusividade de dado transacional que tornem um modelo próprio *defensável* (não copiável em 90 dias)? Alto = candidato a construir; baixo = commodity, comprar.
- **C — Custo (FinOps auditável).** Qual o custo de inferência build vs buy, por jurisdição e sensibilidade? Sem baseline, "ROI de IA" é fé. (Terreno do **Veltrix**.)
- **S — Soberania.** O dado/execução fica sob minha jurisdição ou passa pela API/infra de um terceiro? Alto risco de soberania empurra para construir/parcear mesmo quando o custo favorece comprar.

Decisão de saída (rota):
- **Construir** — alto em D, favorável em C, exige S alta (ex.: NuFormer no dado transacional do Nubank).
- **Comprar** — baixo em D (capacidade é commodity) e sem risco crítico de S.
- **Parcear** — D existe mas falta escala/tempo/capital pra amortizar o build (ex.: BB–UnB, 24 meses): compra tempo e pesquisa sem alugar a margem inteira.

## Quando usar / quando NÃO usar
Usar antes de qualquer decisão de "ter nosso próprio modelo/agente" e na revisão anual de portfólio de IA. **Não** usar como ranking de prioridade (isso é o [[Placar VALE — Priorizacao de Iniciativa de IA]]) nem como credencial de agente (isso é o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]) — o DCS decide a **origem do ativo**, não a ordem nem o mandato.

## Aplicado na prática
Private banking por IA: **D** alto (dado de patrimônio/comportamento é proprietário), **C** a medir via **Veltrix** (custo de inferência do assistente sob carga), **S** alto (aconselhamento não pode vazar por API de terceiro) → rota **construir/parcear**, nunca comprar cru. Já um chatbot de FAQ: **D** baixo, **S** baixo → **comprar**. O **Cohort** entra depois: decidido o ativo, governa quem treina o quê, com que dado, sob que mandato.

## Como cito isto num board
"Antes de dizer que vamos ter nosso modelo, cada capacidade passa pelo DCS — Dado, Custo, Soberania: a matriz diz se construímos, compramos ou parceamos, e traz o número que justifica. Sem isso, 'modelo próprio' é vaidade; com isso, é margem."
