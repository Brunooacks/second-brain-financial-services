---
tipo: iniciativa-ia
jornada: credito
fase: 2
arquetipo: modernizacao
maturidade_atual: L3
maturidade_alvo: L4
score_vale: 23.5
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, soberania]
tags: [iniciativa, backlog, vale, credito, embedded-lending, adquirente, residencia-de-dado]
---

# 💡 Iniciativa — Motor de crédito embedded governado para adquirentes (residência de dado transacional)

**Em uma frase:** Uma camada de governança de modelo sobre o crédito lastreado em fluxo de vendas (Stone/PagBank), garantindo residência de dado transacional, auditabilidade e explicabilidade à medida que a carteira cresce mais rápido do que a governança — modernização para embedded lending de adquirente.

## 🎯 O gap que origina isto
- Jornada: Originação de crédito (F2) · Nível atual (EMA-J): **L3** · Alvo: **L4** · Gap vs líder do piloto: 1
- Vale do de-para: Stone dobrou a carteira de crédito (**+134,9% em 12 m**, R$ 2,836 bi em dez/2025) sobre ML de fluxo de vendas. Crédito embedded cresce sobre dado transacional mais rápido do que a governança do modelo — a dívida de explicabilidade e residência de dado escala junto com a carteira, e a inadimplência é o passivo.

## 🏗️ Arquétipo e desenho
**Modernização governada.** Mantém o motor de risco baseado em fluxo de vendas, mas envolve o modelo numa camada que: (a) fixa a **residência do dado transacional** por jurisdição; (b) versiona e audita o modelo a cada reprecificação mensal; (c) gera explicação da decisão de crédito no padrão exigível pelo Bacen. O diferencial não é o score — é provar governança proporcional à velocidade de crescimento da carteira.

## 📊 Placar VALE
Notas 1–5. Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 5 | 1,5 | Embedded lending é o vetor de crescimento do adquirente (Stone +134,9% de carteira); governar o risco protege o P&L direto. |
| A — Aderência governança/soberania | 4 | 2,0 | Residência de dado transacional + auditabilidade + explicabilidade; forte, mas é camada de governança de modelo, não trilho de soberania pura. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | O dado transacional já existe e o ML já roda; a camada de governança é acréscimo viável. |
| E — Encaixe Veltrix/Cohort | 4 | 1,0 | Cohort (mandato/trilha do modelo) + Veltrix (observabilidade); encaixe forte, não total. |

**Score VALE = (5×1,5)+(4×2,0)+(4×1,0)+(4×1,0) = 7,5+8,0+4,0+4,0 = 23,5 / 27,5** → faixa: **≥ 20 — candidata a proposta agora**

## 🧪 Laboratório vivo
Cohort governa o modelo de risco como um agente com mandato (escopo, limite, trilha) e Veltrix observa o comportamento em produção. O caso de uso é o adquirente que dobra a carteira: a demonstração é que dá para crescer 100%+ sem crescer a dívida de governança na mesma proporção.

## ⚠️ Contraponto real
⏳ **para o Bruno.** Insumos: (1) o adquirente pode ler governança como fricção que reduz aprovação e trava crescimento — a venda tem que provar que residência/auditoria não custam conversão; (2) o dado transacional é o fosso do próprio adquirente — expô-lo a uma camada externa é sensível; (3) sem uma exigência regulatória concreta batendo à porta, vira "nice to have" adiável.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina propôs e pontuou; a tese e o serviço são seus.)

---
**Liga com:** [[De-Para — Originação de crédito (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]]
