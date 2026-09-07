---
tipo: post
data: 2026-09-01
canal: medium
registro: tecnico
status: rascunho
eixos: [governanca, seguranca, agentes, financeiro]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-09-01-autorizacao-na-recuperacao]]"
tags: [post, medium, 2026-W36]
---

# 📰 Medium — O vazamento de IA no banco sai pela recuperação, não pelo prompt

**Título:** O vazamento de IA no banco sai pela recuperação, não pelo prompt

**Dek:**
O controle que todo mundo comprou mede o dado que o funcionário cola na ferramenta.
A taxa que dobrou em um ano mede o dado que o sistema devolve — e o agente que recebe não estranha.

---

## O número

Dois indicadores convivem no mesmo relatório sob o mesmo rótulo. Eles medem falhas diferentes, com causas diferentes e controles diferentes — e só um dos dois costuma existir no relatório mensal de segurança de um banco.

O primeiro é a **violação de política no prompt**: o funcionário cola em uma ferramenta de GenAI um dado que não deveria sair. É o problema conhecido do *shadow AI*, com controle conhecido (DLP na saída do usuário, canal corporativo governado, bloqueio de app pessoal).

O segundo é o **vazamento downstream**: o sistema de IA **devolve** para o usuário — ou para um agente — informação que aquele solicitante não deveria acessar. Não há intenção, não há exfiltração, não há comportamento anômalo do lado humano. Há uma falha de autorização na camada de recuperação.

### Composição das violações com GenAI no Brasil

| Categoria do dado exposto | Apps corporativos | Apps pessoais no trabalho (*shadow AI*) |
|---|---|---|
| **Dado regulado** (registro financeiro, dado de cliente, contrato) | **64%** | **66%** |
| Código-fonte | 21% | — |
| Senhas e chaves de API | 9% | — |
| Propriedade intelectual | 7% | — |

### A série que muda a conversa

| Indicador | Um ano atrás | Hoje | Variação |
|---|---|---|---|
| Vazamento *downstream* (ocorrências semanais por organização) | **12** | **31** | **+158%** |
| Organizações usando GenAI | — | **100%** | — |
| Organizações usando plataformas de IA | — | **88%** | — |
| Organizações usando agentes para desenvolvimento de código | — | **79%** | — |

