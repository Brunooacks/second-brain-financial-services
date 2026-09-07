---
tipo: auditoria
setor: financeiro
data: 2026-09-03
origem: rotina noturna — 48ª passada
tags: [proveniencia, auditoria, ganhos, governanca, dado-e-rei, lote-3, produtos]
status: coleta concluída · tese ⏳ para o Bruno
---

# Auditoria de proveniência dos ganhos do acervo — lote 3 (45 afirmações · 8 Comparativos de Produtos + Investimentos/advisor do piloto)

> **Por que esta passada existe.** O lote 2 (02/09, 47ª passada) deixou como alvo automático o lote 3: os números dos 8 comparativos de `03-Comparativos/Produtos/` (Cartão, Crédito, Adquirência, Conta-PF, Conta PJ, Pagamentos-Pix, Investimentos, Seguros) + os ganhos de investimentos do piloto (Itaú 100 mil, BTG >80%, Bradesco 500 mil/40 mil). Esta passada executa exatamente isso — e é o **último lote**: com ele, os ~90 ganhos do acervo estão auditados.
>
> **Regra mãe respeitada:** verificar proveniência é coleta. Nenhum nível EMA-J foi alterado, nenhuma iniciativa criada, nenhuma jornada aberta, nenhum Comparativo editado (correções ficam aqui, para aval). **Teses ⏳ para o Bruno.** Coleta por três agentes paralelos (3A Investimentos+Seguros · 3B Crédito+Cartão · 3C Pix+Adquirência+Conta), sem browser, e consolidada aqui. Afirmações já derrubadas nos lotes 1–2 (Caixa Tem 130 mi, Stone 11 mi, Pix 30,1 bi, C6 "0 invasão", BB 500 soluções, Santander 280 agentes, NPS +10 p.p. etc.) **não foram reauditadas** — os Comparativos as repetem e herdam as correções.

---

## 1. Placar

| | Contagem |
|---|---|
| Afirmações auditadas | **45** (3A: 19 · 3B: 13 · 3C: 13) |
| ✅ Confirmadas em **primário** (RI/6-K/regulador/associação/site do emissor) | **8** |
| ✅ Confirmadas **com correção de escopo/recorte/data** | **20** |
| 🟨 Só em **secundária** | **2** |
| ❌ **Derrubadas** (erro material, sujeito/moeda/período errado, sem lastro, produto extinto) | **15** |
| 🔍 Não localizadas (sub-itens) | 10 — BTG >80%; Bradesco Seg. 22,8% share; "5 carteiras/mês"; MP 2.500/5.000 variáveis; Stone "2% usam crédito"; Abecs "premium +19%" e "215 mi cartões"; "11 adquirentes = 98%"; Getnet ~10% share; ranking B3 PF atual |

> **Taxa de erro do lote 3: 15 de 45 = 33,3%** (lote 1: 37,5% · lote 2: 25,9%). **Acumulado dos três lotes: 28 erros em 88 afirmações = 31,8%.** Só **8 de 45** (18%) têm proveniência de RI/regulador de verdade; o resto repousa em imprensa, release institucional ou blog de afiliado.

---

## 2. Os erros derrubados (20º ao 34º do acervo)

