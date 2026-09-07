---
tipo: ideia
data: 2026-08-23
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-23]]"
eixos: [financeiro, governanca, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 O próximo ciclo de antifraude não é outro score transacional — é instrumentar a camada de decisão

## A tese
A fraude que mais cresce no Brasil não deixa anomalia técnica: o dispositivo é o do cliente, a geolocalização é a habitual, o horário é normal, a biometria comportamental confere — porque quem digitou foi o titular. Todo o arsenal antifraude transacional comprado nos últimos cinco anos é, **por construção**, cego para essa categoria. Não é falha de implementação; é o modelo funcionando como foi desenhado para um problema que mudou de endereço. Por isso o próximo investimento não é mais um score sobre a transação — é **instrumentar a camada de decisão: registrar o contexto em que a autorização foi dada, não só o fato de que foi dada.** Quem tiver isso vai distinguir, em juízo, "o cliente autorizou" de "o cliente foi induzido a autorizar". Quem não tiver, paga as duas.

## Por que eu acredito nisso
O dado de ontem: engenharia social respondeu por **40%** dos indícios de fraude financeira do Brasil no 1º semestre de 2026 — **3,6 milhões de 9 milhões** de indícios, alta de **10,26%** sobre o 2º sem/2025 (Quod, via [Agência Brasil/EBC, 22/08/2026](https://agenciabrasil.ebc.com.br/geral/noticia/2026-08/engenharia-social-responde-por-40-das-fraudes-financeiras-no-brasil)). O golpe entra pelo **celular em 78%** dos casos e movimenta pelo **Pix em 85%**. Do lado da defesa, o levantamento EY+IIF (**101 bancos, 31 países**) mostra o setor organizado na camada mais fácil de medir: **75%** planejam IA antifraude, mas **80%** travam em qualidade de dados e só **12%** colhem valor em produção ([Let's Money, 09/07/2026](https://www.letsmoney.com.br/noticias/bancos-ia-crimes-financeiros/)). E o vetor está piorando: a IA já joga do lado do atacante (clonagem de voz, imagem, documento falso). José Oliveira (CTO da Certta) faz o corte: *"engenharia social ataca a decisão humana; a fraude ataca o sistema, o documento, a identidade — são camadas diferentes"*. A parte que ninguém colocou no slide do Febraban Tech: **quando o agente autônomo entra em produção executando pagamento em nome do cliente, essa camada ganha um segundo alvo** — hoje o golpista precisa convencer uma pessoa; amanhã pode convencer uma pessoa a *instruir um agente*, que executa sem a fricção residual de quem hesita antes de confirmar. Tratamos "human-in-the-loop" como controle de segurança; o dado diz que o humano no loop é o componente com a **maior taxa de comprometimento** da cadeia — o oposto do que se supõe em [[Human-in-the-loop indiscriminado virou passivo de liquidez no pagamento agentico]].

## Quem discordaria — e por quê
Dois contrapontos legítimos. **(1)** Engenharia social é problema de educação do consumidor, não de arquitetura — e o próprio Certta/Nexus mostra que só **11%** das menções sobre golpes nas redes tratam de prevenção; o banco não controla a cultura. **(2)** Os **12%** da EY podem ser simples imaturidade de curva de adoção, não falha estrutural — três anos atrás o número seria zero. Aceito os dois. Mas nenhum muda quem paga: com **85%** dos golpes no Pix e o MED já rodando **~2,7–2,8 milhões** de pedidos por mês, o prejuízo e o passivo jurídico estão no balanço da instituição, não na educação do titular. Educar reduz incidência; não redistribui responsabilidade.

## O que eu faria / recomendaria
Parar de comprar o próximo score transacional e começar a instrumentar **o estado da decisão**: para toda autorização de risco, registrar quem instruiu, sob que contexto, com que mandato e com que limite — o suficiente para reconstruir, depois do fato, se houve autorização ou indução. É onde meus dois produtos se encaixam: o **Cohort** escreve o mandato do agente pagador (qual agente, sobre qual dado, autorizado por quem, com que teto) e o **Veltrix** fecha o lado técnico (qual modelo respondeu, a que custo, em qual jurisdição). Métrica de board: **% de autorizações de risco com trilha de contexto reconstruível vs. % que só registram o fato**. Sem essa trilha, "liderança humana" é slogan de palco, não controle auditável.

## Lastro
- [Agência Brasil/EBC — Engenharia social responde por 40% das fraudes financeiras no Brasil (22/08/2026)](https://agenciabrasil.ebc.com.br/geral/noticia/2026-08/engenharia-social-responde-por-40-das-fraudes-financeiras-no-brasil) *(pesquisa Quod; Certta/Nexus)*
- [Let's Money — EY/IIF, 101 bancos, 31 países (75% / 80% / 12%)](https://www.letsmoney.com.br/noticias/bancos-ia-crimes-financeiros/)
- Aprendizado do dia [[2026-08-23]]: APP fraud (Authorized Push Payment) — a fraude que a vítima autoriza; sinal está *fora* da transação
- Notas relacionadas: [[Human-in-the-loop indiscriminado virou passivo de liquidez no pagamento agentico]] · [[O regulador virou operador de modelo - o diferencial antifraude migra do score]] · [[Verifiable Intent - quem arbitra a disputa do agente define quem paga a fraude]] · [[Antifraude comportamental e cego ao cliente que nunca existiu]] · [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança e risco (antifraude / agentes)  ·  **Setor:** financeiro (Pix / APP fraud)
