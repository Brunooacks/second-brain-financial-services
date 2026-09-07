---
tipo: iniciativa-ia
jornada: onboarding-kyc
arquetipo: modernizacao
maturidade_atual: L2
maturidade_alvo: L4
score_vale: 23.5
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, onboarding, soberania, veltrix]
---

# 💡 Iniciativa — Camada de validação cruzada de bases públicas com FinOps de inferência

**Em uma frase:** Uma camada de orquestração que cruza bases públicas (GOV.BR, Receita, listas restritivas) no onboarding, com observabilidade de custo e residência de dados por verificação.

## 🎯 O gap que origina isto
- Jornada: Onboarding & KYC · Nível atual (EMA-J): **L2** (validação cruzada hoje é regra/manual) · Alvo: **L4** · Gap: 2 (território de modernização forte). A autorregulação Febraban (27/10/2025) tornou "validação cruzada de bases públicas + reporte ao Bacen" obrigação, e o acordo Inter×GOV.BR (35 mi, jun/2025) mostra a base pública como ativo. Ver [[De-Para — Onboarding & KYC]].

## 🏗️ Arquétipo e desenho
**Modernização (com viés de insight).** Padroniza e observa a etapa hoje mais frágil: o cruzamento de bases. Orquestra as consultas, mede custo/latência por fonte, aplica roteamento por jurisdição (o que sai/não sai do país) e entrega trilha para o reporte Febraban/Bacen. Vira a etapa de compliance em produto governado, não colcha de retalhos.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 3 | 1,5 | Valor real mas indireto (compliance/custo evitado), não receita de topo; reduz retrabalho e risco de multa |
| A — Aderência governança/soberania | 5 | 2,0 | Coração da soberania: residência de dados, roteamento por jurisdição, validação de bases públicas BR — exigência regulatória já vigente |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Integrações conhecidas; desafio é orquestração + observabilidade, não pesquisa |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Veltrix é FinOps + observabilidade de inferência com roteamento — encaixe direto |

**Score VALE = (3×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 23,5 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Veltrix expõe custo por verificação, latência por base e roteamento por jurisdição — a etapa de KYC vira vitrine de FinOps + soberania de dados aplicada a compliance obrigatório.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: valor de negócio é defensivo, não ofensivo — board pode ver como "custo de conformidade"; depende de acesso/estabilidade de bases públicas de terceiros; risco de virar commodity se muitos fornecedores entrarem.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Onboarding & KYC]]
