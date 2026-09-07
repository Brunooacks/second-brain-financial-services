---
tipo: iniciativa-ia
jornada: pagamentos-pix
arquetipo: modernizacao
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 24
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, pagamentos, pix, finops, veltrix, custo-inferencia]
---

# 💡 Iniciativa — FinOps de inferência para Pix conversacional em escala

**Em uma frase:** Uma camada de FinOps e roteamento (método CARO) que coloca custo, latência e jurisdição do modelo sob controle quando o LLM passa a estar no caminho de **cada** transação de Pix por voz/texto/imagem — transformando custo de inferência por transação de despesa invisível em linha de P&L governada.

## 🎯 O gap que origina isto
- Jornada: Pagamentos & Pix · Nível atual (EMA-J): **L4** (Pix conversacional em escala: Nubank 10 mi MAU, BB 20 mi no canal WhatsApp) · Alvo: **L4** (mesmo nível, muito mais eficiente e governado) · Gap de eficiência/governança, não de capacidade. Bradesco já expõe o número: **−60% de custo por transação** no Pix Inteligente. Ver [[De-Para — Pagamentos & Pix]].

## 🏗️ Arquétipo e desenho
**Modernização (economia de IA).** Cada "manda 50 pro Fulano" chama um modelo — com 10–20 milhões de usuários, o custo de inferência por transação vira material. A iniciativa instrumenta esse caminho: mede custo/latência por transação, roteia entre modelos por custo e por jurisdição (dado sensível de pagamento não sai da residência exigida), e dá ao board um painel de FinOps de IA transacional. Não muda o que o usuário vê; muda a economia e a soberania de quem opera.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Custo evitado direto e mensurável (Bradesco −60%/transação); a escala (30,1 bi de Pix/ano no país) transforma centavos por chamada em milhões |
| A — Aderência governança/soberania | 4 | 2,0 | Roteamento por jurisdição e residência de dado de pagamento; auditabilidade de custo. Eixo é mais economia que soberania pura — nota honesta 4 |
| L — Lastro técnico/viabilidade | 5 | 1,0 | É o core do Veltrix (proxy de LLM com FinOps/observabilidade); tecnologia madura, baixo risco regulatório |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | É literalmente o caso de uso canônico do Veltrix aplicado ao pagamento — vitrine viva do método CARO |

**Score VALE = (4×1,5)+(4×2,0)+(5×1,0)+(5×1,0) = 24 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Veltrix é o produto: proxy de LLM que mede custo por transação de Pix conversacional, roteia por custo/jurisdição e observa latência. O Pix conversacional em escala é a prova de que FinOps de inferência não é teoria — é diferença entre margem e prejuízo quando o modelo está em cada transação.

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: FinOps de inferência é "vitamina", não "analgésico" — cliente compra sob pressão de margem, não de dor aguda; risco de virar dashboard bonito sem decisão associada; o ganho depende do volume conversacional realmente escalar. Se não fecha o contraponto, é slogan.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Pagamentos & Pix]] · [[FinOps de inferência nos motores de crédito]]
