---
tipo: comparativo
segmento: cartao
players: [Itaú, Bradesco, Banco do Brasil, Santander, Caixa, Nubank, Inter, C6, Mercado Pago, PicPay, PagBank/Stone]
data_captura: 2026-07-09
fontes: [releases de resultados 2025-2026, RI, Abecs/Bacen, imprensa especializada]
eixos: [financeiro, governanca, soberania, agentes]
tags: [comparativo, cartao, banking, 11-players, fase-1]
---

# 📊 Comparativo — Cartão (11 players · piloto + expansão)

**Recorte (1 frase):** matriz mestre do cartão de crédito/pré-pago dos 11 players do discovery, no ano em que o mercado brasileiro de cartões cruzou **R$ 4,5 tri (+10,1%)** e **215 mi+ cartões de crédito ativos** — e em que a IA no cartão migrou da detecção de fraude (paridade, puxada por regulação) para dois vales: **antifraude/contestação como produto** e o **cartão agêntico sob mandato**, que ninguém entregou.

> **Nota de mercado (Abecs/Bacen 2025):** crédito R$ 3,1 tri (+14,5%, 21,6 bi transações) · débito R$ 1 tri · pré-pago R$ 397 bi · aproximação ~R$ 2 tri (+31%) · compras online R$ 1,1 tri (+18,3%). Categoria premium +19% no ano. Não somar carteiras dos players (moedas e escopos distintos).

## 📊 Matriz mestre
| Player | Classe | Âncora / premium | Dado citável de cartão | IA no cartão (evidência) | EMA-J | Fonte-chave · data |
|---|---|---|---|---|---|---|
| **Nubank** | fintech | roxinho / **Ultravioleta** | 67% da carteira (US$ 32,7 bi) em cartões; ARPAC US$ 15 | NuScore (ML/fklearn) + Modo Rua + nuFormer | **L4** | Nu 4T25 · fev/26 |
| **Santander** | bancão | SX–Free / **Unlimited** metal | **13 mi+** cartões ativos (Bacen) | Contestação de fraude **~95% + rápida**, <1% erro; 280+ agentes | **L3→L4** | Mobills/Bacen · 25 |
| **Mercado Pago** | fintech | crédito + pré-pago | antifraude ~**5.000** variáveis/transação | Rede neural própria + "second score"; score **explicável como produto** | **L3→L4** | MP · 25 |
| **Itaú** | bancão | iti / **Personnalité** alta renda | cartões PF **+8,0% t/t**; emissão +4,7% t/t | Fraude **−50%/2 anos**; **1.300 modelos**; Alerta Pix 80% | **L3→L4** | Itaú 4T25 · fev/26 |
| **Inter** | fintech | Gold–Black–**Win** / Loop | Loop escalonado (1 pt/R$2,50 no Black) | Agente **Seven** com o cartão como superfície (HITL) | **L3→L4** | Inter/Loop · 25 |
| **PicPay** | fintech | crédito na carteira | volume cartões **R$ 25,9 bi/1S25 (+54%)**; 5 mi+ emitidos | Multiagente **A2A/MCP** + CAIO (crédito/cartão HITL) | **L3→L4** | Finsiders · 25 |
| **C6 Bank** | fintech | **C6 Carbon** metal / Átomos | cashback até ~1,7% (Átomos) | Antifraude barrou **deepfake** (709 tentativas, 0 invasão) | **L3** | C6 · 25 |
| **Bradesco** | bancão | Elo / **Aeternum** metal | receitas de cartões **+16,1%** | BIA + risco (sem IA dedicada ao ciclo do cartão) | **L3** | Bradesco 4T25 · fev/26 |
| **Banco do Brasil** | bancão | **Ourocard** / Altus Infinite | carteira total R$ 1,296 tri | Recomendação via Open Finance (sem IA de cartão isolada) | **L3** | BB 4T25 · fev/26 |
| **PagBank/Stone** | adquirente | cartão da conta do lojista | Stone carteira +134,9%; PagBank lucro R$ 2,37 bi | ML sobre transacional em tempo real (sem número isolado) | **L3** | earnings · 2025–26 |
| **Caixa** | público | CAIXA **Ícone** Visa Infinite | **21** cartões novos em 2025 (mira alta renda) | **Sem case público** de IA no cartão | **L2** | CAIXA/imprensa · 25 |

