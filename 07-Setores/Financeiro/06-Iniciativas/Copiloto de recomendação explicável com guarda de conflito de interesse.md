---
tipo: iniciativa-ia
jornada: investimentos
arquetipo: copiloto
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 24
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, soberania, agentes]
tags: [iniciativa, backlog, vale, advisor, explicabilidade, conflito-interesse]
---

# 💡 Iniciativa — Copiloto de recomendação explicável com guarda de conflito de interesse

**Em uma frase:** Uma camada de governança sobre o advisor generativo que, para cada recomendação a cada cliente, produz a **explicação auditável** ("por que este produto, dado seu perfil") e aciona uma **guarda de conflito de interesse** que sinaliza/limita o viés de recomendar o fundo da própria casa.

## 🎯 O gap que origina isto
- Jornada: Investimentos & advisor · Nível atual (EMA-J): **L4** (advisor GenAI já recomenda a 100 mil no Itaú, dezenas de milhões potenciais no Nubank) · Alvo: **L4 governado** · Gap: **0 em capacidade, mas 100% em auditabilidade**
- O vale do de-para: recomendação a milhões sem trilha de explicação + sem separação de conflito é escala de risco supervisório (CVM/Bacen) e reputacional, não de receita.

## 🏗️ Arquétipo e desenho
Copiloto/guardrail. Não substitui o advisor — o **cinturão de segurança** dele. Para cada saída de recomendação: (1) registra a cadeia de evidência (suitability, projeção, restrição) que justifica o produto; (2) roda um classificador de conflito que marca quando a recomendação favorece produto proprietário e exige divulgação/alternativa; (3) entrega ao supervisor e ao regulador um log consultável de "quem recomendou o quê, para quem, por quê". É a diferença entre "a IA sugeriu" e "a IA sugeriu e eu consigo defender no board".

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Não gera receita direta, mas é licença para escalar o advisor sem passivo; destrava o V das outras iniciativas |
| A — Aderência governança/soberania | 5 | 2,0 | Explicabilidade + conflito de interesse + trilha é o núcleo da supervisão de advisory; puro eixo A |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Camada sobre modelo existente; explicabilidade e logging são viáveis com o dado que já circula |
| E — Encaixe Veltrix/Cohort | 4 | 1,0 | Cohort (trilha/mandato) + Veltrix (observabilidade de inferência) demonstram a guarda |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(4×1,0) = 24 / 27,5** → faixa: **Proposta agora**

## 🧪 Laboratório vivo
Veltrix registra e observa cada chamada de inferência do advisor (o que entrou, que modelo, que custo); Cohort ancora a trilha de decisão e a política de conflito. Juntos viram o painel de conformidade de advisory que um regulador pediria.

## ⚠️ Contraponto real
⏳ **para o Bruno.** Insumos: (a) explicabilidade de LLM é parcial — "explicação plausível" não é "causa real", e vender rationale gerado como prova pode ser pior que não ter; (b) a guarda de conflito depende de rotular o que é "produto da casa", o que politicamente incomoda a área comercial; (c) custo de logging/observabilidade a milhões de interações não é zero.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Investimentos & advisor]]
