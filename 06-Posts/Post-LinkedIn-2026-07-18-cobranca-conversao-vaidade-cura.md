---
tipo: post
data: 2026-07-18
canal: linkedin
status: rascunho
eixos: [financeiro, agentes, governanca]
maturidade: 4
tags: [post, linkedin, semana, 2026-W29]
---

# Rascunho — LinkedIn long-form (semana 2026-W29)

> Tese escolhida: **num agente de cobrança, conversão é vaidade; o número de board é a taxa de cura — e o agente que corta o parcelamento de 33 para 14 está escrevendo política de crédito sem mandato assinado.** É o item mais BR-financeiro e verificável da semana (dado nomeado do Banco do Brasil), tem contraponto honesto real (o corte de parcelas provavelmente é bom pro devedor) e conecta direto ao meu núcleo: governança de mandato de agente. Distinta dos posts anteriores (agente na tela, conversa não decide, human-in-the-loop como passivo de liquidez).

---

## POST

Semana passada um número do Banco do Brasil rodou os feeds e todo mundo bateu palma: o agente de cobrança do banco, rodando por WhatsApp, elevou a conversão em negociação de dívida em **+306%** e fechou **50% dos acordos sem nenhum humano no meio** (BBTS/adnews, TI Inside, IT Forum, 13/07/2026).

É um número de aplauso. Aprova sozinho em qualquer comitê.

Mas não foi ele que me tirou o sono. Foi o número que quase ninguém leu na mesma nota: o parcelamento médio dos acordos caiu **de 33,17 para 14,22 parcelas** — um corte de **57%** (mesma fonte, parceria AWS + BRQ).

Parem nessa segunda linha comigo, porque ela muda a natureza da conversa.

Cortar um acordo de dívida de 33 para 14 parcelas não é um ganho de eficiência de atendimento. É **a decisão de crédito mais relevante da operação** — reparcelar, dar desconto, definir prazo. E ela não foi tomada por uma política escrita, aprovada por um comitê de risco. Foi tomada pelo agente, uma negociação de cada vez, dentro da conversa.

Traduzindo em uma frase que eu levaria pro board: **o agente parou de executar a política de crédito e passou a escrevê-la.** E ninguém assinou esse mandato.

### Por que a conversão é a métrica errada

O objetivo treinável de um agente de negociação é claro: **fechar o acordo.** A função de recompensa empurra para a concessão — quanto mais desconto e prazo o agente pode oferecer, mais acordos ele fecha. Conversão sobe. Aplauso vem.

O problema é que conversão mede quantos acordos foram **assinados**, não quantos são **honrados**. E essas duas coisas se descolam exatamente quando o agente está otimizando para fechar: um acordo generoso demais fecha fácil e cura mal.

O número que um board precisa exigir não é o +306%. É a **taxa de cura efetiva** — quanto da dívida acordada de fato entra — dos acordos fechados pelo agente **versus** pelo humano, na **mesma safra**. Se o agente fecha mais e cura menos, ele não recuperou crédito. Otimizou a métrica errada e chamou de vitória.

Some o pano de fundo: Selic a **14,25% a.a.** (mercado, jul/26). Carregar dívida está caro. Nesse cenário, um acordo que fecha e não cura não é neutro — é prejuízo com carimbo de sucesso.

**Conversão é vaidade. Cura é recuperação.**

### O contraponto honesto — e eu diria em voz alta

Aqui é onde a maioria dos posts de LinkedIn erra, então vou fazer o contrário: dar o melhor argumento contra a minha própria tese.

Cortar o parcelamento de 33 para 14 parcelas **provavelmente é boa notícia pro devedor.** Acordo mais curto significa menos juros acumulado, menos tempo negativado, saída mais rápida do buraco. Se o agente está fechando acordos que o atendente humano, cansado no fim do turno, simplesmente não fechava, isso é **inclusão e velocidade de recuperação — não risco.** É plausível que o BB tenha entregado, de uma vez, mais eficiência e mais dignidade.

Eu não descarto nada disso. O ponto da minha tese não é frear o agente. É **nomear**.

O problema nunca foi o número 14. O problema é que **ninguém escreveu que 14 é o alvo.** Se o corte de parcelas foi um resultado desenhado — "nossa política diz que o agente busca o menor prazo que o cliente sustenta" —, ótimo, é estratégia. Se foi um efeito colateral do modelo otimizando conversão, que por acaso deu certo, então é outra coisa.

