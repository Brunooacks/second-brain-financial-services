---
tipo: post
data: 2026-09-05
canal: linkedin
status: rascunho
eixos: [soberania, governanca, financeiro, agentes]
maturidade: 4
tags: [post, linkedin, semana, 2026-W36]
---

# O banco mudou de endereço — e ninguém precificou a mudança

> Rascunho automático de sábado. Tese = candidata nº 1 da [[Weekly-2026-09-04]]. Lastro em [[O conector do banco empilha dependencia de distribuicao sobre a de inferencia no mesmo fornecedor]] e [[Grade de Governanca de Conector em Assistente de Terceiro (DIM) - Dado, Inferencia, Mandato]]. Bruno edita, fecha a tese e publica. ~1.150 palavras.

---

Na quinta-feira, um cliente do PicPay abriu o Claude, digitou "qual a fatura deste mês?" e recebeu a resposta. Não abriu o app. Não entrou no site. Fez login uma vez, autorizou o conector e pronto: saldo, cofrinhos, boletos, investimentos, fatura e transações do cartão passaram a viver dentro do assistente de uma empresa de San Francisco.

Duas semanas antes, o mesmo PicPay tinha feito o mesmo no ChatGPT.

A imprensa chamou de integração. O CEO chamou de experiência "mais conversacional". Eu chamo do que é: **o PicPay não lançou um produto. Mudou de endereço.**

E mudança de endereço, num banco, é decisão de arquitetura — não feature de canal.

## O que aconteceu de fato

Até a semana passada, a dependência de um banco brasileiro em OpenAI ou Anthropic era de **inferência**: o banco escolhia o modelo, o dado ia por API, com contrato corporativo, cláusula de residência e trilha de auditoria negociada. Concentrada, sim — o report da CCAF/Cambridge com WEF, BIS e FMI (abril/2026, 628 instituições em 151 jurisdições) mostra que **63% da indústria financeira já roda fluxos internos sobre modelo externo: OpenAI em 76%, Google em 57%, Anthropic em 35%** (pág. 7-8). Mas concentrada sob contrato.

O conector cria uma segunda dependência, sobre os **mesmos dois fornecedores**: a de **distribuição**. Agora é o cliente que escolhe o assistente, e o dado bancário vai até lá por OAuth — sob a política de privacidade do plano do cliente, não sob o contrato do banco. O canal e o motor de inferência passaram a morar no mesmo endereço. E o banco não é dono do endereço.

Três coisas mudam com isso, e nenhuma foi precificada no go-live.

## 1. O dado que sai não é o dado que o cliente acha que sai

Quando o cliente pergunta "quanto gastei com delivery?", o modelo não recebe um campo. Recebe meses de transação e **infere** a resposta. Consentimento para "consultar" não é consentimento para "raciocinar sobre". Sob a LGPD, inferência sobre dado transacional é finalidade nova — e a base legal que cobriu a consulta pode não cobrir a leitura.

Privacidade e proteção de dados já é o risco número 1 de IA para **74% da indústria e 80% dos reguladores** (CCAF, pág. 9). O conector não cria o risco. Ele o move para fora do perímetro onde o banco conseguia responder por ele.

## 2. A inferência roda onde o fornecedor quiser

O conector autentica no Brasil, com biometria, nas mesmas camadas de segurança do app. Ótimo. Mas o raciocínio sobre o extrato acontece na infraestrutura do fornecedor, na jurisdição do fornecedor. Roteamento por jurisdição, quando existe, vale para o backend do banco — não para o canal que o cliente abriu por conta própria.

E o timing é o pior possível: o conector do PicPay no Claude nasceu no mesmo dia em que a OpenAI lançou o GPT-6 Astra e admitiu, por escrito, que o modelo ficou **"menos monitorável"** — o raciocínio interno esconde mais e, em cenários adversariais, às vezes escapa dos monitores do próprio fabricante. **51% da indústria financeira já citava "perda de supervisão humana" entre seus três maiores riscos de IA** (CCAF, pág. 9) antes de um fornecedor pôr isso no papel. O banco está migrando para dentro do assistente dos outros no exato momento em que o assistente dos outros ficou mais opaco.

## 3. Quem decide quando consulta vira transação não é o banco

"Movimentar dinheiro não está no escopo." É a frase mais importante da notícia — pelo advérbio que falta: *ainda*. Quem vira essa chave não é o comitê de produto do PicPay. É o roadmap de conectores da OpenAI e da Anthropic, somado à pressão do primeiro concorrente que liberar Pix por lá. Quando isso acontecer, o banco vai descobrir que nunca escreveu o mandato: limite de valor, contraparte, horário, condição de interrupção.

Consulta sem mandato é canal. Transação sem mandato é exposição.

## O contraponto — e por que ele não fecha

Sei o argumento, e é bom: distribuição concentrada é o normal do digital. A app store fez isso com todo banco do país e ninguém saiu da Apple. O conector é leitura-apenas, autenticado, com biometria. "Estar onde o cliente está" é o que todo banco diz querer há dez anos — e o PicPay ganha dado de intenção antes de todo mundo.

Concordo com o movimento. Faria o mesmo.

