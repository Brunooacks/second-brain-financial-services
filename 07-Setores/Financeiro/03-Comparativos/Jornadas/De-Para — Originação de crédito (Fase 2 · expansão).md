---
tipo: jornada-depara
jornada: credito
fase: 2
players: [Santander, Caixa, C6, PicPay, PagBank/Stone]
data_captura: 2026-07-04
fontes: [contec.org.br, mobiletime.com.br, convergenciadigital.com.br, letsmoney.com.br, c6bank.com.br, finsidersbrasil, blog.picpay.com, faq.pagbank.com.br, televendasecobranca, braziljournal, tiinside]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, credito, originacao, underwriting, fase-2, expansao]
---

# 🧭 De-Para — Jornada: Originação de crédito (Fase 2 · players de expansão)

**Recorte (1 frase):** Como os 5 players de expansão (Santander, Caixa, C6, PicPay, PagBank/Stone) originam e concedem crédito PF/PME até a parede de login, para testar se o salto do piloto — de ML (L3) para foundation model/GenAI (L4) no motor — se repete fora do grupo de 6, num momento em que a inadimplência sobe e o Bacen aperta a explicabilidade de modelos. Liga com [[De-Para — Originação de crédito]] (piloto).

## 🔍 Decomposição da jornada
Mesmas etapas canônicas do piloto (públicas, até a parede de login):
1. **Descoberta/simulação** — oferta pré-aprovada no app ou simulador público (valor, prazo, parcela).
2. **Coleta de dados** — CPF, renda, dados de relacionamento; cada vez mais via Open Finance (visão 360°) ou fluxo de vendas (adquirentes).
3. **Score/underwriting** — motor de risco (ML/foundation model) atribui score e precifica taxa/limite.
4. **Decisão** — aprovação instantânea (STP) ou análise assíncrona.
5. **Contratação** — assinatura digital e liberação do recurso.
6. **Gestão/limite** — aumentos proativos de limite e renegociação por modelo.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Santander | **L3** (modelagem de risco por ML; sinal L4 emergente) | ~4–5 | +400 projetos de IA no Brasil; **plataforma agnóstica multi-fornecedor (OpenAI/AWS/Google)** habilitando iniciativas em **crédito, risco e cobrança**; GenAI declarada para "**melhorar a modelagem de risco**". Meta do grupo: €1 bi de valor com IA em 2026–2028 (Contec/Mobile Time · 2025–04/2026; ConvergenciaDigital · 14/08/2025). GenAI sobre risco é declarada, não confirmada na decisão de crédito PF em produção → conservador L3. |
| Caixa | **L3** (ML + Open Finance) | ~5–7 | **Única instituição habilitada a operar o consignado via Open Finance** (testes ago/2026, lançamento nov.); mainframe reposicionado (com Bradesco) como **plataforma orientada a dados e IA**; Open Finance + IA para antecipar demanda de crédito (Let's Money · 2026). Base social/estatal, muita fricção residual. |
| C6 (Banco C6) | **L3** | ~4–5 | Análise de crédito por ML; **C6 Assistant** (GenAI) permite consultar gastos/fatura em linguagem natural — mas em **gestão financeira, não na decisão de crédito** (paridade com o Seven do Inter). Lucro R$ 2,46 bi e carteira de crédito **+49% em 2025** (Let's Money · 2026; Reuters/Finsiders · 2025). |
| PicPay | **L3** | ~4–5 | Usa IA "**há vários anos**" para **modelos de concessão de crédito, análise de risco e personalização de ofertas**; **Open Finance como motor de personalização** de taxa/limite; empréstimo 100% digital pré-aprovado (blog.picpay.com · 2025–2026). |
| PagBank/Stone | **L3** | ~3–4 (oferta no fluxo de vendas) | **Embedded lending do adquirente**: empréstimo pré-aprovado com desconto de % das vendas, análise mensal por dado transacional (faq.pagbank.com.br). Stone com **crédito relançado e disciplina de carteira**, acompanhamento rigoroso por modelo (Televendas&Cobrança/Brazil Journal · 2025–2026). |

**Líder da jornada:** empate técnico em **L3** entre os 5 (nenhum exibe foundation model proprietário na decisão, como o nuFormer do Nubank no piloto) · **Gap máximo interno:** 0 nível · **Gap vs líder do piloto (Nubank L4):** 1 nível

> **Sinal de categoria (invertido em relação ao piloto):** enquanto no piloto o topo chegou a **L4** (Nubank com foundation model, Itaú com GenAI industrializada), **o teto da coorte de expansão é L3** — ML preditivo, Open Finance como dado alternativo, GenAI ainda em gestão financeira ou declarada sobre risco, não na decisão. Santander é o mais próximo do L4 (GenAI sobre modelagem de risco, mas não confirmada em produção PF). Com 11 players agora medidos no crédito, a fronteira L4 é ocupada só pelos grandes-tech (Nubank/Itaú); a expansão inteira está um degrau abaixo. Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública específica de crédito = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Stone | Carteira de crédito (dez/2025) | **R$ 2,836 bi**; **+134,9% em 12 m** / +23,4% no tri | Televendas&Cobrança / Brazil Journal · 2025–2026 |
| Stone | Lucro líquido 2025 (contexto) | **R$ 2,477 bi (+17,5%)**; share em crédito/banking "low single digits" (1–2%) | Televendas&Cobrança / Brazil Journal · 2025–2026 |
| C6 | Carteira de crédito 2025 | **+49%** no ano; lucro líq. **R$ 2,46 bi** | Reuters/Finsiders · 2025; Let's Money · 2026 |
| Santander | Meta de valor com IA (grupo; inclui crédito/risco/cobrança) | **€ 1 bi em 2026–2028**; **€ 35 mi só no 1º tri de 2026**; +400 projetos de IA no Brasil | Contec / Mobile Time / ConvergenciaDigital · 2025–2026 |
| Caixa | Pioneirismo no consignado via Open Finance (proxy de motor de crédito) | **Única habilitada** a operar; testes ago/2026, lançamento nov. | Let's Money · 2026 |
| PicPay | Escala da base (contexto do motor de crédito) | 67 mi contas / 42,7 mi ativos (4T25) | Investidor10 / Finsiders · 2025–2026 |
| Santander | Ganho quantitativo de IA na decisão de crédito PF | [sem fonte pública específica] | crédito é uma das áreas, sem métrica isolada |
| Caixa | Ganho quantitativo de IA no crédito | [sem fonte pública específica] | — |
| C6 / PicPay / PagBank | Ganho quantitativo de IA na decisão de crédito | [sem fonte pública específica] | ML declarado, sem número isolado |

## ⭐ Diferenciais reais
- **Caixa** — **única habilitada a operar o consignado via Open Finance** + base social/estatal + mainframe virando plataforma de dados/IA. É o ativo de **soberania de dado estatal** da Fase 2 — motor de crédito sobre a maior base social do país, mas sob procurement estatal e explicabilidade regulatória pesada.
- **PagBank/Stone** — **embedded lending do adquirente**: o dado transacional da maquininha é o motor de risco. Stone dobrou a carteira (+134,9%) em 12 meses — crescimento agressivo de crédito lastreado em fluxo de vendas, não em birô.
- **Santander** — único incumbente da F2 com **GenAI declarada sobre a modelagem de risco** e **plataforma agnóstica multi-fornecedor** (OpenAI/AWS/Google): sinal público de L4 emergente e, de quebra, o caso mais nítido de **custo de inferência distribuído entre fornecedores** (terreno de Veltrix).
- **C6 / PicPay** — **Open Finance como dado alternativo** de score + assistente GenAI (C6 Assistant) na gestão financeira — paridade com o Inter do piloto: GenAI toca o cliente, mas não a decisão de crédito.

## 🕳️ O vale (lacuna vendável)
- **Coorte de expansão travada em L3:** confirma, por baixo, o vale do piloto — ninguém tem foundation model proprietário na decisão nem crédito agêntico (L5). O gap não é entre os 5, é entre a expansão e o patamar L4 dos grandes-tech; e de todos para o agêntico governado.
- **Embedded lending crescendo 100%+ sem governança de modelo proporcional:** Stone dobrou a carteira em 12 meses sobre ML de fluxo de vendas. Quanto mais rápido a carteira cresce sobre dado transacional, maior a **dívida de explicabilidade e de residência de dado** — exatamente onde inadimplência e Bacen apertam. Vale de governança, não de score.
- **Consignado via Open Finance na Caixa é o vale de soberania:** dado estatal + Open Finance + IA sobre público social, sob LGPD e explicabilidade Bacen. Maior impacto social e maior fricção de venda (procurement estatal) no mesmo alvo.
- **Multi-fornecedor sem camada FinOps/roteamento:** Santander roda crédito/risco sobre OpenAI + AWS + Google. Ninguém expõe publicamente uma **camada de FinOps de inferência + roteamento por jurisdição** sobre esse parque — território direto de Veltrix.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (simuladores de empréstimo, ofertas pré-aprovadas). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) com 11 players medidos no crédito, a fronteira L4 (foundation model/GenAI no motor) é ocupada só por Nubank e Itaú — **a coorte de expansão inteira está em L3**; o gap agora é de estrutura de dados/modelo, não de feature. (2) O crédito embedded dos adquirentes (Stone +134,9% de carteira em 12 m) cresce sobre dado transacional mais rápido do que a governança do modelo — a dívida de explicabilidade e residência de dado escala junto com a carteira. (3) A Caixa é o caso onde soberania de dado estatal, Open Finance e o maior público social se encontram num só motor de crédito — impacto máximo, fricção de venda máxima. (4) Santander, rodando crédito sobre três fornecedores de LLM, é a demonstração viva de por que FinOps de inferência + roteamento por jurisdição deixam de ser luxo e viram controle de custo e de conformidade.

---
**Fontes:**
- Contec Brasil — Santander acelera IA (crédito/risco/cobrança, +400 projetos): https://contec.org.br/com-estrategia-global-santander-acelera-uso-de-ia-e-ja-colhe-frutos/
- Mobile Time — Santander, conversacional entre as 3 prioridades de IA (01/04/2026): https://www.mobiletime.com.br/noticias/01/04/2026/ia-prioridade-santander/
- ConvergenciaDigital — Santander × IA generativa, meta €1 bi / €35 mi Q1 (14/08/2025): https://convergenciadigital.com.br/mercado/santander-investe-50-milhoes-de-euros-em-ia-generativa-brasil-tem-papel-chave/
- Let's Money — Open Finance com IA prevê crédito (Caixa única habilitada no consignado): https://www.letsmoney.com.br/open-finance/open-finance-ia-prever-credito-demanda
- Let's Money — Bradesco e Caixa põem IA no coração do mainframe: https://www.letsmoney.com.br/noticias/bradesco-caixa-ia-mainframe-plataforma-dados
- Let's Money — C6 amplia IA que analisa gastos em conta e fatura (C6 Assistant): https://www.letsmoney.com.br/ia/c6-assistant-analise-gastos-conta-fatura/
- Finsiders — C6 lucra R$ 2,5 bi (carteira de crédito): https://finsidersbrasil.com.br/noticias-sobre-fintechs/resultados-financeiros/c6-lucra-r-25-bi-neon-vira-jogo-e-creditas-amplia-perdas/
- blog.picpay.com — como o PicPay usa IA (crédito, risco, personalização): https://blog.picpay.com/como-o-picpay-usa-inteligencia-artificial/
- PagBank FAQ — como funciona o empréstimo (pré-aprovado, desconto de vendas): https://faq.pagbank.com.br/duvida/como-funciona-o-emprestimo-do-pagbank/575
- Televendas & Cobrança — Stone lucro R$ 2,477 bi 2025 (carteira de crédito +134,9%): https://www.televendasecobranca.com.br/credito/stone-tem-lucro-de-r-2477-bilhoes-em-2025-com-expansao-de-175-179040/
- Brazil Journal — Stone entre a maquininha e os novos negócios (crédito, share 1–2%): https://braziljournal.com/stone-vive-entre-o-desafio-da-maquininha-e-a-promessa-dos-novos-negocios/

**Liga com:** [[De-Para — Originação de crédito]] (piloto) · [[De-Para — Onboarding & KYC (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
