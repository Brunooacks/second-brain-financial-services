---
tipo: iniciativa-ia
jornada: fraude
fase: 2
arquetipo: modernizacao
maturidade_atual: L3
maturidade_alvo: L4
score_vale: 25.0
status: candidata
data: 2026-07-05
eixos: [financeiro, governanca, soberania, economia-ia, agentes]
tags: [iniciativa, backlog, vale, fraude, finops, veltrix, soberania, fase-2]
---

# 💡 Iniciativa — Camada FinOps + roteamento por jurisdição de inferência antifraude (Fase 2)

**Em uma frase:** Uma camada que mede, otimiza e roteia (por jurisdição) o custo de inferência do **monitoramento antifraude obrigatório** (Res. BCB 403) — porque o piso regulatório que nivelou a detecção transformou "chamar modelo a cada transação" em item de custo E de soberania, sobretudo nos adquirentes de alto volume.

## 🎯 O gap que origina isto
- Jornada: Prevenção a fraude & disputas (Fase 2) · Nível atual (EMA-J): **L3** (detecção comoditizada por decreto) · Alvo: **L4** (detecção governada e economicamente medida) · Gap: 1 nível de governança/custo, não de função
- O vale do de-para: a Res. 403 obriga **todo** participante do Pix a monitorar antifraude → a detecção virou piso legal. Mas ninguém expõe o **custo por transação** desse piso, e o Santander já declara stack multimodelo (OpenAI/Claude/Gemini + **G42/Abu Dhabi**) — roteamento de dado de fraude por fornecedor sob outra jurisdição.

## 🏗️ Arquétipo e desenho
**Modernização** (com núcleo de soberania). Camada entre o motor antifraude e os modelos que:
1. **Mede** o custo de inferência por transação, por modelo e por SD (Fraud Evaluation/Decisioning/Authorization) — FinOps do piso 403.
2. **Roteia** cada chamada ao modelo certo pelo par custo×risco×**jurisdição do dado** — transação sensível não sai da residência exigida; carga barata vai ao modelo mais econômico.
3. **Governa**: trilha de qual modelo viu qual dado, sob qual jurisdição, com que custo — auditável para o supervisor.
Não substitui o motor de detecção (que é commodity regulatória); torna o piso obrigatório **econômico e defensável**.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Custo evitado real: o monitoramento é obrigatório e roda em toda transação; em adquirente de alto volume (PagBank/Stone) o custo de inferência escala com o TPV. Valor indireto (custo, não receita), por isso não é 5. |
| A — Aderência governança/soberania | 5 | 2,0 | Roteamento por jurisdição + residência de dado de fraude + trilha de proveniência = núcleo puro de soberania. O caso G42 no Santander é a prova viva. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Veltrix já faz FinOps e roteamento de inferência; o antifraude é caso de uso direto, dado transacional disponível. |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | É Veltrix em estado puro (proxy de LLM, FinOps, observabilidade, roteamento por jurisdição). |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 6,0+10,0+4,0+5,0 = 25,0 / 27,5** → faixa: **candidata a proposta agora (≥20)**

## 🧪 Laboratório vivo
Veltrix é a própria camada: mede custo de inferência do antifraude por transação/modelo/SD, roteia por jurisdição (método CARO), e emite a trilha de proveniência que o supervisor pede. Demonstra que FinOps de inferência e soberania de dado são o mesmo produto quando a detecção vira obrigação legal.

## ⚠️ Contraponto real
O ganho é de custo/soberania, não de eficácia de detecção — um board focado em "pegar mais fraude" pode ver como otimização de back-office, não como prioridade. E o roteamento por jurisdição adiciona latência: em autorização antifraude em tempo real, cada milissegundo conta; se a camada atrasar a decisão, cria fricção no pagamento. Precisa provar que o overhead de governança cabe no orçamento de latência da transação.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina estruturou a candidata; a tese e o serviço são seus.)

---
**Liga com:** [[De-Para — Prevenção a fraude & disputas (Fase 2 · expansão)]] · [[Roteamento por jurisdição de dado de pagamento multimodelo — o caso G42 (F2)]] · [[Camada FinOps e roteamento de inferência de crédito multi-fornecedor (F2)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]]
