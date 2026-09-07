---
tipo: post
data: 2026-08-15
canal: linkedin
status: rascunho
eixos: [governanca, financeiro, soberania, economia-ia]
maturidade: 4
tags: [post, linkedin, semana, 2026-W33]
---

# Rascunho — LinkedIn long-form (semana 2026-W33)

> Tese escolhida: **rodar o modelo ficou barato; responder pela decisão que ele tomou ficou caro — e quem regula IA no Brasil hoje é a ANPD, com a LGPD que já está em vigor, não o PL 2338 que ainda espera relator.** Escolhi esta entre as três candidatas da Weekly W33 porque é a mais BR-financeira, a mais datada (Febraban Tech em 9 dias) e a única que ninguém está dizendo em português: *pare de esperar o marco legal, o regulador que chega primeiro já tem lei*. Tem número limpo e citável (delta de 29 pontos), cronograma público e contraponto real (XAI de fronteira é aproximação, não prova). Distinta dos cinco posts anteriores — nenhum tocou regulação aplicada BR.

---

## POST

### O modelo de IA ficou 50% mais barato nesta semana. A explicação da decisão que ele tomou ficou impagável.

Imagine a cena. Três e quarenta da manhã, um pedido de crédito entra pelo app, roda por um modelo, e sai negado em 900 milissegundos. Nenhum humano olhou. Nenhum humano vai olhar. Do lado de fora, uma pessoa lê "não foi possível aprovar seu pedido neste momento" e não entende por quê.

Até semana passada, essa cena era um problema de experiência do cliente.

Nesta semana ela virou um problema de arquitetura — e a razão é que duas curvas se cruzaram em 14 de agosto.

De um lado, o Google cortou o Gemini 3.7 Flash pela metade: US$ 0,75 por milhão de tokens de entrada, US$ 3,75 na saída (InfoWorld/VentureBeat, 14/08). Do outro, a ANPD operacionalizou seu Mapa de Temas Prioritários 2026–2027 e colocou **inteligência artificial e serviços financeiros** entre os quatro eixos de fiscalização ativa — com alvo declarado no **scoring automatizado que nega crédito sem explicação clara**, e a exigência de que a explicabilidade seja *real, não meramente formal* (ANPD, via Daniel Law).

Traduzindo em uma frase que eu levaria pro comitê: **rodar o modelo ficou barato. Responder pelo que ele decidiu ficou caro.**

E é aí que quase todo banco brasileiro está com o dinheiro no lugar errado.

## O delta de 29 pontos

O número que fecha o argumento não é brasileiro, mas descreve o Brasil com precisão desconfortável: **79% dos reguladores classificam explicabilidade como crítica ou importante, mas só 50% da indústria adotou métodos de XAI** — e cerca de dois terços das instituições **não monitoram viés** de forma sistemática (relatório Cambridge/BIS/IMF, pág. 10).

Vinte e nove pontos entre o que o regulador cobra e o que a indústria entrega.

Esse delta não é uma estatística. É um mapa. É exatamente onde a fiscalização vai encostar, porque é o único lugar onde ela encontra assimetria garantida: alta expectativa regulatória, baixa capacidade instalada.

E o cronograma já está publicado: **10 ações programadas** sobre dados biométricos, de saúde ou financeiros no 2º semestre de 2026, mais 25 sobre direitos do titular (ANPD). Não é sinalização. É agenda.

## O regulador que chega primeiro não precisa de lei nova

Aqui está a parte que a maioria dos comitês de IA no Brasil está lendo errado.

O **PL 2338** — nosso espelho do EU AI Act, com classificação por risco, direito a explicação e contestação, criação do SIA e multas de **até R$ 50 milhões por infração** — foi aprovado por unanimidade no Senado em 10/12/2024, chegou à Câmara em março de 2025 e **segue aguardando parecer do relator** na Comissão Especial. A votação prevista para o fim de 2025 escorregou para 2026 por falta de consenso (Senado Federal).

Enquanto isso, o vácuo não ficou vazio. Foi ocupado.

A ANPD **já tem lei, já tem competência e já publicou o cronograma**. A LGPD está em vigor desde 2020, o art. 20 garante revisão de decisão automatizada, e o alvo que ela escolheu é o coração do negócio bancário: decisão automatizada sobre pessoa física.

Ou seja: quem está esperando o marco legal para começar a se preparar está olhando para a porta errada da casa. O regulador não vai bater na porta da frente em 2027. Ele já está na cozinha, com uma lei de seis anos de idade.

