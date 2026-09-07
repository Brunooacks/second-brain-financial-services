---
tipo: ideia
data: 2026-08-22
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-21]]"
eixos: [financeiro, governanca, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Quando o agente constrói o modelo de crédito, o objeto regulado deixa de ser o modelo e passa a ser o processo que o produz

## A tese
A Avaliação de Impacto Algorítmico (AIA) que descreve só o modelo de crédito final está descrevendo metade do sistema. Quando um agente de IA participa da **construção** do modelo — seleção de variável, tratamento de dado incompleto, engenharia de atributos (*feature engineering*), documentação —, o item regulado migra do artefato para a fábrica. E há um custo escondido no ganho de produtividade que ninguém colocou em slide: acelerar a criação de modelo colapsando dez especialistas em um reduz na mesma proporção o número de pessoas capazes de **testemunhar** como aquele modelo foi construído — e em auditoria e processo administrativo, testemunha importa.

## Por que eu acredito nisso
O Bradesco aplicou arquitetura agêntica à criação de modelos de estimativa de renda no **RendaBRA 5.0**: o processo ficou **16x mais rápido** e passou a ser feito por **1 especialista em vez de 10**, inclusive com informação incompleta (Startups/inovabra, 14/08/2026). Isso é uma redução de ~**90% no número de pessoas que sabem como o modelo nasceu**. Do outro lado do calendário, o **PL 762/2026** exige **certificação e registro prévios** para IA de crédito, com **12 meses** de adaptação após publicação (Plugged Ninja, 09/07/2026). Certificar previamente um sistema construído por agentes obriga, inevitavelmente, a descrever os agentes — não só a saída deles. O detalhe que fecha o argumento: o próprio Bradesco fez o certo — a **AgentiX** roda em plataforma própria mas **delega identidade, segurança e auditoria à Bridge** (600+ casos de uso desde abr/2024), ou seja, o rastro existe por desenho. A maioria dos bancos não tem esse rastro no ciclo de vida do modelo.

## Quem discordaria — e por quê
Um head de risco de modelo diria que nenhum regulador do mundo impôs AIA de *processo* — a obrigação sempre recaiu sobre o modelo e sua saída —, e que exigir descrição dos agentes que o construíram é sobre-especificação. Ponto justo. Mas "nenhum regulador impôs ainda" é uma janela, não uma defesa: o PL 762 fala em **certificação prévia**, e não se certifica previamente aquilo que não se descreve. Também discordaria quem diz que o rastro da Bridge já resolve — resolve para quem tem uma Bridge; a tese é sobre os que não têm.

## O que eu faria / recomendaria
Antecipar o inventário — mas não o inventário de modelos, que todo banco já tem. O inventário de **onde há agente dentro do ciclo de vida de modelo regulado**. Levar uma pergunta única ao time de risco de modelo: *quais dos nossos modelos em produção tiveram agente de IA em alguma etapa da construção?* Se a resposta for "não rastreamos", esse é o item mais caro do backlog de conformidade. É exatamente o registro que o **Cohort** mantém — mandato do agente por etapa, com trilha e alçada de promoção — e a outra metade da pergunta que o **Veltrix** responde: quanto custou e sob que jurisdição rodou cada chamada que produziu aquele modelo.

## Lastro
- [Startups / inovabra, 14/08/2026 — Bradesco, RendaBRA 5.0 / AgentiX / Bridge](https://startups.com.br/branded-content/bradesco-e-reconhecido-no-premio-valor-inovacao-2026/)
- [Convergência Digital — Bradesco tem agentes IA em todos os lugares](https://convergenciadigital.com.br/governo/bradesco-tem-agentes-ia-em-todos-os-lugares/)
- [Plugged Ninja, 09/07/2026 — PL 762/2026: certificação prévia para IA de crédito](https://www.plugged.ninja/2026/07/pl-762-2026-pl-704-2026-anpd-fiscalizacao-ia-brasil-pl-2338-julho/)
- Relacionadas: [[Explicabilidade de credito virou requisito de arquitetura, nao compliance]] (lá o objeto é a *decisão* de crédito; aqui é o *processo* que constrói o modelo) · [[ROI de IA na engenharia sem proveniencia troca divida visivel por invisivel]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança  ·  **Setor:** financeiro
