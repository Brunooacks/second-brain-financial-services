---
tipo: jornada-depara
jornada: onboarding-kyc
fase: 2
players: [Santander, Caixa, C6, PicPay, PagBank/Stone]
data_captura: 2026-07-04
fontes: [santander.com.br, caixa.gov.br, c6bank.com.br, gov.br/MGI, blog.picpay.com, finsidersbrasil, TI Inside, Mobile Time, ConvergenciaDigital, idwall]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, onboarding, kyc, fase-2, expansao]
---

# 🧭 De-Para — Jornada: Onboarding & KYC (Fase 2 · players de expansão)

**Recorte (1 frase):** Como os 5 players de expansão (Santander, Caixa, C6, PicPay, PagBank/Stone) conduzem a abertura de conta PF até a parede de login, para testar se o padrão do piloto — mercado inteiro ancorado em L2–L3, ninguém agêntico — se confirma fora do grupo de 6, e onde estão as assimetrias (estatal vs. neobanco vs. incumbente). Liga com [[De-Para — Onboarding & KYC]] (piloto).

## 🔍 Decomposição da jornada
Mesmas etapas canônicas do piloto (público, até a parede de login):
1. **Descoberta/entrada** — download do app/site, início do cadastro (CPF, e-mail, telefone).
2. **Captura documental** — foto de RG/CNH, OCR e checagem de autenticidade.
3. **Prova de vida (liveness)** — selfie + movimentos; verificação facial contra o documento.
4. **Validação cruzada** — cruzamento com bases (CPF/Receita, bases públicas, GOV.BR quando integrado).
5. **Decisão** — aprovação instantânea (STP) ou análise assíncrona.
6. **Ativação** — conta pronta no app.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Santander | **L3** (liveness; sinal L4 emergente) | ~5–6 | Biometria facial com **Liveness anti-fraude/anti-deepfake**; ID Santander (2FA obrigatório) usa a biometria; caso de uso declarado de **análise documental de abertura de conta via OCR + LLM** (santander.com.br/biometria-facial · captura 04/07/2026; ConvergenciaDigital sobre acordo OpenAI · 14/08/2025). O OCR+LLM em onboarding PF é caso de uso divulgado, não confirmado em produção → nível conservador L3. |
| Caixa | **L2** (liveness L3 pontual; muita fricção) | ~5–7 | Abertura de conta digital no app **CAIXA 5.0** com biometria facial; reconhecimento facial compara selfie ao padrão, cadastro em <2 min; porém **fallback presencial** frequente (CPF divergente, foto ruim, suspeita) e foco em base de benefícios sociais (caixa.gov.br/seguranca/biometria · captura 04/07/2026). |
| C6 (Banco C6) | **L3** | ~4–5 | Onboarding **automático sem interação humana, ~5 min**, com liveness e cross-reference de dados; eleito **melhor jornada digital do cliente (idwall, 2 anos consecutivos)**; acordo GOV.BR p/ autenticar ~30 mi de clientes (c6bank.com.br/blog · 2025; gov.br/MGI · 15/07/2025). |
| PicPay | **L3** | ~4–5 | Onboarding **<5 min** com reconhecimento facial + validação de documento analisando movimentos (liveness); base de 67 mi de contas / 42,7 mi ativos no 4T25 (blog.picpay.com; Investidor10/Finsiders · 2025-2026). |
| PagBank/Stone | **L3** | ~4–5 | KYC com **biometria facial como prova de vida** comparando imagem em tempo real ao documento + análise de movimento; **1º player a usar prova de vida em links de pagamento** (aiotbrasil / TudoCelular · 2025; faq.pagbank.com.br). |

**Líder da jornada:** C6 (L3 — melhor jornada digital idwall + STP <5 min + trilho GOV.BR) · **Gap máximo:** 1 nível (L3 vs Caixa L2)

> **Confirmação do sinal de categoria:** o padrão do piloto se repete — **nenhum dos 5 exibe evidência pública de L4 (copiloto GenAI dentro do onboarding) ou L5 (agêntico)**. Santander é o mais próximo do L4 (OCR+LLM declarado), mas não confirmado em produção PF. Mercado inteiro (11 players agora medidos) ancorado em L2–L3 no onboarding → oportunidade de **categoria**, não de catch-up. Ver "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública específica de onboarding = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| C6 | Qualidade da jornada digital (proxy de onboarding) | **Melhor jornada digital do cliente, 2 anos consecutivos** (ranking idwall) | Seu Crédito Digital / c6bank.com.br · 2025 |
| C6 | Escala da base (contexto do KYC) | 40 mi de clientes (fim 2025); lucro líq. R$ 2,46 bi | Reuters/Investing · 2025; c6bank.com.br/blog |
| C6 | Alcance do acordo GOV.BR (autenticação) | ~30 mi de clientes (16ª instituição no arranjo) | gov.br/MGI · 15/07/2025 |
| C6 | Satisfação (proxy, cartão premium) | NPS 71 (titulares Carbon) | c6bank.com.br/blog · 2025 |
| PicPay | Escala da base (contexto do KYC) | 67 mi contas / 42,7 mi ativos (4T25) | Investidor10 / Finsiders · 2025-2026 |
| Santander | Redução tempo de processamento (fraude cartão — **adjacente, não onboarding**) | −95% tempo / 90% automação / <1% erro | Jornal Económico / Contec · 2025 |
| Santander | Onboarding quantificado (tempo/CAC/fraude) | [sem fonte pública específica] | — |
| Caixa | Onboarding quantificado | [sem fonte pública específica] | — |
| PagBank/Stone | Onboarding quantificado | [sem fonte pública específica] | — |

