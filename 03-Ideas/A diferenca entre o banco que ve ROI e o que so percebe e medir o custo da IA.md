---
tipo: ideia
data: 2026-07-17
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-17]]"
eixos: [economia-ia, financeiro, governanca]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 A diferença entre o banco que vê ROI e o que só percebe não é quanto gasta — é se sabe quanto a IA lhe custa

## A tese
"Percepção de ROI" sem baseline de custo de inferência é fé, não FinOps. O indicador que o board comemora — percepção de retorno subindo — é autorrelato, e autorrelato de ROI sem o custo de servir o modelo no denominador mede entusiasmo, não retorno. **A diferença entre o banco que vê ROI e o que só o percebe não é quanto gasta em IA — é se sabe quanto a IA lhe custa.** Enquanto o setor reportar sentimento, estará medindo o numerador e chutando o denominador.

## Por que eu acredito nisso
O dado de humor da **Pesquisa Febraban de Tecnologia Bancária 2026 (34ª ed., Deloitte, jun/2026)** é o mais perigoso do levantamento: a **percepção de ROI de IA subiu 14 pontos percentuais** entre os bancos BR — no mesmo ano em que o gasto específico em IA somou **R$ 826 mi (+39% sobre os R$ 596 mi de 2024)**, dentro de **R$ 50,4 bi previstos em tech para 2026 (+8%)**. Percepção é sentimento; R$ 826 mi é input; ROI de verdade é a razão entre os dois — com o custo de servir no denominador, que ninguém consolida.

O contraste com a biblioteca fecha o argumento. O **MIT (*Culture Eats AI for Breakfast*, pág. 5)** mede a lacuna exata entre *sentir* e *provar*: **95% das organizações veem zero retorno mensurável de IA**. E o **NTT DATA (*Banking AI Leaders' Playbook 2026*, pág. 4)** mostra onde o retorno de fato aparece: **84,1% dos que alinham estratégia de IA e de negócio reportam ≥5% de uplift de lucro** — em quem tem disciplina de medição, não em quem só investe. No pano de fundo global, o CEO da Zafin (Charbel Safadi, via Sam Boboev, 17/07) diz em linguagem de fintech o mesmo que o MIT: o gargalo de ROI não é o modelo, é a arquitetura de produto/dado — com o **JPMorgan gastando US$ 2 bi/ano** como o maior autorrelato de ROI do mundo, e o mais difícil de auditar.

## Quem discordaria — e por quê
O head de negócio, com razão parcial: percepção positiva não é ruído — ela reflete ganhos operacionais reais (atendimento, código, antifraude) que o board vê no dia a dia. Verdade, e eu diria isso em voz alta. Mas ganho operacional *percebido* não é ROI; ROI é ganho **menos** o custo total de servir o modelo, e é justamente esse custo que ninguém mede com rigor. O CFO ainda argumentaria que o custo de inferência está diluído em cloud/software e é impraticável isolar — contraponto honesto, mas que descreve o problema, não o resolve: sem isolar o denominador, "ROI" continua sendo produtividade percebida com outro nome.

## O que eu faria / recomendaria
Levar ao comitê uma pergunta de uma linha que separa fé de FinOps: **"qual é o nosso custo de inferência por caso de uso, e o ROI que reportamos é ganho bruto ou ganho líquido desse custo?"** Se a resposta for "reportamos produtividade percebida", o diagnóstico está feito. Pedir que o próximo report de IA ao board troque *percepção de ROI* por **ROI medido** em pelo menos um caso de uso — um único caso auditado vale mais que dez percepções. É exatamente o denominador que a **Veltrix** instrumenta (custo por token/rota/jurisdição, ROI auditável em vez de percebido). E o timing ajuda: com o Kimi K3 chegando a 40% do preço da classe Opus 4.8, o custo do numerador vai cair — mas só quem mede o denominador transforma essa queda em margem.

## Lastro
- Febraban/Deloitte — 34ª Pesquisa de Tecnologia Bancária 2026 (jun/2026): R$ 50,4 bi tech (+8%); IA R$ 826 mi (+39%); percepção de ROI +14pp; prioridades cyber 100% / cloud 84% / IA 84%. (IT Forum · Forbes Brasil)
- MIT — *Culture Eats AI for Breakfast*, pág. 5: 95% com zero retorno mensurável.
- NTT DATA — *Banking AI Leaders' Playbook 2026*, pág. 4: 84,1% dos que alinham reportam ≥5% de uplift de lucro.
- Sam Boboev / Fintech Wrap Up — Charbel Safadi (CEO, Zafin), 17/07/2026: gargalo é arquitetura, não modelo; JPMorgan US$ 2 bi/ano.
- Vizinhas no vault: [[A maturidade em IA nao se mede em orcamento nem em pilotos - se mede no custo marginal do proximo caso de uso]] (lá a régua é *custo marginal do próximo caso*; aqui é *medir o denominador* de um caso que já roda) · [[A escala chegou a conta ninguem reporta - custo por inferencia e o ponto cego do agent estate]] · [[Regua de Produtividade Agentica (BIH) - Baseline, Inferencia, Human-in-the-loop]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** economia-ia / governança  ·  **Setor:** financeiro (bancos BR)
