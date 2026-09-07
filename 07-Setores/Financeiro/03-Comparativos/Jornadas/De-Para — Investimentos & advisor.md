---
tipo: jornada-depara
jornada: investimentos
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-04
fontes: [CNN Brasil, NeoFeed, Finsiders Brasil, Consumidor Moderno, IA na Prática, Ágora Investimentos, Inter, Jornal do Brás, Baguete, Mercado Pago Blog]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, investimentos, advisor, wealth, suitability]
---

# 🧭 De-Para — Jornada: Investimentos & advisor

**Recorte (1 frase):** Como os 6 players-piloto conduzem a jornada de investir (descoberta → perfil/suitability → recomendação → alocação → acompanhamento) no momento em que o *advisor* deixa de ser tela de recomendação e vira **assessor generativo conversacional** — Itaú abrindo o "Inteligência de Investimentos Itaú" para 100 mil clientes e Nubank reposicionando o serviço como "AI Private Banker" — mas ninguém cruza a parede regulatória do L5 (agente que executa a carteira sob mandato), o que faz desta a primeira jornada do piloto onde a fronteira **ainda não comoditizou** e o gargalo é governança (suitability CVM, dever fiduciário, conflito de interesse na recomendação).

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
1. **Descoberta/educação** — conteúdo, curadoria de produtos, "onde investir".
2. **Perfil/suitability** — questionário de perfil de investidor (apetite a risco, horizonte) — camada regulada (CVM).
3. **Recomendação** — sugestão de produtos/carteira alinhada ao perfil (analista humano → modelo → GenAI conversacional).
4. **Alocação/execução** — aporte, montagem da carteira (self-service → robo-advisor → agente).
5. **Acompanhamento/rebalanceamento** — monitoramento e ajuste da carteira ao longo do tempo.
6. **Advisory contínuo** — relacionamento consultivo (historicamente restrito à alta renda; foco da democratização com IA).

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Itaú | **L4** (assessor de investimentos GenAI conversacional; predom. L3) | ~2–3 (curadoria pública/íon; agente é logado) | "Inteligência de Investimentos Itaú": 1ª IA generativa conversacional dedicada a investimentos, assessoria hiperpersonalizada 24/7, dá opção de produto dentro do apetite a risco e otimiza portfólio; acesso ampliado para **100 mil** clientes do Superapp em 02/12/2025, rollout gradual até 2026 (CNN Brasil · 25/11/2025; NeoFeed · 2025) |
| Nubank | **L4** (pontual — "AI Private Banker" em construção/rollout; predom. L3) | ~2–3 | Assistente financeiro pessoal ("AI Private Banker") que sugere decisões de gastos, crédito e **investimentos**, democratizando aconselhamento antes restrito à alta renda; funcionalidades já usadas por **~15 mi** de MAU; anúncio 10/06/2026, sem data de lançamento (Finsiders · 15/06/2026) |
| Inter | **L3** (robo-advisor por algoritmo + Seven conversacional; gestão de investimentos no roadmap) | ~2–3 | Robô Advisor monta e rebalanceia carteira por perfil automaticamente; Seven (agente de IA) **passará a** fazer gestão de investimentos com sugestões de aporte calibradas ao perfil — função anunciada, ainda não liberada (Inter · robo-advisor; CNN Brasil · 2025; Jornal do Brás · 2025) |
| Bradesco | **L3** (ML + BIA recomenda produtos; curadoria de carteira é humana) | ~1–2 (BIA/Ágora pré-login parcial) | BIA assumiu recomendação de produtos; Ágora Investimentos publica 5 carteiras recomendadas elaboradas **mensalmente por analistas** (humano); BIA acessada por ~500 mil clientes (Consumidor Moderno · 2025; IA na Prática · 2025; Ágora · 2025) |
| Banco do Brasil | **L3** (recomendação personalizada + GenAI em carteira MPE; advisory PF por pesquisa humana) | ~2–3 | "Dicas Personalizadas" (PF) e área de **recomendações inteligentes com IA generativa** para carteira de micro e pequenas empresas; ações recomendadas 2026 no app Investimentos BB (research humano); portfólio de 500 soluções de IA em 10 anos (Baguete · 2025) |
| Mercado Pago | **L2** (rendimento automático + personalização por regra/perfil; sem advisor GenAI) | ~2–3 | Rendimento automático (money box/CDB), organização de finanças e "recomendações de investimento de acordo com o perfil"; sem evidência pública de assessor generativo em escala (Mercado Pago Blog · 2025) |

**Líder da jornada:** Itaú (L4 — assessor GenAI dedicado, em escala de 100 mil e crescendo) — empate técnico de patamar com Nubank (L4 pontual, em rollout) · **Gap máximo:** 2 níveis (L4 do líder vs L2 do Mercado Pago)

