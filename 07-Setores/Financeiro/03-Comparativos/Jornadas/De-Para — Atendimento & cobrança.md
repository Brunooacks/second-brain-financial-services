---
tipo: jornada-depara
jornada: atendimento
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-04
fontes: [TI Inside, Finsiders, Bloomberg Línea, Convergência Digital, OpenAI, Nu International, IT Forum, CNN Brasil, Mobile Time, SpaceMoney, Let's Money, Mercado Pago Blog]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, atendimento, cobranca, contact-center, delinquent]
---

# 🧭 De-Para — Jornada: Atendimento & cobrança

**Recorte (1 frase):** Como os 6 players-piloto atendem e cobram (dúvida → resolução → escalada humana / negociação de dívida → acordo) num momento em que o assistente de atendimento generativo virou paridade de mercado (BIA, i.ai, Seven, copilotos OpenAI) e a cobrança conversacional com IA passou a mostrar número duro — enquanto a inadimplência dos bancos digitais sobe (cartão de "neobancos" foi de 7,71% em 2021 para 20,31% em 2025, +163%) e transforma recuperação de crédito no ponto de maior valor da jornada.

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
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
| Bradesco | **L4** (GenAI generativa + copiloto de operador; predom. L4) | ~1–2 (BIA no app/site, pré-login parcial) | BIA com 87% de resolutividade e 25 mi de interações; plataforma Bridge (GenAI corporativa com governança única e controle de custo); cobrança com MentorIA (copiloto que gera recomendações diárias ao operador) e Renda BRA (TI Inside · 07/01/2026) |
| Banco do Brasil | **L4** (negociação de dívida conversacional que formaliza acordo; predom. L3) | ~1–2 (WhatsApp) | Negociação de dívida e recuperação de crédito via WhatsApp com IA generativa (AWS + BRQ): conduz da intenção à simulação, formaliza acordo e emite boleto; NiCE Copilot na CXone (resumo, histórico, análise de sentimento) (IT Forum · 2025) |
| Nubank | **L4** (copiloto de call center + resolução generativa; predom. L4) | ~2–3 | Solução OpenAI (GPT-4o / GPT-4o mini) resolve 55% das consultas de nível 1, −70% no tempo de resposta do chat; Call Center Copilot em tempo real usado por +45% dos agentes; ~2 mi de chats/e-mails mensais (OpenAI / Nu International · 2025) |
| Itaú | **L4** (pontual — assistente conversacional GenAI em rollout; predom. L3) | ~2–3 | i.ai (ia.i): agente de IA generativa dentro do app que substitui menus/botões por interface conversacional, em liberação gradual a partir de jun/2026; +84% em projetos de GenAI em 2025 (Mobile Time · 09/06/2026; SpaceMoney · 2026) |
| Inter | **L4** (agente conversacional transacional; predom. L3) | ~2–3 | Seven: agente de IA que esclarece dúvidas sobre +180 produtos e ganhou função transacional (Pix, extrato, parcelamento de fatura por conversa); +11 mi de clientes na 1ª fase, +20 mi de acessos em 2026 (CNN Brasil · 2025; Mobile Time · 2026) |
| Mercado Pago | **L3** (assistente + régua de cobrança por regra/algoritmo; predom. L2–L3) | ~2–3 | Assistente Pessoal (dúvidas, lembretes de pagamento); régua de cobrança automatizada que escolhe canal por perfil (e-mail/SMS/push); sem evidência pública de resolução generativa em escala no atendimento (Mercado Pago Blog · 2025) |

**Líder da jornada:** Bradesco (L4 — atendimento generativo governado + copiloto de cobrança com número) · **Gap máximo:** 1 nível (L4 do bloco líder vs L3 do Mercado Pago)

> **Sinal de categoria:** a jornada convergiu para **L4** — o assistente de atendimento generativo virou commodity (todo player top tem o seu: BIA, i.ai, Seven, copiloto OpenAI) e a fronteira migrou do *front* (tirar dúvida) para dois vetores: (a) **copiloto do operador humano** na cobrança/escalada (Bradesco MentorIA, Nubank Call Center Copilot, BB NiCE), e (b) **negociação transacional que formaliza acordo** (BB no WhatsApp). Nenhum player exibe evidência de **L5** — agente que conduz a cobrança ponta-a-ponta sob mandato (escopo de desconto, limite, trilha auditável) e fecha acordo com autonomia governada. BB é quem mais se aproxima, mas ainda é regra + GenAI com humano no circuito. Gap para o patamar agêntico ≥1 para todos.

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Bradesco | Resolutividade da BIA (cliente) + volume | **87% de resolutividade · +25 mi de interações** | TI Inside, "Com 87% de resolutividade e 25 milhões de interações…" · 07/01/2026 |
| Bradesco | Retenção de demandas no atendimento digital (GenAI) | **até 90%** das demandas retidas | TI Inside, "Com IA generativa, BIA já retém até 90%…" · 11/06/2025 |
| Bradesco | Resolução de atendimentos iniciais (GenAI) | **82%** dos atendimentos iniciais resolvidos | Bloomberg Línea, "IA generativa resolve 82% dos atendimentos iniciais no Bradesco" · 2025 |
| Bradesco | Ganho de IA no crédito sobre o lucro (contexto) | **+R$ 1 bi/ano no lucro** vs 2023 (R$ 250 mi ligados à Kunumi) | Let's Money, "Bradesco vê R$ 1 bi extra no lucro anual com IA" · 2025 |
| Bradesco | Uplift de recuperação com agente de cobrança GenAI | **+10% a 20%** na capacidade de recuperação (autorrelato Febraban Tech; R$ 400 mi de benefício citado — valor a confirmar em fonte primária) | TI Inside (cobertura Febraban Tech) · 06/2025 |
| Banco do Brasil | Conversão em negociação de dívida via WhatsApp com IA | **+306%** de conversão | IT Forum, "BB Tecnologia e Serviços usa IA no WhatsApp…" · 2025 |
| Banco do Brasil | Autonomia da negociação de dívida | **50%** das interações concluídas sem intervenção humana | IT Forum · 2025 |
| Banco do Brasil | Nº médio de parcelas nos acordos (qualidade do acordo) | **33,17 → 14,22 parcelas** | IT Forum · 2025 |
| Nubank | Resolução de consultas de nível 1 (OpenAI) | **55%** resolvidas sem escalar · **−70%** no tempo de resposta do chat | OpenAI, "Nubank eleva a experiência do cliente com a OpenAI" · 2025 |
| Nubank | Adoção do Call Center Copilot pelos agentes | **+45%** dos agentes usam as principais funções | OpenAI / Nu International · 2025 |
| Inter | Alcance da assistente Seven | **+11 mi** de clientes (1ª fase) · **+20 mi** de acessos em 2026 | CNN Brasil · 2025; Mobile Time · 2026 |
| Setor (bancos digitais) | Inadimplência de cartão de "neobancos" (contexto) | **7,71% (2021) → 20,31% (2025)** (+163%) | Finsiders, "Inadimplência em bancos digitais sobe 163% em quatro anos" · 2025 |
| Itaú | Ganho quantitativo de IA no atendimento | [sem fonte pública específica] | i.ai em rollout; sem métrica de resolutividade divulgada (Mobile Time · 2026) |
| Mercado Pago | Ganho quantitativo de IA em atendimento/cobrança | [sem fonte pública específica] | régua de cobrança e Assistente descritos, sem número (MP Blog · 2025) |

## ⭐ Diferenciais reais
- **Bradesco** — o único que junta **escala + governança explícita** na mesma frase: BIA a 87%/25 mi rodando sobre a plataforma Bridge (multi-modelo, governança única, controle de custo). É a jogada de FinOps + governança de inferência feita por um incumbente — território direto de Veltrix.
- **Banco do Brasil** — o mais **transacional na cobrança**: a IA no WhatsApp não só conversa, ela **formaliza o acordo e emite o boleto** e melhora a qualidade do acordo (parcelas caem pela metade). É o caso mais próximo de agêntico na jornada.
- **Nubank** — **copiloto do operador** como padrão (45% dos agentes) e resolução L1 a 55% com modelo econômico (GPT-4o mini) — a leitura de custo por token está embutida na escolha do modelo.
- **Inter** — **Seven transacional**: atendimento que vira execução (Pix, parcelamento por conversa) — apaga a fronteira entre "atendimento" e "operação".
- **Itaú** — aposta na **reimaginação da interface** (i.ai elimina menus) mais do que em número de resolutividade — bet de experiência, ainda sem métrica pública.

## 🕳️ O vale (lacuna vendável)
- **Ninguém tem cobrança agêntica governada (L5):** o gargalo de valor virou a **recuperação de crédito** (inadimplência +163% em 4 anos), e o melhor caso (BB) ainda é regra + GenAI com humano no circuito. Falta o agente que negocia sob **mandato** — escopo de desconto, limite de parcelamento, política por jurisdição — e **formaliza com trilha auditável**. É Cohort aplicado à cobrança.
- **Governança da conversa de cobrança é dado sensível puro:** cobrança lida com superendividamento (Lei 14.181), CDC e assédio de cobrança. Um agente conversacional de cobrança sem trilha, sem limite de contato e sem residência de dado é passivo regulatório, não eficiência. Quanto mais autônoma a cobrança, maior a dívida de governança — exatamente o eixo A do VALE.
- **FinOps do atendimento generativo:** com 25 mi de interações (Bradesco) e 2 mi de chats/mês (Nubank), o **custo de inferência do atendimento** vira linha de P&L. A escolha de modelo (GPT-4o vs mini no Nubank; multi-modelo na Bridge) já é decisão de custo — território de Veltrix (roteamento/observabilidade de inferência).

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (páginas de assistente virtual, canais de atendimento, portais de renegociação de dívida). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) o assistente de atendimento generativo **comoditizou** — todo top-player tem o seu, e a resolutividade de front (82–90%) já não diferencia; (2) o valor migrou para dois lugares onde ainda há gap: **copiloto do operador humano** e **cobrança que formaliza acordo** — e a cobrança é onde está o dinheiro, com inadimplência +163% em 4 anos; (3) BB provou que negociação conversacional entrega número duro (+306% conversão, acordos melhores), mas ninguém subiu ao L5 agêntico governado — e cobrança sem trilha/limite é passivo regulatório (superendividamento, CDC), o que transforma governança de agente em pré-condição, não opcional; (4) a 25 mi de interações, o custo de inferência do atendimento virou linha de P&L — a decisão de qual modelo responde já é FinOps.

