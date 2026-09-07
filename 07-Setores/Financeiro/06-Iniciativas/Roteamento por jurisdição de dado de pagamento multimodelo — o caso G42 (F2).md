---
tipo: iniciativa-ia
jornada: pagamentos-pix
arquetipo: modernizacao
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 23.5
status: candidata
data: 2026-07-05
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, fase-2, pagamentos, soberania, residencia-dados, veltrix]
---

# 💡 Iniciativa — Roteamento por jurisdição de dado de pagamento multimodelo (o caso G42)

**Em uma frase:** Uma camada que decide **qual modelo, em qual jurisdição** processa cada chamada de GenAI no fluxo de pagamento conversacional — transformando o stack multimodelo (OpenAI + Claude + Gemini + G42/Abu Dhabi) de risco de **residência de dado** em controle explícito de soberania E de custo.

## 🎯 O gap que origina isto
- Jornada: Pagamentos & Pix (interpretação/intenção por GenAI) · Nível atual (EMA-J): **L4** · Alvo: **L4** governado (não sobe nível; fecha o passivo de soberania) · Gap: 0 de maturidade, **∞ de governança** (ninguém expõe a camada).
- Puxa do de-para F2: Santander declara stack com **OpenAI + Claude + Gemini + G42 (Abu Dhabi)**. Dado de pagamento roteado a um modelo sob outra jurisdição é questão de **residência de dado**, não só de FinOps.

## 🏗️ Arquétipo e desenho
**Modernização com moldura de soberania.** Não muda a experiência de pagar; insere entre a intenção do usuário e o provedor de LLM um **roteador com política**: classifica a sensibilidade do dado (PII de pagamento, valor, contraparte), aplica regra de jurisdição (o que pode/não pode sair do país ou ir a fornecedor sob controle estrangeiro), escolhe o modelo por custo dentro do que é permitido, e registra a decisão em trilha auditável. FinOps e residência de dado no mesmo ponto de controle.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 3 | 1,5 | Valor é mais defensivo (custo evitado + risco regulatório mitigado) que gerador de receita; controle de custo de inferência é real, mas não move ativação. |
| A — Aderência governança/soberania | 5 | 2,0 | Núcleo puro do diferencial: residência de dado + roteamento por jurisdição sobre fornecedor fora do país (G42/Abu Dhabi). Não há caso mais nítido no país. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | É exatamente o que Veltrix faz (proxy de LLM com observabilidade); o stack multimodelo já existe em produção no Santander. |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Veltrix direto — proxy de LLM com FinOps, observabilidade e roteamento por política. Demonstração viva. |

**Score VALE = (3×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 23,5 / 27,5** → faixa: **candidata a proposta agora (≥20)**

## 🧪 Laboratório vivo
Veltrix É esta iniciativa: proxy que roteia por custo E por jurisdição, com observabilidade da chamada. O caso G42 (fornecedor de LLM sob controle de Abu Dhabi no stack de um banco brasileiro) é o exemplo de board que justifica a camada sem precisar de slide.

## ⚠️ Contraponto real
Roteamento por jurisdição adiciona latência e complexidade a um fluxo (pagar) que exige resposta instantânea — a política não pode custar a experiência. E a premissa depende de leitura regulatória: se o Bacen/LGPD não tratar o processamento por LLM estrangeiro como transferência internacional de dado sensível, o valor de conformidade encolhe e sobra só o argumento de custo. Precisa de base jurídica firme para não ser tese de vento.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina montou o desenho e o número; a leitura regulatória e a tese são suas.)
Insumo: um banco grande roda pagamento conversacional sobre quatro fornecedores de LLM, um deles sob jurisdição estrangeira (G42/Abu Dhabi). A pergunta de board não é "quanto custa a inferência", é "por onde passa o dado de pagamento do meu cliente e sob que lei". Veltrix responde às duas no mesmo ponto.

---
**Liga com:** [[De-Para — Pagamentos & Pix (Fase 2 · expansão)]] · [[Camada FinOps e roteamento de inferência de crédito multi-fornecedor (F2)]] · [[INI-FinOps-Inferencia-Pix-Conversacional]] (par de custo do piloto) · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