> **Sinal de categoria — a exceção do piloto:** diferentemente de pagamentos, fraude e atendimento (que já convergiram para L4 e comoditizaram), a jornada de **investimentos ainda está em disputa aberta**. Só Itaú opera um assessor GenAI dedicado em escala pública declarada, e Nubank ainda está montando o dele ("AI Private Banker" sem data). O resto é robo-advisor por regra (Inter), recomendação por ML + curadoria humana (Bradesco, BB) ou rendimento simples (MP). **Ninguém chega ao L5**: nenhum player exibe agente que *executa e rebalanceia a carteira ponta-a-ponta sob mandato* (escopo de risco, limite de alçada, trilha auditável) com autonomia governada. E aqui a parede não é técnica — é **regulatória**: a fronteira entre "recomendar" (suitability, CVM Res. 30) e "gerir com discricionariedade" (gestão autorizada) é jurídica, e o dever de suitability + conflito de interesse (recomendar o fundo da própria casa) travam o salto. Gap para o patamar agêntico ≥1 para todos, inclusive o líder.

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Itaú | Base habilitada ao assessor de IA de investimentos | **100 mil** clientes do Superapp (após +40 mil em 02/12/2025), rollout gradual até 2026 | CNN Brasil, "Itaú amplia acesso a agente de investimentos de IA para 100 mil clientes" · 25/11/2025 |
| Itaú | Escala de IA no banco (contexto) | **+1.800 modelos** de IA em uso · **~500 cientistas** de dados (3T25) | CNN Brasil (via Broadcast/Estadão) · 25/11/2025 |
| Nubank | Adoção de funcionalidades do assistente financeiro (pré-"AI Private Banker") | **~15 mi** de usuários ativos por mês já usam funcionalidades | Finsiders, "Nubank prepara assistente financeiro com IA para clientes" · 15/06/2026 |
| Nubank | Leitura de mercado sobre a aposta AI-first (contexto) | Potencial de alta **>80%** nas ações (relatório BTG no dia do anúncio) | Finsiders · 15/06/2026 |
| Inter | Alcance da assistente Seven (canal do futuro advisor) | **+11 mi** clientes na 1ª fase · **+20 mi** acessos em 2026 | CNN Brasil · 2025; Jornal do Brás · 2025 |
| Bradesco | Alcance da BIA (canal que recomenda produtos) | **~500 mil** clientes acessam · **40 mil** funcionários usam (copiloto) | IA na Prática · 2025; Consumidor Moderno · 2025 |
| Bradesco | Cadência da recomendação de carteira (Ágora) | **5 carteiras** recomendadas, revisadas **mensalmente** por analistas | Ágora Investimentos, "Carteiras Recomendadas" · 2025 |
| Banco do Brasil | Acervo de IA aplicada (contexto) | **500 soluções** de IA/big data em 10 anos; recomendações GenAI p/ carteira MPE | Baguete, "Banco do Brasil: 10 anos de investimentos em IA e big data" · 2025 |
| Mercado Pago | Ganho quantitativo de IA em advisory/investimentos | [sem fonte pública específica] | rendimento automático e "recomendações por perfil" descritos, sem número (MP Blog · 2025) |

## ⭐ Diferenciais reais
- **Itaú** — o único com **assessor GenAI conversacional dedicado a investimentos em produção declarada** (não é chatbot de atendimento que "também fala de investimento"): cura produtos, respeita apetite a risco e otimiza portfólio, rodando sobre base de +1.800 modelos. É wealth management de bancão sendo reembalado como produto digital de massa.
- **Nubank** — a jogada de **narrativa**: reposiciona advisory como "AI Private Banker" e ataca explicitamente a *democratização* (levar à massa o que era da alta renda). Mesmo sem lançar, 15 mi de MAU já tocam funcionalidades — distribuição é o ativo.
- **Inter** — o único com **robo-advisor por algoritmo já executando** alocação/rebalanceamento automático, e com o canal (Seven) pronto para virar o front conversacional do advisor. Tem o "braço executor" que os outros não têm — falta plugar a inteligência generativa.
- **Bradesco / BB** — força de **casa de asset e research** (carteiras de analista, BB Asset/Bradesco Asset entre as maiores do país): profundidade de conteúdo e track record que neobanco não tem, mas ainda entregue por curadoria humana + ML, não por advisor agêntico.
- **Mercado Pago** — aposta em **simplicidade/rendimento automático** para o público que nunca investiu; advisory sofisticado não é o jogo dele (ainda).

