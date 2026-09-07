---
tipo: post
data: 2026-08-01
canal: linkedin
status: rascunho
eixos: [financeiro, economia-ia, soberania]
maturidade: 4
tags: [post, linkedin, semana, 2026-W31]
---

# Rascunho — LinkedIn long-form (semana 2026-W31)

> Tese escolhida: **quando a conversa vira a tela inicial do banco, o custo por conversa vira o novo cost-to-income da interface — e a alavanca não é o modelo, é a plataforma que escolhe o modelo.** É a candidata nº 1 da Weekly W31: o número mais citável do trimestre (-65% de custo de GenAI, Itaú), eixo economia-ia/FinOps ainda não usado nos 4 posts anteriores (fraude, decisão, human-in-the-loop, cobrança), contraponto real (fornecedor único vs. caixa-preta multi-provedor) e conexão natural com Veltrix. A alternativa "agente no atacado" ficou de reserva: forte, mas vizinha demais de "O agente saiu da tela" e "A conversa não é a decisão".

---

## POST

### O Itaú apagou o menu. E o número que paga essa decisão não apareceu na tela.

Na segunda-feira, cerca de **300 mil clientes** do Itaú abriram o app e não encontraram o menu. Encontraram uma conversa. O **ia.i** deixou de ser um recurso escondido num canto e virou **a tela inicial do banco** — voz, texto ou imagem, com conta, cartões, crédito, investimentos e seguros num único ambiente. Até o fim de 2026, é a base completa (TI Inside, 27/07/2026). Já em setembro, a meta é 3 milhões de usuários (Seu Dinheiro/Exame, 28/07).

A imprensa leu como notícia de produto: a arma do Itaú na guerra da principalidade.

Eu li como notícia de FinOps. Porque o número que sustenta a jogada não estava na tela inicial — estava no rodapé do anúncio: **queda de 65% no custo de IA generativa**, obtida com uma plataforma própria **multi-provedor** — OpenAI, Anthropic, Google, AWS, modelos abertos e fechados (TI Inside, 27/07).

Parem nesse número comigo, porque ele muda a natureza da decisão que todo banco vai ter que tomar nos próximos 18 meses.

**Menu é custo fixo. Conversa é custo variável.**

Um tap num menu custa, na prática, zero: infraestrutura amortizada, milésimos de centavo por interação, não importa se o cliente abre o app uma vez por semana ou trinta vezes por dia. A interface tradicional do banco nunca teve uma DRE própria porque nunca precisou.

Uma conversa é outra física. Cada pergunta do cliente roda inferência. Cada resposta consome tokens. Multiplique por dezenas de milhões de clientes, várias conversas por dia, 365 dias por ano — e a interface do banco passa a ter **uma linha de custo variável que cresce junto com o engajamento**. O sucesso do canal encarece o canal.

É por isso que a minha leitura da semana cabe numa frase: **quando a conversa vira a tela inicial, o custo por conversa vira o novo cost-to-income da interface.** A métrica de eficiência do canal deixa de ser "quanto custa manter o app" e passa a ser "quanto custa cada interação — e quanto ela devolve".

E aqui está o detalhe que separa o movimento do Itaú de um lançamento de chatbot: a alavanca dos -65% **não é um modelo melhor. É a plataforma que escolhe o modelo.** Roteamento (model routing): a pergunta trivial vai para o modelo barato, a análise complexa vai para o modelo de fronteira, e a plataforma decide isso a cada requisição, com observabilidade de custo por rota. Quem depende de um único fornecedor de LLM não tem essa alavanca — aceita a tabela de preço que receber.

A mesma semana entregou o segundo ato desse argumento. A Moonshot liberou os pesos do **Kimi K3** — o maior open-weight da história, 2,8 trilhões de parâmetros, licença permissiva, desempenho próximo da fronteira custando **2 a 3 vezes menos para rodar** (Tom's Hardware/Interconnects, 27/07). Ou seja: roteamento multi-provedor deixou de ser só FinOps. Virou **soberania** — um banco com exigência de residência de dados agora tem a opção real de rodar fronteira dentro da própria jurisdição, para a carga regulada, e nuvem para o resto. Não é preocupação de nicho: **62,5% dos líderes de bancos já tratam soberania como tema de board** (NTT DATA, Banking AI Leaders' Playbook 2026, pág. 5).

