---
tipo: ideia
data: 2026-09-04
status: crua
origem: auto-digest
fonte_daily: "[[2026-09-04]]"
eixos: [soberania, financeiro, governanca]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 O conector em assistente de terceiro empilha dependência de distribuição sobre a de inferência — nos mesmos dois fornecedores

## A tese
Até ontem a concentração do banco em OpenAI/Anthropic era de **inferência** (o banco escolhe o modelo, o dado vai por API com contrato). Com o conector do PicPay em Claude e ChatGPT, surge uma segunda dependência sobre os **mesmos dois fornecedores**: a de **distribuição** — o cliente escolhe o assistente e o dado bancário vai por OAuth, sob a política de privacidade do plano do cliente, sem contrato corporativo por trás. Ligar canal de cliente e motor de inferência no mesmo endereço não é feature; é decisão de arquitetura de distribuição.

## Por que eu acredito nisso
O report CCAF/Cambridge com WEF, BIS, FMI e BID (abr/2026, 628 organizações, 151 jurisdições) mostra que **63% da indústria financeira já roda workflows internos sobre foundation model externo — OpenAI 76%, Google 57%, Anthropic 35%, DeepSeek 15%** (pág 7-8). O PicPay acabou de plugar o *canal de cliente* nos dois primeiros dessa lista, quinze dias depois de fazer o mesmo no ChatGPT. Privacidade e proteção de dados já é o risco nº 1 para **74% da indústria e 80% dos reguladores** (pág 9). A frase de controle é do próprio Let's Money: movimentar dinheiro "não está no escopo" — *ainda*; quem decide quando consulta vira transação é o roadmap de conectores do fornecedor, não o do banco.

## Quem discordaria — e por quê
O mesmo aconteceu com app stores e ninguém saiu da Apple — distribuição concentrada é o normal do digital, e o conector é leitura-apenas, autenticado, com biometria. Contraponto honesto e forte. A diferença que sustenta a tese: **a Apple não lê o extrato.** Aqui o fornecedor que distribui é o mesmo que infere sobre 12 meses de transação para responder "quanto gastei com delivery?" — e inferência sobre dado transacional é finalidade nova sob LGPD, não a "consulta" consentida.

## O que eu faria / recomendaria
Tratar conector em assistente de terceiro como decisão de arquitetura, com três perguntas antes do go-live: (1) **qual dado sai** — só o campo respondido ou o histórico que o modelo precisa ler? (2) **onde roda a inferência** e sob que contrato de residência? (3) **quem decide** quando consulta vira transação, e existe mandato escrito com limite de valor/contraparte/horário? A (2) é o roteamento por jurisdição que o **Veltrix** faz por chamada; a (3) é o mandato de agente do **Cohort**. Sem as duas, o conector é um canal que o banco não governa. Estrutura na nota-irmã [[Grade de Governanca de Conector em Assistente de Terceiro (DIM) - Dado, Inferencia, Mandato]].

## Lastro
- CCAF/Cambridge + WEF/BIS/IMF/BID · *The 2026 Global AI in Financial Services Report* (abr/2026), pág 7-8 e 9
- [Let's Money · 03/09 — PicPay integra Claude](https://www.letsmoney.com.br/noticias/picpay-integracao-claude-anthropic/)
- Relacionadas: [[Assistente de big tech plugado no Open Finance - onde reside o dado]] · [[Controle de dado vira alavanca de conversao no assistente financeiro]] · [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** soberania  ·  **Setor:** financeiro (banking AI-native)
