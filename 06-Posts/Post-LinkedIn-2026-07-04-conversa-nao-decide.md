---
tipo: post
data: 2026-07-04
canal: linkedin
status: rascunho
eixos: [governanca, financeiro, agentes]
maturidade: 4
tags: [post, linkedin, semana, 2026-W27]
---

# 📝 Post LinkedIn — A conversa não é a decisão

> Long-form (~1.150 palavras). Voz: Bruno, diretor de tecnologia rumo a CAIO. Storytelling + tese própria com contraponto real + fecho de board. Síntese da semana 29/jun–04/jul/2026 (W27).

---

## O agente que aconselha seu dinheiro não decidiu nada. E é por isso que ele é auditável.

Esta semana um cliente Uniclass abriu o superapp do Itaú, perguntou onde alocar uma sobra de caixa, e recebeu uma recomendação de investimento montada na hora — sem falar com nenhum assessor humano. Do outro lado da tela não havia gerente. Havia a Inteligência de Investimentos: um agente que consulta 50 bases de dados e roda 22 mil simulações antes de sugerir qualquer coisa. Começou com 10 mil clientes Uniclass e Personnalité e caminha para dezenas de milhares ao longo do ano (NeoFeed; Consumidor Moderno; Mobile Time, jul/2026).

A manchete óbvia é "banco automatiza assessoria". Mas o que me fez parar foi um detalhe de arquitetura que quase ninguém está lendo — e que, na minha leitura, é a coisa mais importante que um banco brasileiro publicou este semestre sobre como se constrói IA em produto regulado.

As 22 mil simulações fazem a decisão. O modelo de linguagem só conversa.

Ou seja: quem decide a alocação é um motor determinístico, quantitativo, reproduzível. A IA generativa entra depois, para traduzir aquilo em uma conversa que o cliente entende. A camada de conversa não é a camada de decisão. E essa separação, que parece um detalhe de engenharia, é exatamente o que torna o sistema defensável diante de um regulador.

## Por que a ordem importa (e não é preciosismo)

Pense na pergunta que a CVM ou o Bacen vão fazer no primeiro caso que der errado: *"por que o agente recomendou isto a este cliente?"*

Um motor determinístico tem resposta. Ele deixa um rastro reconstituível: rodei estas simulações, apliquei este perfil de suitability, descartei estas alternativas, cheguei aqui. Você consegue reproduzir o caminho.

Um LLM que *decide* a alocação, não. Ele devolve uma saída plausível e, se você pedir, escreve também uma justificativa bonita para ela. O problema é que a justificativa é gerada *depois* — é narrativa pós-fato, não trilha. O modelo pode racionalizar com fluência uma decisão que não foi a que ele de fato tomou. Em domínio de baixo risco, tudo bem. Em recomendação de investimento — que o EU AI Act classifica como alto risco (high-risk) e cujo prazo de obrigações entra em 02/08/2026, sob multa de até € 15 milhões ou 3% do faturamento global (Art. 99) — "explicação escrita pelo próprio modelo que decidiu" não é adequação demonstrável. É um disclaimer com vocabulário técnico.

Aqui está a frase que eu levaria para dentro de qualquer comitê de produto: **num produto regulado, a camada de conversa nunca pode ser a camada de decisão.** Suitability é dever de adequação — e adequação mora no rastro, não no rodapé.

## A tese — e o contraponto honesto

Minha aposta é que a arquitetura do Itaú (motor determinístico decide, LLM só conversa) vira o padrão de referência para todo agente que toque recomendação regulada no Brasil. Não porque seja a mais sofisticada, mas porque é a única que sobrevive a uma auditoria.

E preciso ser justo com o outro lado, senão isto é slogan, não tese.

O defensor do agente end-to-end tem um argumento forte: modelos de fronteira já raciocinam bem o suficiente para decidir com tool-use, e separar "motor que decide" de "modelo que fala" é uma muleta transitória que trava flexibilidade. A trajetória natural, dizem, é o agente que decide *e* explica sozinho — e amarrá-lo a um motor determinístico é desperdiçar capacidade. Para recomendação de conteúdo, roteirização, atendimento de baixo risco, eles estão certos.

Onde o argumento quebra é justamente no ponto regulado. "Explicação gerada pelo próprio decisor" é convincente para um humano e inútil para um auditor: ela não prova que a decisão nasceu de um processo adequado, só que o modelo sabe escrever uma justificativa. Adequação demonstrável exige que a decisão venha de um processo que você consegue reconstruir sem depender da boa-fé narrativa de uma caixa-preta. O motor determinístico não é atraso tecnológico. É o que separa "o modelo sugeriu" de "consigo provar que foi adequado".

