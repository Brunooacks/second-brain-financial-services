---
tipo: jornada-depara
jornada: pagamentos-pix
fase: 2
players: [Santander, Caixa, C6, PicPay, PagBank/Stone]
data_captura: 2026-07-05
fontes: [c6bank.com.br, revistacobertura, canaltech, letsmoney, news.microsoft.com, abes.org.br, cnnbrasil, mobiletime, tiinside, exame, mobiletime, convergenciadigital, socialhub, conteudo.stone.com.br, antecipafacil, caixa.gov.br, vanquish]
eixos: [financeiro, governanca, soberania, agentes, economia-ia]
tags: [jornada, depara, benchmarking, pagamentos, pix, agentic-commerce, fase-2, expansao]
---

# 🧭 De-Para — Jornada: Pagamentos & Pix / agentic (Fase 2 · players de expansão)

**Recorte (1 frase):** Como os 5 players de expansão (Santander, Caixa, C6, PicPay, PagBank/Stone) conduzem o pagamento no dia a dia (iniciar → interpretar → autorizar → liquidar) até a parede de login, para testar se o achado do piloto — "a interface de pagar comoditizou em L4 (Pix conversacional)" — se repete fora do grupo de 6, num momento em que o Pix Automático vira obrigatório a todas as instituições (até mar/2026) e o trilho de pagamento agêntico via Pix (Iniciador, jun/2026) já tem adquirentes como clientes. Liga com [[De-Para — Pagamentos & Pix]] (piloto).

## 🔍 Decomposição da jornada
Mesmas etapas canônicas do piloto (públicas, até a parede de login):
1. **Iniciação** — usuário/lojista dispara o pagamento (chave Pix, QR, copia-e-cola, ou comando em linguagem natural: voz, texto, imagem).
2. **Interpretação/intenção** — o app/POS resolve destinatário, valor e contexto (cada vez mais via GenAI: "manda 50 pro Fulano" / "R$ 20,50 no débito").
3. **Autorização** — confirmação do usuário (senha, biometria) e checagem antifraude em tempo real.
4. **Liquidação** — execução no trilho (Pix instantâneo, cartão, TED).
5. **Recorrência/mandato** — Pix Automático (débito recorrente autorizado) ou, na fronteira, agente que executa sob mandato (Pix agêntico via Open Finance/biometria).
6. **Pós-transação** — comprovante, categorização, conciliação (lojista) e sugestão de próximos passos.

## 📊 Matriz de maturidade (EMA-J)
Nível pelo passo mais avançado com evidência pública. Ver [[EMA-J — Escala de Maturidade Agentica de Jornada]].

