---
tipo: nota-de-proveniencia
setor: financeiro
data: 2026-09-01
players: 11
tags: [soberania, residencia-de-dados, explicabilidade, governanca-de-modelo, discovery, proveniencia]
relacionado: ["[[_Ledger-Discovery]]", "[[2026-08-31 — Refresh 2T26 e Frame Regulatório]]"]
---

# Residência de dados e explicabilidade nos 11 players — varredura de proveniência

> **O que esta passada é.** Desde 04/07 o acervo carrega a mesma pendência em toda nota: `[sem fonte]` de **residência de dados nos 11** e de **explicabilidade em 10 dos 11**. Nunca foi varrido — foi herdado. Esta passada varre os 11 players contra fonte pública e converte a pendência genérica em **matriz com célula fechada, fonte e nível de proveniência**. É coleta e verificação, não tese. As teses seguem ⏳ para o Bruno.

**Cobertura:** 11/11 players · 4 varreduras paralelas · fontes públicas apenas (política de privacidade e segurança do próprio player, RI/20-F, sala de imprensa, blog de engenharia, release de fornecedor, imprensa especializada, portais gov.br). Nada logado, nada atrás de paywall.

---

## 1. O quadro em uma tabela

| Player | Residência de dado no BR declarada? | Transferência internacional declarada? | Jurisdição da inferência | Doc. próprio de governança de IA | Explicabilidade ao cliente |
|---|---|---|---|---|---|
| **Itaú** | ❌ `[sem fonte]` | ✅ **13 países nomeados** | `[sem fonte]` | ❌ não localizado | Revisão LGPD art. 20 |
| **Bradesco** | ❌ `[sem fonte]` | ✅ genérica ("inclusive fora do Brasil") | `[sem fonte]` | ✅ **Trusted AI (assinado)** | ✅ 3 mecanismos declarados |
| **Banco do Brasil** | ❌ `[sem fonte]` | `[sem fonte]` (política não renderizou) | `[sem fonte]` | 🟨 anunciado, **PDF não publicado** | `[sem fonte]` |
| **Nubank** | ❌ `[sem fonte]` | ✅ genérica (nuvem fora do BR) | `[sem fonte]` | ❌ (diretriz dentro da Pol. de Segurança) | ⛔ **recusa declarada** |
| **Inter** | ❌ `[sem fonte]` | ✅ **EUA, Argentina, Ilhas Cayman** | `[sem fonte]` | ❌ não localizado | Revisão LGPD com ressalva de segredo |
| **Mercado Pago** | ❌ `[sem fonte]` | ✅ genérica ("país diferente do seu") | `[sem fonte]` | ❌ não localizado | `[sem fonte]` |
| **Santander** | ❌ `[sem fonte]` para o BR | — (grupo; ver §4) | `[sem fonte]` | ✅ **framework do CA + código aberto** | `[sem fonte]` |
| **Caixa** | 🟨 via **Serpro (nuvem soberana)** — sem comunicado da própria Caixa | `[sem fonte]` | `[sem fonte]` | ❌ não localizado | `[sem fonte]` |
| **C6** | ❌ `[sem fonte]` | `[sem fonte]` | `[sem fonte]` | ❌ não localizado | `[sem fonte]` |
| **PicPay** | ❌ `[sem fonte]` | ✅ via conteúdo de marca | `[sem fonte]` | ❌ (há CAIO nomeado, não estrutura) | `[sem fonte]` |
| **PagBank** | ❌ `[sem fonte]` — infra de TI em Scala/AWS/Oracle do Brasil (20-F), **não é residência de IA** | `[sem fonte]` | `[sem fonte]` | 🟨 **CoE-AI** (centro técnico); 20-F trata IA como risco de **competitividade e PI** | `[sem fonte]` |
| **Stone** | ❌ `[sem fonte]` | `[sem fonte]` | `[sem fonte]` | 🟨 Vela (fronteira corporativa) + risk factors 20-F | `[sem fonte]` |

**Leitura da tabela (descritiva, não é tese):** **0 de 11** declaram residência de dado no Brasil para carga de IA. **0 de 11** declaram a jurisdição sob a qual a inferência roda. **6 de 11** declaram explicitamente o contrário — transferência internacional de dado pessoal.

---

## 2. Achados com fonte

### 2.1 Ninguém declara residência; seis declaram transferência

