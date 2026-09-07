---
tipo: ideia
data: 2026-07-08
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-07]]"
eixos: [governanca, soberania, seguranca, fronteira, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 O "scratchpad" exposto é feature de fornecedor, não trilha de auditoria de agente

## A tese
Expor o rascunho do modelo (scratchpad / chain-of-thought) não torna o agente auditável. É uma feature do fornecedor — que ele pode remover — e um artefato cuja fidelidade não está garantida: o rascunho mostrado pode não corresponder ao processo real que gerou a decisão. Para um banco, auditabilidade de agente exige rastro verificável, versionável e capturado por mim; não a boa vontade do lab em mostrar o raciocínio. Visibilidade não é verificabilidade.

## Por que eu acredito nisso
A daily de 07/07 (cluster 🔭 No Radar) trouxe o sinal: a Anthropic lançou a família **"Fable"** — que a AINews classificou como "o lançamento mais significativo até hoje" — e detalhou o **scratchpad (chain-of-thought)** que o Claude usa antes de responder (AINews/Smol AI; The Neuron, 06–07/07). O ângulo de board embutido na própria daily foi otimista: "modelo que mostra o rascunho é modelo que se governa". É aqui que eu discordo. Interpretabilidade exposta é avanço real, mas a discussão de fidelidade de chain-of-thought (CoT faithfulness) mostra que o rascunho pode ser uma racionalização pós-hoc, não o cálculo que de fato decidiu — e, sendo feature do provedor, some quando ele muda o produto. Num agente que escreve código para produção ou recomenda crédito, "ver o raciocínio" só vira auditoria se esse rastro for capturado, imutável e independente do humor do fornecedor. *(Item de fronteira, sem número citável na daily — registro a ausência em vez de inventar dado.)*

## Quem discordaria — e por quê
Um head de risco pragmático diria que CoT visível é um salto de auditabilidade frente à caixa-preta anterior, e que exigir "fidelidade provada" e "captura própria" antes de aproveitar isso é deixar o ótimo ser inimigo do bom — melhor um rascunho imperfeito e visível que nada. É verdade parcial. Mas aceitar o scratchpad do fornecedor como trilha de auditoria é o mesmo erro de aceitar "ROI de IA" por autorrelato: confunde o que o modelo *diz* que pensou com prova do que efetivamente decidiu.

## O que eu faria / recomendaria
Tratar interpretabilidade como insumo, nunca como controle. O rastro de decisão do agente — raciocínio + entradas + ferramenta chamada + saída — tem que ser capturado pela minha plataforma/harness, fora do provedor, para sobreviver a troca de modelo e a corte de feature. É **Cohort** em estado puro (trilha de auditoria do agente independe do lab) e conecta a [[Soberania pratica de IA nao esta no modelo esta em quem controla o harness]] (quem controla o harness controla o rastro) e a [[Governanca de agente que importa pra banco fica acima do provedor]] (a governança fica acima do fornecedor, não dentro dele). Métrica de board: **% de decisões de agente com rastro verificável capturado fora do fornecedor** — não "nosso modelo mostra o raciocínio".

## Lastro
- Daily-fonte: [[2026-07-07]] (cluster 🔭 No Radar — Anthropic "Fable" + scratchpad/chain-of-thought)
- AINews/Smol AI — lançamento "Fable" (07/07); The Neuron — Claude scratchpad (06–07/07)
- Debate de fidelidade de chain-of-thought (CoT faithfulness) como contexto de fronteira
- Conexão: [[Soberania pratica de IA nao esta no modelo esta em quem controla o harness]] · [[Governanca de agente que importa pra banco fica acima do provedor]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança / soberania  ·  **Setor:** transversal (aplica a financeiro)
