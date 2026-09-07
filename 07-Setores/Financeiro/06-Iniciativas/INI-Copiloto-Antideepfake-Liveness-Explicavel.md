---
tipo: iniciativa-ia
jornada: onboarding-kyc
arquetipo: copiloto
maturidade_atual: L3
maturidade_alvo: L4
score_vale: 21
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, agentes]
tags: [iniciativa, backlog, vale, onboarding, fraude, veltrix]
---

# 💡 Iniciativa — Copiloto anti-deepfake de verificação de identidade (liveness explicável)

**Em uma frase:** Um copiloto para o time de fraude/KYC que explica em linguagem natural por que uma prova de vida foi aprovada ou barrada, com human-in-the-loop e trilha da decisão.

## 🎯 O gap que origina isto
- Jornada: Onboarding & KYC · Nível atual (EMA-J): **L3** · Alvo: **L4** · Gap: 1 (modernização/copiloto). Itaú já opera 3D liveness anti-deepfake (Mobile Time · 13/06/2025), mas a decisão é caixa-preta — falta camada explicável/auditável. Ver [[De-Para — Onboarding & KYC]].

## 🏗️ Arquétipo e desenho
**Copiloto.** Não substitui o motor de liveness — senta em cima dele. Quando o modelo de visão sinaliza suspeita de deepfake/apresentação fraudulenta, o copiloto resume os fatores (sinais de profundidade, artefatos, inconsistência doc×selfie) para o analista decidir mais rápido, e grava a justificativa. Ataca o vetor deepfake com explicabilidade, que é o que o regulador vai cobrar.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Reduz fraude na porta de entrada e tempo de análise manual; deepfake é ameaça declarada e crescente |
| A — Aderência governança/soberania | 4 | 2,0 | Explicabilidade + trilha da decisão = auditabilidade; não move residência de dados, por isso não é 5 |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Tecnologia madura (3D liveness já em produção no Itaú); camada explicável é incremento viável |
| E — Encaixe Veltrix/Cohort | 3 | 1,0 | Veltrix mede custo/observabilidade da inferência dos modelos de visão; encaixe parcial |

**Score VALE = (4×1,5)+(4×2,0)+(4×1,0)+(3×1,0) = 21 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Veltrix observa e faz FinOps da inferência dos modelos de visão/liveness (custo por verificação, latência, roteamento). O copiloto explicável demonstra observabilidade aplicada a modelo de risco.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: explicabilidade de modelo de visão é notoriamente difícil — risco de "explicação" plausível mas não fiel; custo de inferência do LLM sobre cada caso; não mexe em soberania, então diferencia menos que a INI agêntica.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Onboarding & KYC]]
