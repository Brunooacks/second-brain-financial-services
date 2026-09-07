---
tipo: framework
data: 2026-07-13
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-13]]"
eixos: [soberania, economia-ia, governanca, financeiro]
tags: [framework, auto]
---

# 🧱 Matriz de Roteamento de Inferência (SJC) — Sensibilidade, Jurisdição, Custo

## O problema que ele resolve
O board recebe a pergunta errada: **"nuvem ou on-premise?"** — decisão binária, ideológica, decidida por quem gritou mais alto (o CISO ou o CFO). O **JPMorgan** já respondeu de outro jeito: levou **parte** da inferência para dentro de casa (SambaNova, on-premise, SN40/SN50, Série F de US$ 1 bi a **US$ 11 bi de valuation**, 08/07/2026) **para os dados mais sensíveis, com trilha auditável** — e **continua rodando Anthropic e OpenAI** para o resto. Ou seja: **ele não escolheu on-premise, escolheu roteamento.** Faltava um one-pager que transformasse essa decisão binária numa política por requisição, auditável e legível em 30 segundos.

O [[Matriz Construir-Comprar-Parcear do Ativo de IA (DCS) - Dado, Custo, Soberania]] decide a **origem do ativo** (construir/comprar/parcear). O SJC decide, com o ativo já existindo, **onde cada chamada roda**.

## O framework
Toda chamada a modelo é roteada por **três perguntas — SJC** — decididas por política no barramento (AI gateway), nunca pelo default do fornecedor:

- **S — Sensibilidade do dado.** Que classe de dado entra no prompt? (público / interno / pessoal-LGPD / sigilo bancário). Sensibilidade alta → rota soberana: silício próprio ou região dedicada, com mascaramento e trilha. Sensibilidade baixa → modelo de fronteira na nuvem, sem cerimônia.
- **J — Jurisdição.** Sob que lei essa inferência precisa residir? (LGPD, sigilo bancário, normas do BC, EU AI Act se houver contraparte europeia). A jurisdição é **restrição dura** — ela veta rotas antes de o custo opinar. É onde um banco BR tem **mais** razões de roteamento seletivo que o JPMorgan, não menos.
- **C — Custo por inferência na rota.** Custo total = token/hora de GPU + amortização do hardware próprio + o trabalho humano de manter a rota. O teste real do on-premise é **custo por inferência frente à conveniência da nuvem** — e, com a escassez de memória até 2030 (DRAM +63% no 2T26), esse custo tem **risco de alta**, não de queda. **Sem instrumentação de custo por rota, a decisão vira ideologia.**

**Saída:** uma matriz `classe de dado × jurisdição × rota permitida × custo por 1k inferências`, com um default declarado e exceção justificada. Regra de ouro do desenho: **a rota mais cara nunca é a padrão; a rota soberana nunca é opcional.**

## Quando usar / quando NÃO usar
**Usar** antes de qualquer decisão de nuvem × on-premise × modelo aberto, e na revisão do parque de casos de uso. **Não usar** para decidir de quem é o ativo (isso é o **DCS**), nem para rotear **dinheiro** — o trilho do pagamento agêntico é o [[Roteamento de Trilho do Agente de Pagamento (SRC)]]. SJC roteia **inferência**; SRC roteia **valor**. Também não substitui o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]: o mandato diz *se o agente pode*; o SJC diz *onde ele pensa*.

## Aplicado na prática
É literalmente a função do **Veltrix**: o proxy de LLM só é defensável se a política SJC for aplicada **antes** da chamada (classificação do dado → jurisdição permitida → rota mais barata que satisfaça as duas) e medida **depois** (custo por rota, por caso de uso, por jurisdição). O barramento do Bradesco faz a parte de política (*"controle de todas as leis para garantir o uso do dado no contexto que a gente pode usar"*); o JPMorgan faz a parte de rota (silício próprio para o sensível, fronteira para o resto). **Ninguém publicou ainda a terceira coluna — o custo por rota.** É exatamente aí que a categoria está aberta.

## Como cito isto num board
*"Não vamos decidir nuvem ou on-premise. Vamos decidir a política de roteamento: cada chamada vai para a rota mais barata que satisfaz a sensibilidade do dado e a jurisdição — e nós conseguimos provar isso numa trilha. O JPMorgan já tomou essa decisão; nós ainda estamos discutindo a pergunta errada."*