### Investimentos
- **❌ 20º — Itaú "1.800 modelos / 500 cientistas (3T25)" + "R$ 2,4 tri de custódia".** Os modelos/cientistas são Broadcast/Estadão, não RI; o banco fala em ~1,9 mil *iniciativas* e ~140–150 GenAI em produção (conceitos diferentes). **A custódia de R$ 2,4 tri é fala de executivo de 21/08/2023** — três anos de defasagem. Referência atual: R$ 1,1 tri sob gestão na asset (Itaú Day 2025), outra métrica. Fonte: NeoFeed 18/09/2025.
- **❌ 21º — Bradesco: Ágora "813 mil / 150 mil ativos / R$ 50 bi RV / 4ª maior PF na B3 / 5 carteiras por analista".** Os quatro números vêm de **uma frase de 13/11/2019** (Exame), e a própria fonte diz **3ª colocação**, não 4ª. O "5" não existe em lugar nenhum. BIA "500 mil clientes / 40 mil funcionários" é *"disponível para"*, em customer story da Microsoft (mai/2025), e investimentos é um item de lista, não o recorte.
- **❌ 22º — Inter "concierge de IA para 8,8 mi (Let's Money)".** Let's Money é o **veículo**, não parceiro; a matéria deriva de entrevista ao Valor Investe. O 8,8 mi (investidores com carteira) não aparece no release 1T26. O produto oficial chama-se **Seven**; "Inter Invest" é a plataforma, "Robô Advisor" é o produto.
- **❌ 23º — C6 "TechInvest 0,7% a.a. / Black-Litterman / 500 fundos / 35 mi clientes".** **O TechInvest não existe mais** — as URLs redirecionam para o sucessor **C6 Carbon Sistemático, 2% a.a. + 20% de performance** (quase 3x a taxa citada). Black-Litterman só em imprensa de 2021; "500 fundos" é post de dez/2022 inconsistente (300 no corpo); **35 mi é 2024** — o release do balanço 2025 abre com **40 mi** e o 1S26 diz 42 mi.
- **❌ 24º — BB "custodiante do Tesouro para >3 mi de investidores em FII".** Sujeito errado e dois fatos fundidos: a **B3** é a depositária central; o BB é um agente de custódia entre dezenas. Os números são nacionais: Tesouro Direto **3,81 mi de investidores ativos** (STN, 25/08/2026) e **3,30 mi de investidores em FII** na B3 (jul/2026). A GenAI para MPE existe e chama-se **ARI**, mas os números circulantes divergem entre si.
- **❌ 25º — Mercado Pago "cofrinho 140% CDI Meli+".** Página oficial hoje: **140% só para compras no Mercado Livre (teto R$ 2.000, rendimento gasto na compra)**; **Meli+ rende 120%**; 115% com aporte de R$ 1.000. Os 140% para Meli+ foram campanha de **03/03 a 03/04/2026**. CDB 150% é Black Friday, novos clientes, teto R$ 3.000.

### Seguros
- **❌ 26º — Bradesco Seguros: "22,8% de share" e "sinistro auto +15%".** O único 22,8% público é **ROAE do 2T26** — rentabilidade lida como share; cortar. O "+15%" é **"ganho de até 15% no processo de sinistro"** com IA — ganho de eficiência, de **março/2023** — sentido invertido. "R$ 88 bi de prêmios" é **R$ 88,8 bi de *faturamento* (prêmios + previdência + capitalização), estável**, jan–set/25. Agentes saúde/prev/auto eram **roadmap** (set/2025), não produção.
- **❌ 27º — PicPay "2 mi+ apólices em ~1,5 ano; vida R$ 7,70".** Os 2 mi são de **23/11/2023**; o próprio PicPay anunciou **5 mi vendidas em 12/06/2024** (Revista Apólice `/2024/06/` — o blog do PicPay exibe meta-date de 2026 por migração de CMS, armadilha de datação). Denominador = **vendidas acumuladas**, não ativas. R$ 7,70 é preço de lançamento de jul/2023 (em nov/2023 já era "a partir de R$ 5,55"). A "Carteira Digital" cobre Pix sob **coação/roubo de celular**, não "fraude de Pix" em sentido amplo.
- **❌ 28º — Santander "US$ 40 mi de valor com IA no 1º tri".** O correto é **€35 mi no 1T26, Grupo Santander global**, texto assinado pelo Chief Data & AI Officer (santander.com, 22/06/2026). "US$ 40 mi" é conversão de imprensa (Finextra/PYMNTS). **A outra nota do acervo (€35 mi) é a certa.** É métrica de gestão (valor gerado = receita + custo evitado), não linha auditada de earnings.

