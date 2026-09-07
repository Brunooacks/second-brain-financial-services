---
tipo: jornada-depara
jornada: credito
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-03
fontes: [Building Nubank, Nu International, WhiteSight, TI Inside, Coletivo Tech, Startups.com.br, Finsiders, SpaceMoney, NeoFeed, Mobile Time, CNN Brasil, XP Investimentos]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, credito, originacao, underwriting]
---

# 🧭 De-Para — Jornada: Originação de crédito

**Recorte (1 frase):** Como os 6 players-piloto originam e concedem crédito PF (simulação → score → decisão → contratação) num momento em que os motores saltaram de ML clássico para foundation models/GenAI, enquanto a inadimplência dos bancos digitais sobe (NPL de cartão do grupo S3 foi de 10,6% em dez/2025 para 16,9% em abr/2026) e o Bacen aperta a exigência de explicabilidade de modelos.

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
1. **Descoberta/simulação** — oferta pré-aprovada no app ou simulador público de empréstimo (valor, prazo, parcela).
2. **Coleta de dados** — CPF, renda, dados de relacionamento; cada vez mais via Open Finance (visão 360°).
3. **Score/underwriting** — motor de risco (ML/foundation model) atribui score e precifica taxa/limite.
4. **Decisão** — aprovação instantânea (STP) ou análise assíncrona (Inter cita liberação em até 48h).
5. **Contratação** — assinatura digital e liberação do recurso.
6. **Gestão/limite** — aumentos proativos de limite e renegociação por modelo.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Nubank | **L4** (foundation model na decisão; predom. L3–L4) | ~3–4 (oferta pré-aprovada) | nuFormer, modelo transformer para decisão de crédito, em produção ~18 meses após a compra da Hyperplane (jun/2024) → prod. em 2025; ganhos offline em crédito, renda e X-Sell (Building Nubank / Nu International · 2025) |
| Itaú | **L4** (pontual; predom. L3) | ~4–5 | "Inteligência Itaú" reúne ~750 iniciativas de GenAI, 140 em uso diário em tarefas que incluem **crédito, análise de risco e prevenção a fraudes**; +84% no volume de iniciativas GenAI em 2025 (TI Inside · 11/02/2026) |
| Bradesco | **L3** (Credit Risk Models L4 pontual) | ~4–5 | Motor de elegibilidade cloud-native na plataforma FICO integra bases governamentais + dados internos; consignado saltou de 8→700+ contratos/dia; modelos de risco construídos por **agentes de IA** (−95% de tempo) (Coletivo Tech; TI Inside · 03/09/2025) |
| Banco do Brasil | **L3** | ~4–5 | "Matriz de resiliência" com uso intensivo de IA na aprovação de crédito; IA classifica clientes por capacidade de pagamento p/ expandir, renegociar ou suspender (XP Investimentos · 2025) |
| Inter | **L3** | ~4–5 (decisão até 48h) | Análise de crédito por ML + Open Finance (visão 360°) personaliza limite/taxa; assistente de IA "Seven" (L4, mas em gestão financeira, não na decisão de crédito); função de gestão de crédito no app (Mobile Time/CNN · 03/12/2025) |
| Mercado Pago | **L3** | ~3–4 (oferta no fluxo de pagamento) | ML de credit scoring que aprende a cada transação, ~5.000 variáveis por transação; GenAI sobre o ML (aplicado sobretudo a fraude/aprovação, não à decisão de crédito) (Startups.com.br · 2025) |

**Líder da jornada:** Nubank (L4 — foundation model proprietário na decisão) · **Gap máximo:** 1 nível (L4 vs L3 do bloco BB/Inter/MP)

> **Sinal de categoria:** o salto desta jornada foi de L3 (ML) para L4 (foundation model/GenAI no motor) — nenhum player exibe evidência pública de L5 (agente que origina, negocia e contrata crédito ponta-a-ponta sob mandato com trilha). O foundation model do Nubank **decide**, mas não **age** com mandato auditável. Gap para o patamar agêntico ≥1 para todos. Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Nubank | Inadimplência 90 dias (NPL) após nuFormer | −0,1 p.p. → **6,6%** | Building Nubank / WhiteSight, resultados Q4 2025 · dez/2025 |
| Nubank | Net interest income Q4'25 (contexto de expansão de crédito com IA) | **US$ 2,8 bi (+55% a.a.)**; margem +0,6 p.p. → 10,5% | Nu International / WhiteSight · Q4 2025 |
| Bradesco | Contratos/dia de consignado com motor FICO + IA | **8/dia → 700+/dia (>100x)**; carteira acumulada +30x | Coletivo Tech, "Bradesco amplia consignado em mais de 100 vezes" · 2026 |
| Bradesco | Tempo de desenvolvimento de modelos de risco de crédito | **−95%** com agentes de IA vs tempo humano | TI Inside, "Bradesco acelera IA e reduz em 95% o tempo de modelos de risco" · 03/09/2025 |
| Itaú | Iniciativas GenAI em uso (crédito, risco, fraude) | **750 iniciativas / 140 diárias**; +84% de volume em 2025 | TI Inside · 11/02/2026 |
| Mercado Pago | Variáveis por transação no scoring | **~5.000 variáveis** | Startups.com.br, "Mercado Pago usa machine learning para democratizar crédito" · 2025 |
| Setor (bancos digitais S3) | NPL de cartão do grupo S3 (inclui MP, Inter, C6) | **10,6% (dez/2025) → 16,9% (abr/2026)** | Finsiders/SpaceMoney, alerta Goldman Sachs · abr/2026 (contexto de terceiro) |
| Banco do Brasil | Ganho quantitativo de IA no crédito | [sem fonte pública específica] | matriz de resiliência é qualitativa (XP · 2025) |
| Inter | Ganho quantitativo de IA na decisão de crédito | [sem fonte pública específica] | — |