**Um resultado que você não pediu não é estratégia. É sorte auditável.**

E sorte auditável tem um problema específico num banco público: o BB responde a **TCU e Bacen**. Ali, "a IA decidiu" não é defesa. Cada desconto que o agente concede sozinho, por WhatsApp, é um ato administrativo vinculante em nome de um banco estatal. A pergunta do fiscal não vai ser "qual foi a conversão?". Vai ser "**qual era a alçada, quem a assinou, e onde está a trilha que prova que o agente não a excedeu?**".

### O que eu diria num board

Eu levaria **um slide, duas colunas**, e nada mais:

**Coluna 1 — a métrica certa.** Taxa de cura dos acordos fechados pelo agente versus pelos humanos, na mesma safra, nos mesmos perfis de risco. Não a conversão. A cura. Se a casa não consegue produzir esse corte, esse já é o diagnóstico: estamos comemorando um número que não sabemos se vira caixa.

**Coluna 2 — o mandato.** A matriz de alçada do agente: teto de desconto, teto de reparcelamento, e o gatilho que escala para um humano. Quem assinou cada limite. E a trilha que prova, para um auditor externo, que nenhum acordo passou do teto.

Isso não é burocracia anti-IA. É a diferença entre ter um **piloto impressionante** e ter um **sistema de crédito defensável**. Um agente que fecha metade dos acordos sozinho sem alçada escrita não é automação — é uma procuração em branco rodando em produção.

*Pra usar segunda de manhã,* uma pergunta de uma linha que vale para qualquer agente de execução que a sua casa tenha em piloto — cobrança, crédito, investimento:

**"Qual é a alçada que nosso agente pode conceder sem humano, quem assinou essa alçada, e onde está a trilha que prova que ele não a excedeu?"**

Se a resposta for o número que o modelo produziu, e não o número que a política definiu, o diagnóstico está feito.

O mercado, aliás, já está dizendo isso em voz alta: numa pesquisa recente com acquirers sobre comércio agêntico, **mais de 9 em cada 10 apontaram governança, permissões e consentimento** — não a infraestrutura de pagamento — como a prioridade número um (PYMNTS/Visa Acceptance, 14/07/2026). Quem paga a conta da fraude já sabe onde está o buraco. Falta o board de cada banco fazer a mesma leitura antes do regulador fazer por ele.

O agente que fecha o acordo já é commodity. O banco que sai na frente é o que consegue **provar** o que o agente tinha permissão para fechar — e mostrar a cura, não a conversão.

*Me mostrem a cura antes de comemorar o +306%.*

---

## Ganchos de variação (teste A/B)

1. **"O Banco do Brasil automatizou 50% da sua cobrança. E, sem perceber, deixou um algoritmo reescrever a política de crédito do banco — uma parcela de cada vez."**

2. **"+306% de conversão na cobrança do BB. O número que ninguém leu foi o outro: o parcelamento caiu de 33 para 14 parcelas. Isso não é eficiência de atendimento. É decisão de crédito sem mandato assinado."**

3. **"Todo banco vai te mostrar a conversão do agente de cobrança. Nenhum vai te mostrar a taxa de cura. E é a cura — não a conversão — que decide se você recuperou crédito ou só assinou prejuízo mais rápido."**

---

## Fontes

- **BB/BBTS — agente de cobrança:** +306% de conversão, 50% dos acordos sem intervenção humana, parcela média 33,17 → 14,22 (−57%). Parceria AWS + BRQ. adnews / TI Inside / IT Forum, 13/07/2026.
- **Comércio agêntico — gargalo é governança:** >9 em 10 acquirers apontam governança, permissões e consentimento como prioridade nº 1. PYMNTS / Visa Acceptance (via Sam Boboev), 14/07/2026.
- **Pano de fundo macro:** Selic 14,25% a.a. / CDI ~14,15% a.a. (mercado, jul/2026).
- **Contexto de fraude (opcional pra reforçar urgência):** 1.495.696 tentativas de fraude de identidade no 1T26, +36,6% a/a — uma a cada ~5 segundos (Serasa Experian, Mapa da Fraude 1T26).
- Notas de origem: [[Na cobranca com IA a conversao e vaidade - o numero de board e a taxa de cura]] · [[No banco publico o mandato do agente vira exigencia do TCU nao boa pratica]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] · Daily [[2026-07-15]].