### Crédito / Cartão
- **❌ 29º — Inter "carteira R$ 50 bi (+33%) com NPL 4,6%".** Par impossível: R$ 49,8 bi é **1T26**; 4,6% é o NPL 90+ do **1T25** (ou o 15–90 do 1T26). O NPL 90+ do trimestre da carteira citada é **5,1%** (6-K 1T26). O 4T25 fechou em R$ 48,3 bi / 4,7%.
- **❌ 30º — PagBank/Stone (recortes trocados).** PagBank "carteira R$ 5,0 bi / NPL 3,05%" é **1T26**; no 4T25 é **R$ 4,6 bi / NPL 2,9%**. "Crédito R$ 50 bi" é a **carteira expandida (R$ 49,7 bi, com recebíveis)** — 10x a clássica, na mesma linha. Stone "R$ 2,3 bi / 5,03%" é o **3T25**; o 4T25 é R$ 2.836 mi / NPL >90 **5,21%** (a nota de Fase 2 estava certa). "Só 2% da base usa crédito" 🔍.
- **❌ 31º — Caixa "R$ 1 tri em crédito imobiliário" (2025).** O marco foi atingido em **junho de 2026** — a nota antecipa em seis meses. O ~68% de share ✅. "21 cartões novos" 🟨 só imprensa de cartões.

### Pix / Adquirência / Conta
- **❌ 32º — Pix "79,8 bi de operações, +33,6%".** O +33,6% (BC: 33,8%) é crescimento de **valor** (R$ 26,2 → 35,3 tri); o de **transações é +25,7%** (Relatório de Gestão do Pix, 10/08/2026). E "R$ 179,9 bi" é o valor do dia 05/12; o **recorde de valor em 24h é R$ 193,47 bi em 19/12/2025** — dois recordes colados. "70 mi assíduos +71%" é **Febraban/Deloitte**, não BC.
- **❌ 33º — Adquirência "~R$ 4,2 tri de TPV" e "Rede ultrapassou Cielo em 2025".** Abecs 4T25: **R$ 4,5 tri (+10,1%), 48,1 bi de transações**. A virada da Rede é de **janeiro de 2026 (UBS BB), em TPV** — em número de clientes a Cielo ainda lidera (28% × 25%). "11 adquirentes = 98%" 🔍 — o boxe do REB 2023 do BC conta o oposto (HHI −49%, >25 competidores, **desconcentração**).
- **❌ 34º — PagBank "R$ 75/ano por inatividade".** É **R$ 75 por mês**, a cada mês inativo, após 360 dias sem movimentação (desde out/2025). Erro de 12x num custo ao cliente. No mesmo bloco de Conta PJ: Bradesco cestas são **R$ 52,60–550,70** (tabela 01/06/2026), não 121,90–479,90; C6 CDB é **104% do CDI desde 19/01/2026**; BB "canal WhatsApp 20 mi+" são **20,1 mi de *atendimentos* jan–mai/2024**, não usuários.

---

## 3. Correções de escopo (o número existe, o rótulo mente)

