---
tipo: refresh
setor: financeiro
camada: transversal (Jornadas + Produtos)
data: 2026-08-31
janela_coberta: 2026-07-12 → 2026-08-31
players: 11
status: coleta concluída · teses ⏳ para o Bruno
tags: [refresh, discovery, 2T26, eu-ai-act, governanca, rotina-noturna]
---

# 🔄 Refresh 2T26 + frame regulatório — delta desde 12/07/2026

> **Por que esta passada existe.** As duas trilhas (Jornadas e Produtos) estão esgotadas desde 12/07. Desde então foram **37 passadas consecutivas sem alvo**, e em todas elas a própria rotina registrou no Log a recomendação **(d): passada de refresh 2T26 + reclassificação EMA-J contra o frame regulatório vigente** — descrita como "a única atacável sem nova decisão de escopo". Esta é a execução de (d): **mesmos 11 players, mesmas categorias, só dado novo**. Nenhuma jornada, categoria ou player novo foi aberto — isso segue sendo decisão do Bruno.
>
> Regra mãe respeitada: **coleta automatizada, tese não**. Todo "o que eu diria num board" abaixo está ⏳.

---

## ⚠️ Correção de premissa — o acervo (e o próprio Log) estavam errados

Por **20 passadas seguidas** o Log dos dois ledgers repetiu que *"o EU AI Act está em vigência plena para alto risco desde 02/08/2026"* e que, por isso, o acervo descrevia "o mundo pré-vigência". **Isso não se confirmou.**

O **Regulamento (UE) 2026/1744** ("AI Omnibus"), de 08/07/2026, publicado no JO em 24/07/2026 e em vigor desde **27/07/2026**, alterou o AI Act e **adiou as obrigações do Capítulo III**:

| Categoria | Prazo antigo | **Prazo vigente** |
|---|---|---|
| Alto risco **Anexo III** (inclui credit scoring 5(b) e precificação de seguro de vida/saúde 5(c)) | 02/08/2026 | **02/12/2027** |
| Alto risco **Anexo I** (embarcado em produto) | 02/08/2027 | **02/08/2028** |

O que **de fato** passou a valer em 02/08/2026 é o **Art. 50 (transparência)**: informar que há interação com IA (chatbot), marcação legível por máquina de conteúdo sintético, rotulagem de deepfake e de texto de interesse público. Multa até **€15 mi ou 3% do faturamento global**. Há *grace period* de marcação até **02/12/2026** para sistemas colocados no mercado antes de 02/08/2026.

Gatilho de extraterritorialidade para instituição brasileira segue o **Art. 2(1)(c)**: alcança quem está fora da UE quando **o output do sistema é usado na União** — não exige estabelecimento lá.

> **Implicação de coleta (não é tese):** a janela de adequação de crédito e seguro alargou em ~16 meses, mas a obrigação que hoje pega **todo assistente conversacional de banco** (ia.i, BIA, Seven, Mago, C6 Assistant, plugin do PicPay) é a de **transparência**, que já está valendo. O acervo classificou risco pelo eixo errado.
>
> ⏳ **O que eu diria num board:** para o Bruno.

