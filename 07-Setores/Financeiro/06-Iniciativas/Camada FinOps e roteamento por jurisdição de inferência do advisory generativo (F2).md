---
tipo: iniciativa-ia
jornada: investimentos
arquetipo: modernizacao
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 25
status: candidata
data: 2026-07-06
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, investimentos, advisor, finops, veltrix, fase-2, expansao]
---

# 💡 Iniciativa — Camada FinOps + roteamento por jurisdição de inferência do advisory generativo (F2)

**Em uma frase:** _uma camada de FinOps e roteamento de inferência (Veltrix) sobre o advisory generativo — que é a conversa mais longa e cara do banco — roteando por complexidade da pergunta E por jurisdição do dado do cliente, para os players que já colocaram GenAI no advisory (Santander) ou vão colocar em escala (C6, PicPay)._

## 🎯 O gap que origina isto
<!-- Puxa do de-para: nível atual vs líder, o vale identificado. -->
- Jornada: Investimentos & advisor (Fase 2) · Nível atual (EMA-J): **L4** (advisory GenAI advisor-facing) · Alvo: **L4** (mesmo nível, camada de custo/soberania sob ele) · Gap: 0 no nível, mas **P&L de inferência inexistente/opaco** e **dado de investimento sem roteamento por jurisdição**.
- Do de-para: "advisory é a conversa mais longa e cara do banco"; Santander roda IA sobre stack multi-fornecedor (grupo inclui **G42/Abu Dhabi**, ver F2-3) → roteamento por jurisdição do dado de investimento **não é custo, é soberania**. C6 (35 mi) e PicPay (dezenas de milhões) vão levar advisory/assistente a escala de massa.

## 🏗️ Arquétipo e desenho
**Modernização (FinOps/observabilidade de inferência).** Camada horizontal entre o advisor generativo e os provedores de LLM: (1) **roteamento por complexidade** — pergunta simples de educação financeira vai a modelo barato, recomendação de carteira/cenário vai a modelo caro; (2) **roteamento por jurisdição** — dado sensível de investimento (patrimônio, posições, perfil) roteado a provedor/região conforme residência exigida (LGPD, e evitando exposição a fornecedor sob jurisdição estrangeira sensível); (3) **observabilidade de custo por interação consultiva** — custo por token vira linha de P&L por cliente/assessor. Não muda o nível EMA-J do advisor; torna-o **sustentável e soberano em escala**.

## 📊 Placar VALE
<!-- Notas 1–5. Ver [[Placar VALE — Priorizacao de Iniciativa de IA]] -->
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Advisory é a conversa mais longa/cara; controlar custo de inferência a dezenas de milhões de clientes move margem direto. Valor real, mas indireto (evita custo, não gera receita nova) → 4, não 5. |
| A — Aderência governança/soberania | 5 | 2,0 | Roteamento por jurisdição do dado de investimento = residência de dado + evita exposição a fornecedor sob jurisdição estrangeira (caso G42 no stack Santander). Núcleo do diferencial soberania. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Advisory GenAI já existe (Santander) e vem em escala (C6/PicPay); a camada é software de roteamento/observabilidade, viável com maturidade atual. |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | É **literalmente** o Veltrix (proxy de LLM com FinOps + observabilidade + roteamento por jurisdição). Demonstração viva perfeita. |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 25 / 27,5** → faixa: **Proposta agora**

## 🧪 Laboratório vivo
Veltrix é o produto. O advisory generativo é o caso de uso mais nítido para FinOps de inferência porque combina **volume** (massa), **conversa longa** (caro) e **dado sensível** (jurisdição) — os três eixos que o Veltrix endereça de uma vez. Vira o estudo de caso de referência: "quanto custa, em token, aconselhar um investidor por mês, e por que o roteamento por jurisdição é controle de conformidade além de custo".

## ⚠️ Contraponto real
Iniciativa de valor **indireto** (evita custo/reduz risco, não abre receita) — precisa de um advisory GenAI já rodando em volume para o ganho aparecer; com só o Santander em produção (advisor-facing, escala de assessor, não de massa), o volume ainda é modesto. O ganho de soberania (jurisdição) é forte na tese mas difícil de precificar num board acostumado a ROI direto. Risco de virar "camada de infra que ninguém vê" se não amarrada a um número de P&L.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina propôs e pontuou; a tese e o contraponto são seus.)

---
**Liga com:** [[De-Para — Investimentos & advisor (Fase 2 · expansão)]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Camada FinOps e roteamento por jurisdição de inferência do atendimento multiagente (F2)]]
