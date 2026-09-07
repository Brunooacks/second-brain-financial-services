---
tipo: iniciativa-ia
jornada: onboarding-kyc
fase: 2
arquetipo: insight
maturidade_atual: L3
maturidade_alvo: L5
score_vale: 23
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, soberania, agentes]
tags: [iniciativa, backlog, vale, onboarding, kyc, febraban, portabilidade, cohort, veltrix]
---

# 💡 Iniciativa — Portabilidade de KYC interbancária governada (sob a autorregulação Febraban)

**Em uma frase:** "Abrir conta uma vez": uma camada que permite **reutilizar KYC já verificado entre instituições** sob mandato, com residência de dados e trilha auditável, aproveitando a autorregulação Febraban (27/out/2025) que já obriga validação cruzada e reporte ao Bacen.

## 🎯 O gap que origina isto
- Jornada: Onboarding & KYC · Nível atual (EMA-J): **L3** · Alvo: **L5** · Gap: cada player refaz o KYC do zero; o compartilhamento interbancário de sinais (contas suspeitas) já existe na autorregulação, mas **a reutilização governada de identidade verificada, não**. Ver [[De-Para — Onboarding & KYC (Fase 2 · expansão)]].

## 🏗️ Arquétipo e desenho
**Insight (com salto agêntico).** Um agente de KYC opera sob mandato entre instituições: quando um cliente já foi verificado numa instituição participante, o agente reutiliza a verificação (com consentimento) em vez de refazer captura+liveness+cruzamento, e registra proveniência + jurisdição. O diferencial é **governar a reutilização de identidade privada entre custodiantes distintos** — o oposto de mais um silo de KYC.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Elimina KYC duplicado no setor (custo por verificação × milhões); acelera ativação — mas o valor é compartilhado, não capturável por um só player |
| A — Aderência governança/soberania | 5 | 2,0 | Consentimento, residência, roteamento por jurisdição e trilha entre custodiantes distintos — governança de dado sensível no seu caso mais difícil |
| L — Lastro técnico/viabilidade | 3 | 1,0 | Depende de padrão interbancário e cooperação regulatória (Febraban/Bacen); dependência externa reduz viabilidade no curto prazo |
| E — Encaixe Veltrix/Cohort | 4 | 1,0 | Cohort governa o mandato do agente de reutilização; Veltrix roteia por jurisdição e mede o custo evitado |

**Score VALE = (4×1,5)+(5×2,0)+(3×1,0)+(4×1,0) = 23 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Cohort demonstra o mandato do agente de KYC operando entre instituições (escopo, consentimento, limite, trilha); Veltrix prova o roteamento por jurisdição e o FinOps do custo de verificação evitado. É a governança de agente aplicada ao dado mais sensível — identidade compartilhada.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: depende de padrão setorial que não controlo; responsabilidade em cascata se um KYC reutilizado falhar; risco de concentração e de LGPD/finalidade no compartilhamento entre custodiantes. Se não fecha o contraponto, é slogan.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[De-Para — Onboarding & KYC (Fase 2 · expansão)]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] · [[Malha de inteligência antifraude com residência de dados]] (distinta: malha antifraude vs. reutilização de identidade)
