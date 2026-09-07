---
tipo: jornada-depara
jornada: fraude
fase: 2
players: [Santander, Caixa, C6, PicPay, PagBank/Stone]
data_captura: 2026-07-05
fontes: [Contec Brasil, Let's Money, TI Inside, Mobile Time, Santander Imprensa, Portal Contexto, Blog C6, Blog PicPay, Blog PagBank, Stone Docs, Finsiders Brasil, Serasa Experian, BCB, VAAS, Jusbrasil, Sindpd, WeLiveSecurity/ESET]
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [jornada, depara, benchmarking, fraude, disputas, MED, deepfake, antifraude, fase-2, expansao]
---

# 🧭 De-Para — Jornada: Prevenção a fraude & disputas (Fase 2 · players de expansão)

**Recorte (1 frase):** Como os 5 players de expansão (Santander, Caixa, C6, PicPay, PagBank/Stone) detectam, decidem e resolvem fraude (avaliar risco → decidir → autorizar → resolver disputa/MED) para testar se o achado do piloto — "detecção comoditizou em L3–L4, resolução de disputa segue presa em L2–L3, ninguém no L5" — se repete fora do grupo de 6, num momento em que **o regulador virou o nivelador**: a Res. BCB 403 obriga monitoramento antifraude a todo participante do Pix (desde nov/2024) e o **MED 2.0** (Res. BCB 493, obrigatório desde 02/02/2026) promete elevar a recuperação de ativos de <7% para até 80% via rastreio em cadeia de até 5 camadas. Liga com [[De-Para — Prevenção a fraude & disputas]] (piloto).

## 🔍 Decomposição da jornada
Mesmas etapas canônicas do piloto (públicas, até a parede de login):
1. **Avaliação de risco (Fraud Evaluation)** — scoring da transação/sessão em tempo real: biometria comportamental, device fingerprint, geolocalização, histórico.
2. **Decisão (Fraud Decisioning)** — liberar / desafiar (step-up) / bloquear; migração de regra fixa para modelo que aprende o padrão do cliente.
3. **Autorização (Transaction Authorization)** — liveness/biometria facial + checagem antifraude embarcada; alerta pré-transação e alerta em ligação (falsa central).
4. **Resolução de disputa (Fraud Resolution)** — contestação, **MED 2.0** (bloqueio imediato, prazo 7 dias, rastreio em cadeia de até 5 camadas), chargeback (adquirência).
5. **Realimentação** — denúncia realimenta o modelo e (tendência) o compartilhamento de inteligência entre instituições.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Santander | **L4** (GenAI industrializada na gestão de fraude de cartão + copiloto de intervenção ao cliente; predom. L3) | ~2–3 | Fraude de cartão é onde a IA mostra resultado mais claro no BR: contestação **~95% mais rápida, até 90% de automação, <1% de erro**; **280+ agentes de automação de processo em produção** (crédito, fraude, KYC); **Alerta de Segurança** para PJ e PF avisa na tela em tempo real antes de concluir transação, **Alerta em ligação** desde mai/2025, **Central de Segurança** (jun/2026) (Contec Brasil / Let's Money / TI Inside / Santander Imprensa · 2026). |
| C6 (Banco C6) | **L3** (ML comportamental + alertas visuais em tempo real; liveness/biometria que segurou ataque com IA; predom. L3) | ~2–3 | Sistemas de segurança **barraram ataque que usava IA/deepfake** para simular movimentos faciais: **709 tentativas em 259 contas, zero invasão concretizada** (denúncia do C6 levou à condenação da dupla); app exibe **avisos visuais** em transações atípicas fora do padrão (Portal Contexto / Blog C6 · 2026). |
| PicPay | **L3** (ML de risco + biometria + Modo Seguro; GenAI só no suporte) | ~2–3 | **Central de Segurança** reúne biometria, limites de transação e **Modo Seguro** (proteção extra em local inseguro); IA analisa risco e **identifica devices comprometidos por malware**; membro da **Zetta** (que aponta engenharia social como frente crítica do Pix). GenAI (Azure OpenAI/ChatGPT) está no **atendimento**, não na decisão de fraude (Blog PicPay / Let's Money · 2026). |
| PagBank/Stone | **L3** (antifraude embarcado de adquirente + chargeback; resolução híbrida IA+humano na Stone) | ~2–3 | Antifraude embarcado no e-commerce e no POS: IA **cruza histórico de compra, navegação e localização** para achar padrão de fraude; **Stone** mantém **suporte humano para casos complexos** de chargeback, PagBank com volume crescente e processo **em maturação** (Blog PagBank / Stone Docs / Inteligência Setorial · 2026). |
| Caixa | **L2–L3** (piso regulatório: monitoramento 403 + MED 2.0; sem IA antifraude própria observável) | ~4–6 | **Caixa Tem** (130 mi+ usuários) cumpre o piso do BC: monitoramento antifraude obrigatório (Res. 403), MED 2.0, cartilha de segurança e bloqueio de chaves fraudulentas. **Sem evidência pública de modelo próprio de IA/GenAI antifraude**; postura de conformidade, não de diferenciação tecnológica (caixa.gov.br / Serasa Experian / BCB · 2025–2026). |

**Líder da jornada:** **Santander** em **L4** (único da coorte com GenAI industrializada na fraude + copiloto de intervenção ao cliente) · **Piso da coorte:** **L3** (C6, PicPay, PagBank/Stone — nível forçado pelo mandato de monitoramento da Res. 403) · **Gap máximo:** **2 níveis** (L4 Santander vs L2 Caixa em decisão/resolução)

> **Sinal de categoria (o achado desta passada):** o achado do piloto se confirma e ganha uma camada nova de leitura de **governança**. Confirma-se que a **detecção comoditizou** (todos em L3–L4) e que a **resolução de disputa** segue o vale (L2–L3, regra + prazo + humano; ninguém no L5). Mas a novidade da expansão é *por que* comoditizou: aqui **o nivelador foi o regulador, não a competição**. A Res. BCB 403 obriga **todo** participante do Pix a rodar monitoramento antifraude — ou seja, o piso de maturidade da detecção subiu **por decreto** para L3; ninguém pode ficar abaixo. A diferenciação só sobra em **L4** (GenAI + copiloto de intervenção ao cliente, hoje só o Santander na coorte) e no **L5 inexistente** (agente que resolve a disputa/MED ponta-a-ponta). E o **MED 2.0** (recuperação prometida de <7% para 80% via rastreio em cadeia de 5 camadas) eleva a aposta exatamente no SD mais atrasado: a promessa regulatória de 80% só se cumpre com rastreio automatizado interinstitucional — território agêntico governado que ninguém ocupou. Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública específica = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Santander | Aceleração da contestação de fraude de cartão com IA (BR) | **~95% mais rápida** | Contec Brasil / Let's Money · 2026 |
| Santander | Automação e erro no fluxo de fraude de cartão | **até 90% automação / <1% erro** | Contec Brasil / Let's Money · 2026 |
| Santander | Agentes de automação de processo em produção (crédito, fraude, KYC) | **280+ agentes** | Contec Brasil · 2026 |
| Santander | Valor de negócio projetado com IA (grupo; inclui fraude) | **> €1 bi 2026–2028; €35 mi no 1º tri; >€200 mi em 2026** | Let's Money / Dinheiro Vivo · 2026 |
| C6 | Ataque com IA/deepfake barrado pelos sistemas de segurança | **709 tentativas / 259 contas / 0 invasão concretizada** | Portal Contexto · 2026 |
| Setor (MED 2.0) | Meta de recuperação de ativos e rastreio em cadeia | **de <7% para até 80%; bloqueio em até 5 camadas; prazo 7 dias** (Res. BCB 493, obrigatório 02/02/2026) | VAAS / Jusbrasil / BCB · 2025–2026 |
| Setor (Res. 403) | Monitoramento antifraude obrigatório a todo participante do Pix | vigente desde **nov/2024** | Serasa Experian / BCB · 2024–2026 |
| Setor | Bancos que veem prevenção a fraude como prioridade / que já usam IA em escala | **94% prioridade / 60% usam IA** | Finsiders / DataRudder · 2026 |
| Setor (contexto) | Golpes bancários com IA generativa | **mais que dobraram**; fraude com IA até **4,5× mais lucrativa** (Interpol 2026) | Sindpd / Interpol · 2026 |
| PicPay | Ganho quantitativo de IA antifraude | [sem fonte pública específica] | Central de Segurança confirmada, sem métrica isolada |
| PagBank/Stone | Ganho quantitativo de IA antifraude/chargeback | [sem fonte pública específica] | antifraude embarcado confirmado, sem número |
| Caixa | Ganho quantitativo de IA antifraude | [sem fonte pública específica] | postura de conformidade, sem IA própria observável |

## ⭐ Diferenciais reais
- **Santander** — único **L4** da coorte: **industrializou a IA na gestão de fraude de cartão** (contestação 95% mais rápida, 90% automação, <1% erro, 280+ agentes de processo) e move a defesa para a ponta do cliente com **copiloto de intervenção em tempo real** (Alerta de Segurança PJ/PF, Alerta em ligação). É o análogo, na expansão, ao que Itaú/Nubank fazem no piloto.
- **C6** — **caso público de defesa que segurou um ataque com IA/deepfake**: 709 tentativas em 259 contas, zero sucesso, e denúncia que levou à condenação. Prova de liveness/biometria robusta — usar IA para segurar a IA do fraudador, com número.
- **PagBank/Stone** — **antifraude embarcado de adquirente** + **chargeback com resolução híbrida** (Stone mantém humano para caso complexo). Fraude como problema de **marketplace/e-commerce** (friendly fraud), não só de conta — o análogo do Mercado Pago no piloto.
- **PicPay** — **Central de Segurança** consolidada (biometria + limites + Modo Seguro) e IA de **detecção de device comprometido por malware**; assento na **Zetta**, que centra o debate na **engenharia social** (a susceptibilidade da vítima, não a quebra do sistema).
- **Caixa** — não é diferencial de IA, é **diferencial de base e de piso**: 130 mi+ usuários sob o mínimo regulatório (403/MED 2.0). O ativo é escala e soberania do dado social, não tecnologia antifraude.

## 🕳️ O vale (lacuna vendável)
- **O regulador comprimiu a detecção — o vale migrou por decreto:** a Res. 403 obriga monitoramento antifraude a **todo** participante do Pix, então a detecção comoditizou em L3 **por norma**, não por competição. Isso muda a tese de venda: não adianta vender "detecção com IA" (é piso legal para todos); o que vende é **L4 (copiloto de intervenção ao cliente)** e o **L5 inexistente na resolução**. Achado de governança puro: quando o regulador nivela o piso, a fronteira de valor sobe — e quem entende a norma sabe onde ela empurrou o dinheiro.
- **MED 2.0 abriu o L5 e ninguém entrou:** a promessa de recuperação de **<7% para 80%** só se cumpre com **rastreio automatizado em cadeia de até 5 camadas entre instituições** — que é agente resolvendo disputa/MED ponta-a-ponta sob mandato, com trilha e prazo (7 dias). É o mesmo vale do piloto (Fraud Resolution em L2–L3), agora com a régua regulatória elevando a aposta. E é **interinstitucional por natureza** → problema de residência de dado e jurisdição. Cohort (mandato) + Veltrix (roteamento).
- **O piso 403 tem custo por transação (FinOps):** monitorar toda transação antifraude, obrigatório para todos, significa **chamar modelo a cada transação** — sobretudo nos adquirentes de alto volume (PagBank/Stone). O custo do mínimo regulatório é um problema de **FinOps de inferência** + **roteamento por jurisdição** (o caso G42 no stack do Santander mostra que o roteamento é soberania, não só custo). Veltrix.
- **Caixa é o vale mais profundo (gap 2):** a maior base social do país (130 mi+) no piso mínimo, sem IA antifraude própria observável, e é justamente a base mais visada por **engenharia social** (público 50+, o mesmo perfil das 28 mi de vítimas do piloto). Levar copiloto de intervenção governado a base social sob LGPD/procurement estatal = impacto máximo + fricção máxima. Soberania de dado estatal.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (Central de Segurança Santander/PicPay, Alerta de Segurança/Alerta em ligação do Santander, páginas de MED e cartilha da Caixa, blog de segurança do C6, antifraude PagBank/Stone Docs). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) com 11 players agora medidos em fraude, a **detecção é paridade — e paridade imposta por lei** (Res. 403 obriga monitoramento a todos): o piso é L3 por decreto, e vender "detecção com IA" é vender o mínimo regulatório; a diferenciação sobrou em **L4** (copiloto de intervenção ao cliente, só o Santander na coorte, com 95% de aceleração na fraude de cartão) e no **L5 inexistente**. (2) O **MED 2.0** (recuperação prometida de <7%→80% via rastreio em cadeia de 5 camadas, obrigatório desde 02/02/2026) abriu formalmente o L5 no SD mais atrasado — resolução de disputa — e **ninguém entrou**: o agente que rastreia e recupera ponta-a-ponta sob mandato interinstitucional é o vale mais claro do discovery, e é **problema de residência de dado**, não só de IA. (3) O caso **C6 (709 tentativas / 0 sucesso contra deepfake)** e o caso **G42 no stack do Santander** são os dois exemplos do país de que o próximo round de fraude é **soberania**: a IA do fraudador é 4,5× mais lucrativa (Interpol) e o dado de defesa roteia por fornecedores sob outra jurisdição. (4) A **Caixa (L2–L3, 130 mi+)** é o vale mais profundo — a maior base social, a mais visada por engenharia social, no piso mínimo e sem IA própria.

---
**Fontes:**
- Contec Brasil — Com estratégia global, Santander acelera uso de IA (fraude de cartão 95% mais rápida, 90% automação, <1% erro, 280+ agentes): https://contec.org.br/com-estrategia-global-santander-acelera-uso-de-ia-e-ja-colhe-frutos/
- Let's Money — Santander libera IA para 185 mil e mira €200 mi em 2026: https://www.letsmoney.com.br/noticias/santander-libera-ia-185-mil-funcionarios-200-milhoes/
- TI Inside — Santander reforça estratégia anti-fraudes para empresas (Alerta de Segurança PJ em tempo real): https://tiinside.com.br/07/04/2026/santander-reforca-estrategia-anti-fraudes-para-empresas/
- TI Inside — Santander lança Central de Segurança para pessoa física: https://tiinside.com.br/30/06/2026/santander-lanca-central-de-seguranca-para-pessoa-fisica/
- Santander Imprensa — Alerta de Segurança para empresas contra golpes e fraudes: https://santanderimprensa.com.br/santander-reforca-alerta-de-seguranca-para-empresas-contra-golpes-e-fraudes/
- Mobile Time — Conversacional é uma das três prioridades de IA do Santander (crédito e fraude): https://www.mobiletime.com.br/noticias/01/04/2026/ia-prioridade-santander/
- Portal Contexto — Dupla condenada após 709 tentativas de fraudes bancárias (ataque com IA barrado pelo C6): https://portalcontexto.com/dupla-condenada-apos-709-tentativas-de-fraudes-bancarias-em-goias/
- Blog C6 — Ferramentas para evitar golpes no app (alertas visuais em transações atípicas): https://www.c6bank.com.br/blog/ferramentas-para-evitar-golpes-no-app
- Blog PicPay — PicPay inova com tecnologia e IA para proteger usuários (Central de Segurança, Modo Seguro, malware): https://blog.picpay.com/inteligencia-artificial-seguranca/
- Let's Money — Zetta aponta engenharia social como frente crítica no Pix: https://www.letsmoney.com.br/noticias/zetta-engenharia-social-golpes-pix
- Blog PagBank — Sistema de antifraude para e-commerce (IA cruza histórico e localização): https://blog.pagbank.com.br/antifraude
- Stone Docs — Antifraude: https://docs.stone.com.br/antifraude/
- Inteligência Setorial — Segurança no recebimento de pagamentos digitais (maturidade chargeback Stone/PagBank): https://inteligenciasetorial.com.br/seguranca-no-recebimento-de-pagamentos-digitais/
- VAAS — PIX MED 2.0 e Resolução BCB 493 (recuperação <7%→80%, 5 camadas): https://vaas.com.br/blog/pix-med-2-0-resolucao-bcb-493/
- Jusbrasil — Resolução BCB nº 493/2025 e o MED 2.0 (melhoria no rastreio): https://www.jusbrasil.com.br/artigos/resolucao-bcb-n-493-2025-e-o-med-20-melhoria-no-rastreio-dos-valores-em-uma-fraude/5624341765
- BCB — Mecanismo Especial de Devolução (MED 2.0): https://www.bcb.gov.br/content/estabilidadefinanceira/pix/MED/MED_2-0_Circuito_Pix-Dia_1.pdf
- Serasa Experian — Resolução BCB 403/2024 (monitoramento antifraude obrigatório): https://www.serasaexperian.com.br/conteudos/resolucao-bcb-403-2024-novas-medidas-seguranca-do-pix/
- Finsiders Brasil — Setor financeiro deixa regras fixas para antecipar fraudes (94%/60%): https://finsidersbrasil.com.br/noticias-sobre-fintechs/fraudes/fraudes-ganham-velocidade-com-ia-instituicoes-financeiras-acompanham/
- Sindpd — Golpes bancários mais que dobram com avanço da IA generativa: https://sindpd.org.br/2026/06/15/golpes-bancarios-dobram-ia-generativa/
- WeLiveSecurity/ESET — IA e engenharia social devem tornar golpes com Pix mais sofisticados em 2026: https://www.welivesecurity.com/pt/golpes-fraudes/ia-e-engenharia-social-devem-tornar-golpes-com-pix-mais-sofisticados-em-2026/

**Liga com:** [[De-Para — Prevenção a fraude & disputas]] (piloto) · [[De-Para — Pagamentos & Pix (Fase 2 · expansão)]] · [[De-Para — Onboarding & KYC (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
