---
tipo: framework
data: 2026-07-03
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-03]]"
eixos: [governanca, financeiro, agentes]
tags: [framework, auto]
---

# 🧱 MRR — Matriz de Rastreabilidade da Recomendação

## O problema que ele resolve
Quando um agente de IA passa de *analisar gasto* para *recomendar onde colocar o dinheiro*, a única pergunta que Bacen/CVM vão fazer é: **"por que o agente recomendou isto a este cliente?"**. Disclaimer de "não é garantia" não responde — suitability (dever de adequação) exige adequação *demonstrável no rastro*, não uma ressalva no rodapé. A MRR é o one-pager que transforma cada recomendação de agente em um registro auditável, fechando a lacuna entre "o modelo sugeriu" e "consigo provar que foi adequado".

## O framework
Para **cada** recomendação emitida por um agente regulado, quatro registros obrigatórios:

1. **Fontes** — quais das bases consultadas efetivamente pesaram na sugestão (das 50 bases do Itaú, quais moveram o ponteiro).
2. **Suitability** — qual perfil de adequação foi aplicado (objetivo, capacidade e apetite de risco do cliente) e como ele restringiu o universo de opções.
3. **Alternativas descartadas** — o que foi considerado e *por que* não foi recomendado (a prova de que houve escolha, não sorteio).
4. **Confirmação** — o ponto de checkpoint humano/mandato: o agente pode recomendar, não pode executar sem confirmação.

Regra de arquitetura acoplada: a decisão nasce do **motor determinístico**, o LLM só conversa — a MRR só é preenchível se a camada de decisão for auditável fora do LLM ([[No agente de investimento o motor deterministico decide e o LLM so conversa]]).

## Quando usar / quando NÃO usar
**Usar** em todo agente que toque recomendação regulada ao cliente — investimento, crédito, cobrança. **Não usar** como burocracia em tarefa de baixo risco e não-regulada (resumo de extrato, categorização de gasto): ali a MRR vira atrito sem retorno de compliance. O gatilho é *consequência regulatória da decisão*, não sofisticação do agente.

## Aplicado na prática
No **Cohort**, a MRR é o schema de trilha por decisão que separa "pode conversar" de "pode decidir/executar" — e é critério de promoção de agente a produção. No **Veltrix**, cada linha da matriz carrega o custo de inferência associado (as 22 mil simulações por sugestão), unindo rastreabilidade regulatória e conta de FinOps num só registro. Complementa [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]: o Mandato diz o que o agente *pode* fazer; a MRR prova, caso a caso, que ele fez *bem*.

## Como cito isto num board
"Para cada recomendação do nosso agente registramos fonte, perfil de suitability, alternativas descartadas e ponto de confirmação humana — quando o regulador perguntar por que recomendamos isto a este cliente, a resposta já está no rastro, não no disclaimer."
