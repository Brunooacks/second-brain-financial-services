---
tipo: post
data: 2026-08-08
canal: linkedin
status: rascunho
eixos: [soberania, governanca, economia-ia, financeiro]
maturidade: 4
tags: [post, linkedin, semana, 2026-W32]
---

# 📝 Post LinkedIn — O dia em que quatro demissões viraram cláusula contratual

> Long-form (~1.200 palavras). Voz: Bruno, diretor de tecnologia rumo a CAIO. Storytelling + tese própria com contraponto real + fecho de board. Síntese da semana 03–07/ago/2026 (W32).

---

## Seu contrato de IA tem cláusula para quando o cérebro do fornecedor troca de empresa?

Na quarta-feira, 5 de agosto, quatro pessoas saíram do mesmo lugar ao mesmo tempo.

**Jeff Dean, Sanjay Ghemawat, Oriol Vinyals e Quoc Le** — os arquitetos por trás do Search, do MapReduce e do Gemini — deixaram o Google para fundar a Discovery Loop. No mesmo dia, Demis Hassabis saiu do dia a dia do DeepMind para virar Chair da unidade e Chief Scientist da Alphabet, com Koray Kavukcuoglu assumindo a operação e reportando direto a Sundar Pichai. Foi a maior reorganização da história do laboratório.

O mercado não esperou análise. **A Alphabet caiu ~5% no pregão: entre US$ 160 e 200 bilhões de valor de mercado, em um dia** (Axios, Datacenter Dynamics e The Decoder, 05/08/2026; AINews, 06/08).

Guarde esse número, porque ele não é sobre o Google.

Ele é a primeira medição pública e limpa de uma variável que nenhum banco tem no contrato: **quanto do valor de um fornecedor de fronteira é pessoa, e não plataforma.** O mercado respondeu em oito horas — entre US$ 160 e 200 bilhões. E se o mercado sabe precificar isso, um comitê de fornecedores também deveria.

## O que a nossa due diligence de IA olha hoje

Peça o formulário de avaliação de fornecedor de IA de qualquer instituição financeira brasileira e você vai encontrar, com pequenas variações, duas colunas que decidem a escolha: **desempenho em benchmark** e **preço por token**. Segurança e privacidade entram como anexo jurídico. O resto é comercial.

Olhe para essas duas colunas com o número de quarta-feira na cabeça.

**Benchmark** é uma fotografia que vence em noventa dias. A liderança de modelo troca de mão a cada ciclo de lançamento, e nenhum comitê reabre contrato por isso.

**Preço por token** é ainda pior como critério de longo prazo, porque a curva é descendente por decisão do próprio fornecedor. Na mesma semana, a Anthropic confirmou a montagem de um time interno de design de chips para co-projetar silício e modelo, com alvo declarado de **cortar cerca de 50% do custo de inferência por token** (SiliconANGLE e TechTimes, 05/08). Depois do TPU do Google, é o segundo laboratório de fronteira a puxar o custo para baixo por integração vertical. Quem assina hoje um compromisso plurianual de preço fixo trava o preço de 2026 numa curva que o fornecedor planeja derrubar pela metade.

Ou seja: as duas colunas que decidem a compra são um retrato que expira e um preço que o vendedor pretende cortar sozinho.

E nenhuma das duas responde à pergunta que quarta-feira acabou de tornar concreta: **quem, na organização do meu fornecedor, sustenta o roadmap que eu estou comprando — e o que acontece com o meu contrato se essas pessoas saírem?**

Quando um banco padroniza a esteira de GenAI num único fornecedor, ele não compra um modelo. Compra a **organização** que mantém aquele modelo vivo, versionado, suportado e não descontinuado. Organização é gente. E gente sai — às vezes quatro de uma vez, para uma empresa nova na qual o próprio Google investiu e para a qual o Google Cloud venderá capacidade computacional.

Essa é a tese: **risco de pessoa-chave do laboratório (key-person risk) deixou de ser assunto de imprensa de tecnologia e virou variável de contrato do banco.** Due diligence de fornecedor de IA que se esgota em benchmark e preço por token está estruturalmente cega para a variável que moveu US$ 160 bilhões numa tarde.

## Por que isso é mais grave no Brasil do que parece

Porque a nossa dependência já está em processo crítico, não em piloto.

