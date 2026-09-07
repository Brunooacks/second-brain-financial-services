---
tipo: ideia
data: 2026-07-28
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-28]]"
eixos: [financeiro, economia-ia, soberania]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Quando a conversa vira a tela inicial, o custo por conversa é o novo cost-to-income da interface

## A tese
Ao trocar o menu pela conversa como canal primário do app, o banco troca a métrica de eficiência da interface: o custo por interação (custo por conversa) vira o novo cost-to-income daquele canal — e só fecha conta com roteamento multi-provedor (model routing). Quem depende de um único fornecedor de LLM perde a alavanca.

## Por que eu acredito nisso
O Itaú lançou oficialmente o **ia.i** em 27/07: a IA deixa de ser recurso e passa a ser **a tela inicial** do app, começando com **~300 mil clientes** e indo para a base completa **até o fim de 2026** *(TI Inside, 27/07/2026)*. O dado que sustenta a jogada não é de produto, é de FinOps: plataforma própria multi-provedor (OpenAI, Anthropic, Google, AWS, modelos abertos e fechados) entrega **-65% no custo de GenAI** *(TI Inside, 27/07)*. Menu é custo fixo desprezível; conversa em escala de dezenas de milhões de clientes é custo variável de inferência — sem roteamento, o ia.i seria um centro de custo com boa UX.

## Quem discordaria — e por quê
Quem defende o fornecedor único diria que a complexidade operacional de orquestrar N modelos (avaliação, fallback, segurança, contrato) come o desconto de -65% e adiciona risco de qualidade inconsistente entre respostas. É um contraponto real: sem observabilidade de custo *e* de qualidade por rota, multi-provedor vira caixa-preta cara. A resposta não é "um modelo só", é instrumentar a rota.

## O que eu faria / recomendaria
Levar ao board o one-pager "custo por conversa": tratar o custo de inferência por interação como linha de cost-to-income do canal conversacional, com meta e baseline. A arquitetura que o Itaú diz ter construído internamente (roteamento multi-modelo + observabilidade de custo) é exatamente o que o **Veltrix** entrega como produto para quem não tem 5 anos e um exército de engenharia. O ia.i é o case de validação — usar como benchmark de "custo por conversa" em qualquer conversa com banco médio.

## Lastro
- TI Inside (Itaú ia.i, -65% GenAI, ~300 mil clientes), 27/07/2026
- Seu Dinheiro (guerra da principalidade), 27/07/2026
- Tecnoblog (ia.i, tela inicial), 27/07/2026
- NTT DATA — Banking AI Leaders' Playbook 2026, pág. 4 (52,5% dos líderes "movem rápido e lideram o mercado")
- Relacionadas: [[A diferenca entre o banco que ve ROI e o que so percebe e medir o custo da IA]] · [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]] · [[Demonstracao de Resultado de IA (VCAT) - Valor, Custo, Atribuicao, Trilha]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** economia-ia / FinOps  ·  **Setor:** Financeiro
