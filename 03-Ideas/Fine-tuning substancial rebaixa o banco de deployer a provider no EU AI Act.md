---
tipo: ideia
data: 2026-08-02
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-02]]"
eixos: [governanca, financeiro, soberania]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Fine-tuning substancial ou rebranding de um GPAI move o banco da cadeira de deployer para a de provider — e a multa de 3% muda de dono junto

## A tese
No EU AI Act, a fronteira **provider × deployer** não é jurídica, é de arquitetura: o banco que só consome um GPAI (general-purpose AI) via API é deployer e fica fora do enforcement de hoje; o banco que faz **fine-tuning substancial**, rebatiza o modelo ou o distribui como seu pode ser **reclassificado como provider** e herdar as obrigações do lab — inclusive a multa de até **3% do faturamento global ou €15 mi** que passou a valer em 02/08/2026. Ou seja: a decisão técnica de "quanto eu mexo no modelo" é, na verdade, a decisão de **qual lado da multa eu ocupo**.

## Por que eu acredito nisso
O enforcement do Capítulo V ativou hoje mirando providers, com teto de **3% ou €15 mi** *(EU AI Act, Art. 101 · [artificialintelligenceact.eu](https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/); daily 2026-08-02)*. Mas a fronteira é porosa: a própria daily de hoje ("Aprendizado do dia — provider vs deployer") registra que fine-tuning substancial ou rebranding reclassifica o usuário em provider. A maioria dos times de banco assume que "somos só usuários" — e essa resposta é intuitiva, não jurídica. Quem quer **modelo no próprio dado** (soberania) tende justamente a fine-tunar; é o caminho que mais aproxima o banco da cadeira de provider sem que ninguém tenha decidido isso conscientemente.

## Quem discordaria — e por quê
Um jurista diria que "substancial" é vago e que, na prática, nenhum banco BR vira provider tão cedo — o risco seria teórico enquanto a AI Office prioriza os grandes labs. Faz sentido no curto prazo. O contraponto ao contraponto: o ponto não é a multa amanhã, é que a **escolha fine-tune vs proxy/RAG** carrega um perfil regulatório que hoje ninguém precifica — e retrofitar governança de provider numa base já consolidada é caro, como o próprio caso do Art. 50 mostra.

## O que eu faria / recomendaria
Tratar "fine-tune vs proxy/RAG" como **decisão de perfil regulatório**, não só técnica. Manter um registro de **grau de modificação por modelo** (consumo puro / RAG / fine-tuning leve / fine-tuning substancial / rebranding) e marcar em qual ponto o banco cruza para provider. Um proxy que roteia para o GPAI sem alterá-lo substancialmente (Veltrix) preserva de propósito a fronteira de deployer e mantém a opção de multi-provider; fine-tuning pesado ou modelo rebatizado deve ser escolha consciente de assumir obrigações de provider, não efeito colateral de um roadmap de ML. Conecta a [[Soberania de dado virou tese competitiva - o ativo do banco e o modelo no proprio dado]]: a soberania cobra fine-tuning, e o fine-tuning cobra o passivo de provider — o trade-off precisa ir ao board explícito.

## Lastro
- Daily [[2026-08-02]] — "Aprendizado do dia: provider vs deployer" e enforcement do Cap. V.
- [artificialintelligenceact.eu — enforcement Cap. V](https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/)
- [Comissão Europeia — guidelines GPAI providers](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)
- Relacionadas: [[Enforcement de GPAI do EU AI Act vira risco de continuidade herdado pelo banco]] · [[Soberania de modelo virou risco de continuidade, nao tese]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança  ·  **Setor:** financeiro (banking)
