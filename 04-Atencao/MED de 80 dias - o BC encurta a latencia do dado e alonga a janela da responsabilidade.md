---
tipo: atencao
data: 2026-09-03
status: aberto
origem: auto-digest
fonte_daily: "[[2026-09-03]]"
horizonte: medio
eixos: [financeiro, governanca, agentes]
tags: [atencao, auto]
---

# ⚠️ MED de 80 dias: o BC está encurtando a latência do dado e alongando a janela da responsabilidade — provisão de reversão que ninguém modelou

## O sinal
Três movimentos do BC na mesma semana apontam para o mesmo vetor. Desde **1º/09**, o prazo para contestar uma devolução via **MED (Mecanismo Especial de Devolução)** do Pix passou de **30 para 80 dias** (Agência Brasil, 09/2026); o dado que levava até **45 dias** para chegar às consultas de birô de crédito passa a **7 dias úteis**; e Gilneu Vivan (BC) sinalizou que a agenda do Open Finance vai **dar mais peso à qualidade da entrada de dados**, com **208,79 milhões** de consentimentos ativos em 31/07/2026 (Let's Money, 02/09; Valor, 01/09). Padrão: dado mais fresco na entrada, responsabilidade contestável por mais tempo na saída.

## Por que monitorar
MED em 80 dias significa que uma transação "liquidada" fica **contestável por quase três meses** — para tesouraria e para qualquer agente que transaciona, é provisão de reversão que hoje ninguém carrega no balanço nem no modelo. Para o antifraude é o oposto: 80 dias é mais rótulo (*label*) e mais tempo para o modelo aprender. E a régua de qualidade é o item mais subestimado: no momento em que o BC publicar indicador de qualidade por participante, o agente que consome dado ruim vai errar **com nome e sobrenome do fornecedor**. Se isto evoluir, muda a conta de risco de todo fluxo Pix automatizado e o desenho de quem responde pelo dado que entra no modelo — direto no núcleo de soberania/governança.

## Gatilhos pra reavaliar
- O BC publicar **indicador de qualidade de dado por participante** (vira obrigação, não recomendação) — aí o agente que consome dado ruim é pontuado.
- Primeira disputa relevante de MED sobre transação **conduzida por agente** (Decolar/SOFIA-style) — quem responde pela reversão de uma venda agêntica?
- Tesouraria de algum bancão começar a **provisionar** a janela de 80 dias explicitamente — sinal de que o mercado precificou o risco.

## Atualizações
- 2026-09-03: nota criada a partir da daily. Pergunta a instrumentar (risco + tesouraria): **qual o valor em Pix recebido nos últimos 80 dias ainda contestável, e quanto passou por jornada automatizada?** Ninguém tem esse número hoje — é um campo de log, e o **Cohort** registra mandato por transação exatamente para respondê-lo. Distinta de [[MED 2.0 poe cronometro de 11 dias na fraude com deepfake - deteccao vira requisito de conformidade com prazo]] (aquela é o prazo de análise/detecção; esta é a janela de contestação e a assimetria latência × responsabilidade). Ver também [[O prazo de qualidade de dados e o gargalo real da governanca de IA bancaria]].
