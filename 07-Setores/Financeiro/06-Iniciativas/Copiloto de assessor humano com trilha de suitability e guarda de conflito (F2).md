---
tipo: iniciativa-ia
jornada: investimentos
arquetipo: copiloto
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 23
status: candidata
data: 2026-07-06
eixos: [financeiro, governanca, agentes]
tags: [iniciativa, backlog, vale, investimentos, advisor, copiloto, suitability, conflito-interesse, fase-2, expansao]
---

# 💡 Iniciativa — Copiloto de assessor humano com trilha de suitability e guarda de conflito de interesse (F2)

**Em uma frase:** _uma camada de governança embutida no copiloto GenAI que já assiste o assessor humano (modelo advisor-facing do Santander/Bradesco) — que registra por que cada produto foi recomendado, checa a adequação ao perfil em tempo real e sinaliza conflito de interesse (fundo da casa) — transformando o copiloto do assessor em copiloto auditável._

## 🎯 O gap que origina isto
<!-- Puxa do de-para: nível atual vs líder, o vale identificado. -->
- Jornada: Investimentos & advisor (Fase 2) · Nível atual (EMA-J): **L4** (copiloto GenAI do assessor) · Alvo: **L4** (mesmo nível, com trilha+guarda) · Gap: 0 no nível, mas **sem rastreabilidade da recomendação nem guarda de conflito**.
- Do de-para: o líder da expansão (Santander) e o do piloto (Bradesco) escolheram o modelo **advisor-facing** (humano no loop como fusível de conformidade). O que falta a eles não é mais IA — é **trilha de suitability + guarda de conflito** dentro do copiloto que já têm. Distingue-se do trio do piloto: o **Copiloto de recomendação explicável (piloto)** é *client-facing*; este é *advisor-facing* (copiloto do assessor humano), com foco em MRR/rastreabilidade e checagem de suitability em tempo real.

## 🏗️ Arquétipo e desenho
**Copiloto (human-in-the-loop) com governança embutida.** Sobre o copiloto do assessor: (1) **trilha de recomendação (MRR)** — cada sugestão do copiloto grava insumo, modelo, versão e justificativa (por que este produto, para este perfil); (2) **checagem de suitability em tempo real** — antes de o assessor enviar, o copiloto valida a recomendação contra o perfil do investidor e sinaliza descolamento (advisory dinâmico sobre suitability estático); (3) **guarda de conflito de interesse** — sinaliza quando o produto recomendado é da própria casa e exige registro de alternativa considerada. Não substitui o assessor; torna a recomendação dele **defensável perante CVM/Bacen**.

## 📊 Placar VALE
<!-- Notas 1–5. Ver [[Placar VALE — Priorizacao de Iniciativa de IA]] -->
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Reduz passivo supervisório e retrabalho de compliance; habilita escala do advisory advisor-facing sem estourar risco. Valor de "licença para operar", não de receita direta → 4. |
| A — Aderência governança/soberania | 5 | 2,0 | É governança pura: rastreabilidade da recomendação + suitability + conflito de interesse. Núcleo do eixo A (CVM Res. 30/179, dever fiduciário). |
| L — Lastro técnico/viabilidade | 4 | 1,0 | O copiloto do assessor já existe (Santander/Bradesco); adicionar trilha+guarda é camada de metadados/regra sobre o que já roda. Viável. |
| E — Encaixe Veltrix/Cohort | 3 | 1,0 | Encaixa em Cohort (governança/mandato de agente) na trilha e na guarda, mas o copiloto é human-in-the-loop, não agente autônomo → encaixe parcial, 3. |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(3×1,0) = 23 / 27,5** → faixa: **Proposta agora**

## 🧪 Laboratório vivo
Cohort aplicado ao copiloto: a trilha de recomendação e a guarda de conflito são o mesmo primitivo de **mandato/rastreabilidade** que o Cohort usa para agentes autônomos, aqui sob um humano. Vira a ponte narrativa "governança de copiloto hoje → governança de agente amanhã": o mesmo cliente que compra a trilha do copiloto está pré-adotando o mandato do advisor agêntico (L5) quando a regulação permitir.

## ⚠️ Contraponto real
Valor **defensivo** (evita multa/passivo), o mais difícil de vender a um board que quer receita. Depende de o cliente já ter o copiloto advisor-facing rodando (Santander/Bradesco sim; C6/PicPay ainda não no advisory). Risco de ser visto como "compliance encarecendo o processo" se não mostrar que a trilha também **acelera** a aprovação da recomendação. Encaixe em Cohort é parcial (é copiloto, não agente).

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina propôs e pontuou; a tese e o contraponto são seus.)

---
**Liga com:** [[De-Para — Investimentos & advisor (Fase 2 · expansão)]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[MRR - Matriz de Rastreabilidade da Recomendacao]] · [[Copiloto de recomendação explicável com guarda de conflito de interesse]] (piloto, client-facing)
