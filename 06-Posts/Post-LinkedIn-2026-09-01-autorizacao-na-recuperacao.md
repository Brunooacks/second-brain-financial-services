---
tipo: post
data: 2026-09-01
canal: linkedin
registro: tecnico
status: rascunho
eixos: [governanca, seguranca, agentes, financeiro]
maturidade: 3
medium: "[[Medium-2026-09-01-autorizacao-na-recuperacao]]"
tags: [post, linkedin, tecnico, 2026-W36]
---

# 🔧 Post Técnico — O seu DLP olha o prompt. O vazamento saiu pela resposta.

> Tese técnica de W36. Origem: [[O risco de dado em GenAI e a autorizacao na recuperacao, nao o prompt do shadow AI]] — a **"quarta na fila"** da [[Weekly-2026-08-31]], marcada lá como *"o melhor material técnico da semana"*, com a instrução explícita: *"se a escolha da semana for executiva, esta é a candidata natural para a terça."* Foi o que aconteceu. Lastro na daily [[2026-08-24]] e em [[Shadow AI e dado sensivel cruzando a fronteira da funcao por um canal nao-governado]].
> **Por que não as outras (não-canibalização, últimas 4 semanas):** a candidata nº 1 (antifraude / autorização do titular) já virou a peça executiva de quinta — [[Post-LinkedIn-2026-09-03-quem-paga-a-fraude-autorizada]]. A nº 2 (oferta suprimida) já virou a long-form — [[Post-LinkedIn-2026-08-29-oferta-que-nunca-foi-exibida]]. A nº 3 (agente sem data de expiração) é técnica, mas cairia no mesmo balcão de [[Post-LinkedIn-2026-08-25-trilha-registra-o-que-o-agente-disse]] e [[Post-LinkedIn-2026-08-20-passivo-em-cadeia-a2a]] — três peças de governança de agente em quatro semanas viram "precisamos de mais controle sobre agente". **Fica na fila para W37, com o gancho de validade como 4º eixo do [[Placar do Parque de Agentes (FMC) - Frota, Mandato, Custo]].**
> Distinta de [[Post-LinkedIn-2026-08-25-trilha-registra-o-que-o-agente-disse]] (lá: o canal **entre** agentes, o que trafega; aqui: o que o sistema **devolve** para o agente) e de [[Post-LinkedIn-2026-08-15-explicabilidade-arquitetura-anpd]] (lá: explicar a decisão ao titular; aqui: quem podia ler o documento que embasou a resposta).

---

## O seu DLP olha o prompt. O vazamento saiu pela resposta.

Dois números aparecem no mesmo relatório sob o mesmo rótulo — "violação de dado com IA" — e pedem controles opostos. Um mede o que o funcionário **cola** na ferramenta. O outro mede o que o sistema **devolve** para quem não devia receber. O primeiro tem dono, orçamento e painel. O segundo mais que dobrou em um ano, e quase ninguém consegue calcular a própria taxa.

### O mecanismo

Numa arquitetura de recuperação (RAG), a consulta vira vetor, bate no índice, traz os *top-k* trechos e monta o contexto que o modelo lê. O que decide segurança está no meio do caminho: **o índice foi construído uma vez, por um pipeline de ingestão que rodou com conta de serviço** — e conta de serviço lê tudo.

A permissão costuma ser checada em dois lugares errados: na porta da aplicação (pode usar o chat?) e na ingestão (podia indexar o repositório?). Nenhuma responde a pergunta da consulta: *este solicitante, agora, pode ler este trecho?* Para isso a ACL precisa viajar com o trecho, sobreviver ao *chunking* e ser reavaliada por identidade **a cada recuperação** — não a cada reindexação. Sem isso, quebra em quatro pontos:

1. **Permissão herdada na indexação, não na consulta.** Quem perde acesso na origem segue alcançável pelo índice até a próxima carga.
2. **Trecho sem ACL.** O metadado de permissão é o primeiro a cair no *chunking*.
3. **O consumidor é um agente.** Ele apresenta a conta do pipeline, não a identidade de quem pediu: o privilégio herdado é o do orquestrador.
4. **O agente não estranha.** A pessoa que recebe um contrato que não devia ver hesita; o agente processa e segue para o próximo passo do plano.

O ponto 4 não é retórica: é a remoção da última barreira que hoje segura parte relevante dos incidentes — o desconforto humano. Agrava que a permissão foi desenhada para **cargo** e o uso migrou para **tarefa** — **43,5%** das mensagens de ocupação tratam de tarefa de outra profissão (*Work at the Frontier*, OpenAI, 27/07/2026 — ⚠️ conferir: proxy de comportamento, não medida de acesso). O retriever só conhece grupos de diretório.

### O número

