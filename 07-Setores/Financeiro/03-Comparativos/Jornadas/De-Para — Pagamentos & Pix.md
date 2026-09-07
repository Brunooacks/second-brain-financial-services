---
tipo: jornada-depara
jornada: pagamentos-pix
players: [Itaú, Bradesco, Banco do Brasil, Nubank, Inter, Mercado Pago]
data_captura: 2026-07-03
fontes: [TI Inside, Mobile Time, Nu International, Let's Money, ConvergenciaDigital, StartSe, CNN Brasil, Money Report, Contábeis, O Tempo, InfoMoney, Peers Consulting, Vanquish, Iniciador, Febraban/DGABC, Finsiders, Mercado Libre Tech]
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [jornada, depara, benchmarking, pagamentos, pix, agentic-commerce, pix-automatico]
---

# 🧭 De-Para — Jornada: Pagamentos & Pix / agentic

**Recorte (1 frase):** Como os 6 players-piloto conduzem o pagamento no dia a dia (iniciar → autorizar → confirmar → liquidar) num momento em que o Pix virou trilho dominante (30,1 bi de transações em canais digitais em 2025, +20%, e 42% do e-commerce vs 40% do cartão), o Pix Automático destrava a recorrência, e a interface de pagar migra do "toque no app" para o comando conversacional (voz/texto/imagem) e, na fronteira, para o **agente que paga sozinho sob mandato** via Pix Biometria — modalidade de pagamento agêntico já regulada pelo Bacen.

## 🔍 Decomposição da jornada
Etapas canônicas observadas (públicas, até a parede de login):
1. **Iniciação** — usuário dispara o pagamento (chave Pix, QR Code, copia-e-cola, ou comando em linguagem natural: voz, texto, imagem).
2. **Interpretação/intenção** — o app resolve destinatário, valor e contexto (cada vez mais via GenAI: "manda 50 pro Fulano").
3. **Autorização** — confirmação do usuário (senha, biometria) e checagem antifraude em tempo real.
4. **Liquidação** — execução no trilho (Pix instantâneo, cartão, TED).
5. **Recorrência/mandato** — Pix Automático (débito recorrente autorizado) ou, na fronteira, agente que executa sob mandato (Pix Biometria).
6. **Pós-transação** — comprovante, categorização, alertas e sugestão de próximos pagamentos.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| Inter | **L4** (agente executa Pix via comando; predom. L3) | ~3–4 | Seven, assistente de IA que **executa** transferências via Pix, reinvestimentos e parcelamentos direto no app (não só conversa); >11 mi de clientes na 1ª fase, +20 mi de acessos em 2026 (CNN Brasil / Money Report · 12/2025–2026) |
| Bradesco | **L4** (GenAI executa Pix por NLP; roadmap agêntico) | ~3–4 | "Pix Inteligente" via WhatsApp da BIA (IA generativa): interpreta linguagem natural mesmo sem dizer "Pix", identifica contato, confirma e efetiva; roadmap 2026 "AI Powered Bridge" com capacidades agênticas (ConvergênciaDigital / StartSe · 07/2025–2026) |
| Nubank | **L4** (Pix por voz/texto com GenAI; predom. L2–L3) | ~3 | Pix com IA por voz e texto (app e WhatsApp), evolução do Pix + crédito; **10 mi de usuários ativos mensais** no fim do 1T26; confirmação por senha + antifraude comportamental (Mobile Time / Nu International · 14/05/2026) |
| Banco do Brasil | **L4** (GenAI multimodal — Pix por imagem; predom. L2) | ~3–4 | "Pix por imagem" no WhatsApp: IA reconhece foto de papel manuscrito com chave e valor, sugere pagamentos e lembra transações; canal WhatsApp com **20 mi de usuários** (1º sem/2025) (Contábeis / O Tempo · 10/2025) |
| Itaú | **L4** (Pix conversacional por voz/QR; predom. L3) | ~3–4 | Pix via WhatsApp por texto, áudio e QR Code usando "Itaú Intelligence"; posicionamento de benefícios sobre Pix Automático; +84% em iniciativas GenAI em 2025 (InfoMoney / TI Inside · 2025–02/2026) |
| Mercado Pago | **L3** (ML no scoring/fraude do pagamento; tooling agêntico dev-facing) | ~3 | Checkout Pro integrável via MCP agêntico em <30 min (dev-facing); ML de fraude com ~5.000 variáveis por transação; forte como adquirente/trilho, sem produto conversacional de pagamento ao consumidor de mesma maturidade (Mercado Libre Tech · 2026) |

**Líder da jornada:** empate técnico em **L4** entre Inter, Bradesco, Nubank, BB e Itaú (Pix conversacional/GenAI) · **Gap máximo:** 1 nível (L4 vs L3 do Mercado Pago no fluxo ao consumidor)

> **Sinal de categoria (o achado desta passada):** ao contrário do crédito — onde só o Nubank chegou a L4 —, em pagamentos **a categoria inteira convergiu para L4** via Pix conversacional (voz/texto/imagem). Isso comoditizou a interface de pagar. Nenhum dos 6 exibe evidência pública de **L5 shipado ao consumidor** (agente que paga ponta-a-ponta sob mandato com escopo/limite/trilha auditável). Inter (Seven executa) é o mais próximo, mas por comando transação-a-transação, não sob mandato autônomo. O trilho L5 já existe e **já é regulado**: Pix Biometria / pagamento agêntico via Open Finance, lançado por terceiros (Iniciador/Teller, 1º MCP de Pix agêntico, jun/2026). Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| Bradesco | Conversão de jornadas no Pix Inteligente (WhatsApp/BIA), após 6 meses | **>74%** | StartSe, "Humanos + Agentes: novo modelo AI Powered" · 2026 |
| Bradesco | Tempo por transação no Pix Inteligente | **−75%** | StartSe · 2026 |
| Bradesco | Custo por transação no Pix Inteligente | **−60%** | StartSe · 2026 |
| Nubank | Usuários ativos mensais do Pix com IA (voz/texto) | **10 milhões** (fim do 1T26) | Mobile Time / Nu International · 14/05/2026 |
| Inter | Clientes que usaram a assistente Seven (1ª fase) | **>11 milhões**; +20 mi de acessos em 2026 | CNN Brasil / Money Report · 2025–2026 |
| Banco do Brasil | Usuários do canal WhatsApp (Pix por voz/imagem) | **20 milhões** (1º sem/2025) | Contábeis / O Tempo · 10/2025 |
| Setor (Pix) | Transações Pix em canais digitais em 2025 | **30,1 bilhões (+20% a.a.)**; 42% do e-commerce (vs 40% cartão) | Febraban/DGABC · 26/06/2026; Global Payments Report/Finsiders · 2025 |
| Setor (Pix Automático) | Crescimento de transações Q4'25 → Q1'26 | **+182%** (novos usuários +181%) | PagBrasil, análise Pix Automático 1º tri · 2026 (contexto de terceiro) |
| Itaú | Ganho quantitativo específico do Pix conversacional | [sem fonte pública específica] | posicionamento qualitativo (InfoMoney · 2025) |
| Mercado Pago | Ganho quantitativo do pagamento ao consumidor com IA | [sem fonte pública específica] | força é fraude/adquirência (ver [[De-Para — Originação de crédito]]) |

## ⭐ Diferenciais reais
- **Inter (Seven)** — único que move de "assistente que conversa" para **agente que executa** transação (Pix, reinvestimento, parcelamento) dentro do app. É a ponta agêntica do piloto, ainda que sob comando transação-a-transação.
- **Bradesco** — o incumbente que mais **mostra número** em pagamento conversacional: −75% tempo, −60% custo, >74% conversão no Pix Inteligente via WhatsApp. Roadmap 2026 já nomeia "capacidades agênticas".
- **Banco do Brasil** — único com **Pix multimodal por imagem** (visão computacional lê chave manuscrita numa foto) — inclusão de quem não digita, e superfície de fraude nova.
- **Nubank** — escala do Pix conversacional (10 mi MAU) e o casamento **Pix + crédito** (pagar usando crédito no mesmo fluxo).
- **Mercado Pago** — aposta no **trilho para agentes de terceiros** (MCP/Checkout Pro integrável por IDE agêntico) — infra de pagamento para o agentic commerce, não interface ao consumidor.
- **Trilho BR (fora do piloto)** — Pix + Open Finance + **Pix Biometria** dão ao Brasil um trilho de pagamento agêntico regulado que nenhum outro país replicou na mesma escala (Iniciador/Teller · jun/2026).

## 🕳️ O vale (lacuna vendável)
- **A interface de pagar virou commodity (todos L4), o mandato governado não (ninguém L5 shipado):** o valor migrou de "pagar por voz" para "deixar o agente pagar sob mandato com escopo, limite e trilha". O trilho (Pix Biometria) já é regulado pelo Bacen — falta a camada de **governança do mandato**, que é exatamente Cohort + Veltrix.
- **Pagamento conversacional multiplica a superfície de fraude:** voz, texto e imagem abrem portas para engenharia social, deepfake de voz e imagem forjada (BB lê foto manuscrita → passível de adulteração). Quanto mais natural a interface, maior a dívida de segurança — território de copiloto antifraude em tempo real na autorização.
- **LLM no caminho de cada transação = custo de inferência vira linha de P&L:** com 10 mi (Nubank) e 20 mi (BB) de usuários em canais conversacionais, cada "manda 50 pro Fulano" chama um modelo. Bradesco já reporta −60% de custo/transação; a fronteira é **FinOps de inferência por transação** (roteamento por custo e por jurisdição) — o core do Veltrix.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (landing de Pix, Pix Automático, fluxos de WhatsApp/assistente demonstrados publicamente, simuladores). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) diferente do crédito, em pagamentos **a categoria toda chegou a L4** (Pix conversacional por voz/texto/imagem) — isso comoditizou a interface e move a disputa para o próximo patamar; (2) o patamar L5 (agente paga sob mandato) tem trilho **já regulado** no Brasil (Pix Biometria/Open Finance) e já foi aberto por terceiros (Iniciador/Teller), mas nenhum dos 6 shipou governança de mandato ao consumidor — é vale aberto; (3) o pagamento conversacional em escala cria dois passivos simultâneos, **fraude** (superfície nova) e **custo de inferência por transação** (Bradesco já expõe o número: −60%) — os dois são governança e economia de IA, o seu terreno.

