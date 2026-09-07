---
tipo: iniciativa-ia
jornada: pagamentos-pix
arquetipo: reimaginacao-agentica
maturidade_atual: L4
maturidade_alvo: L5
score_vale: 25
status: candidata
data: 2026-07-05
eixos: [financeiro, governanca, agentes, soberania]
tags: [iniciativa, backlog, vale, fase-2, pagamentos, adquirente, merchant, agentic]
---

# 💡 Iniciativa — Trilho de pagamento agêntico soberano para adquirentes

**Em uma frase:** Uma camada de **mandato governado** (escopo, limite, trilha, residência de dado) sobre o pagamento agêntico do lado do **lojista/adquirente** — Getnet, PagBank, Stone —, transformando a maquininha por voz (L4) e o trilho de Pix agêntico de terceiro em agente que cobra/concilia/antecipa sob governança própria (L5).

## 🎯 O gap que origina isto
- Jornada: Pagamentos & Pix (merchant/acquiring) · Nível atual (EMA-J): **L4** (POS por voz: Getnet, Minizinha Voz) · Alvo: **L5** (agente sob mandato) · Gap: **1** nível — mas o mandato L5 hoje é de **terceiro** (Iniciador), não do adquirente.
- Puxa do de-para F2: os adquirentes subiram ao L4 no lado do lojista e são **clientes** do trilho de Pix agêntico, não donos da governança do mandato. O piloto olhou o consumidor; este é o lado que ninguém governou.

## 🏗️ Arquétipo e desenho
**Reimaginação agêntica (merchant-side).** O agente do lojista deixa de só "entender a cobrança por voz" e passa a **executar rotinas de caixa sob mandato**: cobrar, conciliar recebíveis, antecipar quando o custo de capital compensa, disparar cobrança via WhatsApp — cada ação com escopo (que operação), limite (teto por dia/transação), trilha (log auditável) e residência (onde o dado roda). O trilho de execução pode ser o Pix agêntico de terceiro; a **camada de mandato e auditoria é própria**.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Adquirência move volume alto e recorrente; antecipação/cobrança automatizada é receita direta; agentic commerce crescendo. |
| A — Aderência governança/soberania | 5 | 2,0 | Mandato de agente + trilha auditável + residência de dado no fluxo financeiro do lojista — núcleo de governança; hoje inexistente do lado merchant. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Base L4 já existe (POS por voz) e o trilho Pix agêntico já opera (Iniciador); falta a camada de governança, não a execução. |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Cohort = mandato/frota de agentes do lojista; Veltrix = FinOps + roteamento da inferência por trás da cobrança por voz. Encaixe duplo. |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 25 / 27,5** → faixa: **candidata a proposta agora (≥20)**

## 🧪 Laboratório vivo
Cohort demonstra a **frota de agentes de cobrança/conciliação do lojista** com mandato explícito (escopo/limite/trilha); Veltrix demonstra o **custo de inferência por transação da maquininha por voz** e o roteamento por jurisdição do dado de venda. É o caso merchant do que o piloto propôs no consumidor.

## ⚠️ Contraponto real
O mandato de execução (Pix agêntico) é hoje de terceiro (Iniciador) e já regulado — o adquirente pode preferir **consumir o trilho** a governá-lo, e a camada de governança própria só se paga se houver volume e passivo regulatório que justifiquem. Risco de virar "governança em cima de trilho alheio" sem controle da ponta de execução. Custo de inferência do POS por voz em escala de milhões de lojistas é linha de P&L real.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina propõe o desenho e o número; a tese e o serviço são seus.)
Insumo: dois adquirentes lançaram POS por voz na mesma janela (Getnet, Minizinha Voz) e Stone/PagBank já são clientes do trilho de Pix agêntico — o lado merchant subiu ao L4 e terceirizou o L5. Quem governar o mandato do lado do lojista (não só do consumidor) captura a camada que o trilho não entrega.

---
**Liga com:** [[De-Para — Pagamentos & Pix (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[INI-Pix-Agentico-Governado-Mandato]] (par consumer do piloto)