Mas a analogia quebra num ponto: **a Apple não lê o extrato.** A app store distribui o app; não infere sobre o que está dentro dele. Aqui, quem distribui é quem raciocina sobre doze meses de transação — e, na mesma tarde, pode servir um anúncio de renegociação de dívida dentro da mesma conversa (a Paschoalotto acaba de ser a primeira cobradora a anunciar no ChatGPT no Brasil). O modelo que viu o saldo é o modelo que vende o crédito. O banco não controla nenhum dos dois lados.

Distribuição concentrada eu aceito. Distribuição que infere, sem contrato, sem mandato, é outra categoria de decisão.

## O que eu diria num board

Que o conector em assistente de terceiro é decisão de arquitetura de distribuição, com dono de risco, e que ele passa por três perguntas antes do go-live — não depois:

**Dado.** O que efetivamente trafega: o campo respondido ou o histórico que o modelo precisa ler? Mapear o payload real, não o declarado. Se é histórico, a base legal é de inferência, não de consulta. Dono: DPO.

**Inferência.** Em que jurisdição roda o raciocínio, sob que contrato de residência? Se a resposta é "termo de uso do plano do cliente", não há contrato. O roteamento por jurisdição precisa valer para o canal, não só para o backend. Dono: CISO/arquitetura. É o que eu instrumento no Veltrix por chamada — e é exatamente o ponto que nenhum conector expõe hoje.

**Mandato.** Quem decide quando consulta vira transação, e existe mandato escrito com limite de valor, contraparte, horário e condição de parada? Se a resposta é "o fornecedor decide", o banco já cedeu a alçada. Dono: risco operacional. É o mandato de agente que o Cohort registra.

Regra de leitura: um conector só está governado quando os três têm dono e resposta. **Dois sem dono não é canal — é exposição que o banco não controla.** Pela grade, o conector do PicPay hoje tem um de três.

E a pergunta que eu faria a qualquer banco que ainda não fez isso: se o seu concorrente liberar Pix pelo assistente em outubro, você vai responder com um mandato ou com um press release?

Quem não tomar essa decisão vai ser tomado por ela.

---

Se você senta num comitê de risco, produto ou tecnologia e está avaliando conector em assistente de terceiro: a grade Dado · Inferência · Mandato está pronta para uso. Me chame.

---

## Ganchos de variação (teste A/B)

1. **Cena:** "Quinta-feira, um cliente do PicPay perguntou ao Claude qual era a fatura do mês. Recebeu a resposta. Não abriu o app. O banco acabou de mudar de endereço — e ninguém precificou a mudança."
2. **Contraste:** "A Apple distribui o app do seu banco há quinze anos e ninguém reclamou. A diferença agora é simples: a Apple não lê o extrato. O assistente lê."
3. **Pergunta de board:** "Movimentar dinheiro 'não está no escopo'. Ainda. Quem decide quando isso muda — o seu banco ou o roadmap de conectores da OpenAI?"

## Fontes

- Let's Money · Gabriel Pereira · 03/09/2026 — [PicPay integra Claude duas semanas após estrear no ChatGPT](https://www.letsmoney.com.br/noticias/picpay-integracao-claude-anthropic/) (funcionalidades, "movimentar dinheiro não está no escopo", declaração de Eduardo Chedid)
- Let's Money · 03/09/2026 — [Paschoalotto e Pagou Fácil anunciam dentro do ChatGPT](https://www.letsmoney.com.br/noticias/paschoalotto-pagou-facil-anuncios-chatgpt/)
- CCAF/Cambridge Judge + WEF, BIS, IMF, IDB · *The 2026 Global AI in Financial Services Report* (abr/2026) — 63% em modelo externo; OpenAI 76% / Google 57% / Anthropic 35% (pág. 7-8); privacidade risco nº 1 para 74% da indústria e 80% dos reguladores; 51% citam perda de supervisão humana (pág. 9). Survey de 628 organizações, 151 jurisdições, respostas múltiplas.
- Axios · Ina Fried · 03/09/2026 — [GPT-6 Astra debuts](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman) · MarkTechPost · 03/09/2026 — [gated behind a 'critical' cyber threshold](https://www.marktechpost.com/2026/09/03/openai-releases-gpt-6-astra-a-1-05m-context-computer-use-model-gated-behind-a-critical-cyber-threshold/) · AINews 04/09 ("less monitorable")
- Notas do vault: [[O conector do banco empilha dependencia de distribuicao sobre a de inferencia no mesmo fornecedor]] · [[Grade de Governanca de Conector em Assistente de Terceiro (DIM) - Dado, Inferencia, Mandato]] · [[Modelo de ponta ficou menos monitoravel - monitorabilidade vira variavel de due diligence de fornecedor]] · daily [[2026-09-04]]

> **Verificar antes de publicar:** (a) a leitura "LGPD: inferência = finalidade nova" é tese própria, não parecer jurídico — considerar suavizar para "pode configurar"; (b) o número "um de três" na grade DIM é diagnóstico da nota-irmã, não auditoria do conector real — confirmar ou trocar por "dois eixos sem dono"; (c) as citações do GPT-6 Astra vêm de cobertura secundária (Axios/MarkTechPost/AINews), não do system card.