**Fontes:** ✅ **datas verificadas em fonte institucional (Comissão Europeia) na passada de 31/08 22h — ver seção 4** · [Comissão Europeia — AI Omnibus enters into force, 27/07/2026](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) · [EUR-Lex, Reg. (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) · [White & Case, 04/08/2026](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act) · [Cooley, 03/08/2026](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026) · [Anexo III](https://artificialintelligenceact.eu/annex/3/) · [Art. 2](https://artificialintelligenceact.eu/article/2/)

---

## 1. Frame regulatório BR — o que mudou na janela

| Data | Marco | Efeito sobre o acervo |
|---|---|---|
| 31/07/2026 | **CVM cria a Ditec** (Res. CVM 246) — divisão de tecnologia financeira e IA, vigência imediata | ✅ **Verificado em fonte institucional (§4.3).** Primeiro órgão de estrutura dedicado a IA num regulador de mercado BR. É estrutura interna, **não norma de conduta** — e o escopo de IA é o **uso de IA dentro da própria Autarquia**, não conduta do regulado. |
| 02/08/2026 | **Art. 50 do AI Act** em aplicação | Ver correção acima. |
| 10/08/2026 | Pix: mudanças em notificação de infração e análise de recuperação de valores, com indicação da **etapa do percurso do dinheiro** | Reforça o achado de fraude ("MED é o vale"): o rastreio em cadeia virou infraestrutura. |
| 12/08/2026 | **SUSEP abre Tomada de Subsídios do Plano de Regulação 2027** (Brasil Participativo) | Janela aberta para propor IA em subscrição/sinistro na agenda 2027 — conecta direto com o achado de Seguros. |
| 21/08/2026 | **ANPD notifica 22 plataformas**, incluindo ferramentas de GenAI (ChatGPT, Claude, Gemini, Copilot, Meta AI, Perplexity) | Objeto é ECA Digital/Marco Civil, não crédito — mas mostra a ANPD **operando** sobre GenAI. |
| 24/08/2026 | **PL 2338/2023 adiado** — relator sinaliza votação só no fim de 2026, após as eleições | O marco legal brasileiro de IA **não sai antes de 2027**. |
| 01/09/2026 | MED: prazo de contestação de devoluções sobe de **30 → 80 dias** | Alonga o ciclo de disputa que o acervo já apontava como o SD mais atrasado (L2–L3). |
| ~~01/11/2026~~ → **01/10/2026** | ⚠️ **CORRIGIDO (ver §4.3).** **IN BCB 746/2026** (16/06/2026, DOU 17/06) **não trata de dispositivo não cadastrado**: altera a IN BCB 512/2024, **revoga o tratamento próprio de limites do Pix por aproximação** e traz o **Pix Automático** para a gestão de limites. | O limite de R$ 200/R$ 1.000 é da **Res. BCB 403/2024, em vigor desde 01/11/2024** — é piso vigente há 2 anos, **não prazo futuro**. O que muda em 01/10/2026 é o Pix Automático entrar na gestão de limites. |
| Nov/2026 | Consignado público federal via Open Finance ao público (testes em ago/2026); BC promete novidades de **Pix Parcelado** | Confirma a iniciativa "trilho soberano de consignado" (F2-2). |
| 31/12/2026 | **Res. Conjunta CMN/BCB nº 18, de 28/11/2025**: política formal de qualidade das informações reportadas ao BCB | ✅ **Verificado (§4.3).** Pré-requisito prático de governança de modelo — prazo dentro do horizonte de venda. **12 dimensões de qualidade, diretor responsável perante o BCB, responsabilidade indelegável do CA, dicionário de dados e relatório semestral.** |

**Sinais sem norma (relevantes, mas ainda declaração):**

- **Comef (ata 65, mai/2026)** elevou IA a risco sistêmico cibernético: "não há evidências de ataques totalmente conduzidos por tais modelos até o momento", mas a aceleração "pode elevar riscos sistêmicos".
- **BC desenvolve score de risco de fraude transacional com ML/IA** para compartilhar com participantes do Pix a probabilidade de uma transação ser fraudulenta (Breno Lobo, Decem/BC, 29/07/2026). **Volume de MED: 1,2–1,3 mi/mês em set/2025 → 3,5 mi em jan/2026 → média atual 2,7–2,8 mi/mês.**
- **Pix Automático: 1 mil recebedores no fim de 2025 → 14 mil em ago/2026**; o BC classifica como "processo de teste ainda" (Márcia Vicari, Febraban Tech, 24/08/2026). O acervo registrava obrigatoriedade em mar/26 — **a adoção real está muito abaixo do que a obrigatoriedade sugeria**.
- **Nenhuma norma do BC sobre pagamentos agênticos** até 31/08/2026. `[sem fonte]`
- **Nenhuma norma da ANPD sobre o art. 20 da LGPD** — segue só a Nota Técnica 12/2025 da Tomada de Subsídios. IA está entre os 4 eixos prioritários de fiscalização do biênio 2026-2027 (75 fiscalizações, mapa de 24/12/2025).
- **Nenhuma norma da SUSEP ou da CVM dedicada a IA.** Robo-advisor segue sob CVM 19 e 21/2021.

**Fontes:** [Finsiders 31/07/2026 (MED/BC)](https://finsidersbrasil.com.br/pagamentos/pix/com-med-2-0-bc-quer-diminuir-falsos-positivos-e-rastrear-laranjas/) · [Finsiders 25/08/2026 (Pix Automático)](https://finsidersbrasil.com.br/pagamentos/pix/bc-ve-maior-adocao-do-pix-automatico-nos-proximos-meses/) · [Finsiders 31/07/2026 (Ditec)](https://finsidersbrasil.com.br/inovacao/cvm-cria-divisao-dedicada-a-tecnologia-financeira-e-ia/) · [Mobile Time 24/08/2026 (PL 2338)](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) · [Ata 65 Comef](https://www.bcb.gov.br/content/publicacoes/atascomef/202606/Ata_65_Comef_pt.pdf) · [SUSEP CP 2027](https://www.gov.br/susep/pt-br/central-de-conteudos/noticias/2026/agosto/susep-abre-tomada-de-subsidios-para-o-plano-de-regulacao-2027) · [ANPD 22 plataformas](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-avalia-como-plataformas-digitais-atuam-para-prevenir-conteudos-criminosos-e-proteger-criancas-e-mulheres-na-internet)

---

## 2. Delta por player — 2T26 + IA (jul–ago/2026)

### Incumbentes

**Itaú** — Lucro recorrente **R$ 12,4 bi** (+7,8% a/a), ROE 24,3%, NPL 90d 1,9%, carteira R$ 1,5 tri (04/08/2026). **Delta de IA, o maior do período:** lançou a **ia.i** em 27/07 para 300 mil clientes (conversacional, voz/texto/imagem, executa transação) e no Febraban Tech (24/08) Maluhy anunciou salto de **300 mil → 3 milhões de clientes atendidos por IA, com meta de 100% da base até o fim de 2026**. Arquitetura revelada: plataforma proprietária **"Iara"**, gateway que roteia entre LLMs de mercado e **motores proprietários da NeoSpace** (adquirida) — para dado interno do cliente "a inteligência é totalmente nossa". Guerra (CTO): *"o custo de IA pode explodir se não houver gestão, de forma semelhante ao que vimos na migração para a nuvem"*; transações simples são resolvidas por ML interno **para evitar pagamento desnecessário de tokens**. Tem **camada de verificação de factualidade em tempo real** antes de exibir a resposta. Investiu **>R$ 11 bi em tecnologia entre 2024 e 2025**.
[Capitalizo 05/08](https://capitalizo.com.br/noticias-20260805-itau-unibanco-itub3-itub4-lucro-liquido-recorrente-atinge-r-124-bilhoes-com-roe-de-243-no-2t26/) · [Mobile Time 27/07](https://www.mobiletime.com.br/noticias/27/07/2026/itau-copiloto-ia-i-ai/) · [Exame Insight 28/07](https://exame.com/insight/com-nova-plataforma-proprietaria-de-ia-cto-do-itau-estima-escala-inedita-no-uso-de-agentes/p) · [Convergência Digital 24/08](https://convergenciadigital.com.br/mercado/febraban-tech-2026-inteligencia-artificial-mudou-a-maneira-dos-bancos-fazer-negocios/)

**Bradesco** — Lucro recorrente **R$ 7,05 bi** (+16,2% a/a), ROAE 16,2%, carteira R$ 1,14 tri, **NPL 90d 4,3%** (06/08/2026). **Delta de IA:** BIA fez **~74 mi de transações no 1S26** e acumula **3 bi de interações em 10 anos**; opera como "BIA GenAI" no app e no WhatsApp. **BIA Tech** (GenAI de engenharia) usada por **~8 mil desenvolvedores**. A **Kunumi** (100% Bradesco, 100+ PhDs) desenvolve **modelo fundacional próprio**, computação quântica e **hardware para acelerar IA** — delta forte sobre o case de crédito de R$ 250 mi já no acervo. A plataforma **Bridge integra todos os LLMs de mercado**; modelo declarado é **"human on the loop"**. Noronha (24/08): *"Ética, reputação, responsabilidade institucional. Não dá para delegar para a máquina. Quem responde criminalmente, civilmente, são as pessoas."*
[Mercado&Consumo 06/08](https://mercadoeconsumo.com.br/06/08/2026/mc-capital/lucro-liquido-recorrente-do-bradesco-cresce-162-e-atinge-r-705-bilhoes-no-2o-trimestre/) · [Convergência Digital 25/08](https://convergenciadigital.com.br/mercado/bradesco-investe-em-hardware-para-acelerar-inteligencia-artificial/) · [Finsiders 24/08](https://finsidersbrasil.com.br/tecnologia-para-fintechs/bancos-admitem-que-ainda-nao-entregam-autonomia-total-a-ia/)

**Banco do Brasil** — Lucro ajustado **R$ 3,908 bi** (+3,3% a/a), **ROE 8,3%**, carteira R$ 1,313 tri, **NPL 90d 5,61%** (era 3,96% um ano antes; cartão saltou de 7,1% → **14,58%** em um trimestre) (12/08/2026). **Delta de IA — o mais material do período para a tese de governança:** lançou o **App 5.0** no Febraban Tech (arquitetura agêntica, jornadas conversacionais por voz/texto, 100% da base até fim de set/2026) e **publicou diretrizes próprias para IA generativa e agêntica**, com **certificação de modelos, definição de níveis de autonomia, rastreabilidade, governança de agentes, responsabilidade sobre decisão automatizada, mecanismos de interrupção ("kill switch"), autonomia faseada com supervisão humana em situações críticas e restrição de GenAI em ambiente com dado sensível**. Marisa Reghini (25/08): *"a sociedade está na transição dos negócios digitais para os autônomos"*, é preciso "construir infraestruturas de segurança para bancos, humanos e agentes" — identidade, delegação e autenticidade que "nenhum player resolve sozinho".
[Genial 2T26](https://analisa.genialinvestimentos.com.br/acoes/banco-do-brasil/banco-do-brasil-bbas3-resultado-2t26-agro-estabiliza-mas-pressao-migra-para-pessoa-fisica/) · [Convergência Digital 26/08](https://convergenciadigital.com.br/mercado/banco-do-brasil-lanca-app-5-0-e-atualiza-diretrizes-para-ia-generativa-e-agentica/) · [Startups 25/08](https://startups.com.br/negocios/inteligencia-artificial/agentes-de-ia-colocam-maiores-bancos-do-pais-diante-de-novo-dilema/)

**Santander Brasil** — Lucro gerencial recorrente **R$ 3,0 bi** (−17,6% a/a), **ROE 12,5%** (abaixo da Selic), carteira R$ 715 bi, NPL 90d **3,3%** (+0,7 p.p.) (29/07/2026). **Delta de IA:** meta reexpressa — **>R$ 6 bi de valor com IA até 2028 no grupo, com R$ 500 mi já registrados nos primeiros seis meses** (Richard Silva, CIO BR / CEO F1RST, 25/08). Governança: *"a governança é a direção que permite acelerar mais sem sair da pista"* — só atrapalha quando chega tarde; sobre risco de modelo: *"quando ela erra, erra com muita convicção"*. **Nenhum lançamento de produto de IA no Brasil na janela.** `[sem fonte]` para atualização dos 400+ projetos, do ganho de ~95% em contestação de fraude e da G42 no stack.
[InfoMoney 2T26](https://www.infomoney.com.br/mercados/santander-sanb11-resultados-segundo-trimestre-2026/) · [Startups 25/08](https://startups.com.br/negocios/inteligencia-artificial/agentes-de-ia-colocam-maiores-bancos-do-pais-diante-de-novo-dilema/)

**Caixa** — Lucro recorrente **R$ 3,9 bi** (+5,9% a/a), **ROE 9,16%**, carteira **R$ 1,448 tri** (imobiliária R$ 1,005 tri, ~68% de share habitacional), **NPL 90d 3,64%** (era 2,66%), provisões +97,6% a/a (26/08/2026). **Delta de IA — contradiz parcialmente o "vale sem case público" do acervo:** lançou o **SuperApp em beta para 300 mil clientes** (Android), com onboarding biométrico que eliminou ida à agência; **copiloto de IA liberado a 100% dos empregados**; foco declarado de agentes é **processo interno**. A **assistente ao cliente ainda NÃO transaciona** ("muito em breve"). Darlan Lins (25/08): *"temos segurança operacional para disponibilizar aos clientes agentes de IA que executem transações de forma confiável?"* — num banco com **160 milhões de clientes**, e cita **suitability como camada adicional de proteção**. Carlos Vieira (24/08): "há três anos era uma selva analógica".
[Agência Brasil 26/08](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/lucro-da-caixa-cresce-59-e-chega-r-39-bi-no-segundo-trimestre) · [Convergência Digital 25/08](https://convergenciadigital.com.br/mercado/superapp-da-caixa-unifica-todos-os-servicos-ao-correntista/) · [Startups 25/08](https://startups.com.br/negocios/inteligencia-artificial/agentes-de-ia-colocam-maiores-bancos-do-pais-diante-de-novo-dilema/)

### Digitais e adquirentes

**Nubank** — Lucro **US$ 1,1 bi** (+49% a/a, 1º trimestre acima de US$ 1 bi), ROE 33%, **139 mi de clientes globais** (~118 mi BR; era 112 mi no acervo), carteira US$ 39,4 bi, **NPL 90d 6,9%** (+35 bps) (13/08/2026). **Delta de IA:** o **nuFormer saiu do laboratório** — nova versão **quadruplicou contexto, velocidade de treino e de inferência e reduziu o custo de rodar em produção**, e está **em produção em três carteiras** (cartão BR e MX, crédito sem garantia BR), com PJ e cartão na Colômbia em teste. Modelo em produção com **330 mi de parâmetros**, treinado sobre **100 bi de transações / 600 bi de tokens**. **Agentes conduzem >60% das conversas de atendimento no Brasil** (era 55% de resolução L1). Novo segmento **Croma** (jul/2026) estreia "Conta Inteligente" com recomendação por IA. **AI Private Banker segue sem data** — funcionalidades tocam 15 mi de MAU. Livia Chanes (Febraban Tech): engenharia com **~90% de aumento de capacidade de desenvolvimento de código**.
[Release 2T26 Nu](https://international.nubank.com.br/pt-br/companhia/nu-holdings-ltd-divulga-resultados-financeiros-do-segundo-trimestre-de-2026/) · [TI Inside 25/08](https://tiinside.com.br/25/08/2026/do-cliente-a-seguranca-nubank-defende-uso-amplo-da-ia-nos-bancos/)

**Inter** — Lucro **R$ 421 mi** (+34% a/a; fonte alternativa reporta R$ 447 mi gerencial), ROE 16,3%, **45,3 mi de clientes**, carteira R$ 55,4 bi (+29%), **NPL 90d 5,3%** (05-06/08/2026). **Delta de IA — mudança de arquitetura de governança:** a **Seven 2.0** migra de **múltiplos agentes com governança descentralizada para um agente único centralizado**, previsto para o **3T26**. Números da v1 em 2026: **38 mi de conversas por texto, 7 agentes, 91 ferramentas, 20 mi de acessos**.
[Capitalizo 06/08](https://capitalizo.com.br/noticias-20260806-banco-inter-intr-inbr32-avanco-na-rentabilidade-com-roe-recorde-e-escala-da-carteira-no-2t26/) · [Mobile Time 20/08](https://www.mobiletime.com.br/noticias/20/08/2026/seven-banco-inter-v2/)

**Mercado Pago** — **TPV US$ 101 bi** (+56% a/a; era US$ 83,7 bi), **88 mi de MAU** (+30%), carteira **>US$ 16 bi** (+75%), AUM US$ 23 bi; MELI com receita >US$ 10 bi e lucro US$ 466 mi (~06-07/08/2026). **Delta de IA:** lançou o **"Mago"**, personal banker de IA (14/08), evolução do assistente de out/2025 — **o assistente alcançou 17 mi de pessoas**. Executa Pix e paga boleto por voz, simula cenários, organiza contas, "sempre preservando o controle e a decisão final do cliente"; a nova versão amplia IA na **prevenção de fraude e golpe**.
[Mobile Time LA 10/08](https://mobiletime.la/noticias/10/08/2026/mercado-libre-2q26/) · [TI Inside 14/08](https://tiinside.com.br/14/08/2026/mercado-pago-libera-nova-ia-para-17-milhoes-de-clientes/)

**C6 Bank** — (divulga semestral) Lucro **R$ 1,25 bi no 1S26** (+20%), **ROAE 38%**, **>42 mi de clientes**, carteira R$ 99,8 bi, **NPL 90d 3,6%**, PDD de R$ 996 mi → **R$ 2,4 bi** puxada pelo consignado (19/08/2026). **Delta de IA:** o C6 Assistant ganhou **função lembrete de Pix** e, sobretudo, **investir em renda fixa por conversa** (encontrar produto, tirar dúvida e iniciar aplicação) — vai além do TechInvest registrado no acervo.
[Economic News 19/08](https://economicnewsbrasil.com.br/2026/08/19/c6-bank-inadimplencia-lucro-credito/) · [Mobile Time 23/07](https://www.mobiletime.com.br/noticias/23/07/2026/agentes-ia-bancos/)

**PicPay** — Lucro ajustado **R$ 283 mi** (+135% a/a), receita R$ 4,1 bi (+67%), **70,4 mi de usuários**, carteira R$ 31,9 bi, **NPL 90d 9,8%** (era 4,1% no 2T25) (24/08/2026). **Delta de IA — o mais singular da coorte:** lançou em **13/08 um plugin no ChatGPT**, descrito como inédito na categoria — o cliente consulta saldo, caixinhas, faturas, investimentos, cartões, contatos de Pix e transações **de dentro do ChatGPT**, com **autenticação OAuth**; **somente consulta, não executa Pix nem paga fatura**, e declara conformidade com a LGPD. No mesmo movimento lançou **publicidade dentro do ChatGPT no Brasil**. Uso interno: **>95% dos colaboradores** usam IA via **HubAI**, plataforma que centraliza copilotos, agentes e modelos por área.
[Release 2T26](https://static.poder360.com.br/uploads/2026/08/2t26-picpay-release-24-8-2026.pdf) · [Mobile Time 13/08](https://www.mobiletime.com.br/noticias/13/08/2026/picpay-chatgpt/) · [Sahm Capital 17/08](https://www.sahmcapital.com/news/content/picpay-transforms-how-customers-access-their-financial-information-through-integration-with-chatgpt-2026-08-17)

**PagBank** — Lucro recorrente **R$ 576 mi** (+1,9% a/a), **TPV R$ 133,4 bi** (+3%), **34,1 mi de clientes** (praticamente estável), carteira R$ 5,1 bi (+31%), **NPL 90d 3,4%**. **Nenhum anúncio de IA identificado na janela** — a Minizinha Voz (abr/26) segue como referência mais recente. `[sem fonte]`
[InfoMoney 2T26](https://www.infomoney.com.br/mercados/pagbank-pags34-resultados-segundo-trimestre-2026/)

**Stone** — Lucro ajustado **R$ 582,7 mi** (−2,6% a/a), **TPV R$ 142,2 bi** (+4,3%), **NPL 90d de 6,98% → 8,60% em três meses** (13/08/2026). **Delta de IA:** lançou em **21/07 a "Vela"**, plataforma corporativa de IA apresentada explicitamente como **resposta ao shadow AI** — linguagem natural em português para qualquer pessoa da empresa, **respeitando permissões, regras de governança, segurança e auditoria** dos produtos críticos; **orquestração de agentes especializados**, com **Produto e Crédito já em operação** e novos agentes sendo conectados a **Compliance, Confiabilidade e Custos**. Integrada à plataforma de engenharia Karavela.
[CNN 13/08](https://www.cnnbrasil.com.br/economia/money/negocios/stone-registra-lucro-de-r-583-milhoes-no-2-trimestre-queda-de-26/) · [TI Inside 21/07](https://tiinside.com.br/21/07/2026/stone-lanca-plataforma-de-ia-para-combater-o-avanco-do-shadow-ai/)

### Contexto setorial

- **Pesquisa Febraban de Tecnologia Bancária 2026 (Deloitte):** orçamento de tecnologia dos bancos de **R$ 50,4 bi em 2026** (+8% a/a; +58% em cinco anos). **IA + analytics + big data: R$ 2,97 bi** (era R$ 2,76 bi em 2025 — **+7,6%, abaixo do crescimento do orçamento total**). Cloud R$ 3,9 bi (+30%). GenAI citada por **84%** dos bancos; benefício mais apontado é ganho de velocidade em tarefa rotineira (92%). Uso mais comum de agente: **automação de processo interno (76%)**, chatbot/voicebot e geração de relatório (71% cada).
- **Febraban Tech 2026** (24–26/08, 36ª edição, tema **"Agentes inteligentes, liderança humana"**, 70 mil visitas): mensagem central do painel de CEOs — **nenhuma instituição entrega autonomia total à IA**.
- **Agentic commerce:** a **Mastercard ativou o Agent Pay no Brasil, com Itaú e Santander já processando as primeiras transações reais** (tokens agênticos, permissões e limites definidos pelo consumidor antes da compra). A **Visa** está em teste, com piloto previsto para o fim de 2026, trabalhando com OpenAI, Perplexity, Microsoft e Anthropic. **Nenhum dos seis digitais/adquirentes aparece como parceiro nomeado até 31/08/2026.**
- **Fintechs BR (Nubank, XP, Stone, PagBank, Inter, PicPay, Agibank) somaram R$ 8,94 bi de lucro no 2T26** (+15,3% sobre o 1T26).
- **Soberania:** o único movimento explícito de IA soberana com dado 100% hospedado no Brasil na janela é do **Serpro (26/08/2026)** — **nenhum dos 11 players** fez declaração pública de residência de dados no período.

[Febraban 13/08](https://portal.febraban.org.br/noticia/4485/pt-br/) · [Finsiders 24/08](https://finsidersbrasil.com.br/tecnologia-para-fintechs/bancos-admitem-que-ainda-nao-entregam-autonomia-total-a-ia/) · [Finsiders — pagamentos agênticos](https://finsidersbrasil.com.br/tendencias-de-pagamento/pagamentos-agenticos-avancam-no-brasil-e-atraem-bancos-bandeiras-e-fintechs/) · [Serpro IA Soberana 26/08](https://convergenciadigital.com.br/governo/serpro-lanca-ia-soberana-com-dados-100-hospedados-no-brasil/)

---

## 3. Candidatos de reclassificação EMA-J — ⏳ confirmação do Bruno

> A rotina **não altera nível** sem o Bruno. Abaixo, os movimentos que a evidência pública da janela sustenta, com o SD/categoria afetado.

| Player | Onde | Nível no acervo | Candidato | Evidência pública |
|---|---|---|---|---|
| **Itaú** | Conta-PF / Atendimento / Pagamentos | L4 | **L4 forte → porta do L5** | ia.i executa transação por voz/imagem; 300 mil → 3 mi de clientes; meta 100% da base em 2026 |
| **Nubank** | Originação de crédito | L4 | **L4 → L5 (decisão, não agente)** | nuFormer em produção em 3 carteiras, 330 mi de parâmetros, inferência em tempo real na decisão |
| **BB** | Governança (eixo A, transversal) | — | **salto de eixo A em todas as jornadas** | diretrizes públicas de IA agêntica com níveis de autonomia, kill switch, rastreabilidade |
| **Inter** | Conta-PF / Pagamentos | L4 (HITL) | **manter L4, marcar transição** | Seven 2.0 (agente único centralizado) só no 3T26 — ainda não observável |
| **Mercado Pago** | Conta-PF / Pagamentos | L3–L4 | **L4** | Mago executa Pix e paga boleto por voz; 17 mi alcançados |
| **C6** | Investimentos | L2–L3 | **L3 → L4** | aplicar em renda fixa por conversa no C6 Assistant |
| **Caixa** | Conta-PF / Atendimento | **L2** | **L2 → L3 (interno), segue L2 ao cliente** | copiloto a 100% dos empregados + SuperApp beta; assistente **ainda não transaciona** |
| **PicPay** | Conta-PF | L4 | **L4 com ressalva de escopo** | plugin ChatGPT é **consulta apenas**, OAuth, sem execução |
| **Stone** | Governança (eixo A) | — | **eixo A sobe** | Vela: agentes sob permissão/auditoria, Compliance como agente |
| **PagBank** | todas | inalterado | **inalterado** | sem anúncio na janela |
| **Bradesco / Santander** | Crédito / transversal | L4 | **manter, reforçar eixo A** | Bridge multi-LLM + human on the loop; Santander sem produto novo BR |

**Padrões que a coleta mostra (descritivo, não tese):**

1. **O "vale da Caixa" mudou de forma, não desapareceu.** A Caixa saiu do zero — copiloto a 100% dos empregados, SuperApp beta — mas **colocou a IA no funcionário, não no cliente**: a assistente ainda não transaciona sobre uma base de 160 mi. O gap de 2 níveis persiste **no cliente**.
2. **A fronteira L4→L5 continua vazia e agora tem nome oficial.** O tema do Febraban Tech foi literalmente "agentes inteligentes, **liderança humana**", e o painel de CEOs fechou em "ninguém entrega autonomia total". O que mudou é que **o freio virou posição pública declarada**, não limitação técnica.
3. **A governança de agente deixou de ser lacuna e virou entregável de dois players.** BB (diretrizes com níveis de autonomia e kill switch) e Stone (Vela, agentes sob permissão e auditoria) publicaram o que o acervo listava como vale aberto em 12 notas.
4. **O FinOps de inferência foi validado por um incumbente, em público.** O CTO do Itaú descreveu roteamento entre motores para não pagar token desnecessário e comparou o risco de custo ao da migração para nuvem — é exatamente o eixo do Veltrix, dito por quem opera 1,5 tri de carteira.
5. **Três players construíram modelo/plataforma proprietária na janela:** Itaú (Iara + NeoSpace), Bradesco (modelo fundacional da Kunumi + hardware), Nubank (nuFormer em produção). **A resposta ao risco de fornecedor no BR está sendo "faço o meu", não "roteio por jurisdição".**
6. **O orçamento de IA do setor cresceu menos que o orçamento de tecnologia** (R$ 2,76 bi → 2,97 bi, +7,6%, contra +8% do total e +30% de cloud) — no ano em que a IA foi o tema do setor.
7. **A soberania de dado segue ausente do discurso privado.** Zero declaração de residência de dado entre os 11; o único movimento é estatal (Serpro).

> ⏳ **O que eu diria num board:** para o Bruno — em cada um dos 7 padrões acima.

---

## 4. Lacunas e `[sem fonte]` desta passada

- **Santander:** não confirmado se os "R$ 6 bi até 2028" são os €1 bi 2026-2028 reexpressos ou compromisso ampliado. NPL 15-90d e >90d aparecem ambos como 3,3% na fonte secundária — **conferir no release de RI**.
- **Inter:** divergência R$ 421 mi vs. R$ 447 mi (provável contábil vs. gerencial), não confirmada.
- **Mercado Pago:** NPL 90d do 2T26 não localizado.
- **C6:** não divulga trimestre isolado — números são do 1S26.
- **BB:** 🟨 **parcialmente fechado em 31/08 22h.** O PDF oficial das diretrizes de IA **generativa e agêntica** (anunciadas no Febraban Tech 2026) segue **não localizado publicamente** — só cobertura de imprensa. O que se confirmou: elas são **atualização** de um documento anterior, o *"Guia de Diretrizes e Boas Práticas para IA Ética e Responsável"* (BB, 2025), e a estrutura de governança de IA do BB foi implantada em **projeto com IBM e EY** — este último confirmado em [newsroom da própria IBM](https://brasil.newsroom.ibm.com/news?item=122949), que é fonte de parte interessada, não do BB. **Num board: citar como "diretrizes anunciadas publicamente pelo BB, documento não publicado"** — não citar o conteúdo dos parâmetros (certificação de modelo, níveis de autonomia, kill switch, rastreabilidade) como texto oficial verificado. Fontes de imprensa: [ConvergênciaDigital](https://convergenciadigital.com.br/mercado/banco-do-brasil-lanca-app-5-0-e-atualiza-diretrizes-para-ia-generativa-e-agentica/) · [TI Inside, 11/06/2025](https://tiinside.com.br/11/06/2025/banco-do-brasil-formaliza-diretrizes-para-uso-etico-da-inteligencia-artificial/).
- ~~**Reg. (UE) 2026/1744:** datas de 02/12/2027 e 02/08/2028 vêm de fonte secundária.~~ ✅ **RESOLVIDO em 2026-08-31 22:xx** — confirmado em **fonte institucional da própria Comissão Europeia** ([AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), publicado 27/07/2026, última atualização 31/07/2026), que declara textualmente sob "Extended timelines": Anexo III → **"Rules apply starting 2 December 2027"**; Anexo I (machinery, toys, lifts) → **"Rules apply starting 2 August 2028"**. Entrada em vigor **27/07/2026** confirmada na mesma página; referência do JO **OJ:L_202601744**. **Citável num board.**
  - Confirmado também na mesma passada: **Art. 50** aplica-se desde **02/08/2026**, com *grace period* de marcação legível por máquina (Art. 50(2)) até **02/12/2026** apenas para sistemas colocados no mercado antes de 02/08/2026, e **sem** rotulagem retroativa de conteúdo gerado antes dessa data; multa até **€15 mi ou 3% do faturamento global** (FAQ da Comissão sobre transparência).
  - Precisão adicional: o cronograma original do Anexo I era **02/08/2027** (como consta na tabela da seção 1) — o adiamento é de 1 ano; o do Anexo III era 02/08/2026 — adiamento de ~16 meses.
- **Normas BR** (Res. BCB 493, IN 746, Res. CVM 246, Res. Conjunta 18, Res. 403) vieram de escritórios de advocacia e imprensa setorial, **não de fonte primária do BCB/DOU**. 🟨 **Parcialmente fechado em 31/08 22h — Res. BCB 493:** localizado o **texto normativo primário** ([normativos.bcb.gov.br — Res. 0493](https://normativos.bcb.gov.br/Lists/Normativos/Attachments/40639/Res_0493_v1_O.pdf)) e o **Guia de implementação do MED do próprio BCB** ([Guia_MED.pdf](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Guia_MED.pdf) · [MED 2.0 — Circuito Pix Dia 1](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/MED/MED_2-0_Circuito_Pix-Dia_1.pdf)). ~~⚠️ Divergência a resolver antes de citar~~ ✅ **RESOLVIDA em 2026-09-01** — ver bloco abaixo. As demais (IN 746, CVM 246, Conjunta 18, Res. 403) seguem sem fonte primária.

### ✅ Res. BCB 493 / MED 2.0 — divergência de prazos resolvida (2026-09-01, fonte primária BCB)

A divergência era **de escopo, não de fato**: "7 dias", "11 dias", "80 dias" e "02/02/2026" são **prazos diferentes de etapas diferentes** do mesmo mecanismo, e o acervo vinha misturando-os. O que o texto do BCB diz, literalmente:

| Prazo | A que se refere exatamente | Fonte |
|---|---|---|
| **28/08/2025** | Data de publicação da Res. BCB 493 (altera a Res. BCB nº 1), junto com IN 653, IN 654 (Manual de Tempos v7.0) e IN 655 (Manual DICT v8.0) | [MED 2.0 — Circuito Pix Dia 1](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/MED/MED_2-0_Circuito_Pix-Dia_1.pdf), slide "Arcabouço normativo" |
| **14/10/2025** | "Dia 1" do **Circuito Pix** — janela de teste/implantação, **não** é a obrigatoriedade | mesmo PDF, capa |
| **02/02/2026** | Entrada em vigor / **obrigatoriedade** do MED 2.0 para todos os participantes do Pix, com período de adequação até maio | [InfoMoney](https://www.infomoney.com.br/minhas-financas/med-2-0-passa-a-ser-obrigatorio-em-todas-as-plataformas-que-oferecem-pix/) · [InvestNews](https://investnews.com.br/financas/pix-med-2-0/) — **secundária**, o BCB não datou a obrigatoriedade nos dois PDFs públicos |
| **7 dias corridos** | Período de **análise da notificação de infração pelo PSP recebedor**, contado da abertura da NI. **Não** é o prazo do MED inteiro. | [Guia_MED.pdf v4.3](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Guia_MED.pdf), item 5 do fluxo 4.2.4 |
| **72 horas** | Janela do **PSP pagador** para iniciar a devolução depois que a Recuperação de Valores entra no estado `ANALYSED` | idem, item 8 |
| **6 horas (99% dos casos)** | Tempo do PSP recebedor para efetivar a devolução, contado da abertura da solicitação (Manual de Tempos do Pix) | idem, item 10 |
| **~11 dias** | **Derivado**, não literal: 7 dias de análise + 72h de devolução. É o número que a imprensa usa como "prazo para o dinheiro voltar". | derivação dos dois acima |
| **80 dias / 30 dias** | Idade máxima da **transação raiz** para abrir contestação (80 dias em geral; **30 dias** se o contestado for uma transação de devolução) | idem, seções 4.2.4 e 6 |
| **90 dias** | Mecanismo **diferente**: janela em que qualquer usuário recebedor pode devolver recursos creditados por iniciativa própria — não é MED | idem, seção 3 |
| **01/09/2026 e 26/10/2026** | Vigências da **v4.4 do Guia**. ✅ Detalhadas no bloco "As duas vigências da v4.4" adiante: **01/09 = contestação de devolução sobe de 30 → 80 dias** (IN BCB 766); **26/10 = camada do grafo informada na NI**. | idem, capa + IN BCB 766 |

**Obrigatoriedade (FAQ 4 do Guia, literal):** "Sim. Todos os participantes do Pix devem prever, nos contratos [...] que eles podem bloquear e debitar recursos de suas contas sem prévia autorização" — sem consentimento do cliente, com resolução contratual se o cliente recusar.

**⚠️ Correção de número — a taxa de recuperação:** o acervo vinha registrando "**<7% → 80%**". O número do BCB é **9,3%** — *"Em 2025, foram recuperados em média 9,3% do valor contestado"* (MED 2.0 — Circuito Pix Dia 1, slide "Contextualização"). **Os 80% não foram localizados em nenhuma fonte primária nem secundária** e devem ser tratados como **não citáveis** até aparecer origem. O 9,3% é citável num board; o 80% não é.

**O que o MED 2.0 muda tecnicamente (literal do BCB):** rastreio do dinheiro **além da primeira conta recebedora**, via DICT + GRAF, com parâmetros de profundidade (`MaxHops`), janela temporal (`HopWindow`) e valor mínimo; algoritmo prioriza quais caminhos recebem NI; devolução processada sequencialmente pelo DICT sem intervenção do PSP pagador. O motivo declarado: *"Dinheiro de golpe/fraude é rapidamente pulverizado"*.
- **Explicabilidade:** só o Itaú tem mecanismo público explícito (camada de verificação factual). Para os outros 10, `[sem fonte]`.
- **Residência de dados:** `[sem fonte]` para os 11.
- **MED 2.0:** ~~data de operação plena divergente entre fontes~~ ✅ **RESOLVIDA em 2026-09-01 (2ª passada)** — ver bloco "As duas vigências da v4.4" abaixo.
- **Taxa de recuperação do MED:** o "80%" que circulou no acervo **não tem fonte**. O número do BCB é **9,3% do valor contestado em 2025**. Ver bloco resolvido acima.

---

### ✅ As duas vigências da v4.4 — o que entra em 01/09 e em 26/10 (2026-09-01, 2ª passada)

O PDF da v4.4 do Guia não está publicado em URL indexável (a capa da v4.3 só anuncia "Acesse aqui a versão 4.4"). Mas **o normativo que produz as duas datas foi localizado** e é citável: **Instrução Normativa BCB nº 766, de 27/07/2026** (DOU de 29/07/2026), que divulga a **versão 8.5 do Manual Operacional do DICT** e **revoga a IN BCB nº 752, de 01/07/2026**.

| Data | O que entra em vigor | Seções do Manual DICT |
|---|---|---|
| **10/08/2026** | Novo atributo **`TransactionDepth`** ("Profundidade no grafo") na Notificação de Infração para Solicitação de Devolução, e seu processamento na etapa de **Análise** do Fluxo de Recuperação de Valores | 10.1 e 20.1.5 |
| **01/09/2026** (hoje) | **Prazo para contestar uma transação de devolução sobe de 30 → 80 dias**, na Instauração do Fluxo de Recuperação de Valores, na Contestação de Transação de Devolução por Fraude e no Fluxo de Instauração e Solicitação de Bloqueio. Revoga a IN 752. | 20.1.1, 20.1.9 e 20.2 |

Fonte: [IN BCB nº 766](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=766) · análise de conformidade em [cadoc.ai](https://cadoc.ai/post/instrucao-normativa-bcb-766) · [Manual Operacional do DICT v8.5](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/X_ManualOperacionaldoDICT.pdf) · [meutudo, 30/07/2026](https://meutudo.com.br/blog/noticias/2026/07/30/banco-central-anuncia-mudancas-no-pix-para-reforcar-a-seguranca-das-transacoes-entenda/).

**⚠️ Correção de escopo do "80 dias" (refina a linha da tabela acima).** A tabela de 31/08 registrava "80 dias = idade máxima da transação raiz para contestar; 30 dias se o contestado for uma devolução". O que a IN 766 faz é exatamente **subir esse caso de 30 para 80 dias**. Ou seja, **de hoje em diante o prazo para contestar uma devolução feita pelo MED é 80 dias**, e quem ganha com isso é o **recebedor legítimo** (lojista, prestador de serviço) que teve valor debitado por uma devolução. **Não cria** prazo de 80 dias para a vítima abrir o MED — regra que segue inalterada. Formulação segura num board: *"o prazo de contestação de devolução, não o de abertura do MED"*.

**⚠️ Terceira data de "entrada em vigor" do MED 2.0 — as três coexistem e significam coisas diferentes.** Em nota à imprensa (10/08/2026, via Agência Estado), o BC declarou: *"desde 11 de maio de 2026 já está em produção o MED 2.0"* e que o sistema *"deve entrar em vigor em 26 de outubro de 2026"*, quando passará a **identificar, no encaminhamento da NI, a qual camada do grafo ela se refere** — acrescentando que *"o ajuste não tem qualquer efeito para os usuários do Pix"*. Consolidando:

| Data | Status que ela marca |
|---|---|
| 02/02/2026 | Obrigatoriedade dos endpoints de Recuperação de Valores + extensão do rastreio à 2ª camada (fonte secundária para a obrigatoriedade) |
| 11/05/2026 | MED 2.0 **em produção**, declarado pelo BC |
| 26/10/2026 | Camada do grafo informada ao participante na NI — declaração do BC à imprensa, **normativo não localizado** |

Fonte: [O POVO / Agência Estado, 10/08/2026](https://www.opovo.com.br/noticias/economia/2026/08/10/bc-deve-lancar-versao-2-0-do-mecanismo-especial-de-devolucao-de-valores-do-pix-em-outubro.html).

**⚠️ Segundo número derrubado — "rastreio em 5 camadas" NÃO é citável.** O acervo registrava rastreio em 5 camadas. A fonte primária do BCB ([MED 2.0 — Circuito Pix, Dia 3](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/MED/MED_2-0_Circuito_Pix-Dia_3.pdf)) diz outra coisa no cronograma: **1ª camada** facultativa a partir de 23/11/2025; **2ª camada** "previsto" para 02/02/2026; **3ª camada** "em estudo". Não há 5. Depois do "80%", é o segundo número do acervo sem origem — ambos vinham de cobertura de imprensa.

**🆕 Achado de governança — o regulador brasileiro construiu governança de modelo antes dos regulados.** O mesmo material do BCB descreve que **DICT e GRAF rodam modelos próprios** para selecionar transações no rastreio e priorizar o envio de NIs — isto é, um **modelo algorítmico do BC decide de quem o dinheiro é bloqueado**. Em torno disso o BC montou: (a) **hiperparâmetros obrigatórios** a todos — busca em largura (*breadth-first search*), teto do somatório das NIs como múltiplo do valor da transação raiz, e limite do valor que sai de uma conta pelo valor que entrou nela; (b) **governança formal de modelo** — estrutura e especificação, ciclo de revisão/teste/aprovação e desenho das métricas de acompanhamento, com o **GE-Seg** (Res. BCB 493) e o **GAMED** consultivo, mantendo execução de modelos e métricas no BC; (c) **espaço regulado de diferenciação** — no fluxo interativo, o participante **pode usar modelo próprio** de priorização, desde que obedeça os hiperparâmetros. Objetivos declarados: otimizar recuperação, **minimizar fricção sobre usuários que terão recursos bloqueados** e limitar instabilidade do processo.

**Refino dos ANS (Manual de Tempos v7.0, IN BCB 654, vigentes desde 02/02/2026).** 1.800s @95% entre a reclamação no canal de atendimento e a abertura da NI/RV · 300s @99% entre a transação e a criação da mensagem TRCK.002 · 24h @95% para concluir solicitação de devolução por **falha operacional** (P95 observado era 46h em 25Q1) · 48h @95% por **fundada suspeita de fraude** · 6h @99% quando **não** há análise para fechamento. Complemento: envio de **booktransfer** por TRCK.002 é mandatório desde **25/11/2025** (IN 653, art. 2º-A da IN 32) — sem ele o BC não enxerga transação liquidada fora do SPI.

**⏳ para o Bruno — o que eu diria num board:** aberto. O material está pronto; a tese é sua.

---

### ✅ §4.3 — As quatro normas que estavam `[sem fonte]` primária (2026-09-01, 4ª passada de proveniência)

Fechada a última lista de `[sem fonte]` que a máquina podia resolver sozinha: **IN BCB 746 · Res. CVM 246 · Res. Conjunta 18 · Res. BCB 403**. Uma delas estava **materialmente errada** no acervo.

| Norma | O que o acervo dizia | O que a fonte diz | Veredito |
|---|---|---|---|
| **IN BCB 746/2026** | "01/11/2026 — limita Pix em dispositivo não cadastrado a R$ 200/R$ 1.000" | **16/06/2026, DOU 17/06/2026, vigência 01/10/2026.** Altera a **IN BCB 512/2024** (a norma de limites do Pix): **revoga** o inciso VI do §2º do art. 10, o art. 16-A e o art. 16-C — os dispositivos que davam **tratamento próprio de limite ao Pix por aproximação** — e **altera** os incisos IV e V do §2º do art. 10 e o art. 12 para incluir o **Pix Automático** na gestão de limites. | ❌ **ERRADA — corrigida na tabela da §1** |
| **Res. BCB 403/2024** | "monitoramento antifraude obrigatório a todos desde nov/2024" | **Publicada 22/07/2024**, altera a Res. BCB 1/2020. Vigência na publicação, **exceto as regras de prevenção à fraude, que valem desde 01/11/2024**. É dela — e não da IN 746 — que vêm os **R$ 200/transação e R$ 1.000/dia em dispositivo não previamente cadastrado**, além do monitoramento contínuo e do bloqueio cautelar. | ✅ **CONFIRMADA** |
| **Res. CVM 246** | "31/07/2026, cria a Ditec, estrutura interna, não norma de conduta" | **Publicada e em vigor em 31/07/2026.** Atualiza a **Res. CVM 24 (Regimento Interno)**. Cria a **DITEC na SDI** a partir da extinção da DDEIN. Objetivo declarado: *estabelecer diretrizes técnicas para soluções analíticas e computacionais avançadas, observadas as políticas de governança de dados e de IA da CVM*, e *propor, implementar e revisar políticas e procedimentos internos de governança e uso ético e responsável de IA **na Autarquia***. Trabalhos iniciais: tokenização 2026–2027, próxima rodada do Sandbox Regulatório e Fintech Task Force da IOSCO. | ✅ **CONFIRMADA e refinada** |
| **Res. Conjunta 18** | "Res. Conjunta 18/2025, política de qualidade das informações, prazo 31/12/2026" | **Res. Conjunta CMN/BCB nº 18, de 28/11/2025.** Prazo de adequação **31/12/2026**. Obriga **Política de Qualidade das Informações** formal, documentada e segregada, com **12 dimensões** (acessibilidade, acurácia, adaptabilidade, clareza, comparabilidade, completude, confiabilidade, consistência, integridade, rastreabilidade, relevância, tempestividade), **diretor responsável perante o BCB**, **responsabilidade indelegável** do CA/Diretoria, **dicionário de dados**, trilha de auditoria e **relatório semestral**; o BCB pode **rejeitar** informação e exigir nova remessa. | ✅ **CONFIRMADA e enriquecida** |

**Correção nº 3 do acervo (as duas anteriores: o "80%" de recuperação do MED e o "rastreio em 5 camadas").** As três têm a mesma assinatura: **vieram de imprensa/secundária e colaram dois fatos distintos num só.** Aqui, a colagem foi de **norma + ano**: pegou o limite de R$ 200/R$ 1.000 (Res. 403, **2024**) e o carimbou numa norma de 2026 (IN 746) com data futura (**01/11/2026** em vez de 01/11/**2024**). Efeito prático sobre o argumento: o acervo vinha tratando esse limite como **restrição que vai cair sobre o pagamento agêntico**; ele é, na verdade, **piso já vigente há dois anos** — todo Pix conversacional dos 11 players já opera sob ele.

**🆕 Achado da verificação — o que a IN 746 de fato faz é mais relevante para a tese do que o número errado que ela carregava.** Ela retira o **Pix por aproximação** do regime de limite especial e coloca o **Pix Automático** dentro da gestão de limites. Isto é: o BC está **normalizando o trilho recorrente/automatizado sob o mesmo regime de limite do Pix comum** — o que casa com o padrão que o discovery já registrou em F2-3, F2-4 e Cartão (**"o nivelador foi o regulador, não a competição"**), agora aplicado ao trilho onde o pagamento agêntico vai rodar.

**🆕 Segundo achado — a Res. Conjunta 18 é a norma mais próxima de "governança de modelo" que existe hoje no BR, e não fala de IA.** Diretor responsável nomeado, responsabilidade que o conselho **não pode delegar**, rastreabilidade da origem ao reporte, dicionário de dados, relatório semestral e poder do regulador de rejeitar o dado. Com **PL 2338 adiado para depois de 2026** e **nenhuma norma de IA do BCB, ANPD, CVM ou SUSEP**, esta é a única obrigação de governança de dado com **prazo, dono e sanção** dentro do horizonte — e o prazo é **31/12/2026**.

**Nível de proveniência (honesto).** Fonte **institucional/primária**: Res. CVM 246 ([gov.br/cvm, 31/07/2026](https://www.gov.br/cvm/pt-br/assuntos/noticias/2026/resolucao-cria-divisao-de-tecnologia-financeira-ditec-na-superintendencia-de-desenvolvimento-de-inteligencia-sdi-na-cvm)). Fonte **secundária com convergência independente** (texto integral do BCB não indexável por busca): IN BCB 746 (existência e data confirmadas na listagem do [DOU/in.gov.br](https://www.in.gov.br/en/web/dou); conteúdo dispositivo-a-dispositivo em [TabNews/normativodev](https://www.tabnews.com.br/normativodev/pix-por-aproximacao-perde-regra-propria-de-limites-na-in-bcb-746-vigencia-01-10-2026) e [LegisWeb](https://www.legisweb.com.br/legislacao/?id=496912)); Res. BCB 403/2024 ([Serasa Experian](https://www.serasaexperian.com.br/conteudos/resolucao-bcb-403-2024-novas-medidas-seguranca-do-pix/), [Bankly](https://blog.bankly.com.br/resolucao-403-pix), [QI Tech](https://qitech.blog/resolucao-403-pix/)); Res. Conjunta 18 ([PwC](https://www.pwc.com.br/pt/estudos/setores-atividade/financeiro/2026/resolucao-conjunta-n-18-2025.html), [Deloitte](https://www.deloitte.com/br/pt/Industries/financial-services/perspectives/resolucao-conjunta-numero-dezoito.html), [LegisWeb — data 28/11/2025](https://www.legisweb.com.br/legislacao/?id=487039), [Cetax](https://cetax.com.br/resolucao-conjunta-18-banco-central/)). **Regra de citação:** as três de fonte secundária são citáveis num board pelo **efeito e pela data**; para citar **artigo ou dispositivo específico**, abrir o texto no `normativos.bcb.gov.br` antes.

**⏳ para o Bruno — o que eu diria num board:** aberto. Os fatos estão verificados; a tese é sua.

---

## 5. O que fazer com isto

1. **Corrigir o Log dos dois ledgers** — a premissa do EU AI Act repetida por 20 passadas está errada. ✅ feito nesta passada.
2. **Aplicar as reclassificações EMA-J** da seção 3 nas notas e na planilha mestre — depende do aval do Bruno.
3. **Fechar as teses ⏳** nos 12 De-Para + 8 comparativos + nesta nota. Segue sendo a maior alavanca e segue sendo trabalho do Bruno.
4. **Material novo que esta passada abre sem custo de coleta:** o padrão 4 (FinOps de inferência validado pelo CTO do Itaú) e o padrão 3 (BB e Stone publicando governança de agente) conversam diretamente com Veltrix e Cohort.

---

**Nota de método:** todos os dados desta nota são públicos, com fonte e data. Ganhos de terceiros são **autorrelato do player** — citados como declaração, nunca como fato verificado. Nenhum número foi estimado.
