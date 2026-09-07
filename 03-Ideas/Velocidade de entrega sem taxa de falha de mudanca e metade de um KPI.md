---
tipo: ideia
data: 2026-09-05
status: crua
origem: auto-digest
fonte_daily: "[[2026-09-05]]"
eixos: [economia-ia, financeiro, governanca, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Velocidade de entrega sem taxa de falha de mudança é metade de um KPI — e a metade que falta é a que a auditoria pede

## A tese
Quando um banco anuncia "-88% no tempo de entrega" e não publica a taxa de falha de mudança (change failure rate), ele reportou lead time, não produtividade — e entregou ao board metade de um KPI. A metade que falta não é detalhe técnico: é exatamente a coluna que a auditoria vai cobrar em 2027, porque é a única das quatro métricas DORA que mede qualidade, não velocidade.

## Por que eu acredito nisso
O C6 anunciou no AWS Summit -88% no tempo de entrega com IA agêntica (Kiro + Bedrock): produto novo de 8-10 sprints para 1, compliance regulatório de 2 meses para 8 dias (Let's Money · 04/09; TI Inside · 03/09). A B3, com método mais sóbrio (só trechos aceitos, revisão humana mantida), fala em -35% (Let's Money · 04/09). O AI Index 2026 mede 14% a 26% de ganho em desenvolvimento de software em estudos controlados (Stanford HAI, pág 10). A barra encolhe conforme o método aperta — e nenhuma das quatro medições traz a taxa de falha ao lado. A distância entre 26% e 88% não é fraude: é a diferença entre *tempo de entrega* (cai quando o gargalo era espera) e *produtividade* (sobe quando o trabalho fica melhor). São coisas diferentes, e o board precisa saber qual está comprando.

## Quem discordaria — e por quê
Para um banco em fase de crescimento (C6, 42 mi de clientes, R$ 1,25 bi de lucro no 1S26), velocidade *é* a economia: cada mês a menos de time-to-market é receita antecipada, e cobrar taxa de falha de um número de crescimento seria burocratizar o que está funcionando. Aceito o ponto — mas então que o número apresentado seja receita antecipada em reais, não percentual de tempo. Percentual de tempo sem denominador de qualidade continua sendo meio KPI, mesmo para quem cresce.

## O que eu faria / recomendaria
One-pager com as **quatro colunas que faltaram no release do C6**: (1) lead time antes/depois, (2) taxa de falha de mudança antes/depois, (3) custo de inferência por entrega — a conta do Bedrock que o release não menciona, e que o Veltrix mede por tarefa (método CARO), (4) quem revisou o quê: humano, agente ou os dois. Isso muda a conversa com um cliente que negocia com AWS/Google/Microsoft de "quanto mais rápido" para "quanto mais seguro por real gasto". É a coluna de qualidade que falta na régua [[Regua de Produtividade Agentica (BIH) - Baseline, Inferencia, Human-in-the-loop]] — vale considerar promovê-la a uma quarta letra.

## Lastro
- Let's Money · 04/09/2026 — [C6 Bank -88% com Kiro/AWS](https://www.letsmoney.com.br/noticias/c6-bank-kiro-aws-88-tempo-entrega/)
- TI Inside · 03/09/2026 — [C6 Bank reduz 88% no tempo de entrega](https://tiinside.com.br/03/09/2026/c6-bank-reduz-em-88-o-tempo-de-entrega-de-projetos-com-ia-agentica-da-aws/)
- Let's Money · 04/09/2026 — [B3 oficializa Cursor: -35%](https://www.letsmoney.com.br/noticias/b3-cursor-ia-oficial-engenharia/)
- Stanford HAI · *AI Index Report 2026*, pág 10 (14-26% em dev de software)
- *The Age of Co-Intelligence* (mar/2026), pág 19 (~2/3 da produtividade vira economia direta, 1/3 é cost avoidance)
- Relaciona: [[ROI de IA na engenharia sem proveniencia troca divida visivel por invisivel]] · [[Demonstracao de Resultado de IA (VCAT) - Valor, Custo, Atribuicao, Trilha]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** economia-ia / FinOps  ·  **Setor:** financeiro (engenharia bancária)
