---
tipo: framework
data: 2026-07-02
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-01]]"
eixos: [soberania, financeiro, agentes, economia-ia]
tags: [framework, auto]
---

# 🧱 Roteamento de Trilho do Agente de Pagamento (SRC) — Soberania, Reversibilidade, Custo

## O problema que ele resolve
Quando o agente inicia pagamento, surge uma pergunta que não existia enquanto ele só recomendava: **por qual trilho o dinheiro corre** — Pix, stablecoin ou cartão? Deixar a resposta no *default* do fornecedor de infra (Fireblocks/x402 tendem a stablecoin em dólar; a Iniciador, a Pix) é entregar a decisão de soberania monetária e de residência de transação por omissão. O ELJT ([[Mandato do Agente - escopo, limite, jurisdicao, trilha]]) diz *se* o agente pode pagar e até quanto; ele não diz *por onde*. Esse framework preenche exatamente esse vão — é a política de roteamento que decide o trilho antes de o agente mover R$ 1.

## O framework
Todo pagamento iniciado por agente é roteado por **três perguntas — SRC** — decididas por política, não pelo default do fornecedor:

- **S — Soberania:** em que moeda e sob qual jurisdição a transação precisa residir? Dado sensível ou cliente sob enforcement local → trilho soberano (Pix, real, Bacen). Necessidade real de liquidez cross-border → stablecoin, com o custo de residência assumido conscientemente.
- **R — Reversibilidade:** o pagamento precisa ser revertível? Pix é instantâneo e **irrevogável** (bom para custo, ruim para fraude por manipulação do agente); cartão tem chargeback; stablecoin, conforme a rede. Quanto maior o valor ou o risco de desvio, mais peso para o trilho reversível.
- **C — Custo:** o custo total do trilho = taxa da rede + **custo de inferência da chamada do agente**. Aqui SRC encosta no Veltrix: o mesmo FinOps por agente que mede inferência mede o custo por trilho — roteamento barato no escuro é gasto no escuro.

A saída é uma matriz simples (agente × trilho recomendado × condição), legível por um board: *"para este tipo de pagamento, o default é Pix; stablecoin só sob exceção justificada por liquidez cross-border."*

## Quando usar / quando NÃO usar
**Usar:** ao promover à produção qualquer agente que possa iniciar pagamento; ao avaliar fornecedor de infra de pagamento agêntico (o roteamento é meu ou é o default dele?); ao desenhar política de dado/jurisdição — SRC adiciona a linha "residência de transação" ao one-pager de residência de dado.
**Não usar:** em agente que só recomenda/consulta e não move valor — aí não há trilho a rotear, e SRC vira burocracia. É o portão do *agente que paga*, não de todo agente.

## Aplicado na prática
No **Veltrix**, SRC é a extensão natural do roteamento por jurisdição/sensibilidade da inferência para o roteamento do *pagamento*: a mesma disciplina que escolhe qual modelo/sandbox atende por jurisdição escolhe qual trilho liquida por soberania e custo. No **Cohort**, SRC compõe com o eixo J (jurisdição) do ELJT: o mandato autoriza o agente a pagar; o SRC define por onde — juntos, respondem "pode pagar, até quanto, e por qual trilho soberano".

## Como cito isto num board
"Nenhum agente paga no default do fornecedor: cada pagamento é roteado por Soberania, Reversibilidade e Custo — SRC. É o que impede que a escolha entre Pix e dólar seja tomada por omissão de arquitetura."
