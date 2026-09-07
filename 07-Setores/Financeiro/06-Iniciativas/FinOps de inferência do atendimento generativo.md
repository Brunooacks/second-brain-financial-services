---
tipo: iniciativa-ia
jornada: atendimento
arquetipo: modernizacao
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 23
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, economia-ia, agentes]
tags: [iniciativa, backlog, vale, atendimento, finops, inferencia, veltrix]
---

# 💡 Iniciativa — FinOps de inferência do atendimento generativo

**Em uma frase:** Uma camada de roteamento + observabilidade de inferência que decide **qual modelo responde cada atendimento** por custo, sensibilidade e jurisdição, para operações de atendimento generativo que já rodam em escala de dezenas de milhões de interações.

## 🎯 O gap que origina isto
- Jornada: Atendimento & cobrança (Contact Dialogue / Contact Center Operations) · Nível atual (EMA-J): **L4** · Alvo: **L4 otimizado** · Gap: **0 em maturidade, aberto em eficiência**
- O vale do de-para: a 25 mi de interações (Bradesco) e 2 mi de chats/mês (Nubank), o **custo de inferência do atendimento virou linha de P&L**. A escolha de modelo já é decisão de custo — o Nubank usa GPT-4o mini para o barato, a Bridge do Bradesco é multi-modelo. Falta a camada que **governa essa decisão com número**.

## 🏗️ Arquétipo e desenho
**Modernização (FinOps de inferência).** Um proxy que classifica a intenção e o risco de cada atendimento e roteia para o modelo certo: modelo pequeno/barato para FAQ, modelo grande só quando o caso exige, modelo em jurisdição específica quando o dado é sensível/regulado. Mede custo por atendimento resolvido, desvio de qualidade e residência de dado por rota. Transforma "qual LLM usamos" de decisão de arquitetura única em **política observável e auditável** por tipo de interação.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Custo de inferência a dezenas de milhões de interações é P&L real; ganho direto de margem sem perder resolutividade |
| A — Aderência governança/soberania | 4 | 2,0 | Roteamento por jurisdição/sensibilidade e observabilidade de dado por rota são governança pura, mas o foco primário é custo |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Proxy de roteamento de LLM é maduro e provado; o dado de atendimento já existe |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | É a tese de Veltrix (proxy de LLM com FinOps e observabilidade, método CARO) aplicada a atendimento — laboratório vivo |

**Score VALE = (4×1,5)+(4×2,0)+(4×1,0)+(5×1,0) = 23 / 27,5** → faixa: **Proposta agora (≥20)**

## 🧪 Laboratório vivo
Veltrix é a iniciativa: proxy de LLM com FinOps e observabilidade. O atendimento generativo em escala é o caso de uso onde o custo por token é visível e o roteamento por jurisdição vira diferencial de soberania. Métrica de sucesso: custo por atendimento resolvido ↓ sem queda de resolutividade.

## ⚠️ Contraponto real
Roteamento agressivo para o modelo barato degrada a experiência se a classificação de intenção errar — e um atendimento ruim custa mais em churn do que economiza em token. O contraponto é o **trade-off qualidade × custo**: sem medir a resolutividade por rota, o FinOps vira corte cego. Além disso, é uma venda de eficiência, não de receita nova — precisa de um baseline de custo atual para provar o ganho.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A priorização a máquina calculou; a tese e o serviço proposto são seus.)

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Atendimento & cobrança]] · [[INI-FinOps-Inferencia-Pix-Conversacional]]