E há uma vantagem tática nisso que vale destravar orçamento: **as obrigações da ANPD hoje e as do PL 2338 amanhã têm a mesma raiz** — transparência, explicação, contestação. Investir em explicabilidade agora não é compliance de uma lei futura. É compliance de uma lei presente, com uma opção grátis sobre a futura.

## A escala já saiu na frente da governança

O que torna isso urgente não é o regulador. É o volume.

Nos últimos trinta dias, os quatro maiores bancos do país publicaram os seus números de IA em produção: o **Banco do Brasil** opera **mais de 12 mil agentes Copilot e 1.200 modelos em produção**; o **Santander** conta **mais de 280 agentes** em crédito, fraude, KYC e operações, com meta de **€ 200 milhões** em valor de negócio em 2026; a **b.ia do Bradesco** registrou **74 milhões de interações** só no 1º semestre; e o **ia.i do Itaú** vai de 300 mil clientes para 3 milhões até o fim de setembro, e para a base toda até dezembro (Let's Money, Consumidor Moderno, IT Forum, ago/2026).

São números de vitrine. Mas repare no que eles têm em comum: **nenhum deles é uma métrica de governança.** Interações, funcionários habilitados, agentes em produção, clientes atendidos — quatro unidades de medida diferentes, nenhuma comparável, e nenhuma respondendo à única pergunta que o regulador vai fazer: *por que este cliente recebeu esta decisão?*

Doze mil agentes sem inventário, mandato e escopo por agente não são um ativo. São um passivo que ainda não foi provisionado.

## A distinção que muda o orçamento

Explicabilidade como **relatório** significa: quando o regulador perguntar, a gente reconstrói. Um time de dados, algumas semanas, um documento.

Explicabilidade como **arquitetura** significa: cada negativa de crédito já carrega, no próprio log, o modelo que decidiu, a versão dele, as features determinantes e o nome do humano responsável. Não se reconstrói nada, porque nada foi perdido.

A diferença entre as duas não é técnica. É de tempo — e tempo, aqui, é exposição.

**O teste que eu faria na segunda-feira:** pegue as últimas 10 negativas automáticas de crédito da sua operação e tente reconstruir a explicação com o que está guardado hoje. O tempo que isso levar é, literalmente, a sua distância até a ANPD.

## O contraponto honesto

Não vou vender certeza que não existe.

**XAI em modelo de fronteira é aproximação, não prova.** SHAP, LIME e atribuição de features explicam *correlação de influência*, não causalidade da decisão. Quem prometer ao regulador "explicação perfeita" está criando um passivo maior do que o que quer resolver — porque a primeira vez que a explicação não bater com o comportamento do modelo, a conversa deixa de ser sobre crédito e passa a ser sobre credibilidade.

Por isso a defesa que eu sustento não é explicação perfeita. É **trilha reconstrutível + humano nomeado**. Não "o modelo pensou X", mas "esta decisão foi tomada por este modelo, nesta versão, com estes dados, sob a responsabilidade desta pessoa, e pode ser contestada por este canal".

Isso é auditável. Explicação perfeita não é.

O segundo contraponto também é justo: instrumentar tudo custa. Mas o custo caiu junto com o preço do token — a mesma queda de 50% que abre este texto financia a camada de rastreabilidade. O que mudou não foi a capacidade de pagar. Foi a desculpa.

## O que eu diria num board

Que a economia da IA em banco inverteu de lado, e o orçamento ainda não percebeu. O custo marginal de **rodar** o modelo despenca a cada trimestre. O custo marginal de **responder pelo que ele decidiu** sobe — e sobe com data marcada no calendário do regulador.

Isso muda onde o próximo real deve entrar: não em mais um piloto de GenAI, e sim na camada de rastreabilidade da decisão de crédito. Três providências como decisão, não como estudo:

1. **Instrumentar antes de escalar.** Nenhum novo caso de uso de decisão automatizada entra em produção sem log de modelo, versão, features determinantes e responsável nomeado. Custa mais barato agora do que como retrofit em 12 mil agentes.
2. **Uma folha só para o comitê:** obrigações da LGPD hoje × obrigações do PL 2338 amanhã, com a coluna do meio marcando o que atende as duas. É o material que destrava orçamento sem depender de lei nova.
3. **Nomear o dono.** Para cada decisão automatizada sobre pessoa física, uma pessoa com nome e crachá. Se essa pergunta não tem resposta em cinco minutos, ela vai ter resposta em um processo administrativo.

É o mesmo raciocínio que me levou a construir governança de agentes com mandato e trilha por decisão. Não porque a regra existe — porque, sem isso, escala vira exposição.

Em nove dias começa o Febraban Tech, com o tema "Agentes Inteligentes, liderança humana". A agenda regulatória vai dominar os painéis. Quem chega com posição formada participa da conversa. Quem chega para aprender vira plateia.

**Pergunta que eu deixo aqui:** na sua operação, quanto tempo leva para reconstruir *por que* a última negativa automática de crédito foi negativa? Se a resposta for "algumas semanas", isso não é um gap de compliance. É um gap de arquitetura — e ele não fecha com relatório.

---

## 🪝 Ganchos de variação (teste A/B)

1. **[Contraste de preço]** "O modelo de IA ficou 50% mais barato nesta semana. A explicação da decisão que ele tomou ficou impagável." *(o gancho do corpo — mais editorial, funciona melhor com público executivo)*
2. **[Provocação regulatória]** "Todo mundo no mercado está esperando o PL 2338. O regulador que vai bater na sua porta primeiro não precisa dele — a ANPD já tem lei, já tem competência e já publicou o cronograma." *(mais afiado para o público de risco/compliance; maior potencial de discussão nos comentários)*
3. **[Teste acionável]** "Pegue as últimas 10 negativas automáticas de crédito da sua operação e tente reconstruir a explicação com o que você guarda hoje. O tempo que isso levar é a sua distância até a ANPD." *(o mais compartilhável — vira ação, não opinião; bom para carrossel/versão curta)*

---

## Fontes

- **ANPD** — Mapa de Temas Prioritários 2026–2027 (IA + serviços financeiros entre os 4 eixos de fiscalização; 10 ações sobre dado biométrico/saúde/financeiro no 2º sem., 25 sobre direitos do titular) · via [Daniel Law](https://www.daniel.com.br/pt/client-alert/anpd-em-2026-fiscalizacao-em-escala-e-uma-agenda-mais-ampla-para-o-ambiente-digital/)
- **Relatório Cambridge/BIS/IMF**, pág. 10 — 79% dos reguladores × 50% de adoção de XAI; ~2/3 sem monitoramento de viés *(biblioteca interna, `02-Sources/Reports/`)*
- **Senado Federal** — [PL 2338/2023](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233): aprovado em 10/12/2024, na Câmara desde mar/2025, aguardando relator; multas de até R$ 50 mi
- **InfoWorld, 14/08** — [Gemini 3.7 Flash: corte de 50%](https://www.infoworld.com/article/4209622/google-cuts-gemini-3-7-flash-prices-as-enterprise-ai-economics-diverge-and-pro-cadence-slows.html) (US$ 0,75 / US$ 3,75 por milhão de tokens, promocional até 31/12/2026) · [VentureBeat](https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut)
- **Banco do Brasil** — 12 mil agentes Copilot, 1.200 modelos em produção, AcademIA BB com 36 mil inscritos · [Let's Money](https://www.letsmoney.com.br/noticias/banco-do-brasil-academia-bb-ia-agentica)
- **Santander** — 280+ agentes em produção, IA para 185 mil funcionários, meta de € 200 mi em 2026 · [Let's Money](https://www.letsmoney.com.br/noticias/santander-libera-ia-185-mil-funcionarios-200-milhoes/)
- **Bradesco** — b.ia com 74 milhões de interações no 1S26, 87% de resolutividade · [Consumidor Moderno, 06/08](https://consumidormoderno.com.br/meu-bradesco-novo-ecossistema-solucoes-ia-cx/)
- **Itaú** — ia.i de 300 mil para 3 milhões de clientes até setembro · [IT Forum](https://itforum.com.br/noticias/itau-libera-ia-i-assistente-de-ia-no-app-para-300-mil-clientes/)
- **Febraban Tech 2026** — 24–26/08, Anhembi, tema "Agentes Inteligentes, liderança humana" · [agenda](https://febrabantech.com/agenda)

**Notas internas:** [[Explicabilidade de credito virou requisito de arquitetura, nao compliance]] · [[Credito preditivo em Open Finance vira risco de explicabilidade - testar no sandbox da ANPD]] · [[2026-08-14]] · [[Weekly-2026-08-14]]

**Decisões que tomei sozinho neste rascunho (revise):** (1) escolhi a candidata nº 1 da Weekly porque você não preencheu "A escolha da semana"; (2) mantive a menção a Veltrix/Cohort **implícita e sem nome** no fecho ("governança de agentes com mandato e trilha") para não soar comercial no LinkedIn — se quiser nomear, o lugar é o parágrafo antes do Febraban; (3) o corte de 50% do Gemini entra só como moldura do contraste, não como assunto — a tese é regulatória.