| Afirmação no acervo | O que a fonte diz | Fonte · nível |
|---|---|---|
| Itaú advisor "100 mil clientes" | 100 mil **aptos a usar** (elegíveis), rollout gradual; **25/11/2025** | CNN/Estadão · imprensa |
| Nubank "AI Private Banker em construção; 15 mi tocam" | *"already serve more than 15 million MAU"* — **já em produção**, Nu Holdings **consolidado (BR+MX+CO)** | release 1T26, 14/05/2026 · RI |
| Santander assistente advisor-facing "a partir de abril" | abril de **2025**, desenvolvida em 2024 ("Pitch Maker", BRQ+AWS) | santanderimprensa · release (só snippet) |
| Mercado segurador R$ 223,6 bi "IRB(Re)/CNseg" | **IRB+Inteligência** (não CNseg); prêmios SUSEP, exclui saúde/prev/capitalização; +7,7% | irbre.com 11/03/2026 · release |
| Caixa Seguridade ROE 70,4% | é **ROE do 4T25 (trimestral)**, não anual; lucro **gerencial** R$ 4,32 bi; R$ 9,67 bi só segmento seguros | release 4T25 via imprensa |
| BB Seguridade R$ 9,1 bi (+11,4%) | lucro **ajustado**; operacional +2,1%, financeiro +81% — **crescimento é Selic, não subscrição** | comunicado 09/02/2026 |
| Nubank/Chubb 2 mi apólices | apólices **ativas**, Brasil, **11/06/2024** — dois anos sem atualização | newsroom Nu · release |
| Inter Seguros 5,3 mi contratos | **ativos** 4T24 (+312%), giro curtíssimo (Seguro Pix/fatura); 2,7 mi = **vendidas no tri**; dez/2024 | 6-K 4Q24 SEC · RI |
| C6 Seg 7.000 corretores | é **assessoria para corretores parceiros** (ex-Som.us), não a corretora do banco | c6bank.com.br/c6-seg |
| Itaú carteira R$ 1,402 tri (+6,4%) / cartões PF +8,0% t/t | é **3T25**; 4T25 = R$ 1,49 tri (+6,0%); cartões PF é **+8,0% A/A** no ano, nunca t/t | comunicado RI |
| Bradesco R$ 1,03 tri (+9,6%) NPL 4,1% | **3T25**; 4T25 = R$ 1,089 tri; Kunumi "R$ 250 mi" só imprensa | 6-K 4T25 |
| Mercado Pago US$ 11 bi (+83%) NPL 6,8% | **3T25** e NPL **15–90**, não 90+; 4T25 = US$ 12,5 bi (+90%); "2.500/5.000 variáveis" 🔍 em qualquer fonte oficial — remover | release 3T25/4T25 MELI · 8-K |
| PicPay NPL "guidance 8,9%" | 8,9% é NPL 90+ **realizado do 1T26**; 4T25 = 7,2% | release 4T25/1T26 |
| BB "lucro −45% (4T25)" | 4T25 = **−40,1%**; −45% é o **ano 2025** | RI 4T25 |
| Abecs "aproximação ~R$ 2 tri" | **R$ 1,9 tri** (+31%) | PDF Abecs 11/02/2026 |
| C6 Átomos "cashback até 1,7%" | só **Carbon Black**; Black comum = 1,2% | site oficial |
| Bradesco BIA "24 mi usuários; 85–90% retenção; ~90% resolutividade" | **habilitada para** 24 mi; rótulos invertidos: **retenção até 90%, resolutividade >85%**; RI 2T26 = 34 mi interações/88% (o 74 mi é 1S26 — reconcilia) | TI Inside 06/2025 + RI |
| Pix Inteligente −75%/−60%/>74% | **canal WhatsApp**, 6 meses de operação, não o Pix do banco | IT Forum/StartSe · imprensa |
| Nubank Pix por IA −60% | "**até** 60%", no app; WhatsApp em teste com 2 mi (out/2024) | newsroom 10/12/2024 · release |
| C6 "pioneiro" Pix aproximação | precursor **junto com PicPay** (nov/2024) | imprensa |
| Rede TPV R$ 283,3 bi (+26%) / 150 mil→1 mi | é **1T26**; degrau omitido: **500 mil até fim de 2026** | Let's Money 25/06/2026 |
| Getnet "~130 transações/dia no piloto" | 130/dia em **um único estabelecimento** (Empório Andrade, POA); "agentic commerce" é interpretação da nota | release Getnet 29/06/2026 |
| MP "lucro adquirência R$ 1,93 bi" | **estimativa Itaú BBA para 2024** (abr/2025), não dado do emissor; "72 mi ativos" é 3T25 — 4T25 = **~78 mi MAU** | NeoFeed · sell-side |
| Stone 4,7 mi MPMEs | 4,7 mi **ativas em adquirência** (não base total) | DF 12/2025 · RI |
| Cielo "BB/Bradesco 50/50" | paridade **no bloco de controle** (~30,6% cada), não do capital; OPA liquidada a R$ 5,82 em 14/08/2026 | fato relevante |
| Santander 33,5 mi ativos "out/25" | é **2T25**; de 71,7 mi totais | RI |
| Inter Seven "180+ serviços" | tira dúvidas sobre 180+ produtos; executa Pix com **delega→acompanha→aprova** ✅ | blog Inter |
| Itaú "migra 15 mi do iti" | 15 mi de **seis apps somados** (iti é um deles), projeto One Itaú | Tecnoblog |
| MP cofrinho "115% CDI" | 115% é o **piso** (120% com Meli+/R$ 1.000); conta = 100%/105% | site oficial |
| PagBank "3%–100% CDI até R$ 100 mil" | 100% até R$ 100 mil **e 3% sobre o excedente**; inativa 360 dias → 3% sobre tudo | site oficial |
| Inter × GOV.BR "35 mi" | base **elegível** em jun/2025; Inter é a **15ª** instituição a aderir; RI 2T26 = 45,3 mi | TI Inside/Convergência 05/06/2025 |

