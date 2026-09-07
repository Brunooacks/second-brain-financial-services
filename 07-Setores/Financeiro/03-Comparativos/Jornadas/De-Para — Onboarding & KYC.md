---
tipo: jornada-depara
jornada: onboarding-kyc
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-03
fontes: [Mobile Time, Portal Febraban, gov.br, bb.com.br, TI Inside, sites institucionais]
eixos: [financeiro, governanca, soberania]
tags: [jornada, depara, benchmarking, onboarding, kyc]
---

# 🧭 De-Para — Jornada: Onboarding & KYC

**Recorte (1 frase):** Como os 6 players-piloto conduzem a abertura de conta PF até a parede de login — captura de documento, prova de vida e decisão — num momento em que a autorregulação Febraban (27/out/2025) elevou o piso de diligência do onboarding via biometria e validação cruzada de bases públicas.

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
1. **Descoberta/entrada** — download do app ou site, início do cadastro (CPF, e-mail, telefone).
2. **Captura documental** — foto de RG/CNH, leitura por OCR e checagem de autenticidade.
3. **Prova de vida (liveness)** — selfie + movimentos de cabeça; verificação facial contra o documento.
4. **Validação cruzada** — cruzamento com bases (CPF/Receita, bases públicas, GOV.BR quando integrado).
5. **Decisão** — aprovação instantânea (STP) ou análise assíncrona.
6. **Ativação** — conta pronta no app.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Itaú | **L3** (pontual; predom. L2–L3) | ~5–6 | Biometria evoluiu para 3D liveness anti-deepfake com algoritmos que "contra-atacam" deepfakes; reduziu idas a agência/ATM para habilitar app de 1,5 mi→50 mil/mês (Mobile Time · 13/06/2025) |
| Bradesco | **L3** (pontual; onboarding predom. L2) | ~5–6 | Biometria facial com IA para transações Pix atípicas; rollout PJ (Net Empresa)→PF a partir de mar/2025 (Mobile Time · 30/01/2025) |
| Banco do Brasil | **L2–L3** | ~5–6 | Conta 100% digital "em minutos" pelo app/site; onboarding com FaceMatch, prova de vida e OCR (bb.com.br · captura 03/07/2026); signatário da autorregulação Febraban (Portal Febraban · 27/10/2025) |
| Nubank | **L3** | ~4–5 | "Defesas Inteligentes" — modelo aponta comportamento atípico; onboarding selfie+doc com aprovação em minutos; Selo de Prevenção a Fraudes (TI Inside · 04/06/2025) |
| Inter | **L2** (liveness L3 pontual; decisão assíncrona) | ~6–7 | Onboarding com selfie + movimentos de cabeça; **aprovação em até 3 dias úteis por e-mail** (ajuda.inter.co · captura 03/07/2026); acordo com MGI simplifica autenticação GOV.BR p/ 35 mi de pessoas (gov.br · jun/2025) |
| Mercado Pago | **L3** | ~4–5 | KYC digital com captura de documento, selfie/prova de vida, OCR e cruzamento com bases em tempo real (dimensa/dock · 2025; site institucional) |

**Líder da jornada:** Nubank / Itaú / Mercado Pago (empate em L3) · **Gap máximo:** 1 nível (L3 vs Inter L2)