Fonte: Netskope Threat Labs · Brasil 2026, via [CISO Advisor](https://www.cisoadvisor.com.br/64-das-violacoes-com-ia-no-brasil-envolvem-dados-sensiveis/) e [TI Inside, 11/08/2026](https://tiinside.com.br/11/08/2026/violacoes-de-dados-mais-que-dobram-com-avanco-dos-agentes-de-ia/).

**Método — leia antes de citar (⚠️ conferir):** trabalhei com a cobertura secundária; não consultei o relatório na íntegra e não tenho número de página. A unidade é *ocorrências semanais por organização*, ou seja, uma média sobre a base instalada de telemetria de um fornecedor de segurança de borda — não é um censo do setor financeiro brasileiro, e a base tende a ser enviesada para organizações que já compraram observabilidade. **É por isso que o número não deve ser usado como benchmark, e sim como pergunta:** *qual é o nosso?*

### O contraste que fecha o argumento

Cibersegurança é prioridade declarada por **100%** das instituições financeiras brasileiras para 2026 — o único item com unanimidade; IA/GenAI e nuvem aparecem empatadas em 84% ([Pesquisa Febraban de Tecnologia Bancária 2026 · Deloitte](https://www.deloitte.com/br/pt/Industries/financial-services/research/pesquisa-febraban-tecnologia-bancaria.html)). Prioridade máxima declarada, e o indicador que mais que dobrou não está em painel executivo nenhum. Não por negligência: porque ele mora numa camada que o organograma trata como arquitetura, não como controle.

---

## O mecanismo

### O caminho que a consulta percorre

Numa arquitetura de recuperação aumentada (RAG), o caminho é curto e cada etapa é um lugar onde a permissão pode — ou não — ser avaliada:

1. **Ingestão.** Um pipeline lê os repositórios (Drive, SharePoint, Confluence, wiki, base de contratos), quebra os documentos em trechos (*chunking*), gera embeddings e escreve no índice vetorial. **Roda com conta de serviço.** Conta de serviço lê tudo — é o requisito funcional do trabalho dela.
2. **Consulta.** O solicitante manda a pergunta. A pergunta vira vetor.
3. **Recuperação.** O índice devolve os *top-k* trechos mais próximos semanticamente.
4. **Montagem de contexto.** Os trechos entram no prompt final.
5. **Geração.** O modelo responde com base no que recebeu.

O controle de acesso, na maioria das implementações que vi, mora nas etapas 1 e 2: *este repositório podia ser indexado?* e *este usuário pode usar o chat?*. **A pergunta que importa é da etapa 3**, e é outra: *este solicitante, agora, pode ler este trecho específico?*

Para responder isso, a ACL da origem tem de viajar com o trecho, sobreviver ao *chunking*, e ser reavaliada **por identidade a cada recuperação** — não a cada reindexação. Quando isso não acontece, o índice vira um repositório novo, com uma cópia do conteúdo de todos os repositórios e nenhuma das permissões deles.

### Os quatro pontos de quebra

| # | Falha | Sintoma | Onde se resolve |
|---|---|---|---|
| 1 | Permissão herdada na **indexação**, não na consulta | quem perdeu acesso na origem continua alcançável até a próxima carga | reavaliação de ACL em tempo de consulta |
| 2 | Trecho sem ACL | metadado de permissão cai no *chunking* | ACL como campo obrigatório do trecho; rejeitar ingestão sem ele |
| 3 | Consumidor é **agente**, não pessoa | o retriever vê a conta do orquestrador, não quem pediu | propagação de identidade (*identity propagation*) fim-a-fim |
| 4 | O agente **não estranha** | nenhum alerta a jusante | mandato de agente + rota por sensibilidade |

O ponto 4 é o que muda a natureza do risco em 2026, e não é retórica. Uma pessoa que recebe na tela um contrato de outra área hesita, pergunta, às vezes abre chamado. **Esse desconforto é um controle não escrito, e ele segura uma parte relevante dos incidentes.** O agente não tem desconforto: ele recebe o trecho, extrai o que precisa e segue para o próximo passo do plano — possivelmente colocando o conteúdo em um resumo, um ticket, um e-mail, um commit. O vazamento não termina na resposta; ele começa nela.

### A permissão foi desenhada para cargo; o uso migrou para tarefa

Há um segundo movimento tectônico por baixo. O estudo *Work at the Frontier* (OpenAI, 27/07/2026, mais de 800 mil mensagens analisadas) mostra que **43,5%** das mensagens específicas de ocupação tratam de tarefas de **outra** profissão. Por área: CX 77%, Design 75%, RH 69%, Jurídico 56%, Marketing 53%, Engenharia 28%. *(⚠️ conferir: é um proxy de comportamento de uso, não uma medida de acesso indevido — mas a direção é inequívoca.)*

Traduzindo para controle de acesso: **a tarefa cruza a fronteira da função muito antes de a permissão ser revista.** O analista de marketing que faz uma análise contratual com IA está operando fora do mandato de acesso do cargo dele, e o retriever — que só conhece grupos de diretório — não tem como saber. Enquanto a permissão for por cargo e o uso for por tarefa, a diferença entre os dois é exatamente a superfície de vazamento downstream.

---

## O contraponto

**1. "O salto de 12 para 31 é artefato de detecção."**
Quem instrumenta mais, enxerga mais. Parte do crescimento é lente, não risco. Aceito — e provavelmente é verdade em alguma proporção que ninguém consegue isolar.

Só que a conduta não muda. Se a sua organização não sabe se o próprio número é 12 ou 31, o valor dela é **desconhecido**. E desconhecido é o pior número possível para levar a uma fiscalização: a ANPD incluiu IA no Mapa de Prioridades e programou **20 fiscalizações específicas para 2026–2027**, sem depender do PL 2338 — porque o art. 20 da LGPD já trata de decisão automatizada, e o dado devolvido indevidamente já é incidente de segurança sob a lei em vigor.

**2. "ACL por trecho é caro e degrada a resposta."**
Verdade técnica, e a mais séria das duas. Há três caminhos e nenhum é grátis:

| Estratégia | Custo | Efeito colateral |
|---|---|---|
| Filtro **pós-recuperação** | baixo de implementar | encolhe o *top-k* efetivo; a resposta piora de forma silenciosa |
| Filtro **pré-recuperação** (ACL no filtro do índice) | médio; exige metadado consistente | latência sobe com a cardinalidade de grupos |
| Índice **particionado por permissão** | alto; duplicação de conteúdo | custo de armazenamento e reindexação |

A resposta honesta não é escolher a mais cara para tudo. É que **num banco a lista de repositórios com dado regulado é curta** — contratos, crédito, risco, jurídico, RH — e é exatamente essa lista que não deveria estar num índice único construído por conta de serviço. Para o resto do acervo, filtro pós-recuperação resolve. A decisão é de classificação, não de orçamento.

**3. "Isso é problema do fornecedor de RAG."**
Parcialmente. Mas o titular do dado reclama do banco, não do fornecedor — o mesmo raciocínio que vale para a decisão de crédito terceirizada. Se o contrato de plataforma não obriga propagação de identidade e log de recuperação exportável, o banco comprou funcionalidade e ficou com o passivo.

---

## O que eu faria

Três medições, nesta ordem. Nenhuma exige projeto novo — todas exigem que alguém aceite o número que vai sair.

**1. Separar a taxa de vazamento downstream da taxa de prompt.**
Ponto de instrumentação: **a saída do retriever**, não a saída do modelo. Para cada consulta, compare o conjunto de trechos devolvidos contra a ACL efetiva do solicitante **no instante da consulta**. Métrica: *ocorrências por semana*, na mesma unidade do mercado, para permitir comparação. Se o relatório de segurança traz só a taxa de prompt, metade do risco não está sendo medida — e é a metade que está crescendo.

**2. Defasagem de ACL (ACL lag), p95 em horas.**
Tempo entre a revogação de acesso na origem e a revogação efetivamente refletida no índice. Instrumentação barata: **documento-canário** por repositório. Você revoga o acesso de uma identidade de teste, consulta em laço, e cronometra até o trecho parar de voltar. O p95 dessa medida é o tamanho da janela em que um desligamento, uma mudança de área ou uma segregação de função existe no papel e não existe no sistema.

**3. Identidade efetiva na recuperação.**
Percentual de consultas em que o retriever avalia a identidade do **solicitante**, e não a conta de serviço do pipeline. Denominador: todas as chamadas de recuperação, humanas e de agente. É a métrica mais desconfortável das três, porque na maioria das casas o valor inicial é baixo — e quando ninguém consegue calcular, o valor é **0%**.

**Onde isso encaixa no acervo.** Os três fecham o eixo **A (Autorização)** do [[Censo do Corpus Exposto (RSJA) - Repositorio, Sensibilidade, Jurisdicao, Autorizacao]], que hoje pergunta *quem autorizou este acervo a sair de casa*. A pergunta desta semana é o degrau seguinte, no fluxo e não no estoque: *quem autorizou este trecho a voltar, para este solicitante, agora* — e isso conversa diretamente com a [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]], que governa o que sai, e com o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]], que define o que o agente consumidor pode sequer pedir.

