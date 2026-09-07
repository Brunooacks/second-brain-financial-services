---
tipo: framework
data: 2026-07-07
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-07]]"
eixos: [economia-ia, agentes, governanca, financeiro]
tags: [framework, auto]
---

# 🧱 Régua de Produtividade Agêntica (BIH) — Baseline, Inferência, Human-in-the-loop

> Toda vez que um agente entrega "300% mais rápido" ou "18 dias em 14 horas", a régua BIH separa dado citável de métrica de vaidade. Se o ganho não passa pelas três colunas, não é FinOps — é torcida.

## O problema que ele resolve
O número de velocidade agêntica sem denominador é a "métrica de vaidade" da era dos agentes — o equivalente a "ROI de IA" sem custo de inferência. Casos como o do Itaú (ciclo de produto de **18 dias → ~14 h** 100% automatizado, **5 dias** híbrido; ganho de ~**300%** em squads de Seguros — TI Inside, 03/06/2026) impressionam no palco e não sobrevivem ao comitê de risco quando falta a linha de base. A BIH força a pergunta que o board deveria fazer antes de aplaudir: **300% contra o quê, a que custo, e com quanto humano no meio?**

## O framework
Para todo ganho de produtividade agêntica apresentado, exija **três colunas** ao lado do número:

- **B — Baseline (linha de base):** contra que processo e prazo o ganho foi medido? Sem o "de → para" honesto (ex.: 18 dias → 14 h), o percentual é solto. Baseline errado infla qualquer ganho.
- **I — Inferência (custo total):** qual o custo de inferência do ciclo agêntico — por caso de uso, incluindo retrabalho? Velocidade que multiplica chamadas caras pode destruir a economia que promete. É o terreno do Veltrix (medir a conta por trás do ganho).
- **H — Human-in-the-loop (% de intervenção):** que fração dos ciclos rodou 100% automatizada vs. híbrida (humano nas decisões críticas)? A razão automatizado:híbrido é o verdadeiro apetite de risco — 14 h sem humano é benchmark de laboratório; 5 dias com humano é produção governada.

Regra de leitura: um ganho só é "citável num board" quando as três colunas estão preenchidas. Falta uma → é sinal amarelo; faltam duas → é slogan.

## Quando usar / quando NÃO usar
**Usar:** ao avaliar qualquer case de produtividade agêntica no comitê (interno ou de concorrente), como filtro anti-hype e para comparar iniciativas entre squads/áreas. **Não usar** como métrica de acompanhamento contínuo do parque (para isso é o [[Placar do Parque de Agentes (FMC) - Frota, Mandato, Custo]]) nem para autorizar o que o agente pode fazer (isso é o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]). A BIH valida uma *alegação de ganho*; ela não governa o agente nem mede o estate.

## Aplicado na prática
No case do Itaú, a BIH transforma "300% / 14 horas" em três perguntas de board: **B** — 18 dias era o baseline real de ponta a ponta ou só de uma etapa? **I** — o custo de inferência dos agentes de PM+Tech Lead+dev cabe no ganho de prazo? **H** — quantos ciclos rodaram no modo "14 h" (sem humano) vs. "5 dias" (com humano nas decisões críticas)? A coluna I é Veltrix puro (observabilidade de custo por inferência); a coluna H conversa com Cohort (mandato e trilha do agente que agora escreve código de produção). Sem as três, o 300% é o mesmo tipo de fé que, segundo o rascunho do US Treasury, inflou a comparação com a dotcom ([[US Treasury alerta bolha de IA e concentracao de inferencia vira risco de balanco]]).

## Como cito isto num board
"Todo ganho de produtividade agêntica entra aqui com três colunas — baseline, custo de inferência e % de human-in-the-loop —; sem elas, não é FinOps, é torcida."