## 🕳️ O vale (lacuna vendável)
- **Ninguém tem advisor agêntico governado (L5):** todos param em "recomendar, humano decide/aloca" — inclusive o líder. Falta o agente que **executa e rebalanceia sob mandato** (escopo de risco, limite de alçada por classe de ativo, trilha auditável de cada decisão) dentro da fronteira regulatória. É Cohort aplicado a wealth — e o desenho do mandato **é** o produto, porque a linha "recomendação × gestão discricionária" é o que separa o legal do ilegal.
- **A camada de suitability está descolada do advisor:** o assessor no topo é L4 (conversa, personaliza), mas o **suitability embaixo segue L2** (questionário fixo de perfil, CVM). Um advisor generativo sofisticado apoiado em perfil estático é passivo regulatório: recomenda com fluência sobre uma base de adequação pobre. Modernizar o suitability para dinâmico e explicável é vale de modernização com peso de governança direto.
- **Explicabilidade e conflito de interesse são o calcanhar:** quando a IA recomenda a milhões, "por que este produto?" precisa de resposta auditável — e o viés de recomendar o **fundo da própria casa** vira risco supervisório (CVM/Bacen) e reputacional. Advisor sem trilha de explicação + sem separação de conflito é escala de risco, não de receita — exatamente o eixo A do VALE.
- **FinOps do advisory generativo:** advisory hiperpersonalizado 24/7 para 100 mil (Itaú) e potencialmente dezenas de milhões (Nubank) faz o **custo de inferência por interação consultiva** virar linha de P&L — e advisory é conversa longa e cara. Roteamento de modelo por complexidade da pergunta é território de Veltrix.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (páginas do "Inteligência de Investimentos Itaú", Robô Advisor Inter, carteiras recomendadas Ágora, páginas de investimentos NuInvest/BB/MP). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) esta é a **primeira jornada do piloto que ainda NÃO comoditizou** — só Itaú tem advisor GenAI dedicado em escala declarada (100 mil), Nubank está montando o dele, e o resto ainda é robo-advisor/ML+curadoria humana; a janela competitiva está aberta; (2) o teto de todos é o mesmo e é **regulatório, não técnico**: a fronteira "recomendar × gerir com discricionariedade" (suitability CVM Res. 30, dever fiduciário, gestão autorizada) segura o L5 — quem desenhar primeiro o **mandato governado** de advisor agêntico ganha a categoria; (3) há um descolamento perigoso — **advisor L4 sobre suitability L2** (perfil por questionário fixo), o que transforma fluência generativa em risco de adequação; (4) o **conflito de interesse** (recomendar o fundo da própria casa) e a **explicabilidade** da recomendação a milhões são o passivo supervisório central — governança de advisor não é opcional, é a licença para operar; (5) a 100 mil–dezenas de milhões de conversas consultivas, o **custo de inferência do advisory** vira P&L, e advisory é a conversa mais longa e cara do banco.

---
**Fontes:**
- CNN Brasil — Itaú amplia acesso a agente de investimentos de IA para 100 mil clientes (25/11/2025): https://www.cnnbrasil.com.br/economia/negocios/itau-amplia-acesso-a-agente-de-investimentos-de-ia-para-100-mil-clientes/
- NeoFeed — Itaú "aplica" na IA generativa como agente de investimentos: https://neofeed.com.br/wealth-management/itau-aplica-na-ia-generativa-como-agente-de-investimentos/
- Itaú — Inteligência de Investimentos: https://www.itau.com.br/investimentos/inteligencia-de-investimentos
- Finsiders — Nubank prepara assistente financeiro com IA ("AI Private Banker") (15/06/2026): https://finsidersbrasil.com.br/bancos-digitais/nubank-reforca-uso-da-ia-como-camada-estrategica-no-credito/
- Inter — Robô Advisor: https://inter.co/robo-advisor/
- CNN Brasil — Inter lança assistente de IA (Seven) para apoiar gestão financeira: https://www.cnnbrasil.com.br/economia/negocios/inter-lanca-assistente-de-ia-para-apoiar-gestao-financeira-no-aplicativo/
- Jornal do Brás — Inter lança Seven e inaugura nova era dos agentes de IA: https://jornaldobras.com.br/noticia/119494/inter-lanca-seven-coloca-o-cliente-no-comando-do-proprio-banco-e-inaugura-nova-era-dos-agentes-de-ia
- Consumidor Moderno — Bradesco: inovação e inteligência artificial: https://consumidormoderno.com.br/revista/bradesco-inovacao-e-inteligencia-artificial/
- IA na Prática — BIA Tech: a evolução da IA no Bradesco: https://iaempratica.com.br/aplicacao-pratica/bia-tech-a-evolucao-da-inteligencia-artificial-no-bradesco/
- Ágora Investimentos — Carteiras Recomendadas: https://conteudo.agorainvestimentos.com.br/carteiras-recomendadas/
- Baguete — Banco do Brasil: 10 anos de investimentos em IA e big data: https://www.baguete.com.br/noticias/banco-do-brasil-10-anos-de-investimentos-em-ia-e-big-data
- Mercado Pago Blog — Investimentos e IA: como a tecnologia te ajuda a investir: https://www.mercadopago.com.br/blog/papel-inteligencia-artificial-investimentos

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[De-Para — Atendimento & cobrança]] · [[De-Para — Originação de crédito]]
