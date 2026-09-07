---
tipo: jornada-depara
jornada: fraude
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-03
fontes: [Mobile Time, UGT, Finsiders Brasil, Nu International, Blog Nubank, Contábeis, InfoMoney, Startups.com.br, Estado de Minas, Fórum Brasileiro de Segurança Pública, Banco Central, ACI Worldwide, Deloitte/Febraban]
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [jornada, depara, benchmarking, fraude, disputas, MED, deepfake, antifraude]
---

# 🧭 De-Para — Jornada: Prevenção a fraude & disputas

**Recorte (1 frase):** Como os 6 players-piloto detectam, decidem e resolvem fraude no fluxo transacional (avaliar risco → decidir bloquear/liberar → autorizar → resolver disputa/MED) num momento em que o golpe virou epidemia de escala industrial — R$ 6,5 bi de perdas com Pix só em 2025 (BC), 28 mi de vítimas, deepfakes +126% e personificação +140% no ano — e em que a IA deixou de ser vantagem para virar arma dos dois lados (o mesmo modelo que o banco usa para detectar, o fraudador usa para personalizar o golpe).

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
1. **Avaliação de risco (Fraud Evaluation)** — scoring da transação/sessão em tempo real: biometria comportamental (digitação, mouse, bateria, geolocalização), device fingerprint, histórico.
2. **Decisão (Fraud Decisioning)** — liberar / desafiar (step-up) / bloquear com base no score; migração de regra fixa para modelo que aprende o padrão de cada cliente.
3. **Autorização (Transaction Authorization)** — confirmação com liveness/biometria facial 3D + checagem antifraude embarcada no ato de pagar.
4. **Intervenção ao cliente** — alerta pré-transação quando a conta-destino é suspeita ("você pode estar sendo enganado"); interrupção de chamada de falsa central.
5. **Resolução de disputa (Fraud Resolution)** — contestação, MED (bloqueio em até 7 dias, contestação em até 80 dias), rastreio do dinheiro entre contas-laranja, chargeback (adquirência).
6. **Realimentação** — denúncia do cliente alimenta o modelo e (tendência) o compartilhamento de inteligência entre instituições.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Itaú | **L4** (deepfake detection GenAI + copiloto de alerta ao cliente; predom. L3) | ~2–3 | 1.300 modelos de IA (50 preventivos, metade comportamentais); liveness 3D; **modelo próprio de detecção de deepfake**; "Alerta Pix" e "Protect Call" intervêm em tempo real junto ao cliente (Mobile Time · 14/04/2025; UGT · 2025) |
| Nubank | **L4** (IA comportamental + Alerta de Golpe conversacional pré-transação; predom. L3) | ~2–3 | Sistema de IA identifica comportamento atípico e bloqueia; **Alerta de Golpe** avisa antes de concluir o Pix se a conta-destino é suspeita; "Modo Rua" (5 mi+ clientes); denúncias realimentam o modelo (rede); Selo CNF de Prevenção a Fraudes 2025 (Blog Nubank / Nu International · 2025) |
| Mercado Pago | **L3** (ML de fraude transacional em escala de adquirente) | ~2–3 | ML de fraude com **~5.000 variáveis por transação** (device fingerprint, cadência de digitação, padrões de sessão); força em adquirência/chargeback do e-commerce; sem produto público de intervenção conversacional ao consumidor (Startups.com.br · 2025; Mercado Libre Tech · 2026) |
| Bradesco | **L3** (detecção comportamental em tempo real; predom. L2–L3) | ~2–3 | Migração para modelos que aprendem o padrão do cliente e detectam desvio antes da conclusão; camada de segurança Pix; sem número público específico de fraude (Finsiders · 02/07/2026; banco.bradesco/seguranca) |
| Banco do Brasil | **L3** (IA antifraude + MED; predom. L2–L3) | ~2–3 | IA para golpes e comportamento suspeito; bloqueio automático de contas suspeitas sob a nova regra do BC (abr/2026); matriz de resiliência com IA; sem número público específico (Blog BB · 2025; Estado de Minas · 04/2026) |
| Inter | **L3** (biometria comportamental; predom. L2–L3) | ~2–3 | Biometria comportamental contínua e avaliação de risco de device como padrão de mercado; sem evidência pública de GenAI antifraude nem número específico (contexto setorial Finsiders · 2026) |

**Líder da jornada:** empate técnico em **L4** entre **Itaú** e **Nubank** (Itaú pela detecção de deepfake com GenAI + copiloto de intervenção ao cliente; Nubank pelo Alerta de Golpe conversacional pré-transação com efeito de rede) · **Gap máximo:** 1 nível (L4 vs L3 de Bradesco, BB, Inter e Mercado Pago)