---
**Fontes:**
- TI Inside — Nubank lança Pix Automático com busca inteligente (13/06/2025): https://tiinside.com.br/13/06/2025/nubank-lanca-pix-automatico-com-busca-inteligente-de-contas/
- Mobile Time — Nubank IA Pix voz/áudio (13/06/2025): https://www.mobiletime.com.br/noticias/13/06/2025/nubank-ia-pix-voz-audio/
- Mobile Time — Pix com IA chega a 10 mi no Nubank (14/05/2026): https://www.mobiletime.com.br/noticias/14/05/2026/pix-ia-nubank-10-mi/
- Nu International — Pix com IA no App e WhatsApp: https://international.nubank.com.br/pt-br/consumidores/pix-com-inteligencia-artificial-agora-no-app-e-whatsapp-do-nu/
- ConvergênciaDigital — Bradesco Pix por voz no WhatsApp da BIA: https://convergenciadigital.com.br/mercado/bradesco-lanca-pix-por-comando-de-voz-pelo-whatsapp-da-ia-generativa-bia/
- Mobile Time — Bradesco Pix por voz WhatsApp BIA (14/07/2025): https://www.mobiletime.com.br/noticias/14/07/2025/pix-whatsapp-bradesco/
- StartSe — Humanos + Agentes / Bradesco AI Powered (ganhos Pix Inteligente): https://www.startse.com/artigos/humanos-agentes-o-novo-modelo-ai-powered-que-esta-redefinindo-o-futuro-dos-bancos/
- CNN Brasil — Inter assistente de IA Seven: https://www.cnnbrasil.com.br/economia/negocios/inter-lanca-assistente-de-ia-para-apoiar-gestao-financeira-no-aplicativo/
- Money Report — Inter libera Seven, agente que faz Pix e reinvestimentos: https://www.moneyreport.com.br/negocios/inter-libera-seven-agente-de-ia-que-realiza-reinvestimentos-e-transferencias-via-pix/
- Contábeis — BB lança Pix por imagem com IA no WhatsApp: https://www.contabeis.com.br/noticias/73271/banco-do-brasil-lanca-pix-por-imagem-com-ia-no-whatsapp/
- O Tempo — BB Pix por imagem com IA (08/10/2025): https://www.otempo.com.br/economia/2025/10/8/banco-do-brasil-lanca-pix-por-imagem-com-ia-veja-como-vai-funcionar
- InfoMoney — Itaú e o Pix Automático: https://www.infomoney.com.br/minhas-financas/itau-quer-surfar-no-lancamento-do-pix-automatico-oferecendo-beneficios-aos-clientes/
- Vanquish — Pix virou trilho de agentes de IA (Iniciador): https://www.vanquish.com.br/blog/pix-agentes-ia-iniciador-open-finance
- Let's Money — Iniciador lança 1º MCP de pagamentos agênticos via Pix: https://www.letsmoney.com.br/pagamentos/iniciador-lanca-o-primeiro-mcp-de-pagamentos-agenticos-via-pix/
- DGABC/Febraban — Pix em canais digitais +20% a 30,1 bi em 2025 (26/06/2026): https://www.dgabc.com.br/Noticia/4331599/pagamentos-com-pix-em-canais-digitais-subiu-20-em-2025-a-30-1-bilhoes-diz-febraban
- PagBrasil — Análise Pix Automático 1º tri 2026: https://www.pagbrasil.com/pt-br/blog/noticias/pix-automatic-2026/
- Mercado Libre Tech — Agentic IDEs e MCP aplicados ao Mercado Pago: https://medium.com/mercadolibre-tech/agentic-ides-and-model-context-protocol-applied-to-mercado-pago-fa47429894a9

**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[De-Para — Originação de crédito]] · [[De-Para — Onboarding & KYC]]