No Brasil, **64%** das violações de política em apps de GenAI envolvem **dado regulado** — registro financeiro, dado de cliente, contrato. Mas o número que muda a curva é o *downstream*: **de 12 para 31 ocorrências semanais por organização em um ano**, num recorte em que **79%** já adotam agentes para desenvolvimento de código (Netskope Threat Labs · Brasil 2026, via CISO Advisor e TI Inside, 11/08/2026 — ⚠️ conferir: relatório não consultado na íntegra, sem página; telemetria de base instalada de fornecedor). No mesmo ano, cibersegurança é prioridade declarada em **100%** das instituições financeiras brasileiras (Febraban/Deloitte 2026). Unanimidade no slide, e a taxa que dobrou não está em painel nenhum.

### O contraponto honesto

**"31 é artefato de lente"** — quem instrumenta mais, enxerga mais. Em parte, verdade. Só que a conduta não muda: se você não sabe se o seu número é 12 ou 31, o seu é **desconhecido** — o pior valor possível diante de uma ANPD com **20 fiscalizações de IA agendadas para 2026–2027**.

**"ACL por trecho é caro"** — é, e o custo é real em latência e reindexação. Mas a lista de repositórios com dado regulado num banco é curta, e é justamente ela que não deveria estar num índice único de conta de serviço.

### O que eu instrumentaria primeiro

1. **Taxa de vazamento downstream (ocorrências/semana), separada da de prompt.** Medir **na saída do retriever**, não na do modelo: trechos devolvidos contra a ACL efetiva do solicitante no instante da consulta. Se o relatório de segurança só traz a taxa de prompt, metade do risco não está medida.
2. **Defasagem de ACL (ACL lag), p95 em horas** — da revogação na origem até ela valer no índice. Instrumentação barata: **documento-canário** por repositório, revoga, consulta em laço, cronometra. Esse p95 é a janela em que a segregação de função existe no papel e não no sistema.
3. **Identidade efetiva na recuperação: % de consultas em que o retriever avalia o solicitante, e não a conta de serviço do pipeline.** Denominador: todas as chamadas de retrieval, humanas e de agente. Quando ninguém consegue calcular, o valor é 0%.

Os três fecham o eixo **A (Autorização)** do [[Censo do Corpus Exposto (RSJA) - Repositorio, Sensibilidade, Jurisdicao, Autorizacao]]: ele pergunta quem autorizou o acervo a sair de casa; o degrau seguinte é *quem autorizou este trecho a voltar, para este solicitante, agora*.

É onde o **Cohort** escreve o mandato do agente consumidor e o **Veltrix** roteia por sensibilidade e jurisdição.

*Permission inheritance* na camada de recuperação parou de ser detalhe de arquitetura. Virou controle de LGPD.

---

**Assinatura:**
*Escrevo sobre IA aplicada ao setor financeiro — governança, soberania de dados e a economia de rodar agentes em produção.*

**Expansão Medium:** [[Medium-2026-09-01-autorizacao-na-recuperacao]]

**Brief de arte:** motivo de **mecanismo / estrutura exposta**, conforme [[Identidade-Visual-Editorial]].
*Cena:* **uma esteira de pedra saindo de uma parede monumental de gavetas de arquivo abertas, devolvendo pastas para uma bandeja no chão; a figura minúscula está de costas, já se afastando, sem olhar para a bandeja; uma única pasta na esteira em vermelhão queimado.** Leitura: o vazamento não entra — ele volta; e quem recebe não estranha. Um só evento visual, acento em menos de 8% do quadro, zero texto na ilustração.

**Fontes:**
- Netskope Threat Labs · Brasil 2026 — via [CISO Advisor](https://www.cisoadvisor.com.br/64-das-violacoes-com-ia-no-brasil-envolvem-dados-sensiveis/) e [TI Inside, 11/08/2026](https://tiinside.com.br/11/08/2026/violacoes-de-dados-mais-que-dobram-com-avanco-dos-agentes-de-ia/)
- OpenAI · *Work at the Frontier*, 27/07/2026 (via [[Shadow AI e dado sensivel cruzando a fronteira da funcao por um canal nao-governado]])
- [Pesquisa Febraban de Tecnologia Bancária 2026 · Deloitte](https://www.deloitte.com/br/pt/Industries/financial-services/research/pesquisa-febraban-tecnologia-bancaria.html)
- ANPD · Mapa de Prioridades / 20 fiscalizações de IA 2026–2027 — via [[ANPD agendou 20 fiscalizacoes de IA para 2026-2027 - compliance virou calendario]]

---
## ✅ Checklist antes de publicar
- [x] Nomeia **onde medir**? (saída do retriever · defasagem de ACL p95 · identidade efetiva na recuperação)
- [x] Todo número tem fonte? (dois marcados `⚠️ conferir`)
- [x] Tem contraponto real declarado? (dois)
- [x] NÃO virou tutorial?
- [x] Tese distinta das outras peças da semana?