**O contraponto honesto — porque tese sem contraponto é slogan.**

Quem defende o fornecedor único tem um argumento sério: orquestrar N modelos custa caro. Avaliação contínua, fallback, contratos, segurança, consistência de resposta entre rotas — essa complexidade operacional pode comer os -65% e ainda entregar uma experiência irregular ao cliente. Conheço times que tentaram multi-provedor sem instrumentação e terminaram com o pior dos dois mundos: caixa-preta cara.

O ponto é que esse contraponto não derruba a tese — ele a qualifica. A resposta ao risco da complexidade não é voltar ao modelo único; é **instrumentar a rota**: custo, latência e qualidade medidos por caminho, com baseline. Multi-provedor sem observabilidade é caos. Com observabilidade, é a única alavanca de preço que existe nesse mercado.

E há um segundo risco, que quase ninguém nomeou no lançamento: **menu não aconselha — conversa aconselha.** Cada resposta do ia.i sobre crédito ou investimento é, potencialmente, uma recomendação regulada. A trilha de auditoria dessa conversa vale mais que a UX dela. O banco que escalar o canal conversacional sem trilha vai descobrir isso na primeira fiscalização, não no primeiro NPS.

**O que eu diria num board:**

Se eu estivesse levando isso a um comitê na segunda-feira, seriam quatro perguntas, nenhuma retórica:

1. Qual é o nosso **custo por conversa** hoje — e qual é o baseline? Se ninguém sabe, não temos uma estratégia de canal conversacional; temos uma aposta com boa UX.
2. Quantos fornecedores de modelo conseguimos **trocar em 30 dias** sem reescrever produto? Essa resposta mede nossa alavanca de negociação — e o Itaú acabou de mostrar que ela vale 65% do custo.
3. Onde roda cada carga? Dado regulado tem rota de **jurisdição** definida, ou tudo sai pela mesma porta?
4. Quem **audita o conselho** que a nossa IA dá — e a trilha existiria se o Bacen pedisse amanhã?

O comportamento de líder já tem número: 52,5% dos bancos líderes "movem rápido e lideram o mercado" (NTT DATA, Playbook 2026, pág. 4). O Itaú é isso em produção. Para os demais, a pergunta não é "se" respondem — é com que plataforma, e a que custo por conversa.

É exatamente a categoria em que estou construindo o **Veltrix**: roteamento multi-modelo com FinOps e observabilidade por rota — a alavanca do Itaú, para quem não tem cinco anos e um exército de engenharia para construí-la em casa.

Se você está desenhando canal conversacional numa instituição financeira: você sabe o seu custo por conversa? Comparo notas com prazer — os comentários (ou a DM) estão abertos.

---

## Ganchos de variação (teste A/B)

1. **"O Itaú não lançou um chatbot. Trocou a DRE da interface."** — direto ao contraste produto vs. FinOps; melhor para audiência executiva.
2. **"Menu é custo fixo. Conversa é custo variável. O seu app sabe disso?"** — o par de frases mais compartilhável; melhor para alcance.
3. **"O número mais importante do lançamento do ia.i não apareceu na tela inicial: -65%."** — curiosidade/número; melhor para CTR de leitura longa.

## Fontes

- TI Inside, 27/07/2026 — lançamento do ia.i: tela inicial, ~300 mil clientes, base completa até fim de 2026; plataforma multi-provedor (OpenAI, Anthropic, Google, AWS); -65% no custo de GenAI.
- Seu Dinheiro / Exame, 27–28/07/2026 — guerra da principalidade; meta de 3 milhões de usuários em setembro.
- Tecnoblog, 27/07/2026 — ia.i como tela inicial.
- Tom's Hardware / Interconnects, 27/07/2026 — Kimi K3 open-weight: 2,8 tri de parâmetros, 2–3x mais barato de rodar.
- NTT DATA — *Banking AI Leaders' Playbook 2026* — pág. 4 (52,5% dos líderes "movem rápido"); pág. 5 (62,5% tratam soberania como preocupação de board).
- Notas relacionadas: [[Quando a conversa vira a tela inicial o custo por conversa e o novo cost-to-income da interface]] · [[A diferenca entre o banco que ve ROI e o que so percebe e medir o custo da IA]] · [[Soberania de dado virou tese competitiva - o ativo do banco e o modelo no proprio dado]]
