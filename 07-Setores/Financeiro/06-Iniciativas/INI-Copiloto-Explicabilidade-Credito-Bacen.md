---
tipo: iniciativa-ia
jornada: credito
arquetipo: copiloto
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 24
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, soberania, agentes]
tags: [iniciativa, backlog, vale, credito, explicabilidade, bacen, veltrix]
---

# 💡 Iniciativa — Copiloto de explicabilidade de crédito (Bacen-ready)

**Em uma frase:** Um copiloto que traduz a decisão de um foundation model/ML de crédito em explicação auditável — motivo do score, variáveis determinantes, contrafactual — para atender a exigência de explicabilidade do Bacen sem sacrificar o poder preditivo do motor.

## 🎯 O gap que origina isto
- Jornada: Originação de crédito · Nível atual (EMA-J): **L4** (Nubank foundation model, Itaú GenAI) · Alvo: **L4 governado** · Gap: quanto mais avançado o motor, pior a explicabilidade — e é exatamente onde o Bacen aperta. O vale não é mais modelo, é explicar o modelo. Ver [[De-Para — Originação de crédito]].

## 🏗️ Arquétipo e desenho
**Copiloto.** Não substitui o motor de crédito — senta ao lado dele. Para cada decisão, gera a explicação em linguagem de negócio e a trilha técnica (SHAP/contrafactual + narrativa GenAI), registra proveniência do dado e monta o dossiê que o regulador e o cliente podem exigir. Human-in-the-loop no analista de crédito e no time de compliance.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Custo evitado (multa/veto regulatório), destrava uso de motores mais potentes que hoje travam por risco de compliance |
| A — Aderência governança/soberania | 5 | 2,0 | Núcleo da tese: explicabilidade, auditabilidade e proveniência do dado; casa direto com a agenda do Bacen |
| L — Lastro técnico/viabilidade | 4 | 1,0 | XAI (SHAP, contrafactual) sobre modelos é maduro; a camada GenAI de narrativa é viável hoje |
| E — Encaixe Veltrix/Cohort | 4 | 1,0 | Veltrix dá a observabilidade e o custo por decisão; Cohort dá a trilha auditável |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(4×1,0) = 24 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Veltrix mede o custo de inferência por explicação gerada (FinOps) e roteia o modelo de narrativa por residência de dado; Cohort registra a trilha de quem/o quê explicou cada decisão. A explicabilidade de crédito vira o segundo caso público do par Veltrix+Cohort, depois do onboarding.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: explicação gerada por GenAI pode ela mesma alucinar/racionalizar a decisão — explicabilidade falsa é pior que nenhuma; custo de inferência por decisão em alto volume; risco de a "explicação" virar teatro de compliance sem mudar o modelo. Se não fecha o contraponto, é slogan.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Originação de crédito]]