## ⭐ Diferenciais reais
- **C6** — trilho **GOV.BR** (30 mi) + **melhor jornada digital idwall** (2 anos): soberania/base pública como ativo de onboarding + experiência premiada. É o Inter da Fase 2 (ambos usam GOV.BR como diferencial, não só compliance).
- **Santander** — **liveness anti-deepfake** + estratégia GenAI em escala (acordo OpenAI, €1 bi de meta IA 2026–2028): único incumbente da Fase 2 com sinal público de L4 emergente no onboarding (OCR+LLM declarado).
- **PagBank/Stone** — **1º a usar prova de vida em links de pagamento**: leva o liveness para além do onboarding, ao ponto da transação do vendedor (ângulo de adquirência).
- **Caixa** — **player estatal** com a maior base social do país; onboarding mais atrasado (L2) mas com peso de soberania/govtech e integração GOV.BR nativa — vale profundo, porém sob restrição de compra pública.

## 🕳️ O vale (lacuna vendável)
- Confirma o vale do piloto: todos param em L2–L3, **nenhum tem agente que conduza o onboarding ponta-a-ponta sob mandato com trilha auditável (L5)**. A validação cruzada de bases é regra/etapa manual, não orquestração agêntica governada.
- **Caixa (L2)** é o vale mais profundo dos 11 players: base social gigante, fricção alta, fallback presencial — modernização governada de altíssimo impacto social, mas com atrito de procurement estatal.
- Dois players (C6, e Inter no piloto) já usam **GOV.BR como trilho de identidade**; ninguém expõe esse trilho como **camada soberana reutilizável com residência/roteamento por jurisdição** — território direto de Veltrix/Cohort.
- A autorregulação Febraban (27/out/2025) impõe validação cruzada + reporte ao Bacen; Santander e Caixa (incumbentes/estatal) constam; **C6, PicPay, PagBank não constam** na lista divulgada — assimetria de piso de diligência dentro da própria Fase 2.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login. Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) com 11 players medidos, o teto do onboarding no Brasil é **L3 em todos** — o gap não é entre concorrentes, é entre o setor e o patamar agêntico; a categoria inteira é vale aberto. (2) A soberania de identidade está virando ativo competitivo concreto: C6 e Inter plugam GOV.BR, e ninguém governou esse trilho como camada reutilizável com residência de dados. (3) Há uma **assimetria de piso regulatório** dentro do próprio mercado — incumbentes/estatal dentro da autorregulação Febraban, neobancos de expansão fora — que muda o custo de conformidade e abre janela de oferta. (4) Caixa é o caso onde valor social e atraso de maturidade se encontram: o maior impacto e a maior fricção de venda no mesmo alvo.

---
**Fontes:**
- Santander — Biometria Facial / Liveness anti-deepfake: https://www.santander.com.br/biometria-facial
- ConvergenciaDigital — Santander × OpenAI, banco orientado por IA (14/08/2025): https://convergenciadigital.com.br/mercado/santander-investe-50-milhoes-de-euros-em-ia-generativa-brasil-tem-papel-chave/
- CAIXA — Biometria / CAIXA 5.0: https://www.caixa.gov.br/seguranca/biometria/Paginas/default.aspx
- C6 Bank — melhor experiência de abertura de conta (idwall): https://www.c6bank.com.br/blog/c6-bank-e-o-banco-digital-com-melhor-experiencia-de-abertura-de-conta-diz-pesquisa
- C6 Bank — como abrir conta (onboarding ~5 min, automático): https://www.c6bank.com.br/blog/como-abrir-uma-conta-no-app-do-c6-bank
- gov.br/MGI — acordo C6 × GOV.BR, ~30 mi (15/07/2025): https://www.gov.br/gestao/pt-br/assuntos/noticias/2025/julho/gestao-e-c6-bank-fazem-acordo-para-simplificar-e-aumentar-a-seguranca-na-autenticacao-de-30-milhoes-de-clientes-no-gov.br
- Investidor10 — PicPay 42,7 mi ativos / 67 mi contas (4T25): https://investidor10.com.br/noticias/picpay-pics-1-balanco-apos-ipo-traz-lucro-136-maior-e-42-7-mi-de-clientes-ativos-119308/
- blog.picpay.com — criar conta (onboarding): https://blog.picpay.com/criar-conta-picpay/
- AioT Brasil — PagBank biometria facial como prova de vida: https://aiotbrasil.com.br/noticias/pagbank-adota-biometria-facial-com-prova-de-vida-para-pagamentos
- Reuters/Investing — C6 lucro R$ 2,46 bi / 40 mi clientes (2025): https://br.investing.com/news/stock-market-news/c6-bank-tem-lucro-liquido-de-r246-bi-em-2025-com-expansao-de-49-na-carteira-de-credito-1821278

**Liga com:** [[De-Para — Onboarding & KYC]] (piloto) · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
