---
tipo: ideia
data: 2026-09-03
status: crua
origem: auto-digest
fonte_daily: "[[2026-09-03]]"
eixos: [agentes, governanca, soberania, financeiro]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Governança de agente vem antes do piloto, não depois — o Bradesco pôs identidade e observabilidade antes do Ato 3, invertendo a ordem de 90% do mercado

## A tese
O número que importa na entrevista do Bradesco não é o 20x de produtividade — é de **sequência**: identidade não humana (non-human identity) e observabilidade agêntica foram colocadas como pré-requisito de escala, *antes* da autonomia ponta a ponta, não como camada que se adiciona quando o auditor pergunta. Isso inverte a ordem em que a maioria opera — piloto primeiro, governança depois. A tese defensável: em agente, quem trata governança como fase posterior não vai escalar; a estrutura (identidade + observabilidade + critério de promoção) é o que separa os <10% que escalam do resto.

## Por que eu acredito nisso
Francesco Di Marcello (CIO do Bradesco) descreveu ao TI INSIDE, pós-Febraban Tech, dois componentes como base para sustentar autonomia: **identidade não humana** (cada agente com autenticação, permissão e auditoria próprias) e **observabilidade agêntica** (rastreia contexto usado, decisão tomada e impacto). A frase-âncora: *"Se no dia 1 não tivermos o 'RH dos agentes', o risco de proliferação é muito alto"* (TI INSIDE, 01/09 e 26/08/2026). O dado da biblioteca sustenta: a McKinsey/QuantumBlack (*Building the foundations for agentic AI at scale*, abr/2026) mostra que **quase 2/3 das empresas experimentaram agentes e menos de 10% escalaram** (pág 1-2) e nomeia *identity management* como pré-requisito com governança federada — domínio governa o dia a dia, centro mantém guardrails (pág 9). E no *2026 Global AI Report* da NTT DATA, **32,5% dos líderes** já atribuem o risco de IA diretamente ao CAIO (pág 24-25): o "RH de agentes" precisa de um dono com cadeira.

## Quem discordaria — e por quê
Dois contrapontos sérios. Primeiro, o pragmático de produto: multiplicador anunciado em palco de Febraban Tech é marketing de talento, não medição — "5 a 20x" sem custo de inferência, sem taxa de retrabalho e sem baseline é fé, e governança-primeiro pode virar exatamente o comitê burocrático que a IA veio matar ("RH de agentes" como cartório). Segundo, o defensor do piloto-primeiro: você só descobre o que precisa governar depois de rodar; instrumentar antes é over-engineering que trava o aprendizado. Ambos valem — e por isso a tese não é sobre o número, é sobre a **estrutura mínima** que evita proliferação sem dono, não sobre erguer um comitê antes de qualquer agente rodar.

## O que eu faria / recomendaria
Separar "governança-primeiro" de "burocracia-primeiro": o pré-requisito não é comitê, são três artefatos técnicos por agente em produção — identidade própria (não a credencial compartilhada do serviço que o hospeda), log de decisão (contexto + decisão + impacto, não só a chamada ao modelo) e critério escrito de promoção de "humano aprova" para "autônomo". A primeira e a terceira são o núcleo do **Cohort** (mandato, escopo, promoção a produção); a segunda é o que o **Veltrix** instrumenta por chamada, por jornada e por jurisdição. Leitura de soberania: identidade não humana é o pré-requisito para dizer *qual agente* tocou *qual dado* em *qual jurisdição* — sem ela, residência de dado é declaração, não controle.

## Lastro
- [[2026-09-03]] — leitura de hoje (Bradesco, agente no organograma)
- [TI INSIDE · 01/09/2026](https://tiinside.com.br/01/09/2026/bradesco-ve-times-hibridos-de-humanos-e-agentes-como-o-futuro-da-tecnologia/) · [TI INSIDE · 26/08/2026](https://tiinside.com.br/26/08/2026/bradesco-amplia-uso-de-agentes-de-ia-e-registra-ate-20-vezes-mais-produtividade/)
- Biblioteca: McKinsey/QuantumBlack · *Building the foundations for agentic AI at scale* (abr/2026), pág 1-2 e 9 · NTT DATA · *2026 Global AI Report — Banking & Financial Services*, pág 24-25
- Relacionadas: [[Agente sem data de expiracao e passivo permanente - falta RH ao agent estate]] · [[No agentico a decisao de board nao e adotar agentes e desenhar a curva de autonomia]] · [[Contar agentes e vaidade - o numero de board e quantos tem mandato e quem orquestra]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** agentes/governança + soberania  ·  **Setor:** Financeiro
