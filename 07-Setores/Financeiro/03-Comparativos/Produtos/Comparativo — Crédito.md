---
tipo: comparativo
segmento: credito
players: [Itaú, Bradesco, Banco do Brasil, Santander, Caixa, Nubank, Inter, C6, Mercado Pago, PicPay, PagBank/Stone]
data_captura: 2026-07-09
fontes: [releases de resultados 2025-2026, RI, imprensa especializada, Bacen]
eixos: [financeiro, governanca, soberania, agentes]
tags: [comparativo, credito, banking, 11-players, fase-1]
---

# 📊 Comparativo — Crédito (11 players · piloto + expansão)

**Recorte (1 frase):** matriz mestre do crédito PF/PJ dos 11 players do discovery — 5 incumbentes (Itaú, Bradesco, BB, **Santander**, Caixa) × 6 fintechs/adquirentes (Nubank, Inter, C6, Mercado Pago, PicPay, PagBank/Stone) — no momento em que a IA em concessão chegou ao teto **L4** (foundation model, GenAI em risco) e a portabilidade no Open Finance passa a pressionar spread e retenção de todos.

> **Nota:** o Santander — ausente das versões anteriores da base de Produtos — entra aqui com dado sourced e é, junto de Nubank e Bradesco, um dos três casos mais fortes de IA em crédito da amostra.

## 📊 Matriz mestre
| Player | Classe | Carteira de crédito | NPL 90+ | IA em crédito (evidência) | EMA-J | Fonte-chave · data |
|---|---|---|---|---|---|---|
| **Nubank** | fintech | US$ 32,7 bi (+40% A/A) | 6,6% | **nuFormer** (foundation model no underwriting) + NuScore | **L3,5→L4** | Nu 4T25 · fev/26 |
| **Itaú** | bancão | R$ 1,402 tri (+6,4%) | **1,9%** | +1.300 modelos IA · 150 GenAI em produção | **L3→L4** | Seu Dinheiro 3T25 · out/25 |
| **Bradesco** | bancão | ~R$ 1,03 tri (+9,6%) | 4,1% | Plataforma "Bridge" + Kunumi (**R$ 250 mi ROI**) | **L3→L4** | Forbes · jun/25 |
| **Santander** | bancão | R$ 714,9 bi (+3,7%) | 3,7% | Hub global GenAI · **+400 projetos** (risco+cobrança) | **L3→L4** | Convergência Digital · 25 |
| **Mercado Pago** | fintech | US$ 11 bi (+83%) | 6,8% (15–90d) | Motor **2.500 variáveis** + score explicável | **L3→L4** | Mercado&Consumo · out/25 |
| **PicPay** | fintech | R$ 24,1 bi (+128%) | 7,2%→8,9%* | Multiagente **A2A/MCP** + CAIO nomeado | **L3→L4** | Let's Money · 4T25 |
| **Inter** | fintech | R$ 50 bi (+33%) | 4,6% | Agente **Seven** (crédito no roadmap, HITL) | **L3→L4** | GlobeNewswire · mai/26 |
| **C6 Bank** | fintech | R$ 89,3 bi (+49%) | 2,9% | ML na concessão + GenAI em renegociação | **L3** | CNN Brasil · fev/26 |
| **Banco do Brasil** | bancão | R$ 1,296 tri (+2,5%) | 5,17% | IA em recomendação via Open Finance | **L3** | Seu Dinheiro 4T25 · fev/26 |
| **PagBank/Stone** | adquirente | R$ 5,0 bi / R$ 2,3 bi | 3,05% / 5,03% | ML sobre transacional em tempo real | **L3** | earnings · 2025–26 |
| **Caixa** | público | R$ 1 tri (imobiliário) | [sem fonte] | Sem case público de ML/GenAI em concessão | **L2→L3** | Money Times · jul/26 |

*\*PicPay: NPL 90+ em maturação, guidance de 8,9%. · Carteiras em US$ e R$ conforme moeda de reporte do player; não somar linhas.*