---

## 4. Sobreviveram intactos (citáveis sem ressalva)

- **Nubank 4T25**: carteira US$ 32,7 bi (+40%), NPL 90+ 6,6%, ARPAC US$ 15 — Nu Holdings consolidado (release 25/02/2026, 6-K).
- **Santander BR 4T25**: carteira expandida R$ 714,9 bi (+3,7%), NPL 90+ 3,7% (RI).
- **C6 2025**: carteira expandida R$ 89,3 bi (+49%), NPL 2,9% (**2,0% ex-Res. 4.966**), lucro R$ 2,46 bi (blog institucional 27/02/2026).
- **Abecs 2025**: R$ 4,5 tri (+10,1%); crédito R$ 3,1 tri (+14,5%, 21,6 bi transações); débito R$ 1 tri; pré-pago R$ 397 bi; online R$ 1,1 tri (+18,3%); **Tap on Phone R$ 78 bi (+241%)** (PDF 11/02/2026).
- **Pix 2025 (BC)**: 79,8 bi transações (+25,7%), R$ 35,3 tri, **54,7% das transações no 2S25**, recorde 313,3 mi em 05/12.
- **Stone 2025**: TPV R$ 560,9 bi (+8,7%), 4,7 mi MPMEs ativas, portfólio R$ 2.836 mi (+134,9%) (DF/6-K).
- **PagBank 4T25**: 34 mi clientes, lucro R$ 678 mi, R$ 2,37 bi no ano, depósitos R$ 40,7 bi, Minizinha Voz R$ 11,50 (RI/release).
- **Inter Seguros 4T24**: 5,3 mi contratos ativos (6-K SEC). **C6 Seg 7 mil corretores** (site). **Inter Loop 1 pt/R$ 2,50 no Black** (site). **Caixa Ícone Visa Infinite** (release out/2025). **MP NPS Prism Bain 78 pts, 1º no BR, 3T25**.
- **Santander grupo**: €1 bi 2026–28, **€35 mi no 1T26**, 185 mil funcionários (santander.com 22/06/2026).

---

## 5. Achados da passada

**🆕 Achado 1 — o defeito dominante do lote 3 é *defasagem temporal*, não invenção.** Em 3A, 10 de 19 afirmações usam marco de imprensa antigo como estado corrente (Ágora 2019, custódia Itaú 2023, PicPay 2023, Nubank/Chubb 2024, C6 clientes 2024, Santander abr/2025). Em 3B, 7 de 11 números de crédito são corretos **em outro trimestre** (3T25 rotulado 4T25; 1T26 rotulado 2025). **Nenhuma afirmação do acervo carrega a data do dado, só a data da nota** — e as notas de Produtos foram montadas em jul/2026 com os releases de 1T26 já publicados, empilhando snippets de vintages diferentes na mesma frase (MP: TPV 4T25 + usuários 3T25).

**🆕 Achado 2 — carteira "expandida" × "clássica" e NPL "90+" × "15–90" nunca são qualificados.** Itaú, Bradesco, Santander, BB, C6 e PagBank reportam expandida e a nota escreve "carteira": viés de alta de 5–15% nos grandes e **erro de 10x no PagBank** (R$ 49,7 bi × R$ 4,6 bi). MP 6,8% é 15–90 ao lado de 90+ dos outros. E **2025 é o primeiro ano da Res. CMN 4.966** — qualquer ranking de NPL entre players com bases distintas é ruído (o C6 é o único transparente: 2,9% com, 2,0% sem).

**🆕 Achado 3 — o setor comunica piloto como escala, e o acervo reproduziu o enquadramento.** Todo ganho de IA do lote (Pix Inteligente −75%, Nubank −60%, Getnet 130/dia, BIA 24 mi) é real **dentro de um canal, um app ou um estabelecimento** — e foi registrado como métrica de instituição. Nenhum banco divulgou ganho de IA em base consolidada. Números de IA têm proveniência **estruturalmente pior** que números financeiros: nenhum dos "1.300 modelos / 150 GenAI / 400 projetos / R$ 250 mi Kunumi" aparece em release, ITR ou 6-K — todos são declaração de executivo a veículo de tecnologia.