- **Itaú — o único que nomeia os países.** A Política de Privacidade prevê transferência internacional "inclusive a utilização de serviços de armazenamento e/ou processamento de dados em nuvem ou servidores localizados em outros países", com lista: Argentina, Alemanha, Bahamas, Canadá, Chile, Colômbia, EUA, França, Ilhas Cayman, Portugal, Reino Unido, Suíça, Uruguai. Residência no Brasil aparece **só para cookies essenciais/analíticos** (item 12). — [Itaú, Política de Privacidade e Cookies](https://www.itau.com.br/privacidade/politica-de-privacidade-e-cookies), últ. atual. **01/09/2026**. *Declarado pelo player.*
- **Inter — três países nomeados.** "O Inter pode transferir seus Dados Pessoais... para os países abaixo: Estados Unidos da América; Argentina; Ilhas Cayman." — [Inter, Política de Privacidade](https://inter.co/politica-de-privacidade/privacidade/), atual. **05/03/2026**. *Declarado pelo player.*
- **Nubank — genérica.** "Alguns de seus dados pessoais, ou todos eles, poderão ser transferidos para o exterior, por exemplo quando são armazenados pelo Nu em servidores de computação em nuvem localizados fora do Brasil." — [Nubank, Política de Privacidade](https://nubank.com.br/transparencia/politicas-de-privacidade-e-seguranca/politica-de-privacidade). *Declarado pelo player.*
- **Bradesco — genérica.** Dados podem ser compartilhados com "Unidades Externas (inclusive as localizadas fora do Brasil)". — [Bradesco, Diretiva de Privacidade](https://banco.bradesco/assets/common/inc/diretiva_privacidade_lgpd.shtm), **sem data exibida na página**. *Declarado pelo player.*
- **Mercado Pago — genérica, com admissão de risco.** Infraestrutura "como servidores e serviços de nuvem, que podem estar estabelecidos em país diferente do seu"; a declaração reconhece que alguns países receptores podem **não oferecer nível adequado de proteção**, mitigado por contrato/normas internas. — [Mercado Pago, Declaração de Privacidade](https://www.mercadopago.com.br/privacidade/declaracao-privacidade). ⚠️ *Página renderizada por JS; conteúdo obtido via índice de busca — revalidar antes de citar literalmente num board.*
- **PicPay** — transferência para fora do Brasil aparece em conteúdo de marca; o Aviso de Privacidade (atual. **ago/2026**) não expôs o bloco na coleta. 🟨 *parcial.*

### 2.2 O único trilho de residência declarada no país é **estatal**

- **Caixa × Serpro — "nuvem soberana".** Contrato assinado em **maio/2025**, Serpro como *broker*, 5 anos, **R$ 752,6 mi**; aditivo em **20/08/2025** eleva para **R$ 763,8 mi**; contratação por **inexigibilidade de licitação**; serviço hospedado em ambiente **Microsoft Azure**, com a multicloud do Serpro (Google, AWS, Huawei, Oracle, Azure, IBM) entrando na TI do banco. A própria reportagem registra que **não houve comunicado oficial da Caixa**. — [Capital Digital](https://capitaldigital.com.br/caixa-adota-nuvem-soberana-do-serpro-em-ambiente-microsoft-ao-custo-de-r-7638-milhoes/), **27/08/2025**. *Imprensa. Declaração da própria Caixa:* `[sem fonte]`.
- **Serpro "IA Brasil"** — dados e processamento 100% no país, família de LLMs em português (~12 bi a 120+ bi de parâmetros), lançada **26/08/2026** no Febraban Tech. — [Serpro](https://www.serpro.gov.br/menu/noticias/noticias-2026/serpro-lanca-ia-brasil) e [Convergência Digital](https://convergenciadigital.com.br/governo/serpro-lanca-ia-soberana-com-dados-100-hospedados-no-brasil/), **26/08/2026**. **Vínculo público da Caixa como cliente dessa plataforma:** `[sem fonte]`.
- ⚠️ **Higiene de citação:** "IA soberana com dados 100% no Brasil" é do **Serpro**, não do BB nem da Caixa. Não colar.

### 2.3 Fornecedor e concentração (o que dá para afirmar)

| Stack declarado | Players |
|---|---|
| **AWS** (nuvem e/ou Bedrock) | Nubank, Inter (FMaaS sobre Bedrock), Mercado Pago, C6 ("nuvem preferencial"), PagBank (Rekognition + Bedrock + SageMaker), Itaú (principal), Santander (ecossistema) |
| **Azure / Azure OpenAI** | Bradesco (**Bridge**: Foundry, ~2 mi req./dia, 2 bi de tokens/dia), PicPay (**GPT-4.1**, multiagente A2A+MCP), Caixa (M365 Copilot + Copilot Studio), Itaú (secundário) |
| **OpenAI direto** | Nubank (GPT-4o, Copilot de call center), Mercado Pago (**Verdi**), Santander (ChatGPT Enterprise, ~15 mil → meta 30 mil usuários), PicPay (**plugin no ChatGPT**) |
| **Google Cloud / Gemini** | Santander (core **Gravity**, Dual Run), C6 (**Gemini Enterprise** em fraude/PLD) |
| **G42 — Abu Dhabi (EAU)** | Santander (**MoU 03/06/2026**, Inception/Presight, "agentic financial services") |
| **Modelo/plataforma própria** | Nubank (**nuFormer**), Itaú (**Iara**), Bradesco (fundacional **Kunumi**), Stone (**Vela** sobre Karavela — fornecedor não declarado) |

- **Bradesco/Bridge:** "10 grandes modelos de linguagem, mais de 400 experimentos, pelo menos 20 casos de uso em produção"; "mais de dois milhões de requisições e dois bilhões de tokens de inferência" por dia. **Nenhuma menção a região, país ou jurisdição de processamento.** — [Microsoft Customer Stories](https://www.microsoft.com/pt-br/customers/story/25888-bradesco-microsoft-foundry), **18/12/2025**. *Release de fornecedor.*
- **Santander × G42:** MoU não vinculante cobrindo "banking intelligence, agentic financial services and large-scale AI infrastructure"; Presight fala em "um dos maiores mandatos corporativos de IA agêntica em banking europeu e latino-americano". **Nenhuma menção ao Brasil, à residência do dado ou à jurisdição.** — [Santander, press release](https://www.santander.com/en/press-room/press-releases/2026/06/banco-santander-and-g42-sign-memorandum-of-understanding-to-explore-strategic-cooperation-in-artificial-intelligence), **03/06/2026**. *Declarado pelo player.*
- **Santander, declaração mais próxima do tema — e é sobre treino, não residência:** "nenhum dado de cliente é compartilhado externamente para treinar modelos". — [santander.com, story OpenAI](https://www.santander.com/en/stories/santander-data-ai-first-strategy-accelerates-through-openai-collaboration), **ago/2025**.
- **PicPay × ChatGPT (17/08/2026):** escopo **somente leitura** — saldo, cofrinhos, boletos pendentes, investimentos, cartões ativos, Pix favoritos, lançamentos recentes e futuros; **"no transactional capabilities"**; **OAuth** com redirecionamento ao app; revogação por desinstalar o plugin; "todos os intercâmbios seguem os padrões de segurança do PicPay e cumprem a LGPD". **O que trafega campo a campo para a OpenAI, se há retenção e se o dado é usado para treino:** `[sem fonte]`. — Release próprio do PicPay via GlobeNewswire, **17/08/2026**.

### 2.4 Explicabilidade — a assimetria real

Quatro posições distintas, e a distância entre elas é maior do que o acervo registrava:

**① Documento próprio, autoral e assinado — só o Bradesco.**
*Trusted AI — Compromisso do Bradesco com a IA Confiável*, assinado por Rafael Forte Araujo Cavalcanti (Diretor de Inteligência de Dados), canal `governanca.ia@bradesco.com.br`, produzido para os critérios de governança do Dow Jones Sustainability Index. Declara: **alinhamento explícito ao EU AI Act e aos princípios da OCDE**; **Política de Riscos de IA aprovada pelo Conselho de Administração** + norma interna + Comissão de Governança; explicabilidade em três mecanismos (identificação de conteúdo gerado por IA; canal formal de questionamento e revisão com validação humana; registro de decisões para rastreabilidade); **human-in-the-loop** para usos críticos "prevenindo decisões irreversíveis"; **kill switch** ("correção, pausa ou desativação"); **auditorias técnicas independentes** e monitoramento de modelos em produção; **usos proibidos** (manipulação, social scoring, biometria em tempo real não autorizada); BIA sob termo de responsabilidade **opt-in**. — [Bradesco, Trusted AI (PDF)](https://assets.bradesco/content/dam/portal-bradesco/assets/classic/pdf/sustentabilidade/trusted-ai.pdf). ⚠️ **documento sem data** — referencia o Relatório ESG 2025, p. 65. *Declarado pelo player.* **É o único dos 11 que cita o EU AI Act.**

**② Framework corporativo + governança em código aberto — Santander.**
*Data and Artificial Intelligence Corporate Framework* aprovado pelo Conselho, sob **três linhas de defesa** com supervisão independente proporcional ao risco; cinco princípios de IA responsável (transparência — o usuário sempre sabe que interage com IA; fairness; accountability com donos definidos por ciclo de vida; privacidade by design; contribuição a valor); **treinamento obrigatório** de IA responsável. — [santander.com/our-approach/data-and-ai](https://www.santander.com/en/our-approach/data-and-ai), *página sem data, consultada 01/09/2026*.
Mais concreto e mais raro: **14 repositórios Apache-2.0 do Santander AI Lab** (atualizados **01/07/2026**), entre eles `mech-gov-framework` (regimes de governança R1/R2/R3, *hard gates*, métricas para decisões de LLM de alto risco), `autoguardrails`, `mutatis-mutandis` (teste de situação com comparadores contrafactuais para análise de discriminação), `causal-perception-implementation` (modelos causais aplicados a **decisão de crédito justa**), `auto-bayesian` (redes bayesianas interpretáveis); release sob **OSPO com FOSS Review Board** (OSPO Lead + Jurídico + CISO + Arquiteto), com declaração de uso apenas de dado sintético ou anonimizado. — [github.com/SantanderAI](https://github.com/SantanderAI). *Declarado pelo player, e é o único material do conjunto que é **inspecionável**, não apenas afirmado.* Também mantém `llm_bridge`, biblioteca com adaptadores plugáveis para **OpenAI, AWS Bedrock e Google Gemini** — neutralidade de fornecedor implementada em código.

**③ Anunciado, mas não publicado — Banco do Brasil.**
Parâmetros declarados na atualização de **ago/2026** para IA generativa e agêntica: certificação de modelos; uso seguro de dados; **níveis de autonomia**; **rastreabilidade**; governança de agentes; responsabilidade sobre decisões automatizadas; avaliação/aprovação/monitoramento por ciclo de vida; **kill switch**; **autonomia faseada com supervisão humana em situações críticas**; restrições para GenAI sobre **dado sensível**. — [Convergência Digital](https://convergenciadigital.com.br/mercado/banco-do-brasil-lanca-app-5-0-e-atualiza-diretrizes-para-ia-generativa-e-agentica/), **26/08/2026** (falas de Giuliane Paulista, Ger. Exec. de Governança de IA, e Rafael Rovani, Head de IA).
Estrutura construída com **IBM (watsonx.governance, Cloud Pak for Data) e EY (Generative AI Lifecycle Framework)**: monitoramento de **viés, transparência, drift e desempenho**, checklist de validação de fornecedores, papéis definidos; escala de 1,4 mil soluções analíticas, ~700 com IA, 600+ casos em operação. — [IBM Brasil Newsroom](https://brasil.newsroom.ibm.com/news?item=122949), **17/06/2025** e [EY Brasil](https://www.ey.com/pt_br/newsroom/2025/06/banco-do-brasil-adota-governanca-de-ia-com-ibm-e-ey), mesma data.
⚠️ **Regra de citação (reafirmada da passada de 31/08):** o PDF do guia **segue não publicado**. Citar como "diretrizes anunciadas publicamente" — **nunca** o conteúdo dos parâmetros como texto oficial verificado. A descrição mais rica vem de **fornecedor**, que é parte interessada.

**④ Recusa explícita — Nubank. O achado mais afiado da passada.**
No Aviso de Privacidade, sobre decisões automatizadas: **"Por motivos de segredo de negócio, proteção de informações confidenciais e preservação da concorrência, o Nu não informa a forma de funcionamento desses sistemas automatizados."** Há direito de revisão, sem garantia de resultado diferente. — [Nubank, Política de Privacidade](https://nubank.com.br/transparencia/politicas-de-privacidade-e-seguranca/politica-de-privacidade). *Declarado pelo player.*
Internamente há governança: a Política de Segurança (atual. **05/03/2026**) exige que IA siga "modelos de governança e as melhores práticas do mercado", com três linhas de defesa; o blog de engenharia descreve **Model Catalog, Model View e Reporting Tool** para rastreio de artefatos, inputs e outputs. — [building.nubank.com](https://building.nubank.com/foundation-models-ai-nubank-transformation/), **11/06/2025**. **A governança existe para dentro e é negada para fora, por escrito.**
O **Inter** ocupa posição intermediária: concede revisão "respeitados os segredos comercial e industrial do Inter" (Pol. de Privacidade, **05/03/2026**).

**Os sete restantes** (Itaú, Mercado Pago, Caixa, C6, PicPay, PagBank, Stone): nenhum documento próprio de governança de IA localizado. O que existe:
- **Itaú** — dois princípios declarados para a ia.i (confiança e responsabilidade, com "supervisão humana"), escape para humano a qualquer momento, e o direito de revisão do art. 20 da LGPD. Áreas RAI/HAX Itaú e política de IA responsável **aparecem em busca mas não em página coletável** (fonte provável no Medium Itaú Tech, atrás de login). — [Meio & Mensagem](https://www.meioemensagem.com.br/marketing/diretor-do-itau-unibanco-explica-fundamentos-do-projeto-ia-i), **31/07/2026**; [feito.itaú](https://feito.itau.com.br/itau-iai-superapp-inteligencia-artificial/), **28/07/2026**.
- **Stone/Vela** — herda "permissões, regras de governança, segurança e auditoria aplicadas aos produtos mais críticos"; arquitetura de agentes por domínio (Produto e Crédito **em operação**; **Compliance, Confiabilidade e Custos são roadmap, não produção**). O 20-F reconhece **model risk** de forma explícita (seleção errada de variáveis, método inadequado, falha em detectar mudança de regime, erro de deploy). — [StoneCo, Key Risk Factors](https://investors.stone.co/about-us/key-risk-factors/); Vela via TI Inside **21/07/2026** ⚠️ *não verificada no original (site bloqueou fetch)*.
- **PagBank** — **CoE-AI** declarado, atuando com Planejamento Estratégico na seleção de modelos; é centro técnico, não comitê com mandato de veto. — [Blog AWS Brasil, coautoria PagBank](https://aws.amazon.com/pt/blogs/aws-brasil/como-o-pagbank-implementou-um-modelo-de-ml-para-forecasting-de-vendas-das-maquininhas-pagbank/), **27/08/2024** ⚠️ *2024*.
- **Caixa** — validação interna, supervisão humana, restrição de acesso e catálogo de agentes validados para agentes criados pelas áreas em Copilot Studio; via imprensa/caso de fornecedor. — [TI Inside](https://tiinside.com.br/12/08/2026/caixa-reduz-processos-de-ate-12-dias-para-30-minutos-e-ganha-80-de-produtividade-com-ia/), **12/08/2026**.
- **PicPay** — há **Chief AI Officer nomeado** (Renan Oliveira); estrutura de governança descrita: `[sem fonte]`.
- **Mercado Pago** — posição pública sem documento: Pablo Segura, diretor de Privacidade de Dados do Mercado Livre, defende "responsabilidade demonstrada" (*accountability*) e privacy by design, listando transparência, rastreabilidade e supervisão humana como desafios. — [MinTIC Colômbia](https://www.mintic.gov.co/portal/715/w3-article-417873.html), últ. atual. **04/11/2025**.
- **C6** — nada localizado além de fala de executivo sobre custo/escala de GenAI (Finsiders, **26/09/2024**).

### 2.5 Frameworks internacionais: quase deserto

- **ISO 42001:** `[sem fonte]` em **11 de 11**.
- **NIST AI RMF:** `[sem fonte]` em **11 de 11**.
- **EU AI Act:** citado por **1 de 11** — só o Bradesco, no Trusted AI. (O Santander é grupo europeu e o EU AI Act se aplica a ele, mas **não há material do próprio banco citando a norma** — a associação aparece só em comentário de terceiro.)

---

## 3. ⚠️ Quarta correção do acervo

O Log do Ledger vem registrando, desde 31/08: *"explicabilidade em 10 dos 11 `[sem fonte]` — **só o Itaú tem mecanismo público**"*.

**Está errado, e invertido.** O que o Itaú tem de público é o **direito de revisão do art. 20 da LGPD** — obrigação legal, presente também em Bradesco e Inter, e que **não é mecanismo de explicabilidade**. Os players com material público de governança/explicabilidade de modelo são, nesta ordem de verificabilidade:

1. **Santander** — framework do Conselho **+ código aberto inspecionável** (o único que dá para auditar sem acreditar).
2. **Bradesco** — documento próprio, assinado, com EU AI Act, kill switch e auditoria independente (afirmado, não inspecionável).
3. **Banco do Brasil** — parâmetros ricos, **PDF não publicado**, descritos por fornecedor.

E o Itaú não está entre eles. **Este é o quarto erro material derrubado em quatro passadas** — depois do "80%" de recuperação do MED, do "rastreio em 5 camadas" e da IN BCB 746. Padrão: os quatro vieram de fonte secundária ou de repetição interna sem verificação. *A regra derivada na passada anterior — nada entra sem documento primário atrás — vale também para afirmação sobre player, não só para norma.*

---

## 4. Lacunas que sobraram (não são ausência, são não-verificado)

- **Itaú:** Medium/Itaú Tech atrás de login — a política de IA responsável, RAI/HAX e Red Team/Blue Team podem existir e não foram coletáveis. Blog AWS sobre Bedrock **não verificado** (fetch recusado).
- **Banco do Brasil:** corpo da política de privacidade não renderizou (`bb.com.br`, metadado **03/08/2026**); guia de IA sem PDF público.
- **Mercado Pago:** todas as páginas de `mercadopago.com.br` renderizadas por JS, conteúdo obtido via índice de busca — **revalidar antes de citar literalmente**.
- **Nubank:** 20-F FY2025 capturado só parcialmente; seção de fatores de risco não lida. → *parcialmente resolvido em §4.2 (02/09): existe fator de risco dedicado a IA, recuperado por busca sobre o documento primário — corpo integral segue não lido.*
- **PagSeguro:** 20-F FY2025 (arquivado **29/04/2026**) não lido — sec.gov inacessível no ambiente. → *✅ **resolvido em §4.2 (02/09)**: documento aberto e lido da capa ao meio do Item 3.D, incluindo os dois fatores de risco de IA e o de LGPD.*
- **Stone:** todo o bloco da Vela vem de snippet de busca (TI Inside bloqueou fetch). **Não citar número da Vela num board sem reabrir a fonte.** → *parcialmente resolvido em §4.1 (02/09): números conferidos no SEC 6-K e corrigidos; a Vela em si segue não-primária.*
- **C6:** material principal é de **2024**; o único item de 2026 (Gemini Enterprise em fraude/PLD, ganho de 26,42% no tempo médio de análise) veio de snippet não verificado.
- **Caixa:** dissertação "Governança de IA em instituições financeiras: o caso da CEF" (repositório IDP) — conteúdo integral não acessível. Pista aberta.

---

## 4.1 — Passada de recuperação de fontes (2026-09-02)

> Varredura da lista de §4 acima. **Browser renderizado indisponível** nesta passada (navegação exige aprovação interativa; rotina agendada não pode responder). Tudo abaixo foi recuperado por `web_fetch`/busca. Nenhum nível EMA-J alterado.

### ✅ RESOLVIDO — o "sec.gov inacessível" estava errado
`sec.gov` **é acessível** neste ambiente. O que impede a leitura não é acesso, é **tamanho**: o fetch trunca documentos longos. Os dois filings estão localizados e abertos:

- **Nubank — 20-F FY2025:** [sec.gov/Archives/.../nuform20f_2025.htm](https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm). Captura desta passada cobre **do índice até ~Business Overview (Item 4.B)**; **Risk Factors (Item 3.D, a partir da p. 85) segue não lido** — é lá que moram os fatores de risco de dado/IA. No trecho lido, o 20-F trata IA como **ativo competitivo, não como risco governado**: *"60+ machine learning algorithms"*, "Unique Data", NuX credit engine. **Zero menção a explicabilidade, residência de dado ou jurisdição de inferência no trecho lido** — coerente com a recusa escrita do Aviso de Privacidade (§2).
- **PagSeguro/PagBank — 20-F FY2025:** [sec.gov/Archives/.../pags-20251231.htm](https://www.sec.gov/Archives/edgar/data/0001712807/000155485526000826/pags-20251231.htm) — **localizado e acessível**, não lido nesta passada. Deixa de ser "inacessível" e passa a ser "pendente de leitura em chunks".

### ⚠️ QUINTO ERRO — o número da Vela (Stone) está desatualizado
O acervo registrava, junto ao lançamento da Vela, "**4,7 mi de clientes ativos**" e "R$ 560,9 bi processados em 2025". Conferido no **primário** (SEC, Form 6-K — *Earnings Release 4Q25*, 02/03/2026):

- **TPV total 2025 = R$ 560,9 bi** (vs. R$ 516,2 bi em 2024, **+8,7%**) — ✅ **confirmado**.
- **Base de clientes ativos = 4.803,5 mil (4,8 mi)** ao fim de 2025, **+15,1% a/a**. Os **4,7 mi** são ou a base **MSMB**, ou o número do **3T25 (4.716,2 mil)** — **não** a base ativa total no momento do anúncio da Vela (21/07/2026).
- **Formulação segura num board:** *"Stone: R$ 560,9 bi de TPV e 4,8 mi de clientes ativos de pagamento em 2025 (SEC 6-K 4Q25)"*.

**A Vela em si segue não-primária.** `blog.stone.co` é página institucional parada em 2018; o RI (`investors.stone.co/news-events/press-releases`) carrega os releases por JS e devolve "Loading..."; o TI Inside recusa fetch. Existência, data e escopo da Vela convergem em **duas leituras secundárias independentes** (TI Inside, 21/07/2026, e índice do RI): plataforma corporativa de IA **em operação interna**, agentes dedicados a **Produto e Crédito**, novos agentes sendo conectados a **Compliance, Confiabilidade e Custos**, integrada ao **Karavela**, acesso em linguagem natural em português sob permissões/governança/auditoria; CTO **Raúl Rentería** enquadra IA como "infraestrutura crítica". **Citável por existência, data e escopo — nunca por número.**

### ⚠️ SEXTO ERRO — os "17 mi do Mago" colam dois fatos
O acervo registrava "Mercado Pago lançou o **Mago** (17 mi alcançados, executa Pix/boleto por voz)". Recuperado em fonte secundária **aberta e datada** (Meio & Mensagem, 17/10/2025):

- O **assistente pessoal** foi anunciado em **16/10/2025**, primeira versão com **60 funcionalidades** conversacionais, texto **ou voz**, **tecnologia proprietária**, lançado **primeiro no Brasil**. Contexto: MELI investiu **US$ 1,9 bi em tecnologia em 2024**, ~20 mil desenvolvedores na AL.
- Os **17 mi são alcance acumulado do assistente desde out/2025** — **não** usuários do Mago, que é a **evolução** anunciada em ago/2026.
- ⚠️ **Divergência de data do Mago não resolvida:** TI Inside marca **14/08/2026**; outras coberturas marcam **18/08/2026**. Não citar data do Mago sem reabrir.
- `mercadopago.com.br/blog` **segue devolvendo corpo vazio** por renderização JS — o player não foi lido em fonte própria. **Continua valendo: não citar o Mercado Pago literalmente.**

### 🟨 NÃO RESOLVIDO — BB
`bb.com.br/site/politicas-de-uso-e-privacidade` é página **Elementor com corpo carregado por JS**: o fetch devolve só o cabeçalho. Recuperado apenas o metadado — **última modificação 03/08/2026** — e a **descrição declarada** ("informar como o Banco do Brasil trata seus dados pessoais em conformidade com a LGPD e com as leis aplicáveis à privacidade, sigilo e proteção de dados"). **Nada sobre transferência internacional, decisão automatizada ou explicabilidade foi lido.** BB permanece `[não-verificado]` — e agora com o **motivo** documentado, não como lacuna genérica.

### Padrão acumulado — agora são seis
"80%" do MED · "rastreio em 5 camadas" · IN BCB 746 · "só o Itaú tem explicabilidade" · "4,7 mi" da Stone · "17 mi do Mago". **Seis erros, todos do mesmo tipo:** vieram de **imprensa ou snippet** e **colaram dois fatos distintos num só** (ou congelaram um número num recorte errado). A regra derivada nas passadas anteriores — *nada entra sem documento do emissor atrás* — vale agora também para **número de player**, não só para norma. **Corolário novo:** todo número do acervo cuja origem seja snippet de busca deve ser tratado como **hipótese**, não como dado.

---

## 4.2 — Passada de leitura dos 20-F (2026-09-02, 2ª do dia)

> Alvo: as duas pendências de §4.1 que dependiam só de **leitura em chunks**, não de browser — o 20-F do PagSeguro (nunca lido) e os fatores de risco do 20-F do Nubank. **O browser renderizado foi negado de novo** (`preview_start` e `navigate` recusados sem aprovação interativa): 2ª passada consecutiva. As lacunas de BB, Mercado Pago e RI da Stone **seguem fechadas para a esteira automática**. Nenhum nível EMA-J alterado, nenhuma iniciativa nova.

### ✅ LIDO — PagSeguro/PagBank, 20-F FY2025 (o player que nunca tinha sido aberto em primário)

Fonte: [SEC, PagSeguro Digital Ltd., Form 20-F FY2025, `pags-20251231.htm`](https://www.sec.gov/Archives/edgar/data/0001712807/000155485526000826/pags-20251231.htm). **Trecho lido:** da capa até o meio do Item 3.D (Risk Factors) — os fatores de risco de IA e de LGPD estão dentro do trecho lido; o restante do documento **não foi lido**.

O PagBank tem **dois fatores de risco nomeados sobre IA**, e o par diz mais pelo que não diz:

1. *"We may lose our competitiveness if we are unable to incorporate AI tools into our business operations and products."* — risco de **não adotar**. Casos citados: cliente manda foto do problema na maquininha e a IA decide se troca o equipamento; análise do histórico de atendimento cruzado com portais de **open finance**; geração de código e teste automatizado. O corpo do risco é quase todo **propriedade intelectual** (origem de dado e algoritmo de terceiro, uso inadvertido de material protegido, autoria de conteúdo gerado).
2. *"AI regulation is rapidly evolving and AI regulation in Brazil remains uncertain."* — ancorado **exclusivamente no PL 2338/23** ("aprovado no Senado, em discussão na Câmara"). **Nenhuma menção ao EU AI Act.**

**O que não aparece em nenhum dos dois:** explicabilidade, viés, governança de modelo, residência de dado, jurisdição de inferência. O risco de IA está enquadrado como **risco de competitividade e de PI**, não como risco de modelo.
→ Amarração: o único vetor regulatório que o PagBank nomeia (**PL 2338**) está **adiado para depois de 2026** (§4 da nota de 31/08), enquanto o **Art. 50 do EU AI Act** já vige desde 02/08/2026 e a **Res. Conjunta 18** vence em 31/12/2026. O risco declarado aponta para o prazo que não chega; os prazos que chegam não estão declarados.

### 🆕 Achado novo — o stack de infraestrutura do PagBank está nomeado no 20-F

Literal: *"our IT infrastructure managed services and cloud computing environment are supported by solutions from **Scala Data Centers S.A.**, **Amazon Web Services, Inc.**, and **Oracle do Brasil Sistemas Ltda.**"* — mais um cliente da IBM/AWS na matriz de §2.3, que tinha o PagBank só sob AWS. **Ressalva de honestidade:** Scala e "Oracle do Brasil" são entidades brasileiras, mas o 20-F fala de **infraestrutura de TI**, não de carga de IA — **não é declaração de residência de inferência**. O placar de §2.1 segue **0/11**.

### 🟨 PARCIAL — Nubank: existe, sim, um fator de risco dedicado a IA (qualifica §4.1)

O fetch do 20-F volta a truncar no mesmo ponto (~p. 29, Colômbia), então **o corpo do Item 3.D segue não lido diretamente**. Mas **busca sobre o próprio documento do sec.gov** recupera o título e parte do corpo de um fator de risco dedicado:

> *"Our use and provision of solutions powered by artificial intelligence could lead to operational or reputational damage, competitive harm, legal and regulatory risk and additional costs."*

Com escopo de uso declarado (atendimento, **análise de crédito**, analytics, **detecção de fraude**, PLD, **triagem de sanções**, personalização de produto, marketing) e admissão de que os modelos *"might not always be correctly designed or implemented and could rely on data that is **biased, incomplete, or otherwise suboptimal**"*.

**Isto qualifica o que §4.1 registrou.** A frase "o 20-F trata IA como ativo competitivo, não como risco governado" vale para o **Item 4.B (Business)**, que foi o trecho efetivamente lido — **não para o filing inteiro**. No documento obrigatório aos reguladores americanos, o Nubank **nomeia viés e falha de modelo**; no Aviso de Privacidade ao cliente brasileiro, **recusa por escrito explicar como o sistema funciona** (§2.4). A assimetria não é entre ter e não ter governança — é **entre a quem ela é declarada**.
⚠️ **Nível de proveniência:** título e trechos vêm de **busca sobre o documento primário**, não de leitura direta. Pela regra do próprio acervo, **hipótese forte, não dado** — **confirmar literal antes de citar num board**.

### Constraint que virou padrão

Duas passadas seguidas com o browser negado. As três lacunas que só JS resolve (**BB**, **Mercado Pago**, **release da Vela no RI da Stone**) são agora **estruturalmente inalcançáveis** pela rotina automática. O item (c) do cardápio — passada supervisionada com browser — deixou de ser preferência e virou **a única via**.

---

## 5. Conexão com o frame regulatório (§4 da nota de 31/08)

Duas amarrações que a varredura torna literais, ambas **descritivas**:

- O achado da passada de 04:08 — *a **Res. Conjunta CMN/BCB nº 18/2025** (prazo **31/12/2026**, diretor responsável nomeado, responsabilidade indelegável do CA, dicionário de dados, trilha de auditoria, relatório semestral) é a norma mais próxima de governança de modelo vigente no Brasil, e não menciona IA* — encontra aqui o outro lado da conta: **10 dos 11 players não publicam explicabilidade e 11 dos 11 não publicam jurisdição de inferência**, a quatro meses do prazo.
- O **Art. 50 do EU AI Act** (transparência, em aplicação desde **02/08/2026**, marcação até 02/12/2026) pega todo assistente conversacional do conjunto. **Um único player dos 11 cita a norma em material próprio.**

---

## 6. O que eu diria sobre isso num board

⏳ **para o Bruno.**

Matéria-prima que a passada deixa na mesa, sem interpretação:

- 0/11 residência declarada · 0/11 jurisdição de inferência · 6/11 transferência internacional declarada · 1/11 cita EU AI Act · 0/11 ISO 42001 ou NIST AI RMF.
- O único trilho de residência no país é **estatal** (Serpro), contratado por **inexigibilidade**, e roda **em Azure**.
- Um player **nega explicabilidade por escrito**, invocando segredo de negócio, enquanto opera modelo fundacional próprio sobre 100 bi de transações.
- Um player põe **governança de modelo em repositório público Apache-2.0** — incluindo teste contrafactual de discriminação em crédito — e é o mesmo que assinou MoU de IA agêntica com fornecedor sob jurisdição de **Abu Dhabi**.
- Três construíram **modelo/plataforma própria** (nuFormer, Iara, Kunumi): a resposta brasileira ao risco de fornecedor tem sido "faço o meu", não "roteio por jurisdição".

**Contraponto a considerar** ⏳: ausência de declaração pública **não é** ausência de controle — nenhum destes bancos é obrigado a publicar residência de dado, e o silêncio pode ser postura jurídica, não lacuna operacional. A afirmação segura é sobre **o que é verificável por um terceiro**, não sobre o que existe.

---

*Telas 🖼️ pendentes (captura supervisionada). Nenhum nível EMA-J alterado nesta passada — a máquina não reclassifica sozinha.*
