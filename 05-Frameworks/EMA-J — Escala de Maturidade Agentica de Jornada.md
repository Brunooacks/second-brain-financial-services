---
tipo: framework
data: 2026-07-03
status: testando    # rascunho | testando | publicado
eixos: [financeiro, agentes, governanca]
tags: [framework, maturidade, jornada, agentic, benchmarking]
---

# 🧱 EMA-J — Escala de Maturidade Agêntica de Jornada

> Frameworks tornam alguém citável. A EMA-J dá **um número auditável** ao "nível de maturidade tecnológica" de qualquer jornada financeira — comparável entre players e defensável num board em 30 segundos.

## O problema que ele resolve
"Nível de maturidade" vira achismo quando não tem régua. Sem escala, não dá pra dizer "o Nubank está L4 no onboarding e o banco X está L2" com lastro. A EMA-J transforma observação de tela pública em **nota comparável**, e a diferença de nota (o *gap*) vira o argumento de venda.

## O framework — 6 níveis (L0 → L5)

| Nível | Rótulo | Definição | Sinal observável (público) |
|---|---|---|---|
| **L0** | Manual/analógico | Humano em todo passo; sem canal digital | Exige agência, papel, telefone |
| **L1** | Digitalizado | Self-service digital, fluxo estático | App/site faz o passo, mas sem inteligência: formulário fixo |
| **L2** | Automatizado (regras) | Decisão por regra determinística; STP parcial | Aprovação/negativa instantânea por critério fixo; esteira sem humano |
| **L3** | Preditivo (ML) | Modelo estatístico decide/prioriza | Score de crédito/fraude, limite dinâmico, personalização por modelo |
| **L4** | Assistido por IA (GenAI) | Copiloto/generativo com human-in-the-loop | Atendimento generativo, assistente financeiro, resumo/explicação automática |
| **L5** | Agêntico | Agente executa a jornada ponta-a-ponta sob mandato e governança | Agente age (paga, contrata, negocia) com escopo/limite/trilha auditável |

**Regra de atribuição:** o nível é o do **passo mais avançado com evidência pública**, mas anote também o nível *predominante* da jornada. Ex.: onboarding com score de fraude (L3) mas resto estático → "L3 pontual, L1 predominante". Sem evidência = `[não observável]`, nunca chute.

## Como se lê o gap
`gap = nível do líder da jornada − nível do player-alvo`. Gap ≥ 2 = território de reimaginação; gap = 1 = modernização/copiloto; gap = 0 com líder em L≤2 = mercado inteiro atrasado (oportunidade de categoria). O gap escolhe o arquétipo de iniciativa no [[Placar VALE — Priorizacao de Iniciativa de IA]].

## Quando usar / quando NÃO usar
**Usar:** comparar players numa mesma jornada; medir evolução de um player no tempo; justificar prioridade de iniciativa.
**NÃO usar:** como nota de "qualidade" do produto (um L3 bem-feito bate um L4 mal-feito); nem para jornada logada sem evidência pública — aí o nível é hipótese, e tem que estar marcado como tal.

## Aplicado na prática
No de-para de onboarding, um neobanco costuma marcar L3–L4 (KYC com liveness + score de fraude), enquanto uma esteira de PJ de bancão pode ficar em L1–L2 (formulário longo, análise humana). O gap de 2 níveis no PJ é exatamente onde entra a proposta de esteira agêntica governada (Cohort) — não porque "IA é legal", mas porque o número mostra o vale. *(Níveis a confirmar com evidência na coleta — aqui é ilustração do método.)*

## Como cito isto num board
"Sua jornada de crédito PJ está em L2; o líder do seu segmento opera em L4, e cada nível de gap é ativação e perda que dá pra medir. A EMA-J diz onde investir primeiro."

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]
