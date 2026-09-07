---
tipo: jornada-depara
jornada: atendimento
fase: 2
players: [Santander, Caixa, C6, PicPay, PagBank/Stone]
data_captura: 2026-07-05
fontes: [Convergência Digital, Mobile Time, Contec Brasil, Let's Money, IT Forum, Microsoft News Brasil, Finsiders Brasil, Blog PicPay, Blog C6 Bank, Startups, Bloomberg Línea, TI Inside, Consumidor Moderno, Portal ClienteSA, Blog PagBank, Vanquish, Iniciador, Infra News Telecom, Tek Sapo, Caixa.gov.br, Neofeed, Exame]
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [jornada, depara, benchmarking, atendimento, cobranca, contact-center, delinquent, fase-2, expansao]
---

# 🧭 De-Para — Jornada: Atendimento & cobrança (Fase 2 · players de expansão)

**Recorte (1 frase):** Como os 5 players de expansão (Santander, Caixa, C6, PicPay, PagBank/Stone) atendem e cobram (dúvida → resolução → escalada humana / negociação de dívida → acordo) para testar se o achado do piloto — "o assistente generativo comoditizou em L4, o valor migrou para copiloto do operador e cobrança que formaliza acordo, ninguém no L5" — se repete fora do grupo de 6, num momento em que a inadimplência dos digitais dispara (cartão de "neobancos" +163% de 2021 a 2025) e a cobrança conversacional já mostra número duro. Liga com [[De-Para — Atendimento & cobrança]] (piloto).

## 🔍 Decomposição da jornada
Mesmas etapas canônicas do piloto (públicas, até a parede de login):
1. **Contato/entrada** — canal de atendimento (app, WhatsApp, 0800, chat) recebe a demanda.
2. **Triagem/roteamento** — classificação de intenção e direcionamento (bot → humano).
3. **Diálogo/resolução** — assistente generativo resolve dúvida ou executa transação (informacional → transacional).
4. **Escalada assistida** — copiloto apoia o operador humano em tempo real quando o caso sobe.
5. **Gestão do caso** — acompanhamento do ticket até fechamento (Customer Case Mgmt).
6. **Cobrança/negociação** — régua de cobrança, negociação de dívida e formalização de acordo (Delinquent Account Handling).

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| PicPay | **L4** (assistente GenAI multiagente com número de atendimento; predom. L4) | ~2–3 | Assistente atualizado para **GPT-4.1** (Azure OpenAI) com **arquitetura multiagente** (agentes por tema + supervisor que define plano de ação); resolve questões complexas (seguros, investimentos, limites, vencimentos) via app e WhatsApp; **NPS +10 p.p. e −8 p.p. de handoff humano** nas primeiras horas de uso (Microsoft News Brasil / IT Forum / Blog PicPay · 2026). |
| Santander | **L4** (conversacional entre 3 prioridades de IA + copiloto de operador; predom. L3) | ~2–3 | **Conversacional é uma das três prioridades de IA** do banco; **copiloto no atendimento** que orienta o agente humano em tempo real (dicas/respostas, sem eliminar o humano); plataforma agnóstica que **habilita cobrança, risco e atendimento**; caso Desenrola (renegociação) codificado em 1 mês vs meses; +400 projetos de IA no BR; meta grupo **€1 bi 2026–2028** (Mobile Time / Contec Brasil / Convergência Digital / Let's Money · 2026). |
| C6 (Banco C6) | **L4** (assistente GenAI transacional **+ renegociação de dívida generativa que fecha acordo**; predom. L3) | ~2–3 | **C6 Assistant** (GenAI no app, lançado 12/2024) lê dado de pagamento de texto/imagem/manuscrito e executa Pix/pagamento; separadamente, **chat de renegociação de dívida de cartão com GenAI** que "conversa de forma natural até gerar o acordo e finalizar a transação", em teste no app e ampliação no WhatsApp (**2 mil → 7 mil clientes**) (Blog C6 / Convergência Digital / Startups · 2024–2026). |
| PagBank/Stone | **L3–L4** (chatbot de atendimento com número consolidado + cobrança agêntica via trilho de terceiro; predom. L3) | ~2–3 | **PagBank: −27% de custo** no atendimento com IA/chatbot, **~34 mi de atendimentos 2021–2023**, abertura automática de OS por análise de foto (troca de maquininha); atendimento híbrido (mantém humano). **Stone**: cliente da **Iniciador** (trilho de pagamento agêntico via Pix, jun/2026) que embute **agente que lembra, negocia e cobra inadimplentes** disparando Pix sob consentimento — cobrança agêntica, mas **sobre trilho de terceiro** (Consumidor Moderno / IT Forum / TI Inside / Blog PagBank / Vanquish / Iniciador · 2024–2026). |
| Caixa | **L2** (assistente virtual + negociação por sistema/regra; sem GenAI observável no atendimento ao cliente; predom. L1–L2) | ~4–6 | **Aixa** (assistente virtual) é projeto com Stefanini focado em **TI interna**, não no cliente final; atendimento ao cliente por **WhatsApp 0800 104 0 104** e assistente virtual 24h; negociação de dívida via **SINEB/app** (emissão de boleto por sistema/regra); **Caixa Tem 130 mi+ usuários**. **Sem evidência pública de GenAI resolutiva ou cobrança conversacional própria** (Infra News Telecom / Tek Sapo / caixa.gov.br · 2018–2026). |

**Líder da jornada:** empate técnico **PicPay** e **Santander** em **L4** (PicPay com o número mais duro — NPS +10 p.p., −8 p.p. de handoff; Santander com copiloto de operador + plataforma que cobre a cobrança) · **Piso da coorte:** **Caixa L2** · **Gap máximo:** **2 níveis** (L4 vs L2 Caixa)

> **Sinal de categoria (o achado desta passada):** o achado do piloto se **confirma e se refina**. Confirma: **4 dos 5 já têm assistente de atendimento generativo** — comoditização de front idêntica à do piloto (BIA/Seven/i.ai lá, GPT-4.1/C6 Assistant/copiloto Santander aqui). Refina, com dois recortes novos: (1) **a fronteira de cobrança se divide por modelo de negócio.** Neobancos (PicPay, C6) empurram GenAI para o **front** (multiagente, resolução); C6, sozinho, empurra GenAI para a **negociação de dívida que fecha acordo** — o análogo do BB no piloto, agora fora do grupo dos 6. Adquirentes (PagBank, Stone) empurram para a **cobrança agêntica** — mas **sobre trilho de terceiro** (Iniciador): Stone é **cliente** do mandato, não dono. É exatamente o padrão que apareceu na passada de pagamentos (F2-3): o L5 agêntico existe no país, mas quem tem o mandato/trilho é um terceiro. (2) **A Caixa (L2, 130 mi+) repete o papel de vale mais profundo** — a maior base social do país sem GenAI resolutiva no atendimento nem cobrança conversacional própria, e é a base sob maior pressão de superendividamento. Nenhum player exibe **L5 próprio** (agente que conduz a cobrança ponta-a-ponta sob mandato — escopo de desconto, limite, política por jurisdição — e formaliza com trilha auditável). Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública específica = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| PicPay | Satisfação após GPT-4.1 no Assistente (multiagente) | **NPS +10 p.p.** nas primeiras horas | Microsoft News Brasil / IT Forum / Blog PicPay · 2026 |
| PicPay | Redução de escalada a humano após GPT-4.1 | **−8 p.p.** de atendimentos direcionados a humano | Microsoft News Brasil / Blog PicPay · 2026 |
| PagBank | Redução de custo no atendimento com IA/chatbot | **−27% de custo** | IT Forum / Consumidor Moderno / TI Inside · 2024–2026 |
| PagBank | Volume de atendimentos pelo chatbot | **~34 mi de atendimentos (2021–2023)** | Portal ClienteSA / TI Inside · 2024 |
| Santander | Valor de negócio projetado com IA (grupo; inclui atendimento/cobrança) | **€1 bi 2026–2028; +400 projetos no BR** | Convergência Digital / Let's Money / Contec Brasil · 2026 |
| Santander | Aceleração de entrega em cobrança (caso Desenrola) | codificação **de meses para ~1 mês** | Mobile Time · 2026 |
| C6 | Escopo do piloto de renegociação de dívida com GenAI | **2 mil → 7 mil clientes** (curto prazo, valores baixos) | Convergência Digital · 2024–2026 |
| Setor (bancos digitais) | Inadimplência de cartão de "neobancos" (contexto) | **7,71% (2021) → 20,31% (2025)** (+163%) | Finsiders Brasil · 2025 |
| Stone | Ganho quantitativo de IA em cobrança agêntica (via Iniciador) | [sem fonte pública específica] | cobrança agêntica confirmada via Iniciador, sem número isolado |
| Caixa | Ganho quantitativo de IA no atendimento/cobrança ao cliente | [sem fonte pública específica] | Aixa é TI interna; atendimento ao cliente sem GenAI/número público |

## ⭐ Diferenciais reais
- **PicPay** — o **número mais duro da coorte** e a arquitetura mais moderna: **multiagente** (agentes por tema + supervisor) sobre GPT-4.1, com **NPS +10 p.p. e −8 p.p. de handoff** medidos. É o caso mais nítido de que orquestração multiagente entrega resultado — e, com isso, de que o custo de inferência do atendimento vira decisão de arquitetura (território de FinOps de inferência).
- **Santander** — o único que trata **conversacional como prioridade estratégica declarada** e junta **copiloto de operador** a uma **plataforma agnóstica** que cobre atendimento, cobrança e risco no mesmo trilho — a jogada de governança + FinOps de inferência feita por incumbente, análoga à Bridge do Bradesco no piloto.
- **C6** — o **mais transacional na cobrança** da coorte: além do C6 Assistant que executa Pix, tem **renegociação de dívida com GenAI que conversa até fechar o acordo e finalizar a transação** — o análogo do BB no piloto, o caso mais próximo de agêntico na negociação de dívida.
- **PagBank/Stone** — **atendimento com número consolidado** (PagBank −27%/34 mi) e **cobrança agêntica de fato** (Stone via Iniciador: agente que lembra, negocia e dispara Pix) — mas **sobre trilho de terceiro**, o que faz do adquirente cliente do mandato, não dono.
- **Caixa** — não é diferencial de IA, é **diferencial de base e de piso**: 130 mi+ no Caixa Tem sob atendimento por regra/assistente virtual sem GenAI resolutiva. O ativo é escala e soberania do dado social, não tecnologia de atendimento.

## 🕳️ O vale (lacuna vendável)
- **Ninguém tem cobrança agêntica governada e própria (L5):** o gargalo de valor é a **recuperação de crédito** (inadimplência +163% em 4 anos), e os dois casos mais avançados da coorte são incompletos — C6 tem GenAI que fecha acordo, mas ainda em piloto de 7 mil clientes; Stone tem cobrança agêntica de verdade, mas **sobre a Iniciador** (é cliente, não dono do mandato). Falta o agente que negocia sob **mandato próprio** — escopo de desconto, limite de parcelamento, política por jurisdição — e **formaliza com trilha auditável**. Cohort aplicado à cobrança, sobre trilho governado.
- **Quem tem o mandato da cobrança agêntica? — o mesmo achado de pagamentos (F2-3):** a cobrança agêntica já existe no país (Stone/Iniciador), mas o **mandato e o trilho são de um terceiro**. Adquirentes de alto volume disparando Pix de cobrança em nome de milhares de lojistas, sem camada própria de escopo/limite/trilha, é **passivo de governança que escala com a operação**. Vender a camada de mandato (Cohort) sobre o trilho de terceiro é o vale mais claro do lado adquirente.
- **Governança da conversa de cobrança é dado sensível puro:** cobrança lida com superendividamento (Lei 14.181), CDC e assédio de cobrança. Um agente conversacional de cobrança sem trilha, sem limite de contato e sem residência de dado é passivo regulatório, não eficiência — e o risco cresce com a autonomia. Exatamente o eixo A do VALE.
- **FinOps do atendimento multiagente vira P&L:** PicPay (multiagente sobre GPT-4.1), PagBank (34 mi de atendimentos), Santander (plataforma agnóstica multi-fornecedor). A escolha de qual agente/modelo responde a cada microtarefa **já é decisão de custo por token** — território de Veltrix (roteamento/observabilidade de inferência), agora com a camada extra de que a orquestração multiagente multiplica as chamadas.
- **Caixa é o vale mais profundo (gap 2):** a maior base social do país (130 mi+) no piso de atendimento por regra, sem GenAI resolutiva nem cobrança conversacional própria — e é a base sob maior pressão de superendividamento. Levar negociação conversacional **governada** a base social sob LGPD/procurement estatal = impacto máximo + fricção máxima. Soberania de dado estatal.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (Assistente PicPay, C6 Assistant e página de renegociação do C6, canais de atendimento/copiloto do Santander, chatbot/central PagBank, atendimento e negociação da Caixa/SINEB). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) com 11 players agora medidos em atendimento, o **assistente generativo é paridade** também na expansão — 4 de 5 têm o seu; o front (tirar dúvida) não diferencia mais e o número que ainda impressiona (PicPay NPS +10 p.p., −8 p.p. de handoff) é sobre a **experiência de front**, não sobre recuperação de dinheiro. (2) O valor migrou, de novo, para a **cobrança** — onde a inadimplência dos digitais subiu +163% em 4 anos — e aqui a coorte se divide: C6 tem GenAI que **fecha acordo** (ainda em piloto de 7 mil), Stone tem **cobrança agêntica de verdade, mas sobre a Iniciador** (cliente, não dono do mandato). O **L5 próprio e governado não existe** — é o mesmo vale de pagamentos: o trilho agêntico é de terceiro, e quem controla escopo/limite/trilha detém a governança. (3) Cobrança sem trilha/limite é passivo regulatório (superendividamento, Lei 14.181, CDC), o que torna **governança de agente pré-condição, não opcional** — e a cobrança agêntica dos adquirentes de alto volume amplia esse passivo. (4) Com PicPay multiagente e PagBank a 34 mi de atendimentos, o **custo de inferência do atendimento virou linha de P&L**, e a orquestração multiagente multiplica as chamadas — a decisão de qual agente responde já é FinOps. (5) A **Caixa (L2, 130 mi+)** é o vale mais profundo — a maior base social, a mais exposta a superendividamento, no piso de atendimento por regra.

---
**Fontes:**
- Convergência Digital — Santander investe €50 mi em IA generativa, Brasil papel-chave: https://convergenciadigital.com.br/mercado/santander-investe-50-milhoes-de-euros-em-ia-generativa-brasil-tem-papel-chave/
- Mobile Time — Conversacional é uma das três prioridades de IA do Santander: https://www.mobiletime.com.br/noticias/01/04/2026/ia-prioridade-santander/
- Contec Brasil — Com estratégia global, Santander acelera uso de IA: https://contec.org.br/com-estrategia-global-santander-acelera-uso-de-ia-e-ja-colhe-frutos/
- Let's Money — Santander libera IA para 185 mil e mira €200 mi em 2026: https://www.letsmoney.com.br/noticias/santander-libera-ia-185-mil-funcionarios-200-milhoes/
- Microsoft News Brasil — PicPay adota GPT-4.1 e entra na era dos multiagentes (NPS +10 p.p., −8 p.p. handoff): https://news.microsoft.com/pt-br/picpay-adota-ia-mais-avancada-do-modelo-gpt-em-seu-assistente-e-entra-na-era-dos-multiagentes/
- IT Forum — PicPay adota GPT-4.1 e aposta em multiagentes: https://itforum.com.br/noticias/picpay-gpt-4-multiagentes/
- Blog PicPay — PicPay adota multiagentes: https://blog.picpay.com/picpay-adota-multiagentes/
- Blog C6 Bank — C6 Bank lança assistente com IA generativa para transações: https://www.c6bank.com.br/blog/c6-bank-lanca-assistente-com-ia-generativa-para-facilitar-transacoes-do-dia-a-dia
- Convergência Digital — C6 Bank usa IA generativa para renegociar dívidas e revisar código: https://convergenciadigital.com.br/mercado/c6-bank-usa-ia-generativa-para-renegociar-dividas-e-revisar-codigo-fonte/
- Startups — C6 Bank lança assistente com IA generativa para transações: https://startups.com.br/negocios/fintech/c6-bank-lanca-assistente-com-ia-generativa-para-transacoes/
- IT Forum — PagBank reduz custos em 27% usando IA no atendimento: https://itforum.com.br/noticias/pagbank-reduz-custos-27-usando-ia-atendimento/
- Consumidor Moderno — PagBank reduz custos em 27% com IA e chatbots: https://consumidormoderno.com.br/pagbank-reduz-custos/
- Portal ClienteSA — PagBank reduz custos em 27% (34 mi de atendimentos): https://portal.clientesa.com.br/pagbank-reduz-custos-em-27-ao-implementar-ia-no-atendimento/
- Vanquish — Pix virou trilho de agentes de IA: o que a Iniciador está construindo (Stone/PagBank clientes): https://www.vanquish.com.br/blog/pix-agentes-ia-iniciador-open-finance
- Let's Money — Iniciador lança o primeiro MCP de pagamentos agênticos via Pix: https://www.letsmoney.com.br/pagamentos/iniciador-lanca-o-primeiro-mcp-de-pagamentos-agenticos-via-pix/
- Infra News Telecom — Caixa e Stefanini iniciam projeto de IA (Aixa, TI interna): https://www.infranewstelecom.com.br/caixa-e-stefanini-inciam-projeto-de-inteligencia-artificial/
- Tek Sapo — Assistente virtual "Caixa" já teve quase um milhão de conversas: https://tek.sapo.pt/noticias/internet/artigos/ja-falou-com-a-caixa-assistente-virtual-ja-teve-quase-um-milhao-de-conversas-com-clientes-do-banco
- Caixa — Canais digitais / WhatsApp: https://www.caixa.gov.br/atendimento/canais-digitais/whatsapp/Paginas/default.aspx
- Finsiders Brasil — Inadimplência em bancos digitais sobe 163% em quatro anos: https://finsidersbrasil.com.br/bancos-digitais/inadimplencia-em-bancos-digitais-sobe-163-em-quatro-anos/

**Liga com:** [[De-Para — Atendimento & cobrança]] (piloto) · [[De-Para — Prevenção a fraude & disputas (Fase 2 · expansão)]] · [[De-Para — Pagamentos & Pix (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
