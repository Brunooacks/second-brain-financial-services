---
tipo: auditoria
setor: financeiro
data: 2026-09-02
origem: rotina noturna — 47ª passada
tags: [proveniencia, auditoria, ganhos, governanca, dado-e-rei, lote-2]
status: coleta concluída · tese ⏳ para o Bruno
---

# Auditoria de proveniência dos ganhos do acervo — lote 2 (27 afirmações · Inter, Mercado Pago, Caixa, C6, PicPay, Stone/PagBank + setor fraude/Pix/MED)

> **Por que esta passada existe.** O lote 1 (02/09, 46ª passada) auditou os 16 números mais visíveis do acervo e achou 37,5% de erro. Deixou como alvo automático o lote 2: os players de expansão + os ganhos setoriais de fraude/MED. Esta passada executa exatamente isso.
>
> **Regra mãe respeitada:** verificar proveniência é coleta. Nenhum nível EMA-J foi alterado, nenhuma iniciativa criada, nenhuma jornada aberta. **Teses ⏳ para o Bruno.** Coleta feita por três agentes paralelos (players 1–3 / players 4–5 / adquirentes + setor) e consolidada aqui.

---

## 1. Placar da auditoria

| | Contagem |
|---|---|
| Afirmações auditadas | **27** |
| ✅ Confirmadas em **primário (emissor/RI/regulador)** | **7** |
| ✅ Confirmadas **com correção de escopo/rótulo** | **8** |
| 🟨 Só em **secundária** (imprensa/fornecedor) | **4** |
| ❌ **Derrubadas** (erro material, sujeito errado ou sem lastro) | **7** |
| 🔍 **Não localizadas** — não citáveis | **1** |

> **Taxa de erro do lote 2: 7 de 27 = 25,9%** (lote 1: 37,5%). Acumulado dos dois lotes: **13 erros em 43 afirmações = 30,2%**. Dos 7 erros deste lote, **4 são setoriais** (Pix/MED/fraude) — o bloco "de contexto" do acervo, que parecia o mais seguro, é o mais podre.

---

## 2. Os erros derrubados (13º ao 19º do acervo)