| Player | Nível EMA-J | Nº passos até login | Evidência (fonte · data) |
|--------|-------------|---------------------|--------------------------|
| C6 (Banco C6) | **L4** (consumer; GenAI executa Pix) | ~3 | **C6 Assistant** faz Pix e pagamentos a partir de **foto/print** enviado ao chat, e executa **múltiplos Pix de uma única imagem** (tabela/print com valores + chaves), após confirmação; disponível desde o fim de 2024, ampliado em 2026 para "conversar com a fatura" (Revista Cobertura / Canaltech / Let's Money / TI Inside · 05/2026). |
| PicPay | **L4** (consumer; GenAI multiagente executa Pix) | ~3 | Assistente com **GPT-4.1 em arquitetura multiagente** (agentes especializados: cartões, transferências, crédito); faz **Pix por áudio, foto ou texto** encaminhado, inclusive lendo chave no meio de uma tabela de preços; levado ao **WhatsApp** (Microsoft News / ABES / CNN Brasil / Mundo Conectado · 2026). |
| Santander (via Getnet) | **L4** (merchant/acquiring por voz; consumer L2–L3) | ~3–4 | **Getnet** (adquirente do grupo) lançou **maquininha com GenAI conversacional por voz**: lojista aperta botão, diz "R$ 20,50 no débito", o device interpreta e monta a cobrança. Abordagem **multimodelo** (OpenAI/Claude/Gemini + G42/Abu Dhabi); IA liberada a **185 mil funcionários**. Sem assistente Pix conversacional **ao consumidor** de marca própria observado → L4 é no fluxo do lojista (Exame / ConvergenciaDigital / Let's Money · 2026). |
| PagBank/Stone | **L4** (merchant/acquiring por voz; trilho agêntico via terceiro) | ~3–4 | PagBank lançou a **Minizinha Voz** (jan/2026), **1ª maquininha do Brasil com assistente de vendas por IA** operado por voz (calcula, consulta vendas, monitora estoque, cobra por comando). **Stone** posiciona **agentic commerce** e cobrança via WhatsApp (11 mi+ clientes); **PagBank/Stone são clientes** do trilho de Pix agêntico da Iniciador (TI Inside / Mobile Time / SocialHub / Stone / Vanquish · 2026). |
| Caixa | **L2** (regras; Pix Automático/agendado, sem IA conversacional) | ~4–6 | **Caixa Tem** (130 mi+ usuários) é self-service digital; oferece **Pix Automático** (autorização única, débito recorrente — recorrência por regra) e Pix agendado. **Sem evidência pública de IA conversacional/generativa** no fluxo de pagamento; recorrência é determinística, não agêntica (Antecipa Fácil / caixa.gov.br / CNN Brasil · 2025–2026). |

**Líder da jornada:** empate técnico em **L4** entre C6, PicPay, Santander/Getnet e PagBank/Stone · **Gap máximo interno:** **2 níveis** (L4 vs Caixa L2) · **Gap vs líderes do piloto (L4):** 0 nível

> **Sinal de categoria (o achado desta passada):** o padrão do piloto **se confirma e se refina**. Confirma: a interface de pagar comoditizou em **L4** também na expansão — quatro dos cinco players já têm GenAI que **executa** o pagamento (Pix por foto/áudio, cobrança por voz). Refina, e este é o achado novo: a comoditização **se divide por lado da maquininha**. Neobancos (C6, PicPay) subiram ao L4 **no lado do consumidor** (Pix por imagem/áudio); os adquirentes (Santander/Getnet, PagBank/Stone) subiram ao L4 **no lado do lojista** (maquininha por voz) — dois deles lançaram POS por voz na **mesma janela** (Getnet e Minizinha Voz, início de 2026). E a **Caixa, sozinha em L2**, opera a maior base social do país (130 mi+) sem nenhuma camada de IA no pagamento. Ninguém exibe **L5 agêntico próprio shipado**: o trilho L5 (Pix agêntico da Iniciador, jun/2026) é de terceiro, e os adquirentes desta coorte são **clientes** dele, não donos do mandato. Leitura em "O que eu diria num board".

## 💰 Ganhos de negócio publicados
DADO É REI: só autorrelato COM fonte. Sem fonte pública específica = `[sem fonte]`.

| Player | Métrica | Valor | Fonte · página · data |
|--------|---------|-------|-----------------------|
| PicPay | Salto de NPS nas primeiras horas do GPT-4.1 no Assistente | **+10 p.p.** | Microsoft News Center Brasil · 2026 |
| PicPay | Redução de atendimentos direcionados ao humano (pós-GPT-4.1) | **−8 p.p.** | Microsoft News Center Brasil · 2026 |
| PicPay | Escala da base (contexto do assistente de pagamento) | 67 mi contas / 42,7 mi ativas (4T25) | Investidor10 / Finsiders · 2025–2026 |
| Santander | Valor de negócio projetado com IA (grupo; inclui pagamentos/Getnet) | **> €200 mi em 2026**; meta €1 bi 2026–2028; €35 mi no 1º tri; IA para 185 mil funcionários | Let's Money / ConvergenciaDigital · 2026 |
| Stone | Base atendida (contexto do agentic commerce / cobrança WhatsApp) | **11 mi+ clientes**; taxas débito 1,29% / crédito 2,89% / antecipação 0,68–1,15% a.m. | SocialHub · 2026 |
| Caixa | Escala social do Caixa Tem (proxy do vale de inclusão) | **130 mi+ usuários** | Antecipa Fácil · 2026 |
| Setor (Pix Automático) | Obrigatoriedade a todas as instituições | até **mar/2026** (lançado 28/10/2025) | CNN Brasil / caixa.gov.br · 2025–2026 |
| C6 | Ganho quantitativo do Pix conversacional | [sem fonte pública específica] | funcionalidade confirmada, sem métrica isolada |
| PagBank | Ganho quantitativo da Minizinha Voz | [sem fonte pública específica] | marco de lançamento (jan/2026), sem número |
| Santander/Getnet | Ganho quantitativo da maquininha por voz | [sem fonte pública específica] | lançamento, sem métrica isolada |

## ⭐ Diferenciais reais
- **C6 (consumer)** — **múltiplos Pix de uma só imagem** via GenAI: manda um print de tabela com vários valores+chaves e o assistente lista e executa todos após confirmação. É o Pix conversacional mais "denso" da coorte no lado do cliente.
- **PicPay (consumer)** — **arquitetura multiagente sobre GPT-4.1** (orquestrador + agentes por tema), com número público de impacto (NPS +10 p.p., −8 p.p. de handoff humano) — raro na coorte, que quase não abre métrica de pagamento.
- **Santander/Getnet e PagBank (merchant)** — **maquininha por voz com GenAI**: o L4 aqui não é do consumidor, é do **lojista** ("R$ 20,50 no débito" por comando). Dois adquirentes lançaram na mesma janela — sinal de comoditização do POS conversacional.
- **Stone (merchant/agentic)** — posicionamento explícito de **agentic commerce** + cobrança via WhatsApp; junto com PagBank, é **cliente do trilho de Pix agêntico** (Iniciador) — a ponta que mais perto está do L5, mas com o mandato na mão de um terceiro.
- **Caixa (base social)** — não é diferencial de IA, é **diferencial de base**: 130 mi+ usuários e Pix Automático sobre público social. O ativo é a escala e a soberania do dado, não a tecnologia de pagamento.

## 🕳️ O vale (lacuna vendável)
- **L4 dos dois lados, L5 governado de ninguém:** a interface de pagar (consumer e merchant) virou commodity na expansão inteira; o valor migrou para o **mandato agêntico governado** — e nesta coorte o trilho L5 (Pix agêntico) é **de terceiro** (Iniciador), com Santander/PagBank/Stone como clientes. Falta a camada de **escopo/limite/trilha/residência** sobre esse mandato — Cohort + Veltrix.
- **Adquirente por voz sem governança proporcional do agente:** Getnet e Minizinha Voz colocam GenAI no POS do lojista. Quanto mais o device "entende e cobra sozinho", maior a superfície de erro/fraude e a **dívida de trilha auditável** no fluxo de merchant acquiring — vale de governança no lado que ninguém está olhando (o piloto olhou o consumidor).
- **Multimodelo com fornecedor fora de jurisdição = problema de soberania, não só de custo:** o Santander declara stack com **OpenAI + Claude + Gemini + G42 (Abu Dhabi)**. Dado de pagamento roteado a um modelo sob outra jurisdição é questão de **residência de dado**, não de FinOps. Vale de roteamento por jurisdição — Veltrix — com moldura de soberania.
- **Caixa é o vale mais profundo (gap 2):** maior base social do país travada em L2 no pagamento. Levar Pix conversacional/agêntico governado a 130 mi+ sob LGPD e procurement estatal = impacto máximo + fricção máxima. Soberania de dado estatal no mesmo alvo.

## 🖼️ Telas de evidência
🖼️ **pendente — captura supervisionada (Claude in Chrome).** Só telas públicas, pré-login (landing de Pix, Pix Automático, demos públicas de C6 Assistant / Assistente PicPay / Minizinha Voz / Getnet voz). Ver [[TPL-Spec-Tela]].

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina coletou e mediu; a tese é sua.)
Insumos factuais para a sua leitura: (1) com 11 players agora medidos em pagamentos, o **L4 é o teto e é paridade** — a interface de pagar comoditizou em toda a linha; a novidade da expansão é que a comoditização **se divide por lado da maquininha**: neobancos (C6, PicPay) no consumidor, adquirentes (Getnet, PagBank/Stone) no lojista, dois POS por voz lançados na mesma janela. (2) O **L5 agêntico** existe como trilho regulado (Iniciador, Pix agêntico), mas nesta coorte ele é **de terceiro** — Santander, PagBank e Stone são clientes, não donos do mandato; quem governar o mandato (escopo/limite/trilha/residência) captura a camada que o trilho não entrega. (3) O caso **G42 no stack do Santander** é o exemplo mais nítido do país de por que roteamento por jurisdição de dado de pagamento é soberania, não custo. (4) A **Caixa (L2, 130 mi+)** é o vale mais profundo do discovery até aqui — a distância entre base social e maturidade de IA no pagamento é de 2 níveis.

---
**Fontes:**
- Revista Cobertura — C6 lança função de vários Pix de uma vez com IA: https://www.revistacobertura.com.br/noticias/servicos-financeiros/c6-bank-lanca-funcao-que-permite-fazer-varios-pix-de-uma-vez-so-com-ia/
- Canaltech — C6 Bank permite "conversar" com a fatura via IA: https://canaltech.com.br/apps/c6-bank-permite-conversar-com-a-fatura-do-cartao-via-ia-entenda-como-funciona/
- C6 Bank — C6 Assistant (Pix e boletos por IA): https://www.c6bank.com.br/blog/c6-assistant
- Let's Money — C6 IA faz múltiplos Pix a partir de uma imagem: https://www.letsmoney.com.br/fintech/c6-ia-pix-imagem/
- Microsoft News Center Brasil — PicPay adota GPT-4.1 e entra na era dos multiagentes (NPS +10 p.p., −8 p.p. humano): https://news.microsoft.com/pt-br/picpay-adota-ia-mais-avancada-do-modelo-gpt-em-seu-assistente-e-entra-na-era-dos-multiagentes/
- CNN Brasil — PicPay leva Pix ao WhatsApp com IA (áudio, imagens, texto): https://www.cnnbrasil.com.br/economia/negocios/picpay-leva-pix-ao-whatsapp-com-ia-que-interpreta-audio-imagens-e-texto/
- Exame — Getnet lança maquininha que aceita pagamento por voz com IA generativa: https://exame.com/inteligencia-artificial/exclusivo-getnet-lanca-maquininha-que-aceita-pagamento-por-voz-com-ia-generativa/
- ConvergenciaDigital — Santander × IA generativa (stack multimodelo, meta €1 bi): https://convergenciadigital.com.br/mercado/santander-investe-50-milhoes-de-euros-em-ia-generativa-brasil-tem-papel-chave/
- Let's Money — Santander libera IA para 185 mil e mira €200 mi em 2026: https://www.letsmoney.com.br/noticias/santander-libera-ia-185-mil-funcionarios-200-milhoes/
- TI Inside — PagBank lança Minizinha Voz (1ª maquininha com assistente de vendas por IA): https://tiinside.com.br/27/01/2026/pagbank-lanca-minizinha-voz-primeira-maquininha-do-brasil-com-assistente-de-vendas-por-inteligencia-artificial/
- Mobile Time — PagBank lança POS com IA e comando de voz: https://www.mobiletime.com.br/noticias/02/02/2026/pagbank-minizinha-voz/
- SocialHub — Cobrança WhatsApp + Stone (11 mi+ clientes, taxas): https://www.socialhub.pro/blog/cobranca-whatsapp-stone-pagamentos-maquininha-antecipacao-recebivel-pme-varejo-2026/
- Stone — Agentic commerce (posicionamento): https://conteudo.stone.com.br/agentic-commerce/
- Vanquish — Pix virou trilho de agentes de IA (Iniciador, Open Finance): https://www.vanquish.com.br/blog/pix-agentes-ia-iniciador-open-finance
- Antecipa Fácil — Caixa Tem 2026 (130 mi+ usuários, Pix): https://antecipafacil.com.br/artigo/caixa-tem-2026-guia-completo-como-usar-saldo-pix
- CAIXA — Pix Automático (recorrência por autorização única): https://www.caixa.gov.br/empresa/pagamentos-recebimentos/recebimentos/pix-automatico/Paginas/default.aspx

**Liga com:** [[De-Para — Pagamentos & Pix]] (piloto) · [[De-Para — Originação de crédito (Fase 2 · expansão)]] · [[De-Para — Onboarding & KYC (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[TPL-Iniciativa-IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[Placar VALE — Priorizacao de Iniciativa de IA]]
