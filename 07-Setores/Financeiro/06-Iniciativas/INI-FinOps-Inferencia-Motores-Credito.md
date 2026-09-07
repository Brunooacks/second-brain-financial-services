---
tipo: iniciativa-ia
jornada: credito
arquetipo: modernizacao
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 22.5
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, credito, finops, veltrix, inferencia]
---

# 💡 Iniciativa — Camada FinOps de inferência para motores de crédito (Veltrix)

**Em uma frase:** Uma camada que mede e governa o custo de inferência por decisão de crédito e roteia cada chamada de modelo por jurisdição/residência de dado — transformando o gasto opaco de foundation models e GenAI no motor de crédito em custo por decisão auditável.

## 🎯 O gap que origina isto
- Jornada: Originação de crédito · Nível atual (EMA-J): **L4** (motores caros de foundation model/GenAI) · Alvo: **L4 governado em custo** · Gap: quem migrou para foundation model (Nubank) e GenAI (Itaú) ganhou acurácia e herdou um custo de inferência crescente e invisível por decisão. Ninguém expõe custo por decisão nem roteamento por jurisdição como controle. Ver [[De-Para — Originação de crédito]].

## 🏗️ Arquétipo e desenho
**Modernização (com viés de insight).** Não muda o motor de crédito — instrumenta a camada de inferência: mede custo/latência por decisão, roteia por residência de dado (jurisdição), aplica orçamento e alerta de derrapagem de custo. É FinOps de IA aplicado ao ponto de maior volume de inferência do banco.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 3 | 1,5 | Custo evitado de inferência em alto volume; não move receita diretamente, move margem |
| A — Aderência governança/soberania | 4 | 2,0 | Roteamento por jurisdição e residência de dado; auditabilidade de custo; soberania sem cobrir o eixo de explicabilidade inteiro |
| L — Lastro técnico/viabilidade | 5 | 1,0 | É exatamente o que Veltrix já faz (proxy de LLM com FinOps/observabilidade) — viabilidade máxima |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Veltrix puro; demonstração viva do método CARO no fluxo de maior volume |

**Score VALE = (3×1,5)+(4×2,0)+(5×1,0)+(5×1,0) = 22,5 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
É Veltrix no seu terreno natural: proxy de inferência com FinOps e observabilidade, roteando por jurisdição. O motor de crédito é o caso onde o custo por decisão × volume dá o argumento comercial mais direto.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: é a de menor valor de negócio das três — mexe em margem, não em ponteiro de receita; risco de virar "monitoramento de custo" sem tese de governança se o eixo de residência de dado não for tratado como diferencial. Se não fecha o contraponto, é slogan.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Originação de crédito]]