> **Sinal de categoria (o achado desta passada):** a **detecção** de fraude é hoje L3–L4 em todo o piloto (ML comportamental é commodity; a diferença é quem tem GenAI e efeito de rede). Mas a **resolução de disputa** (Fraud Resolution / MED / chargeback) segue presa em L2–L3: processo por regra, prazos longos (bloqueio 7 dias, contestação 80 dias) e humano no meio. Ninguém shipou **L5** — agente que resolve a disputa ponta-a-ponta sob mandato, reúne evidência, aciona o MED e presta contas com trilha auditável. E há um vetor novo: o setor pede **compartilhamento de inteligência entre bancos** (88% acham que teria impacto relevante; 89% querem dado em tempo real da conta-destino) — mas isso esbarra em residência de dados e jurisdição, que é exatamente o terreno de governança/soberania. Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Itaú | Redução de perdas por fraude (com IA, em 2 anos) | **−50%** | Mobile Time · 14/04/2025; UGT · 2025 |
| Itaú | Redução de incidentes de alto impacto desde 2018 | **−98%** | Mobile Time · 14/04/2025 |
| Itaú | Golpes identificados pela ferramenta "Alerta Pix" | **80% (8 em cada 10)** | UGT · 2025 |
| Itaú | Modelos de IA em uso (preventivos) | **1.300 modelos / 50 preventivos** (metade comportamentais) | Mobile Time · 14/04/2025 |
| Nubank | Clientes que ativaram o "Modo Rua" (limite fora de rede confiável) | **5 milhões+** | Nu International · 2025 |
| Mercado Pago | Variáveis por transação no ML de fraude/scoring | **~5.000 variáveis** | Startups.com.br · 2025 |
| Setor (Pix) | Perdas com golpes de Pix em 2025 | **R$ 6,5 bilhões** (28 mi de vítimas; 53% com 50+ anos) | Banco Central / Estado de Minas · 2025–2026 |
| Setor (Pix+boleto) | Vítimas jul/2024–jun/2025 e prejuízo | **24 mi de vítimas / ~R$ 29 bi** | Fórum Brasileiro de Segurança Pública · 2025 |
| Setor (deepfake) | Crescimento de ataques com deepfake / personificação em 2025 | **+126% / +140%** | levantamento setorial · 2025 |
| Setor (projeção) | Fraude com Pix projetada até 2028 | **> R$ 12 bilhões** | ACI Worldwide · 2025 |
| Contexto global | Ganho de detecção com GenAI embarcada (Mastercard) | **até +300%** (autorrelato de terceiro, não-BR) | Mastercard · 2025 |
| Bradesco / BB / Inter | Ganho quantitativo específico de IA antifraude | [sem fonte pública específica] | qualitativo (Finsiders · 2026) |

## ⭐ Diferenciais reais
- **Itaú** — o único com **modelo próprio de detecção de deepfake** e com **intervenção em tempo real na ponta do cliente** (Alerta Pix identifica 80% dos golpes; Protect Call derruba a falsa central). Move a defesa do "back-office do banco" para o "copiloto de segurança do consumidor". É o L4 mais completo.
- **Nubank** — **Alerta de Golpe conversacional pré-transação** + **efeito de rede** (a denúncia de um cliente protege milhões) + "Modo Rua" como controle na mão do usuário. Defesa distribuída, não só central.
- **Mercado Pago** — profundidade de **ML transacional de adquirente** (~5.000 variáveis) e a dor de **chargeback/friendly fraud** do e-commerce, que os bancos de varejo não enfrentam na mesma intensidade. Fraude como problema de marketplace, não só de conta.
- **Banco do Brasil** — ancoragem no **MED e no arcabouço regulatório** (rastreio do dinheiro entre contas-laranja, bloqueio automático sob a regra do BC de abr/2026). Força institucional/processual.
- **Trilho BR (contexto)** — Resolução BCB 403 (nov/2024, monitoramento antifraude obrigatório) + MED + bloqueio automático de chaves fazem do Brasil um dos arcabouços de pagamento instantâneo mais regulados do mundo. A régua de compliance é alta — e é ativo para quem sabe operá-la.