## 🧭 Leitura de maturidade (o gap)
- **A detecção de fraude no cartão comoditizou por decreto, não por competição:** a Res. BCB 403 obriga todo participante do Pix a monitorar antifraude — o piso subiu para L3 por regulação. Vender "antifraude com IA no cartão" é vender o mínimo legal.
- **Teto = L4, ocupado por três lógicas distintas:** Nubank (dado de 112 mi + foundation model), Santander (IA na jornada de contestação, número duro) e Mercado Pago (antifraude/score como produto vendável). Nenhum cruzou **L5** — cartão emitido/gerido por agente sob mandato não existe.
- **A fronteira agêntica é roadmap:** Inter (Seven) e PicPay (multiagente A2A/MCP) têm o cartão como superfície do agente, mas human-in-the-loop. O NPL do PicPay rumo a 8,9% é o alerta de agêntico sem trilha de mandato.
- **O vale é a Caixa (L2):** maior base social (Caixa Tem 130 mi+), subiu de portfólio (Ícone) mas sem IA no cartão — gap de 2 níveis, o mais profundo da amostra.
- **Assimetria da bandeira nacional:** BB + Bradesco + Caixa controlam a **Elo** e nenhum dos três instrumentou a bandeira própria com IA de dado — ativo estratégico subutilizado.

## ⭐ Diferenciais reais (o que só um faz)
- **Mercado Pago** — único que trata antifraude (Antifraude Plus) e explicabilidade de score como **produto vendável**, sobre o grafo do Mercado Livre.
- **Santander** — único incumbente com número duro de IA na jornada de cartão (contestação ~95% + rápida) e o caso vivo de soberania (stack multi-fornecedor, G42).
- **C6** — único com case público de defesa contra ataque coordenado com **deepfake** (709 tentativas, 0 invasão).
- **Nubank** — único que transformou segurança do cartão em feature de produto (Modo Rua, NuScore) para 112 mi de pessoas.
- **Caixa** — único com escala social (130 mi+) e o mais atrasado em IA no cartão.

## 🕳️ Lacuna vendável (→ oferta consultiva)
1. **Cartão agêntico governado sob mandato** — Inter e PicPay caminham para o agente atuar sobre o cartão sem trilha de mandato/limite madura (gancho Cohort).
2. **FinOps + roteamento por jurisdição de inferência de fraude de cartão** — Santander roda risco/fraude de cartão em GenAI multi-fornecedor (G42/Abu Dhabi): custo E soberania no mesmo problema (gancho Veltrix).
3. **Antifraude de cartão como produto governado** — Mercado Pago já vende (Antifraude Plus); a lacuna é uma malha governada por residência de dado que outros players possam consumir sem entregar o grafo.
4. **Explicabilidade de limite/decisão a milhões (LGPD art. 20)** — nenhum bancão divulga metodologia; só o Mercado Pago trata como feature. Maior lacuna transversal.
5. **IA de cartão soberana para base social + bandeira nacional (Caixa/Elo)** — maior impacto, maior gap, sob procurement estatal, sobre uma bandeira co-controlada por três estatais/incumbentes.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (Insumos consolidados: em 2026 o cartão é um mercado de R$ 4,5 tri onde a IA de detecção virou piso regulatório e a diferenciação migrou para três eixos que ninguém fechou — **antifraude/score como produto governado** (só o Mercado Pago), **soberania/roteamento de inferência** (Santander é o caso vivo) e o **cartão agêntico sob mandato** (Inter/PicPay entrando sem trilha). O ativo estratégico ocioso é a Elo: bandeira nacional co-controlada por BB/Bradesco/Caixa, sem inteligência de dado embarcada. A tese de oferta mora onde antifraude governado, explicabilidade auditável e residência de dado cruzam — o terreno Veltrix+Cohort.)

---
**Fontes:** fichas individuais em `02-Produtos/Cartao/` (11 players) · [Panorama Abecs — cartões movimentam R$ 4,5 tri em 2025](https://panoramaabecs.com.br/economia-pagamentos-cartoes-brasil-2025-dados-abecs/) · releases de resultados 2025–2026 · imprensa especializada (Seu Dinheiro, InfoMoney, Finsiders, Mobills, CNN Brasil) · dados de fraude nos De-Para de Fraude (piloto + Fase 2)
**Liga com:** [[00-Blueprint-Mapeamento-Produtos-Banking-BR]] · [[Comparativo — Crédito]] · [[De-Para — Prevenção a fraude & disputas]] · [[De-Para — Pagamentos & Pix]] · [[_Ledger-Produtos]]