> **Sinal de categoria:** nenhum dos 6 exibe evidência pública de L4 (copiloto GenAI no onboarding) ou L5 (agêntico) — o mercado inteiro está ancorado em L2–L3. Gap ~0 entre líderes com líder em L≤3 = mercado atrasado no eixo agêntico (oportunidade de categoria, não de catch-up). Ver leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Itaú | Idas a agência/ATM p/ habilitar app | 1,5 mi/mês → 50 mil/mês | Mobile Time, "Biometria reduziu ida de 1,5 mi nos ATMs do Itaú por mês" · 13/06/2025 |
| Nubank | Base de clientes (contexto de escala do KYC) | 118 mi global / 104 mi Brasil | TI Inside, "Nubank recebe Selo de Prevenção a Fraudes" · 04/06/2025 |
| Inter | Alcance do acordo GOV.BR (autenticação) | 35 mi de pessoas | gov.br/MGI, nota oficial · jun/2025 |
| Setor (benchmark de terceiro) | Redução de tempo de onboarding / custo por aquisição | até −70% tempo / −40% CAC | Deloitte, citada por dimensa.com · 2025 (autorrelato de fornecedor, não dos players) |
| Bradesco | Ganho quantificado de onboarding | [sem fonte pública específica] | — |
| Banco do Brasil | Ganho quantificado de onboarding | [sem fonte pública específica] | — |
| Mercado Pago | Ganho quantificado de onboarding | [sem fonte pública específica] | — |

## ⭐ Diferenciais reais
- **Itaú** — 3D liveness anti-deepfake é o passo defensivo mais avançado publicamente declarado; trata deepfake como vetor ativo, não hipótese.
- **Inter** — única integração pública com GOV.BR (via MGI) para autenticação — soberania/base pública como ativo de onboarding, não só compliance.
- **Nubank** — STP real (aprovação em minutos) + "Defesas Inteligentes" comportamental; menor atrito declarado entre os 6.
- **Bloco incumbente (Itaú, BB, Bradesco, Santander, Caixa)** — signatários da autorregulação Febraban (27/10/2025): reporte obrigatório ao Bacen e compartilhamento interbancário de contas suspeitas. Nubank, Inter e Mercado Pago **não constam** na lista de participantes divulgada.

## 🕳️ O vale (lacuna vendável)
- Todos param em L2–L3: verificam identidade, mas **nenhum tem agente que conduza o onboarding ponta-a-ponta sob mandato com trilha auditável** (L5). A validação cruzada de bases públicas é etapa manual/regra, não orquestrada por agente governado.
- Inter perde no **tempo de decisão** (até 3 dias úteis) — atrito de ativação vs. STP dos neobanks.
- A exigência Febraban de "validação cruzada de bases públicas + reporte ao Bacen" cria demanda por uma **camada de governança de dados com residência/roteamento por jurisdição** que hoje nenhum player expõe como diferencial — território direto de Veltrix/Cohort.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login. Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) o mercado inteiro está em L2–L3 — o gap não é entre players, é entre o setor e o patamar agêntico; (2) a autorregulação Febraban virou a governança de onboarding de "boa prática" em obrigação com reporte ao Bacen — vento de cauda para oferta de governança; (3) incumbentes estão dentro da autorregulação, neobanks-piloto não constam — assimetria a explorar.

---
**Fontes:**
- Mobile Time — Itaú biometria/ATMs (13/06/2025): https://www.mobiletime.com.br/noticias/13/06/2025/itau-biometria-reduziu/
- Mobile Time — Bradesco biometria Pix (30/01/2025): https://www.mobiletime.com.br/noticias/30/01/2025/bradesco-biometria-pix/
- Portal Febraban — autorregulação contas laranja (27/10/2025): https://portal.febraban.org.br/noticia/4367/pt-br/
- gov.br/MGI — acordo Inter × GOV.BR, 35 mi (jun/2025): https://www.gov.br/gestao/pt-br/assuntos/noticias/2025/junho/acordo-da-gestao-com-banco-inter-simplifica-autenticacao-no-gov-br-para-35-milhoes-de-pessoas
- TI Inside — Nubank Selo Prevenção a Fraudes (04/06/2025): https://tiinside.com.br/04/06/2025/nubank-recebe-selo-de-prevencao-a-fraudes/
- Banco do Brasil — Conta PF Digital: https://www.bb.com.br/site/pra-voce/contas/
- ajuda.inter.co — primeiro acesso/onboarding: https://ajuda.inter.co/conta-digital-pessoa-fisica-e-mei/como-faco-para-acessar-minha-conta-no-app-do-inter-pela-primeira-vez

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
