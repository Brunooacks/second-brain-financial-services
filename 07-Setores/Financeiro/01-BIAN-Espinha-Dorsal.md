---
tipo: referencia
setor: financeiro
status: ativo
data: 2026-07-03
fontes: [https://bian.org/deliverables/service-landscape/, https://bian.org/news-room/bian-unveils-new-service-landscape-14-0-to-accelerate-ai-ready-banking-architecture/]
eixos: [financeiro, governanca, agentes]
tags: [bian, arquitetura, taxonomia, jornadas, referencia, espinha-dorsal]
---

# 🏛️ BIAN como espinha dorsal do discovery

> Trocar a taxonomia caseira pela **canônica do setor**. BIAN (Banking Industry Architecture Network) é o modelo de arquitetura de referência que os próprios bancos usam. Ancorar o de-para nele dá granularidade real e — mais importante — autoridade de board: passo a falar a língua de arquitetura do cliente. Plugin do [[00b-Plano-Discovery-Jornadas-para-Iniciativas]].

## Por que BIAN (a tese)

Comparar "onboarding do Nubank vs do Itaú" é jornalismo de produto. Comparar **Service Domains** ("Customer Reference Data Mgmt", "Fraud Decisioning", "Party Lifecycle Management") é arquitetura — e é isso que um CTO/board de banco reconhece como sério. BIAN me dá um dicionário não-sobreponível de capacidades: cada jornada nossa decompõe em Service Domains, cada Service Domain recebe maturidade [[EMA-J — Escala de Maturidade Agentica de Jornada]], e o gap vira iniciativa no [[Placar VALE — Priorizacao de Iniciativa de IA]].

## O modelo em 3 camadas

`Business Area  →  Business Domain  →  Service Domain`

- **Business Area** — grande bloco da cadeia de valor (ex.: *Products*, *Operations*, *Customers*, *Channels*, *Finance & Risk*).
- **Business Domain** — agrupamento de capacidade (ex.: *Loans & Deposits*, *Cards*, *Market Risk*).
- **Service Domain** — o tijolo elementar, não-sobreponível (ex.: *Consumer Loan*, *Card Authorization*, *Fraud Decisioning*). É a **unidade de análise** do nosso benchmarking.

Estrutura formal atual (v14): **7 Business Areas · 36 Business Domains · ~280 Service Domains** (fonte: bian.org).

## O dado que importa num board (com fonte)

- **BIAN 14.0** foi lançado em **março/2026** com posicionamento explícito de *"AI-Ready Banking Architecture"*: novos Service Domains para casos de uso de IA, Behaviour Qualifiers atualizados e **242 especificações de API**. *(Fonte: [BIAN News Room, mar/2026](https://bian.org/news-room/bian-unveils-new-service-landscape-14-0-to-accelerate-ai-ready-banking-architecture/))*
- Alinhamento reforçado com **ISO 20022** (mensageria financeira). *(Fonte: [BIAN v14 Release Notes](https://bian.org/deliverables/service-landscape/))*
- BIAN reúne **100+ bancos e fornecedores** membros; padrão desde 2008. *(Fonte: [Wikipedia — BIAN](https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network))*

**O que eu diria num board:** o próprio padrão de arquitetura do setor virou "AI-ready" em 2026 — quem mapeia maturidade de IA por Service Domain não está inventando uma régua, está usando a que o mercado adotou. Isso desarma a objeção de "é framework de consultoria": é o vocabulário do CIO deles.

## Mapa das nossas 6 jornadas → BIAN (Fase 1)

| Jornada nossa | Service Domains BIAN centrais |
|---|---|
| **Onboarding & KYC** | Customer Reference Data Mgmt · Party Reference Data Directory · Party Lifecycle Management · Customer Access Entitlement |
| **Originação de crédito** | Consumer Loan · Corporate Loan · Underwriting · Credit Management · Customer Credit Rating · Credit Risk Models |
| **Pagamentos & Pix / agentic** | Payment Order · Payments Execution · Payment Initiation · Card Authorization · Card Clearing · Merchant Acquiring |
| **Prevenção a fraude & disputas** | Fraud Evaluation · Fraud Decisioning · Fraud Resolution · Fraud Models · Transaction Authorization |
| **Atendimento & cobrança** | Contact Handler · Contact Dialogue · Customer Case Mgmt · Collections · Delinquent Account Handling |
| **Investimentos & advisor** | Consumer Investments · Investment Portfolio Mgmt · Suitability Checking · Consumer Advisory Services |

O mapa completo (todos os Business Domains e Service Domains da paisagem) está na planilha mestre, aba **BIAN Landscape** — cada Service Domain com relevância para IA, jornada relacionada e maturidade do líder.

## Como usar na prática

1. A **unidade de coleta** deixa de ser "a jornada" e passa a ser "o Service Domain dentro da jornada" — mais fino, mais citável.
2. A rotina noturna preenche maturidade EMA-J por Service Domain dos players-piloto.
3. Service Domains marcados como **Relevância IA = Alta** são a fila natural do backlog VALE.
4. Expansão do estudo = descer a Business Domains ainda não cobertos (Trade Banking, Market Trading, Corporate Banking…), sem perder a estrutura.

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[00-Blueprint-Mapeamento-Produtos-Banking-BR]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
**Fonte da paisagem:** BIAN Service Landscape (Value Chain Layout) — versão atual 14.0 · bian.org
