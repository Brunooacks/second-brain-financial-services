---
tipo: framework
data: 2026-09-02
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-09-02]]"
eixos: [financeiro, agentes, governanca]
tags: [framework, auto]
---

# 🧱 Matriz de Exposição à Portabilidade Agêntica (ESR) — Exposição, Sobrevivência, Retenção

## O problema que ele resolve
Quando a portabilidade de crédito unificada (agenda do BC/Fazenda) encontra o agente com mandato de otimização, o risco não é "perder o cliente" — é perder **spread**, carteira a carteira, sem que ninguém no comitê tenha medido a exposição. O comitê de IA não faz a pergunta; o de crédito não sabe que ela existe. Falta uma métrica que traduza "meu agente pode portar" em número de balanço.

## O framework
Para cada carteira de crédito, três eixos:

- **E — Exposição:** ticket médio × spread × volume. Quanto de margem está no book. É o que está em jogo.
- **S — Sobrevivência:** que fração desse spread sobrevive a um agente que compara N ofertas por semana. Produto comoditizado e comparável (consignado, financiamento padrão) tem sobrevivência baixa; produto com garantia complexa ou bundling tem alta.
- **R — Retenção:** qual a fricção **comercial** real que segura o cliente — garantia cruzada, relacionamento, switching cost contratual. É a única defesa que **não** é cognitiva; a fricção cognitiva o agente dissolve.

Leitura: **Exposição alta × Sobrevivência baixa × Retenção baixa = carteira que o agente porta primeiro.** É onde o spread evapora sem aviso.

## Quando usar / quando NÃO usar
Usar para priorizar defesa de carteira diante da portabilidade automatizada e para dimensionar mandato de agente próprio (o que o meu agente pode portar para dentro). NÃO usar como previsão de churn de curto prazo — hoje o volume de portabilidade ainda é baixo; a matriz mede **exposição estrutural**, não fluxo do trimestre.

## Aplicado na prática
- **Cohort** materializa o eixo R↔mandato: define o que um agente (meu ou do cliente) pode portar, até que valor, com qual trilha de autenticação e prova.
- **Veltrix** precifica o custo de rodar a comparação agêntica por jurisdição/sensibilidade — o outro lado da conta de quem oferece a jornada de portabilidade.

## Como cito isto num board
"Ordenei as carteiras por Exposição × Sobrevivência × Retenção: estas três concentram o spread que um agente comparador porta primeiro — e a defesa que sobra não é preço, é retenção contratual."