E o vetor está piorando, não melhorando. Na mesma semana, o Claude Sonnet 5 chegou a US$ 2 / US$ 10 por milhão de tokens (input/output), agente quase-Opus a preço de commodity (Anthropic, 30/jun). Quando o agente que executa fica barato, o número de agentes que tocam decisão financeira explode — e a tentação de deixar o modelo "resolver tudo sozinho" para economizar uma camada de engenharia vira política de risco tomada por omissão.

## O que eu faria num board

Se eu sentasse num comitê executivo na segunda, não sairia da sala sem três coisas.

Primeiro, um princípio escrito: todo agente que recomenda algo regulado ao cliente decide no motor auditável, conversa no LLM — nessa ordem, sem exceção, com aprovação de produção condicionada a isso. É barato de decidir agora e caríssimo de reverter depois que dez agentes já estão em produção com a ordem invertida.

Segundo, a matriz que operacionaliza esse princípio. Chamo de **MRR — Matriz de Rastreabilidade da Recomendação**: para *cada* recomendação emitida, quatro registros obrigatórios — (1) quais fontes efetivamente pesaram na sugestão, (2) qual perfil de suitability foi aplicado e como restringiu as opções, (3) quais alternativas foram descartadas e por quê, e (4) onde está o ponto de confirmação humana. Quando o regulador perguntar "por que este cliente recebeu esta recomendação?", a resposta já está no rastro. A adequação vira registro, não argumento.

Terceiro, a pergunta que conecta isso ao dinheiro: qual o custo de inferência por recomendação, e como ele escala? 22 mil simulações por sugestão, multiplicadas por dezenas de milhares de clientes, é uma linha de custo material que quase ninguém instrumenta. Rastreabilidade regulatória e conta de FinOps são, na prática, o mesmo registro — e quem trata as duas como um problema só sai na frente nas duas.

Uma nota de honestidade sobre onde eu construo: a separação "pode conversar" versus "pode decidir/executar" é exatamente o eixo do Cohort, e a conta das 22 mil simulações é o tipo de número que o Veltrix existe para tornar visível. Não trago isso como pitch — trago porque é o ângulo de onde eu enxergo o problema, e prefiro ser transparente sobre a lente.

## O resto é manchete

A leitura preguiçosa da semana é "os bancos brasileiros estão automatizando a assessoria". Verdade — o Nubank já testa seu AI Private Banker com mais de 15 milhões de usuários ativos (Finsiders; Nu International). Mas automação não é a notícia. A notícia é que, no meio da euforia, alguém acertou a arquitetura: a decisão no motor auditável, a conversa no modelo.

Os bancos que vão liderar a próxima fase não serão os que colocarem o LLM mais esperto para decidir. Serão os que souberem, decisão por decisão, provar *como* se chegou ali. Num produto regulado, quem deixa a caixa que fala ser também a caixa que decide não está inovando.

Está escrevendo o próprio termo de responsabilidade — com uma fluência que o regulador não vai achar charmosa.

---

*Curadoria e tese: Bruno Oliveira · Escrevo sobre IA aplicada ao setor financeiro — governança, soberania de dados e a economia de rodar agentes em produção. Se a sua área já colocou agente para recomendar algo regulado ao cliente, vale conversar sobre onde mora a decisão — e se ela é auditável fora do modelo.*

> **Ganchos de variação (para teste A/B):**
> - **Provocação/board:** "Seu agente de IA recomenda investimento a milhares de clientes. Quando o regulador perguntar *por quê*, a resposta está no rastro — ou no disclaimer?"
> - **Dado-first:** "50 bases. 22 mil simulações. Zero assessor humano. E o número que importa nessa arquitetura não é nenhum desses — é *quem* decide."
> - **Contraste técnico:** "Todo mundo quer o LLM que decide sozinho. O Itaú fez o contrário — e foi por isso que ficou auditável. A camada de conversa nunca pode ser a camada de decisão."

**Fontes:** Itaú Inteligência de Investimentos — 50 bases, 22 mil simulações, teste com 10 mil clientes Uniclass/Personnalité sem assessor humano, expansão no ano (NeoFeed; Consumidor Moderno; Mobile Time; Convergência Digital; CNN Brasil, jul/2026); EU AI Act — obrigações de alto risco a partir de 02/08/2026, Art. 99 multa de € 15 mi ou 3% do faturamento global (Finextra; Legal Nodes); Nubank AI Private Banker / nuFormer — 15M+ MAU em teste (Finsiders; Nu International, jun/2026); Claude Sonnet 5 — US$ 2 / US$ 10 por milhão de tokens (Anthropic; TechCrunch, 30/jun/2026). Frameworks próprios: MRR — Matriz de Rastreabilidade da Recomendação; complementa Mandato do Agente (ELJT).