## 🕳️ O vale (lacuna vendável)
- **A detecção comoditizou (L3–L4), a resolução de disputa não (L2–L3):** o dinheiro e a dor migraram para o pós-fraude — MED, contestação, rastreio de contas-laranja, chargeback — que ainda é regra + humano + prazo longo. Território de **agente de resolução de disputa governado sob mandato** (reúne evidência, aciona MED, presta contas): Fraud Resolution é o SD mais atrasado da jornada e o de maior exposição regulatória (responsabilidade objetiva crescente no judiciário). Encaixe direto em Cohort.
- **O setor quer compartilhar inteligência antifraude, mas trombou na soberania do dado:** 88% dos players veem valor em troca entre bancos e 89% querem dado em tempo real da conta-destino — mas isso exige residência de dados, roteamento por jurisdição e trilha de quem viu o quê. É a malha de inteligência antifraude **como problema de governança/soberania** — exatamente o meu núcleo (Veltrix roteia; a governança do compartilhamento é o produto).
- **A interface conversacional multiplica a superfície de fraude por deepfake/engenharia social:** com Pix por voz/texto/imagem em escala (ver [[De-Para — Pagamentos & Pix]]), a autorização precisa de um **copiloto antideepfake em tempo real** no ato de pagar. A defesa também tem custo de inferência por transação (FinOps) — cada checagem chama um modelo.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (landings de segurança/prevenção a golpes, Alerta Pix/Alerta de Golpe demonstrados publicamente, Modo Rua, páginas de MED). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) a **detecção** de fraude virou paridade competitiva — todos em L3–L4, ML comportamental é commodity; a diferença real é quem tem GenAI (Itaú, deepfake) e efeito de rede (Nubank); (2) o vale aberto é a **resolução de disputa/MED**, presa em L2–L3, com prazo longo, humano no meio e **responsabilidade objetiva crescente no judiciário** — dor cara, regulada e agentificável sob mandato; (3) o desejo de **compartilhar inteligência entre bancos** (88%/89%) é bloqueado por **residência de dados e jurisdição** — ou seja, o próximo salto antifraude do país é, na verdade, um problema de governança/soberania, o seu terreno; (4) o número que ancora tudo: **R$ 6,5 bi de perdas com Pix em 2025** e projeção de **>R$ 12 bi até 2028** (ACI) — o board não precisa ser convencido de que o problema é grande, precisa saber onde a IA governada corta a perda sem criar passivo regulatório novo.

---
**Fontes:**
- Mobile Time — Itaú usa IA e comportamento para combater fraudes (14/04/2025): https://www.mobiletime.com.br/noticias/14/04/2025/itau-ia-comportamento/
- UGT — Como bancos usam IA para rastrear ações suspeitas (Alerta Pix 80%, −50% perdas): https://www.ugt.org.br/Noticias/78830-Contra-golpes-virtuais-veja-como-bancos-usam-IA-para-rastrear-acoes-suspeitas-e-barrar-ameacas
- Finsiders Brasil — Setor financeiro deixa regras fixas para antecipar fraudes (02/07/2026): https://finsidersbrasil.com.br/noticias-sobre-fintechs/fraudes/fraudes-ganham-velocidade-com-ia-instituicoes-financeiras-acompanham/
- Blog Nubank — Proteção em várias camadas / Alerta de Golpe: https://blog.nubank.com.br/nubank-seguranca/
- Nu International — Modo Rua protege 5 mi+ de clientes: https://international.nubank.com.br/pt-br/consumidores/carnaval-seguro-pioneiro-modo-rua-do-nubank-ja-protege-mais-de-5-milhoes-de-clientes/
- Estado de Minas — Nova regra do Pix: bloqueio automático de contas suspeitas (04/2026): https://www.em.com.br/emfoco/2026/04/29/nova-regra-do-pix-entrou-em-vigor-bancos-como-nubank-itau-e-caixa-devem-bloquear-contas-suspeitas-automaticamente/
- Blog BB — Golpes com inteligência artificial: como agir: https://blog.bb.com.br/golpes-com-inteligencia-artificial/
- Startups.com.br — Mercado Pago ~5.000 variáveis por transação: https://startups.com.br/eventos/
- Banco Central / Estado de Minas — perdas Pix R$ 6,5 bi em 2025: https://www.em.com.br/emfoco/2026/04/22/bancos-como-nubank-itau-e-caixa-passam-a-seguir-novas-regras-do-banco-central-para-limites-e-bloqueio-automatico-do-pix/
- WeLiveSecurity/ESET — Golpes com Pix mais sofisticados com IA em 2026: https://www.welivesecurity.com/pt/golpes-fraudes/ia-e-engenharia-social-devem-tornar-golpes-com-pix-mais-sofisticados-em-2026/

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[De-Para — Pagamentos & Pix]] · [[De-Para — Originação de crédito]]