### ❌ 13º — Caixa: "Caixa Tem com 130 milhões+ de usuários"
Sem lastro oficial. A única ocorrência é o título de um blog de fintech (Antecipa Fácil, 05/05/2026) sem fonte. O último número **oficial** localizado é *"marca de 100 milhões de poupanças sociais digitais"* ([Agência Brasil, 04/11/2020](https://agenciabrasil.ebc.com.br)) — são **contas**, não usuários, e o dado tem quase 6 anos. Imprensa de jun/2026 cita "158 milhões de clientes" da **Caixa inteira**, não do app. A Caixa não publica métrica de usuários do Caixa Tem em 2026; `caixa.gov.br/caixatem` não renderiza.
- **Impacto:** o "130 mi+" sustentava o argumento "maior base social do país sem IA" em **quatro** notas de Fase 2 (pagamentos, fraude, atendimento, advisor). O argumento sobrevive com "100 mi de poupanças sociais digitais (nov/2020)" ou "158 mi de clientes do banco (imprensa, 2026)" — mas com recorte explícito.

### ❌ 14º — Caixa: "única habilitada no consignado CLT via Open Finance, testes em ago/2026"
Três erros numa frase.
- (i) A Caixa é a única iniciadora de **portabilidade de crédito pessoal sem garantia** no Open Finance (desde fev/2026), **não** de consignado. Literal: *"A única iniciadora de portabilidade habilitada hoje é a Caixa Econômica Federal"* — Elcio Calefi, Associação Open Finance ([Finsiders, 01/06/2026](https://finsidersbrasil.com.br)).
- (ii) O próximo produto no trilho é **consignado público federal**, não CLT. O cronograma (piloto ago/2026, lançamento nov/2026) foi **pausado**: *"Minha percepção hoje é que o piloto deve ficar para 2027"* (mesma fonte).
- (iii) O consignado CLT roda na plataforma **Crédito do Trabalhador / Dataprev** (Lei 15.179/2025), com 80+ instituições, sem trilho Open Finance definido.
- **Fonte:** Associação Open Finance via imprensa — não Caixa, MTE nem Bacen. 🟨
- **Impacto:** a iniciativa F2 "Trilho soberano de consignado via Open Finance" (score 23) foi construída sobre um fato errado. Reabrir.

### ❌ 15º — C6: "NPS 71 no Carbon"
Única fonte é blog afiliado de cartões ([cartoespremium.online, 01/03/2026](https://cartoespremium.online/c6-carbon-vale-a-pena/)), sem origem citada e com erro factual no mesmo parágrafo ("30 mi de clientes" quando o C6 declara 40 mi). Não aparece em release, RI, imprensa de negócios nem fala de executivo. **Não usar.**

### ❌ 16º — Stone: "11 milhões+ de clientes" no agentic commerce / cobrança WhatsApp via Iniciador
Dois erros.
- O número: "11 milhões" só aparece em blog de terceiro (SocialHub), sem fonte Stone. O emissor diz **4,8 mi de clientes ativos** (6-K 2T26, [SEC](https://www.sec.gov/Archives/edgar/data/0001745431/000207097926000275/stoneco_earningsrelease2q2.htm)) e "quase 5 milhões de empreendedores" no rebranding (Let's Money, 20/07/2026).
- O vínculo: **nenhum anúncio da Stone** de agente de cobrança no WhatsApp foi localizado. O Pix agêntico do **Iniciador** (ITP independente) é com Tyxter/Magie/Jota — sem vínculo Stone localizado.
- **Impacto:** o achado F2-5 *"Stone é cliente do mandato, não dono"* perde o sujeito. A frase precisa de fonte ou sai. A iniciativa F2 "Camada de mandato de cobrança agêntica sobre trilho de terceiro p/ adquirentes" (score 25, a mais alta do lote) fica **sem caso âncora**.

### ❌ 17º — Setor: "Pix — R$ 6,5 bi de perda em 2025 e 28 milhões de vítimas"
- **R$ 6,5 bi não foi localizado em nenhuma fonte.**
- **28 milhões** existe, mas com sujeito e recorte errados: *"entre janeiro e setembro de 2025, foram contabilizados 28 milhões de **fraudes** envolvendo o Pix"* — **ADDP** (associação privada) via [Correio Braziliense, 21/11/2025](https://www.correiobraziliense.com.br). São **casos**, não vítimas; **jan–set**, não ano cheio.
- **Substitutos com fonte:** Febraban/FBSP — **24 mi de vítimas de Pix+boleto, ~R$ 29 bi, jul/24–jun/25** (audiência no Senado, ago/2025); ou o número BC/Febraban de 2024 (R$ 4,94 bi).

### ❌ 18º — Setor: "MED 2.0 — recuperação sobe de <7% para 80% via rastreio em 5 camadas"
O **80% é folclore de fornecedor**. Circula em blogs da Matera, Okai e VAAS atribuído a "estudos do Bacen" sem link. O BC **nega meta numérica**: *"o BC não tem um número definido para o novo índice de devolução"* — Breno Lobo, BC ([Finsiders, 22/04/2026](https://finsidersbrasil.com.br/pagamentos/pix/o-que-muda-no-pix-a-partir-de-maio-com-o-med-2-0/)). Taxa real: **13,31% (fev/2026, BC)**; 8% em 2024. E as 5 camadas são **objetivo**: *"Estamos, atualmente, indo até a segunda camada"* (Finsiders, 31/07/2026).
- **Impacto:** o "L5 aberto pelo MED 2.0 com 80% de recuperação prometida" (achado F2-4, iniciativa "Malha de rastreio MED 2.0", score 24) precisa ser reescrito: o vale existe (13% de recuperação, rastreio na 2ª de 5 camadas), mas a "promessa de 80%" não é do regulador.

### ❌ 19º — Setor: "Pix — 30,1 bi de transações em 2025, +20%"
Não bate com nenhum recorte do BC. Relatório de Gestão do Pix (BC, 10/08/2026): **79,8 bi de transações em 2025, +25,7%** (vs 63,4 bi), R$ 35 tri (+33,8%). O 1S25 sozinho foi 27 bi. O "42% do e-commerce" é verdadeiro mas **não é BC**: é o **Worldpay Global Payments Report 2026** (share em valor, 2025; cartão de crédito 40%). 🟨

---

## 3. Correções de escopo (o número existe, o rótulo mente)

| Afirmação no acervo | O que a fonte diz literalmente | Consequência |
|---|---|---|
| **Inter: "35 mi de clientes" + "onboarding via GOV.BR"** | *"autenticação de 35 milhões de clientes do banco no portal de serviços do governo federal"* — release MGI, 05/06/2025 (espelho Convergência Digital; gov.br/gestao não renderiza) | **Sujeito invertido:** não é o Inter fazendo onboarding via GOV.BR — é o **login bancário do Inter elevando a conta GOV.BR a nível Prata** (acordo MGI+Febraban; Inter foi a 15ª instituição). 35 mi é jun/2025; RI 2T26 diz **45,3 mi totais / 26,4 mi ativos**. ✅ corrigido |
| **Inter: "Seven >11 mi clientes / +20 mi acessos"** | *"mais de 11 milhões de clientes utilizaram a ferramenta, somando mais de 20 milhões de acessos somente em 2026"* — release Inter via ClienteSA (12/05/2026) e brand story paga (NeoFeed) | O **blog oficial do Inter não traz esses números** (só "base de mais de 43 mi"). 11 mi = fase 1 conversacional desde 2025; 20 mi = só 2026 até maio. 🟨 release via imprensa |
| **Inter: "Seven executa Pix"** | *"permitindo que o cliente execute ações via conversas… transferências via Pix"* / *"aprova o resultado antes de qualquer ação sensível"* ([blog.inter.co, 05/05/2026](https://blog.inter.co)) | Executa, **com validação prévia do cliente** — L4 com humano no loop, não L5. ✅ primário |
| **Inter: "Seven com Cohere/Nvidia"** | — | 🔍 **Nenhuma fonte pública.** Não afirmar. |
| **Mercado Pago: "~5.000 variáveis por transação"** | *"São mais de cinco mil variáveis analisadas"* — [empresas.mercadopago.com.br](https://empresas.mercadopago.com.br), página sem data (cita dados de 2021–22) | É Mercado Pago (não ML), fase **"1st score" do antifraude de checkout e-commerce**, texto ~2022/23. Versão de ~2019 dizia "milhares". ✅ primário sem data |
| **Caixa: "Aixa" como assistente ao cliente** | *"plataforma cognitiva para oferecer aos seus funcionários e prestadores de serviço… 150 mil usuários"* — release Stefanini/Caixa, fev/2018 | Aixa nasceu **interno (service desk de TI)**. Existe aixa.caixa.gov.br mas não renderiza; caixa.gov.br descreve "assistente virtual 24h" sem nomeá-lo. **Nenhuma métrica pública atual.** ⚠️ o "Assistente Digital Caixa" premiado nos Banking Tech Awards é da **CGD (Portugal)**. ✅ corrigido |
| **C6: "melhor jornada digital idwall 2 anos consecutivos"** | 2024: 1º em jornada geral **e** em abertura de conta ([c6bank.com.br/blog, 13/03/2024](https://www.c6bank.com.br/blog/c6-bank-e-o-banco-com-melhor-jornada-do-cliente-diz-pesquisa)). 2025: 1º em jornada geral **entre digitais**; **Melhor Onboarding Digital foi do PagBank** (2º PicPay, 3º MP) — ClienteSA, 05/06/2025 | "2 anos consecutivos" só vale para **jornada geral entre digitais**. Em **onboarding, o C6 não venceu em 2025** — e o acervo usou isso como líder L3 de onboarding. ✅ corrigido |
| **C6: "40 mi clientes / lucro R$ 2,46 bi"** | *"Com 40 milhões de clientes… lucro líquido de R$ 2,5 bilhões, crescimento de 8,5%"* ([c6bank.com.br/blog/lucro-c6-bank](https://www.c6bank.com.br/blog/lucro-c6-bank), 27/02/2026) | Ano cheio 2025. Emissor arredonda 2,5; 2,46 é da imprensa. C6 é fechado — teto é blog institucional, não RI. 40 mi = base total, não ativos. ✅ primário |
| **C6: "acordo GOV.BR jul/2025 ~30 mi"** | Título do MGI: *"autenticação de 30 milhões de clientes no GOV.BR"* (15/07/2025; gov.br não renderiza — espelhos TI Inside/Convergência) | São **clientes do C6** que **podem** logar no GOV.BR com credencial bancária (nível prata). Potencial, não entrega. C6 = 16ª instituição. 🟨 |
| **C6: "carteira +49% no ano"** | *"A carteira de crédito **expandida** fechou o ano em R$ 89,3 bilhões, avanço de 49%"* (mesma fonte) | Denominador é carteira **expandida**, 2025 vs 2024. ✅ primário |
| **C6: "ataque deepfake — 709 tentativas / 259 contas / 0 invasão / condenação"** | *"709 tentativas de acesso a 259 contas bancárias diferentes, além da abertura de uma conta falsa"* — sentença da 4ª Vara Criminal de Goiânia via [Mais Goiás](https://www.maisgoias.com.br) / O Hoje, 06–07/10/2025 | Fonte é **sentença judicial via imprensa local**, origem em denúncia do C6 (O Hoje). **"0 invasão concretizada" não está escrito em lugar nenhum** — o que consta é tipificação por *tentativa* + **uma conta falsa aberta** com sucesso. ✅ corrigido |
| **C6: "renegociação GenAI 2 mil → 7 mil clientes"** | *"Abrimos primeiro para base de 2 mil clientes e depois expandimos para 7 mil"* — Gustavo Torres, C6 ([Convergência Digital, 24/06/2024](https://convergenciadigital.com.br/mercado/c6-bank-usa-ia-generativa-para-renegociar-dividas-e-revisar-codigo-fonte/)) | **Piloto de maio/2024**, cartão, dívidas curtas e baixas, conversas monitoradas. Dado tem **2 anos** e nunca foi atualizado — não usar como estado atual. ✅ corrigido |
| **PicPay: "67 mi contas / 42,7 mi ativos 4T25"** | Earnings Release 4Q25, 6-K PicS N.V. ([SEC](https://www.sec.gov/Archives/edgar/data/1841644/000121390026031560/ea028233701ex99-2.htm)) | ✅ RI de listada. Mas "ativo" = *"opened the app and/or made at least one transaction and/or generated revenues in the quarter"* — **abrir o app já conta**. Não é MAU. |
| **PicPay: "GPT-4.1 multiagente — NPS +10 p.p. / −8 p.p. handoff"** | *"Já nas primeiras horas após iniciar o uso do GPT-4.1 no Assistente PicPay, o NPS… saltou 10 pontos percentuais"* — release [PicPay + Microsoft, 02/06/2025](https://news.microsoft.com/pt-br/picpay-adota-ia-mais-avancada-do-modelo-gpt-em-seu-assistente-e-entra-na-era-dos-multiagentes/) | Não é OpenAI: é **Azure OpenAI Service**. Denominador do NPS = **só quem interage com o Assistente**. "Primeiras horas" é literal — **sem baseline nem janela**. Dado de jun/2025. ✅ primário (release conjunto) |
| **Stone: "carteira R$ 2,836 bi +134,9% / lucro R$ 2,477 bi 2025"** | *"total credit portfolio reached R$2,836.3 million"* / *"Net income from Continuing Operations… 2,477.2"* — 4Q25 Earnings Release, 02/03/2026 | R$ 2.477,2 mi é **lucro AJUSTADO de operações continuadas** (+17,5%); contábil total = R$ 2.609,9 mi. Carteira em 31/12/25, +23,4% t/t, +134,9% a/a. ✅ primário |
| **PagBank: "−27% custo atendimento / ~34 mi atendimentos 2021–23"** | *"reduzir seus custos operacionais em 27%… cerca de 34 milhões de atendimentos pelo chatbot"* — Arilda Lima, PagBank ([Consumidor Moderno, 01/07/2024](https://consumidormoderno.com.br/pagbank-reduz-custos/)) | Entrevista à imprensa, não RI. 27% = custo **do atendimento**, período não declarado; 34 mi = **pelo chatbot**. Dado de 2024. 🟨 |
| **PagBank: "Minizinha Voz início de 2026"** | *"A primeira maquininha que vende por voz"* ([pagbank.com.br/campanhas/minizinha-voz](https://pagbank.com.br/campanhas/minizinha-voz)); anúncio 27/01/2026, grupo restrito fev/26 a R$ 11,50, geral previsto abr/26 | ✅ primário (página de campanha; nada em RI) |
| **Setor: "ACI projeta >R$ 12 bi até 2028"** | *"pode alcançar R$ 12,22 bilhões até 2028"* — ACI Scamscope via [CNN Brasil, 22/01/2025](https://www.cnnbrasil.com.br/economia/financas/golpes-com-pix-podem-superar-r-12-bi-ate-2028-diz-estudo/) | Escopo = **APP scams em pagamentos em tempo real**, 6 países. R$ 12,22 bi é o **cenário pessimista** (neutro 9,6; otimista 7,5). Base 2023 = R$ 2,2 bi. PDF ACI não acessado. 🟨 |
| **Setor: "deepfake +126% / personificação +140%"** | *"alta de 126% nas fraudes com deepfakes e identidades sintéticas em 2025"* (Sumsub 2025–26 via BPMoney, 13/12/2025); *"identidade sintética… salto de 140%… primeiro trimestre de 2025"* (Sumsub 1T25 via TI Inside) | Emissor é **Sumsub** (fornecedor KYC, base = suas verificações). **140% não é "personificação"**: é **identidade sintética, 1T25 vs 1T24**. Dois períodos diferentes colados. ✅ corrigido |
| **Setor: "Pix Automático +182% 4T25→1T26"** | *"o Pix Automático cresceu na PagBrasil, registrando… 182% no volume de transações"* — Ralf Germer, CEO PagBrasil ([Central do Varejo, 08/07/2026](https://centraldovarejo.com.br/volume-de-transacoes-via-pix-automatico-cresce-182/)) | **Base da PagBrasil**, não BC nem mercado. ✅ corrigido |

---

## 4. O que ficou **✅ citável num board sem ressalva**

1. **Inter — Seven executa Pix com validação prévia do cliente** (blog.inter.co, 05/05/2026); base **45,3 mi totais / 26,4 mi ativos** (RI 2T26).
2. **C6 — 40 mi de clientes, lucro R$ 2,5 bi (+8,5%), carteira expandida R$ 89,3 bi (+49%), 2025** (c6bank.com.br, 27/02/2026) — blog institucional, banco fechado.
3. **PicPay — 67 mi de contas registradas (+11%) / 42,7 mi ativos no trimestre (+10%), 4T25** (6-K SEC) — com a ressalva de que "ativo" inclui abrir o app.
4. **Stone — carteira de crédito R$ 2.836,3 mi (+134,9% a/a), lucro ajustado de operações continuadas R$ 2.477,2 mi, 2025** (4Q25 release, 02/03/2026); **4,8 mi de clientes ativos** (2T26).
5. **Mercado Pago — "mais de cinco mil variáveis" no 1st score do antifraude** (site do emissor, sem data).
6. **PagBank — Minizinha Voz** (página de campanha, anúncio 27/01/2026).
7. **Setor Pix — 79,8 bi de transações em 2025 (+25,7%), R$ 35 tri (+33,8%)** (BC, Relatório de Gestão do Pix, 10/08/2026); **recuperação MED 13,31% em fev/2026** (BC via Finsiders).

---

## 5. Achados da passada (descritivos — a tese é do Bruno)

**5.1 — O bloco setorial é o mais frágil do acervo.** 4 dos 7 erros deste lote são números "de contexto" (perda com Pix, vítimas, meta do MED, volume do Pix). Eles entraram sem emissor porque pareciam consensuais — e três deles (R$ 6,5 bi, 80% de recuperação, 30,1 bi) **não existem em fonte nenhuma**. O 80% do MED 2.0 é o caso mais grave: é **folclore de fornecedor** que virou "promessa do regulador" em uma nota de-para e numa iniciativa de score 24.

**5.2 — A assinatura de erro do lote 1 se repete, com um tipo novo.** Recortes colados (Sumsub 126%+140%), rótulo trocado (fraudes→vítimas; ajustado→lucro; expandida→carteira; tentativa→"0 invasão"), sujeito trocado (Inter onboarding via GOV.BR → GOV.BR via Inter; PagBrasil → mercado; Worldpay → BC). O tipo novo: **número órfão** — sem emissor identificável em lugar nenhum (R$ 6,5 bi; 30,1 bi; 11 mi da Stone; NPS 71). No lote 1 todo erro tinha um número real por trás; aqui quatro não têm.

**5.3 — Três iniciativas de Fase 2 perderam o caso âncora.** "Trilho soberano de consignado via Open Finance" (fato errado: é portabilidade de crédito pessoal, piloto de consignado público adiado para 2027); "Camada de mandato de cobrança agêntica sobre trilho de terceiro" (Stone × Iniciador sem fonte); "Malha de rastreio MED 2.0" (80% não é do BC; rastreio hoje na 2ª camada). Os vales continuam existindo — mas a **evidência que os justificava era secundária ou inexistente**. ⏳ reclassificar após aval do Bruno.

**5.4 — A hierarquia de proveniência do lote 1 se confirma e ganha um degrau.** RI de listada (PicPay 6-K, Stone 4Q25, Inter 2T26) foi 100% limpo. Blog institucional de banco fechado (C6) foi limpo mas arredondado. Release conjunto com fornecedor (PicPay+Microsoft) foi fiel, com denominador escorregadio. Imprensa citando executivo foi fiel mas **envelhecida** (C6 2024, PagBank 2024). Blog de fornecedor e blog afiliado foram a origem de **todos os números órfãos**. Degrau novo, abaixo do snippet: **blog de fornecedor atribuindo número ao regulador sem link**.

**5.5 — A Caixa, "vale mais profundo" de seis notas, está medida com régua sem lastro.** O 130 mi+ não existe; o Aixa é service desk de 2018; a exclusividade no consignado é outra coisa. O que sobra com fonte: 100 mi de poupanças sociais digitais (2020), única iniciadora de portabilidade de crédito pessoal no OF (2026), L2 em quase tudo. O **argumento** (maior base social, menor maturidade) provavelmente sobrevive — mas hoje está sustentado por três números que não sustentam nada.

**5.6 — Barreira de renderização, 4ª passada.** Novos sites só legíveis com browser: `gov.br/gestao` e `gov.br/governodigital` ("Conteúdo Restrito"), `caixa.gov.br/caixatem`, `aixa.caixa.gov.br`, `mercadopago.com.br/blog`. Somam-se a BB, Mercado Pago (RI), RI da Stone (PDF mziq — lido só via web_fetch), TI Inside e Mobile Time. **Nove fontes BR** dependem do item (c).

---

## 6. Regra de higiene derivada (a 4ª do acervo)

As três anteriores: (1) norma só com PDF do regulador/DOU; (2) player só com documento do emissor; (3) todo ganho carrega recorte, denominador, sujeito e nível de proveniência.

> **4. Número setorial ("de contexto") entra com o mesmo rigor de número de player — e número atribuído ao regulador só entra com documento do regulador.** O acervo tratava contexto como pano de fundo e o pano de fundo era o que estava rasgado. "Estudos do Bacen" sem link é blog de fornecedor.

**Projeção:** ~47 ganhos do acervo seguem não auditados (Produtos + resto das jornadas do piloto). À taxa acumulada (30%), ordem de **14 correções pendentes**. Lote 3 sugerido: **ganhos das 8 categorias de Produtos + ganhos de investimentos/advisor do piloto (Itaú 100 mil, BTG >80%, Bradesco 500 mil/40 mil)**.

---

## 7. O que eu diria sobre isso num board

⏳ **para o Bruno.**

Matéria-prima nova que esta passada entrega:
- acumulado de **13 erros em 43 afirmações (30,2%)** e uma categoria nova de erro — **número órfão** — concentrada no bloco setorial;
- a constatação de que o **"80% de recuperação do MED 2.0" não é do BC** (recuperação real: 13,3%; rastreio hoje na 2ª de 5 camadas);
- três iniciativas de Fase 2 (scores 25, 24, 23) **sem caso âncora com fonte**;
- a Caixa como vale medido com números que não existem;
- e o dado mais robusto do lote, que **fortalece** a tese de escala: **Pix fez 79,8 bi de transações em 2025 (+25,7%)** — 2,6× o que o acervo dizia.

**Contraponto que a máquina registra sem resolver:** ⏳ para o Bruno.

---

## Ligações
- [[2026-09-02 — Auditoria de Proveniencia dos Ganhos do Acervo]] (lote 1)
- [[2026-09-01 — Residencia de Dados e Explicabilidade nos 11 Players]]
- [[_Ledger-Discovery]]
- [[De-Para — Onboarding & KYC (Fase 2 · expansão)]] · [[De-Para — Originação de crédito (Fase 2 · expansão)]] · [[De-Para — Pagamentos & Pix (Fase 2 · expansão)]] · [[De-Para — Prevenção a fraude & disputas (Fase 2 · expansão)]] · [[De-Para — Atendimento & cobrança (Fase 2 · expansão)]]
