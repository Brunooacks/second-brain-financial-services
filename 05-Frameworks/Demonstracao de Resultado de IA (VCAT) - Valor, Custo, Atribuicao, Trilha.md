---
tipo: framework
data: 2026-07-24
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-24]]"
eixos: [economia-ia, financeiro, governanca, agentes]
tags: [framework, auto]
---

# 🧱 Demonstração de Resultado de IA (VCAT) — Valor, Custo, Atribuição, Trilha

## O problema que ele resolve
O Santander criou o padrão que todo board vai passar a cobrar: reportar valor de IA em **moeda por trimestre** (**€35 mi no Q1**, meta de **€200 mi em 2026** e **€1 bi em 2026-28**) *(Noticias Bancarias, 22/07/2026)*. O problema é que esse padrão publica só a primeira linha: o valor bruto. Valor sem custo é meia contabilidade; valor sem atribuição e trilha é meia governança. O VCAT dá ao board a demonstração de resultado completa da IA — o que impressiona no earnings call **e** o que sobrevive a uma auditoria de FinOps.

## O framework
Quatro linhas, na ordem em que um board lê um P&L:

1. **V — Valor bruto gerado.** O número em moeda por período (padrão Santander). É o que já se publica.
2. **C — Custo de inferência.** Quanto se gastou para gerar aquele valor, por caso de uso. Sem esta linha, "ROI de IA" é receita/eficiência disfarçada de margem.
3. **A — Atribuição por agente.** Qual dos N agentes em produção gerou o quê. Sem isso, o valor é agregado indefensável — não se sabe o que escalar nem o que cortar.
4. **T — Trilha auditável.** Quem/qual agente fez o quê, rastreável. É o que transforma o número de slide de earnings em número auditável.

A leitura de board em 30s: *"IA tem demonstração de resultado — Valor menos Custo, com Atribuição e Trilha. Se falta uma das quatro, o número não fecha."*

## Quando usar / quando NÃO usar
**Usar** sempre que um banco (ou concorrente) anunciar meta ou realizado de valor de IA em moeda — para cobrar as três linhas que faltam. **Não usar** como vara de medir pilotos ou provas de conceito: antes de escala, não há custo de inferência nem frota que justifiquem a demonstração completa; ali o número relevante ainda é baseline, não margem.

## Aplicado na prática
Santander reporta a linha **V** (€35 mi Q1) e roda **280+ agentes em produção**, mas não publica **C** (custo de inferência), **A** (atribuição por agente) nem **T** (trilha). O VCAT vira o one-pager de diagnóstico: **Veltrix** instrumenta V e C (valor e custo de inferência por caso de uso); **Cohort** instrumenta A e T (atribuição por agente e trilha). Pitch pronto para qualquer banco que anunciou meta de valor com IA — a pergunta de entrada é "qual é o seu €35 mi, e quanto custou?".

## Como cito isto num board
"IA agora tem P&L. O Santander publicou o Valor; a nossa vantagem é publicar as outras três linhas — Custo, Atribuição e Trilha — antes que o auditor pergunte."