É onde os dois produtos que construo se encontram: o **Cohort** escreve o mandato do agente consumidor (escopo, limite, jurisdição, trilha) porque não há barreira humana a jusante; o **Veltrix** aplica roteamento por sensibilidade e jurisdição, decidindo o que pode ser recuperado por qual consumidor e a que custo.

**O que eu diria num board:** *permission inheritance* na camada de recuperação parou de ser detalhe de arquitetura e virou controle de LGPD. A pergunta de uma linha para o próximo comitê de segurança é esta — **"qual é a nossa taxa de vazamento downstream, separada da de prompt?"**. Se a resposta demorar mais de uma semana, a resposta já apareceu.

---

**Frameworks citados:** [[Censo do Corpus Exposto (RSJA) - Repositorio, Sensibilidade, Jurisdicao, Autorizacao]] · [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]
**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-09-01-autorizacao-na-recuperacao]]
**Nota de origem:** [[O risco de dado em GenAI e a autorizacao na recuperacao, nao o prompt do shadow AI]] · [[Shadow AI e dado sensivel cruzando a fronteira da funcao por um canal nao-governado]]
**Capa:** 16:9 conforme [[Identidade-Visual-Editorial]] — mesma cena do card 4:5 (esteira de pedra devolvendo pastas de uma parede de arquivo monumental; figura minúscula de costas; uma única pasta em vermelhão), reenquadrada na horizontal com mais parede à esquerda.

## Fontes

1. Netskope Threat Labs · Brasil 2026 — [CISO Advisor · "64% das violações com IA no Brasil envolvem dados sensíveis"](https://www.cisoadvisor.com.br/64-das-violacoes-com-ia-no-brasil-envolvem-dados-sensiveis/) e [TI Inside · "Violações de dados mais que dobram com avanço dos agentes de IA", 11/08/2026](https://tiinside.com.br/11/08/2026/violacoes-de-dados-mais-que-dobram-com-avanco-dos-agentes-de-ia/) — ⚠️ conferir: cobertura secundária, sem página.
2. [Pesquisa Febraban de Tecnologia Bancária 2026 · Deloitte](https://www.deloitte.com/br/pt/Industries/financial-services/research/pesquisa-febraban-tecnologia-bancaria.html) — prioridades declaradas para 2026.
3. OpenAI · *Work at the Frontier*, 27/07/2026 — ⚠️ conferir: link direto não registrado na nota de origem.
4. [ANPD · Segunda análise do Projeto de Lei sobre inteligência artificial](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-segunda-analise-do-projeto-de-lei-sobre-inteligencia-artificial) e [Plugged.ninja · ANPD prevê 20 fiscalizações de IA](https://www.plugged.ninja/2026/07/pl-762-2026-pl-704-2026-anpd-fiscalizacao-ia-brasil-pl-2338-julho/).
5. Daily de origem: [[2026-08-24]] · Weekly: [[Weekly-2026-08-31]].

---
## ✅ Checklist antes de publicar
- [x] Acrescenta o que **não** cabia no feed? (composição das violações, série, método e viés da amostra, tabela de estratégias de filtro, tabela dos 4 pontos de quebra)
- [x] Título é afirmação e cabe em 12 palavras? (11)
- [x] Linka o post de origem e as notas de `05-Frameworks/`?
- [x] Fontes com link?
- [ ] Conferir os dois `⚠️` antes de publicar (relatório Netskope na íntegra + link do estudo da OpenAI).