**🆕 Achado 4 — denominadores de seguros não são comparáveis e o acervo os alinha como se fossem.** Nubank = apólices **ativas**; PicPay = **vendidas acumuladas**; PagBank = **clientes**; C6 = **corretores**; Inter = ativas *e* vendidas. Qualquer ranking cruzado é inválido. E o bloco de **tarifas/rendimento de Conta PJ** é o mais frágil do acervo: metade veio de blog de afiliado, e **3 de 3** verificadas contra o site oficial (MP, PagBank, C6) divergiam. Tratar Inter/PicPay/Stone como não confirmadas.

**🆕 Achado 5 — três Comparativos perderam um pilar de "diferencial real".** C6 "único com robo quantitativo declarado (TechInvest)" — produto extinto; BB "custodiante de >3 mi em FII" — dado nacional da B3; Bradesco Seguros "22,8% de share / sinistro +15%" — sem lastro/sentido invertido. O argumento estrutural de cada comparativo (investimentos não comoditizou; seguro para na porta do produto) **sobrevive**; a evidência citada, não.

**📏 5ª REGRA DE HIGIENE derivada:** *todo número entra com **vintage** (trimestre/data do dado, não da nota), com o **qualificador contábil** (expandida/clássica; 90+/15–90; pré/pós-4.966; ativas/vendidas), e ganho de IA entra com o **perímetro** (canal/app/loja ou consolidado). Sem os três, é hipótese.*

---

## 6. Lacunas que sobraram (não-verificado, não ausência)

- **Fontes que não renderizaram no web_fetch:** `bcb.gov.br` Estatísticas do Pix (recusado — validado por triangulação), santanderimprensa (só snippet), TI Inside 28/08/2025 (corpo vazio), 2 PDFs de tarifário PJ do Bradesco (vazio — faixa vem de metadados), PDF Abecs 4T25 (números recuperados por consistência). RIs de **Bradesco Seguros, CXSE3 e BBSE3** vieram via imprensa reproduzindo release — suficientes para nota, insuficientes para board. **Lista de fontes só-com-browser sobe para ~13.**
- **Reclassificações que dependem do Bruno (⏳):** Comparativo — Investimentos (C6 TechInvest → Carbon Sistemático; BB FII; Itaú custódia; Inter "concierge"); Comparativo — Seguros (Bradesco share/sinistro; PicPay 5 mi; Santander €35 mi); Comparativo — Crédito (Inter 5,1%; PagBank expandida; Caixa jun/2026; BB −40,1%; MP 15–90); Comparativo — Adquirência (R$ 4,5 tri; Rede jan/2026; Getnet 1 loja; MP estimativa BBA 2024); Comparativo — Pagamentos-Pix (+25,7%; R$ 193,5 bi 19/12); Comparativo — Conta PJ (bloco de tarifas inteiro); Comparativo — Conta-PF (BB atendimentos; Itaú 6 apps; Santander 2T25).

---

## 7. O que eu diria num board
⏳ **para o Bruno.** (Insumo: fechada a auditoria dos ~90 ganhos, **28 de 88 caíram (31,8%)** — e caíram com assinatura: número certo com recorte, sujeito, moeda ou vintage errados, herdado de imprensa e nunca reaberto. O acervo tinha razão nas teses estruturais e errado nas provas. A regra de proveniência emergente — RI > associação > release > customer story > imprensa > snippet, com vintage, qualificador contábil e perímetro obrigatórios — é ela própria a demonstração da governança que a oferta vende.)

**Liga com:** [[2026-09-02 — Auditoria de Proveniencia dos Ganhos do Acervo]] · [[2026-09-02 — Auditoria de Proveniencia dos Ganhos — Lote 2]] · [[Comparativo — Investimentos]] · [[Comparativo — Seguros]] · [[Comparativo — Crédito]] · [[Comparativo — Cartão]] · [[Comparativo — Adquirência]] · [[Comparativo — Pagamentos-Pix]] · [[Comparativo — Conta PJ]] · [[Comparativo — Conta-PF]] · [[De-Para — Investimentos & advisor]] · [[_Ledger-Discovery]]