## ⭐ Diferenciais reais
- **Nubank** — único com **foundation model proprietário** na decisão de crédito (nuFormer, via aquisição da Hyperplane). Vantagem estrutural de dados de 1ª parte; escala do modelo é o fosso, não a feature.
- **Bradesco** — o incumbente que mais **mostra número**: 8→700 contratos/dia no consignado e −95% no tempo de modelagem com agentes de IA. Motor FICO integrando bases governamentais é o ponto de soberania de dado.
- **Itaú** — GenAI **industrializada** (750 iniciativas) tocando crédito, risco e fraude no mesmo estoque tecnológico — largura, não profundidade num só ponto.
- **Inter / Mercado Pago** — **Open Finance como dado alternativo** de score (visão 360°) — inclusão de quem tem histórico fino no birô tradicional.

## 🕳️ O vale (lacuna vendável)
- **Ninguém tem crédito agêntico governado (L5):** o foundation model decide, mas não há agente que conduza simulação → decisão → contratação sob mandato com escopo/limite/trilha auditável. É o mesmo vale do onboarding, agora no motor de maior valor.
- **Explicabilidade × poder preditivo:** foundation models e GenAI elevam a acurácia e **derrubam a explicabilidade** — exatamente onde o Bacen aperta (exigência de explicabilidade de modelos de crédito). Quanto mais avançado o motor, maior a dívida de governança. Território direto de Veltrix (observabilidade) + Cohort (trilha).
- **Inadimplência subindo apesar de mais IA:** NPL S3 em 16,9% (abr/2026) mostra que empilhar modelo preditivo não resolveu risco — o gargalo virou **governança do modelo** (residência de dado, auditabilidade, roteamento por jurisdição), não mais um score.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (simuladores de empréstimo, ofertas pré-aprovadas). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) a jornada saltou de ML (L3) para foundation model/GenAI (L4) no motor — Nubank lidera com modelo proprietário, mas ninguém chegou ao agêntico (L5); (2) quanto mais avançado o motor, pior a explicabilidade — e o Bacen está apertando exatamente aí, o que transforma governança de modelo em obrigação, não diferencial opcional; (3) a inadimplência sobe (NPL S3 16,9%) apesar de mais IA — sinal de que o próximo ponto de valor é governar o modelo, não empilhar outro.

---
**Fontes:**
- Building Nubank — Foundation models / nuFormer: https://building.nubank.com/foundation-models-ai-nubank-transformation/
- Nu International — AI transformation strategy: https://international.nubank.com.br/company/nubank-details-ai-transformation-strategy-built-on-data-foundation-models-and-democratized-financial-advice/
- WhiteSight — Nubank's AI Model Rewrites Credit Underwriting: https://whitesight.net/nubanks-ai-model-rewrites-credit-underwriting/
- Coletivo Tech — Bradesco FICO consignado (100x): https://coletivo.tech/noticias/bradesco-fico-plataforma-consignado/
- TI Inside — Bradesco −95% tempo de modelos de risco (03/09/2025): https://tiinside.com.br/03/09/2025/bradesco-acelera-ia-e-reduz-em-95-o-tempo-de-modelos-de-risco-de-credito/
- TI Inside — Itaú +35% velocidade / GenAI (11/02/2026): https://tiinside.com.br/11/02/2026/itau-avanca-35-em-velocidade-de-implantacoes-tecnologicas-em-2025-e-amplia-uso-de-ia-generativa-na-experiencia-dos-clientes/
- Startups.com.br — Mercado Pago ML no crédito: https://startups.com.br/eventos/payment-revolution/mercado-pago-usa-machine-learning-para-democratizar-o-acesso-ao-credito/
- Finsiders — Inadimplência bancos digitais / NPL S3: https://finsidersbrasil.com.br/bancos-digitais/inadimplencia-em-bancos-digitais-sobe-163-em-quatro-anos
- Mobile Time — Inter gestão de crédito no app (03/12/2025): https://www.mobiletime.com.br/noticias/03/12/2025/inter-credito-aplicativo/
- CNN Brasil — Inter assistente de IA (Seven): https://www.cnnbrasil.com.br/economia/negocios/inter-lanca-assistente-de-ia-para-apoiar-gestao-financeira-no-aplicativo/
- XP Investimentos — BB matriz de resiliência com IA: https://conteudos.xpi.com.br/acoes/relatorios/banco-do-brasil-bbas3-recuperacao-de-bbas-uma-maratona-nao-um-sprint/

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[De-Para — Onboarding & KYC]]