---
**Fontes:**
- TI Inside — Bradesco 87%/25 mi interações (07/01/2026): https://tiinside.com.br/07/01/2026/com-87-de-resolutividade-e-25-milhoes-de-interacoes-bradesco-consolida-ia-como-infraestrutura-estrategica/
- TI Inside — BIA retém até 90% (11/06/2025): https://tiinside.com.br/11/06/2025/com-ia-generativa-bia-ja-retem-ate-90-das-demandas-no-atendimento-digital-do-bradesco/
- Bloomberg Línea — IA resolve 82% dos atendimentos iniciais no Bradesco: https://www.bloomberglinea.com.br/negocios/ia-generativa-resolve-82-dos-atendimentos-iniciais-no-bradesco-diz-diretora/
- Let's Money — Bradesco vê R$ 1 bi extra no lucro anual com IA (Kunumi): https://www.letsmoney.com.br/noticias/bradesco-ia-credito-kunumi-250-milhoes
- Convergência Digital — BIA alcança milhões de interações: https://convergenciadigital.com.br/inovacao/bia-a-ia-do-bradesco-alcana-45-milhes-de-interaes/
- IT Forum — BB IA no WhatsApp eleva conversão de negociação em 306%: https://itforum.com.br/noticias/banco-do-brasil-ia-whatsapp/
- OpenAI — Nubank eleva a experiência do cliente: https://openai.com/index/nubank/
- Nu International — estratégia de IA: https://international.nubank.com.br/pt-br/consumidores/nubank-inicia-testes-com-inteligencia-artificial-generativa-para-aprimorar-experiencia-do-cliente-com-uso-de-credito/
- Mobile Time — Itaú i.ai (09/06/2026): https://www.mobiletime.com.br/noticias/09/06/2026/itau-iai/
- SpaceMoney — Itaú i.ai elimina menus e botões: https://www.spacemoney.com.br/tecnologia/itau-i-ai-banco-testa-ia-que-elimina-menus-e-botoes/
- CNN Brasil — Inter assistente Seven: https://www.cnnbrasil.com.br/economia/negocios/conheca-a-seven-nova-assistente-de-ia-do-super-app-do-inter/
- Finsiders — Inadimplência em bancos digitais sobe 163%: https://finsidersbrasil.com.br/bancos-digitais/inadimplencia-em-bancos-digitais-sobe-163-em-quatro-anos/
- Mercado Pago Blog — assistentes financeiros digitais / IA na rotina: https://www.mercadopago.com.br/blog/assistentes-financeiros-digitais-gestao-negocio

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[De-Para — Prevenção a fraude & disputas]] · [[De-Para — Originação de crédito]]
