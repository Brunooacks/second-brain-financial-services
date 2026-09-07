---
tipo: iniciativa-ia
jornada: atendimento
arquetipo: reimaginacao-agentica
maturidade_atual: L3
maturidade_alvo: L5
score_vale: 25.5
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, soberania, agentes]
tags: [iniciativa, backlog, vale, cobranca, delinquent-account-handling, mandato]
---

# 💡 Iniciativa — Cobrança agêntica governada sob mandato

**Em uma frase:** Um agente de negociação de dívida que conduz a cobrança ponta-a-ponta (contato → simulação → acordo → formalização) sob **mandato explícito** (escopo de desconto, limite de parcelamento, política por perfil/jurisdição) e **trilha auditável**, para bancos e fintechs com carteira inadimplente crescente.

## 🎯 O gap que origina isto
- Jornada: Atendimento & cobrança (Delinquent Account Handling) · Nível atual (EMA-J): **L3** · Alvo: **L5** · Gap: **até 2 níveis** vs o patamar agêntico (ninguém opera L5)
- O vale do de-para: o BB provou que negociação conversacional entrega número (+306% conversão, parcelas 33,17→14,22), mas ainda é regra + GenAI com humano no circuito. Ninguém tem o agente que **negocia sob mandato e formaliza com trilha**. E o valor está aqui: inadimplência de "neobancos" +163% em 4 anos.

## 🏗️ Arquétipo e desenho
**Reimaginação agêntica.** O agente recebe um mandato assinado pela política de crédito (faixa de desconto, nº máximo de parcelas, canais e horários permitidos por CDC/Lei 14.181, gatilhos de escalada humana). Conduz o diálogo, simula cenários dentro do mandato, fecha o acordo e emite o instrumento — cada ação com carimbo de escopo, limite consumido e proveniência de dado. Fora do mandato, escala para humano. A diferença para o estado da arte não é "conversar melhor": é **agir com autonomia limitada e auditável**.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 5 | 1,5 | Recuperação de crédito é o ponto de maior valor da jornada; inadimplência +163% em 4 anos; BB já mostrou +306% de conversão com a versão fraca |
| A — Aderência governança/soberania | 5 | 2,0 | Mandato + trilha + residência de dado + limites de contato (CDC, Lei do Superendividamento) são o coração do desenho, não enfeite |
| L — Lastro técnico/viabilidade | 3 | 1,0 | Base conversacional existe e está provada (BB); o salto é a camada de mandato/autonomia governada — factível, mas nova |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Cohort é exatamente governança de mandato de agente; caso de uso vivo |

**Score VALE = (5×1,5)+(5×2,0)+(3×1,0)+(5×1,0) = 25,5 / 27,5** → faixa: **Proposta agora (≥20)**

## 🧪 Laboratório vivo
Cohort define e fiscaliza o mandato do agente de cobrança (escopo, limite, jurisdição, trilha) — é a demonstração canônica do produto. Veltrix entra na observabilidade e no FinOps da inferência de cada negociação (custo por acordo fechado, roteamento de modelo por sensibilidade do caso).

## ⚠️ Contraponto real
Cobrança é o terreno de maior risco reputacional e regulatório do banco: um agente que erra desconto, contata fora de hora ou pressiona superendividado vira multa e manchete. O contraponto não é técnico, é de **responsabilidade**: quem responde pelo acordo que o agente fechou? Sem mandato juridicamente ancorado e trilha à prova de auditoria, a autonomia é passivo, não ativo. Custo de inferência por negociação também precisa fechar contra o valor recuperado.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A priorização a máquina calculou; a tese e o serviço proposto são seus.)

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Atendimento & cobrança]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]