O Santander Brasil roda **mais de 400 projetos de IA** sob um Chief Data and AI Officer. Só no cartão, a análise de contestação de fraude ficou **~95% mais rápida, com até 90% de automação e taxa de erro abaixo de 1%** (Contec; Let's Money, ago/2026). Isso não é um chatbot de FAQ. É triagem de fraude — processo que, se degradar, aparece em perda operacional e em reclamação regulatória na mesma semana.

Na engenharia, o quadro é o mesmo. O PicPay reporta **59,1% do código escrito com IA** (Blog PicPay / Tech Talks, medição DX de maio). A fábrica de software financeiro brasileira já é majoritariamente assistida por modelo de terceiro.

Agora some o lado do regulador. A ata do Comef já elevou o uso de IA a risco cibernético sistêmico e nomeou o problema das **dependências comuns** — a concentração que transforma a falha de um fornecedor em risco de todos. E o PL 2338 caminha para votação com a ANPD desenhada como coordenadora do sistema nacional de IA e reguladora residual, num modelo baseado em risco com **multa de até R$ 50 milhões por infração** (Convergência Digital; JOTA). Para banco, o desenho importa mais que a data: com a ANPD residual, IA em serviços financeiros tende a ficar sob a régua do Bacen, que já sabe cobrar continuidade e terceirização.

Em outras palavras: o regulador brasileiro vai perguntar sobre continuidade de fornecedor antes de perguntar sobre qualidade de modelo. Ele sempre pergunta nessa ordem.

## O contraponto honesto

O melhor argumento contra a minha tese é simples e forte: **o Google é maior do que qualquer indivíduo.** O Gemini continua com milhares de engenheiros, capital quase ilimitado e processos que não dependem de quatro nomes. Os -5% foram reação de manchete, não de fundamento, e podem reverter em semanas — como já reverteram em episódios parecidos. Nessa leitura, superdimensionar saída de executivo é ruído: o que importa é a instituição, e ela continua de pé.

Concordo com quase tudo isso. Não estou dizendo que o Gemini vai degradar amanhã — provavelmente não vai.

Meu ponto é outro, e ele sobrevive à reversão do papel: **um questionário de due diligence que não tem uma única linha sobre continuidade de roadmap está cego para uma variável que já moveu US$ 160 bilhões.** Se o mercado precifica risco organizacional de laboratório e o seu comitê de fornecedores não, a diferença entre os dois é exposição não contratada. Risco material não deixa de ser material porque a ação se recuperou.

E há uma correção que eu devo fazer em público. Semana passada argumentei que arquitetura multi-modelo é, sobretudo, alavanca de preço. Retiro a ênfase: **preço é a razão menos importante para ter dois modelos.** A razão principal é poder trocar de fornecedor em trinta dias sem reescrever produto — e conseguir provar, por log, que a alternativa existe e funciona. É isso que estou construindo no **Veltrix**: roteamento multi-modelo com prova auditável de que há plano B pronto. Hedge de fornecedor, não economia de rodapé.

## O que eu faria na segunda-feira

Três perguntas de comitê, nenhuma retórica:

**Primeira:** em quais processos críticos — fraude, crédito, atendimento regulado — a nossa operação para se o roadmap de um único fornecedor mudar de direção? Não "qual modelo usamos". Onde dói se ele mudar.

**Segunda:** algum dos nossos contratos de IA tem cláusula de aviso mínimo para descontinuidade de modelo (model deprecation) e compromisso de suporte a versão? Se a resposta for "o contrato segue o padrão de nuvem", a resposta é não.

**Terceira:** conseguimos trocar de fornecedor de modelo em trinta dias sem reescrever produto — e temos log que prove isso, ou temos uma arquitetura que alguém acredita que permitiria?

Gestão de fornecedores é uma das frentes nucleares de quem responde por IA num board. Não a mais glamourosa. É a que aparece primeiro na fiscalização.

Modelo se troca. Organização, não.

---

*Bruno Oliveira · Escrevo sobre IA aplicada ao setor financeiro: governança, soberania de dados e a economia real de rodar agentes em produção. Se a sua casa está renovando contrato de LLM neste semestre, a cláusula de continuidade custa uma reunião agora e um incidente depois.*

> **Ganchos de variação (para testar):**
> - Versão dado-first: abrir com "US$ 160 bilhões em um dia" e só depois revelar que foram quatro demissões.
> - Versão contrato: "Seu contrato de IA tem cláusula para quando o cérebro do fornecedor troca de empresa?" como primeira linha, sem contexto.
> - Versão BR-first: abrir pelo Santander Brasil (90% da triagem de fraude automatizada) e perguntar de quem é o roadmap que sustenta esse número.

**Fontes:**
- Axios · Datacenter Dynamics · The Decoder, 05/08/2026 · AINews/Smol AI, 06/08 — reorganização do Google DeepMind: Hassabis vira Chair do DeepMind e Chief Scientist da Alphabet, Kavukcuoglu assume como SVP; saída de Jeff Dean, Sanjay Ghemawat, Oriol Vinyals e Quoc Le para fundar a Discovery Loop; Alphabet -5% no dia (~US$ 160–200 bi).
- SiliconANGLE · TechTimes, 05/08/2026 — Anthropic confirma time interno de design de chips (co-design silício-modelo), alvo de cortar ~50% do custo de inferência por token.
- Contec · Let's Money, ago/2026 — Santander Brasil: 400+ projetos de IA; contestação de fraude de cartão ~95% mais rápida, até 90% de automação, erro <1%.
- Blog PicPay / Tech Talks (medição DX, maio/2026) — 59,1% do código de engenharia escrito com IA.
- Convergência Digital · JOTA, ago/2026 — PL 2338: ANPD como coordenadora do SIA e reguladora residual, modelo baseado em risco, multa de até R$ 50 mi por infração. Ata do Comef — IA como risco cibernético sistêmico e "dependências comuns".
- Notas de origem: [[Key-person risk do lab de IA virou variavel de contrato do banco]] · [[Integracao vertical dos labs derruba o preco por token - contrato fixo envelhece mal]] · [[Soberania de modelo virou risco de continuidade, nao tese]] · [[Banco no board do fornecedor de IA transforma concentracao em risco competitivo]] · Daily [[2026-08-06]].

---

> ⚠️ **Conferir antes de publicar** (post retroativo, gerado em 16/08 a partir da [[Weekly-2026-08-07]]):
> - `Santander Brasil: 400+ projetos / ~95% mais rápido / até 90% de automação / erro <1%` e `PicPay 59,1%` vêm da daily de 06/08 (Contec, Let's Money, Blog PicPay) — **não há nota atômica própria**. Confirmar na fonte primária.
> - A atribuição ao **Comef** ("dependências comuns", IA como risco cibernético sistêmico) veio da daily 06/08 + do post de 27/06, **sem ata citada com número de página**. Localizar a ata antes de citar num board.
> - `Alphabet −5% no dia (~US$ 160–200 bi)` é faixa, não valor fechado — manter como faixa no texto.
