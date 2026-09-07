---
tipo: ideia
data: 2026-08-24
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-24]]"
eixos: [governanca, seguranca, agentes, financeiro]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 O risco de dado em GenAI não é o prompt do shadow AI — é a autorização na recuperação (retrieval)

## A tese
O controle que o banco já tem (DLP no prompt, política de shadow AI) resolve o problema conhecido e barato. O risco que cresce é o oposto: o **sistema devolvendo** dado que o usuário — ou o agente — não deveria acessar. Isso é falha de **autorização na camada de recuperação (retrieval)**, não de comportamento humano. E quando quem recebe a resposta é um agente, some a última barreira: a pessoa que vê um dado que não devia estranha; o agente processa e segue.

## Por que eu acredito nisso
O Netskope Threat Labs reporta que, no Brasil, **64%** das violações de política em apps de GenAI envolvem **dado regulado** (registro financeiro, dado de cliente, contrato); depois vêm código-fonte (21%), senhas/chaves de API (9%) e PI (7%) — e em apps pessoais no trabalho (shadow AI) o dado regulado é **66%**. Mas o número que muda a curva é outro: o vazamento *downstream* — o sistema devolvendo o que não devia — **mais que dobrou em um ano, de 12 para 31 ocorrências semanais por organização**. Adoção que amplifica: **100%** das organizações usam GenAI, **88%** já usam plataformas de IA e **79%** adotam agentes para código *(Netskope Threat Labs · Brasil 2026, via [CISO Advisor](https://www.cisoadvisor.com.br/64-das-violacoes-com-ia-no-brasil-envolvem-dados-sensiveis/) e [TI Inside, 11/08/2026](https://tiinside.com.br/11/08/2026/violacoes-de-dados-mais-que-dobram-com-avanco-dos-agentes-de-ia/))*. Prompt e downstream são falhas diferentes com controles diferentes: prompt se resolve com DLP na saída do usuário; downstream se resolve com **autorização (permission inheritance) na camada de retrieval**. Um relatório que só traz a taxa de prompt está medindo metade do risco.

## Quem discordaria — e por quê
Que "12 → 31 por semana" é artefato de melhor detecção: quem instrumenta mais, enxerga mais, e o número subiu porque a lente melhorou, não porque o risco cresceu. Plausível e provavelmente em parte verdadeiro. Mas para um banco não muda a conduta: se você não sabe se o seu número é 12 ou 31, o seu é **desconhecido** — e desconhecido é o pior valor possível para reportar à ANPD.

## O que eu faria / recomendaria
Pedir ao time de segurança a taxa de **vazamento downstream**, separada da de prompt — se o relatório só tem a primeira, metade do risco não está sendo medida. No desenho, tratar *permission inheritance* na camada de RAG como controle de LGPD, não detalhe de arquitetura. É o ponto onde **Cohort** entra: agente que não estranha precisa de mandato e autorização por construção, porque não há barreira humana a jusante. E onde **Veltrix** conecta: roteamento por sensibilidade decide o que sequer pode ser recuperado por qual consumidor. Casa direto com o framework [[Censo do Corpus Exposto (RSJA) - Repositorio, Sensibilidade, Jurisdicao, Autorizacao]] — o "A" (Autorização) é exatamente esta lacuna.

## Lastro
- Netskope Threat Labs · Brasil 2026 — via [CISO Advisor](https://www.cisoadvisor.com.br/64-das-violacoes-com-ia-no-brasil-envolvem-dados-sensiveis/) e [TI Inside, 11/08/2026](https://tiinside.com.br/11/08/2026/violacoes-de-dados-mais-que-dobram-com-avanco-dos-agentes-de-ia/)
- Distinto de [[Shadow AI e dado sensivel cruzando a fronteira da funcao por um canal nao-governado]] (lá o foco é o dado que o humano injeta/exfiltra pelo prompt; aqui é o que o sistema devolve por falha de autorização).
- Adjacente a [[A defesa do agent estate saiu do perimetro para o canal lateral entre agentes]] (agente como consumidor sem estranhamento).

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança/segurança  ·  **Setor:** financeiro