## 🧭 Leitura de maturidade (o gap)
- **Teto = L4, e é ocupado por dois lados:** os grandes-tech (Itaú, Bradesco, Santander pelo volume de modelos/GenAI) e o Nubank (único **foundation model proprietário** no underwriting). Nenhum cruzou **L5** (crédito agêntico autônomo sob mandato).
- **A fronteira agêntica é roadmap, não produto:** Inter (Seven) e PicPay (multiagente A2A/MCP) têm crédito no agente, mas human-in-the-loop. Quando o Seven executar concessão, será o **primeiro teste real de crédito L5 no país**.
- **O vale é a Caixa (L2→L3):** maior base social e ~68% do imobiliário, sem case público de IA no motor. Maior gap de maturidade da amostra.
- **Divergência qualidade × IA:** Itaú (NPL 1,9%, 1.300 modelos) vs. BB (concentração agro, lucro −45%) e PicPay (NPL rumo a 8,9%). Onde a IA de risco é madura E o colateral pesa (C6 2,9%, PagBank 3,05%), a inadimplência é menor.

## ⭐ Diferenciais reais (o que só um faz)
- **Nubank** — único foundation model proprietário confirmado no motor de crédito (nuFormer).
- **Bradesco** — único case público de ROI direto de GenAI em crédito (Kunumi: R$ 250 mi).
- **Santander** — único a declarar Brasil como hub global de GenAI, com risco+cobrança no escopo e stack multi-fornecedor (caso G42).
- **Mercado Pago** — único com explicabilidade do score exposta como feature de produto.
- **Caixa** — único com escala habitacional social (R$ 1 tri), e o mais atrasado em IA.

## 🕳️ Lacuna vendável (→ oferta consultiva)
1. **Governança de crédito agêntico antes do go-live** — Inter e PicPay caminham para o agente executar concessão sem trilha de mandato madura; o NPL do PicPay rumo a 8,9% é o alerta vivo (gancho Cohort / [[INI-Originacao-Credito-Agentica-Governada]]).
2. **FinOps + roteamento por jurisdição de inferência** — Santander roda risco de crédito em GenAI multi-fornecedor (Gemini, caso G42/Abu Dhabi): custo E soberania de dado no mesmo problema (gancho Veltrix / [[Camada FinOps e roteamento de inferência de crédito multi-fornecedor (F2)]]).
3. **Explicabilidade a milhões (LGPD art. 20)** — ninguém entre os bancões divulga metodologia de explicabilidade de decisão automatizada; o Mercado Pago já a trata como produto. Maior lacuna transversal de categoria ([[INI-Copiloto-Explicabilidade-Credito-Bacen]]).
4. **Motor de crédito embedded governado para adquirentes** — só 2% da base Stone usa crédito; a carteira embedded escala mais rápido que a governança de modelo ([[Motor de crédito embedded governado para adquirentes (F2)]]).
5. **Motor de crédito soberano para base social (Caixa)** — maior impacto, maior gap, sob procurement estatal ([[Trilho soberano de crédito consignado via Open Finance (F2)]]).

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (Insumos consolidados: em 2026 o crédito no país tem ML como paridade e GenAI como fronteira competitiva — mas a diferenciação real migrou para três eixos que ninguém fechou: **governança do modelo agêntico** (Inter/PicPay entrando sem trilha), **explicabilidade auditável a milhões** (só o Mercado Pago trata como produto) e **soberania/roteamento de inferência** (Santander é o caso vivo). A portabilidade no Open Finance (Res. Conjunta 15, fev/2026) comprime spread e transforma retenção num problema de dado. A tese de oferta mora onde os três eixos cruzam: instrumentar o motor de crédito com mandato, explicabilidade e residência de dado auditáveis — exatamente o terreno Veltrix+Cohort.)

---
**Fontes:** fichas individuais em `02-Produtos/Credito/` (11 players) · releases de resultados 2025–2026 · imprensa especializada (Seu Dinheiro, Forbes, Convergência Digital, Mobile Time, GlobeNewswire, CNN Brasil, Mercado&Consumo) · [Agência Brasil — portabilidade de crédito no Open Finance (nov/2025)](https://agenciabrasil.ebc.com.br/economia/noticia/2025-11/banco-central-lanca-portabilidade-de-credito-no-open-finance)
**Liga com:** [[00-Blueprint-Mapeamento-Produtos-Banking-BR]] · [[De-Para — Originação de crédito]] · [[De-Para — Originação de crédito (Fase 2 · expansão)]] · [[_Ledger-Produtos]]
