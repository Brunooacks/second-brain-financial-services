---
tipo: atencao
data: 2026-08-06
status: aberto
origem: auto-digest
fonte_daily: "[[2026-08-06]]"
horizonte: medio
eixos: [economia-ia, financeiro, soberania]
tags: [atencao, auto]
---

# ⚠️ Integração vertical dos labs derruba o preço por token — contrato plurianual de preço fixo envelhece mal

## O sinal
A Anthropic confirmou (05/08) a montagem de um time interno de design de chips (sob Clive Chan) para **co-projetar silício e modelo (hardware–software co-design)** com alvo declarado de cortar **~50% do custo de inferência por token**; a Samsung é sondada como fabricante e a empresa diz que não abandona Nvidia/AMD/AWS/Google — o chip próprio é mais uma camada (*SiliconANGLE · TechTimes, 05/08 — via [[2026-08-06]]*). O padrão importa mais que o anúncio: depois do TPU do Google, é o segundo lab de fronteira a puxar o custo por token para baixo **por integração vertical**, não só por otimização de modelo. A curva de preço de inferência é descendente por design — e agora os próprios fornecedores estão empurrando a queda.

## Por que monitorar
Se a curva cai por decisão dos labs, **compromisso plurianual de preço fixo por token envelhece mal**: quem assina hoje trava o preço de 2026 numa curva que o fornecedor planeja derrubar pela metade. Para o banco que está fechando contratos de LLM de 2–3 anos agora (esteira de agentes indo a produção), isso é passivo silencioso — paga em 2028 o preço de 2026. O ponto de board não é "o custo vai cair" (todo mundo sabe), é que **capturar essa queda exige processo — observabilidade por token e renegociação recorrente —, não planilha anual**. É o terreno do Veltrix (FinOps por inferência). Distinto de [[A escala chegou a conta ninguem reporta - custo por inferencia e o ponto cego do agent estate]] (lá o problema é o denominador de custo ausente; aqui é o **preço unitário caindo mais rápido que o ciclo de contrato**).

## Gatilhos pra reavaliar
- Anthropic (ou outro lab) publicar preço por token efetivamente menor depois do silício próprio entrar em produção — confirma a curva, não só a promessa.
- Primeiro banco/fintech BR que embutir cláusula de **repasse de queda de preço** ("most favored pricing" + janela de renegociação semestral) em contrato de LLM.
- Fechamento da parceria de fabricação (Samsung) — sinal de que o alvo de -50% saiu do slide.

## Atualizações
- 2026-08-06: nota criada a partir da daily. Contraponto honesto: alvo de -50% é **promessa de engenharia** — o TPU do Google levou anos até pagar-se; não se ancora business case em preço futuro. A disciplina defensável não é apostar na queda, é **desenhar o contrato para capturá-la se e quando vier**. Dado: -50% de custo por token (alvo Anthropic, TechTimes 05/08). Conecta a [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]] e a [[Demonstracao de Resultado de IA (VCAT) - Valor, Custo, Atribuicao, Trilha]].
- 2026-08-07: **3º sinal na mesma direção** (daily [[2026-08-07]]). A AMD anunciou (06/08) a compra da **Taalas** (Toronto, fundada 2023), que grava **os pesos do modelo direto nos transistores** (model-specific integrated circuits), eliminando o vai-e-vem de HBM que domina o custo de inferência; a Taalas captou **US$ 219 mi**, fechamento previsto p/ 4T26 (AMD Newsroom · Bloomberg · The Register, 06/08 — AINews chama de "inference inflection"). Confirma o padrão: TPU (Google) → silício próprio (Anthropic) → modelo gravado no chip (AMD/Taalas). Nova faceta pro banco: o silício dedicado é **imbatível em custo e péssimo em flexibilidade** — um chip que "é" o modelo congela a versão. Em crédito, onde o modelo muda por regulação, isso é feature e risco ao mesmo tempo — reforça a camada de roteamento (Veltrix) como árbitro de preço/modelo sem reescrever a aplicação. Gatilho novo: contrato de IA em renovação com **cláusula de repactuação de preço indexada a mercado** (ninguém está pedindo ainda).
- 2026-08-14: **contraprova do mesmo sinal** (daily [[2026-08-14]]). No mesmo dia o Google cortou o Gemini 3.7 Flash −50% (3,75) e a DeepSeek subiu o V4-Pro +10x — a curva não é só descendente, é **volátil nas duas direções**. E o preço do Flash é **promocional até 31/12/2026** (dobra p/ 7,50 em 01/01/2027). Desdobrei o lado inverso desta tese em [[Preco de IA virou imprevisivel - promo expira e orcamento de 2027 nasce furado]]: aqui o risco é travar preço numa curva que cai; lá é orçar sobre promo que sobe.
