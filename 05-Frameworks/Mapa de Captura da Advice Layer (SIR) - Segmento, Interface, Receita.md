---
tipo: framework
data: 2026-08-05
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-08-05]]"
eixos: [financeiro, soberania, agentes]
tags: [framework, auto]
---

# 🧱 Mapa de Captura da Advice Layer (SIR) — Segmento, Interface, Receita

## O problema que ele resolve
Quando a IA vira a interface que recomenda, o incumbente perde o cliente sem perder o produto — vira prateleira. Mas a maioria dos boards discute "temos IA?" em vez de "**quem é dono da recomendação em cada segmento e por onde ela pode ser roubada?**". Falta um diagnóstico de uma página que mostre, sem hype, onde a camada de aconselhamento (advice layer) está exposta à captura por um agente externo via Open Finance.

## O framework
Uma linha por **segmento**; três colunas + a leitura do vetor de ataque:

- **S — Segmento**: varejo, alta renda, private/wealth. (Onde o valor do aconselhamento é maior é onde o atacante entra primeiro.)
- **I — Interface que recomenda hoje**: quem controla a tela/canal que faz a recomendação? (app do banco, gerente humano, super-app, ou já um terceiro).
- **R — Receita da recomendação**: como essa interface ganha dinheiro? **comissão** (conflitada — empurra a maior tarifa), **fee-based** (alinhada) ou **assinatura** (isenta). O modelo de receita é o que o atacante ataca.
- **Vetor de captura (leitura sobre o mapa)**: por onde um agente externo entra pelo **Open Finance** para assumir a recomendação sem passar pelo banco — o cliente leva o dado, o terceiro leva o relacionamento.

A leitura de board: quanto mais a receita depende de **comissão**, mais exposta a linha — porque o atacante que cobra **assinatura** (ex.: Decade, R$ 200/mês) vende exatamente a isenção que a comissão não tem.

## Quando usar / quando NÃO usar
- **Usar**: estratégia defensiva de wealth/banking AI-native; avaliar ameaça de fintech de aconselhamento; decidir se a resposta é produto novo ou novo modelo de receita.
- **NÃO usar**: para produtos sem componente de recomendação (ex.: liquidação, custódia pura), onde a advice layer não é o ativo em disputa. Não é modelo de risco de agente — para mandato/trilha use o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]].

## Aplicado na prática
Caso de ontem: no segmento **alta renda/private**, a interface que recomenda hoje é o gerente/plataforma do banco, com receita de **comissão** de distribuição de produto — linha vermelha. A Decade entra pelo Open Finance com receita de **assinatura** (R$ 200/mês) e ataca justamente o conflito da comissão. Onde a linha for comissão, o pitch de produto é claro: governança da recomendação e FinOps do custo por conselho (Cohort + Veltrix) são a infra de quem quer migrar de comissão para fee/assinatura sem virar passivo.

## Como cito isto num board
"Não pergunte se temos IA — pergunte, por segmento, quem é dono da recomendação, como ela ganha dinheiro e por onde o Open Finance deixa um terceiro roubá-la. Onde a receita for comissão, já estamos à venda."
