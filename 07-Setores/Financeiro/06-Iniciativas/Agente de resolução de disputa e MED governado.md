---
tipo: iniciativa-ia
jornada: fraude
arquetipo: reimaginacao-agentica
maturidade_atual: L3
maturidade_alvo: L5
score_vale: 24
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, agentes]
tags: [iniciativa, backlog, vale, fraude, MED, disputa, cohort]
---

# 💡 Iniciativa — Agente de resolução de disputa e MED governado

**Em uma frase:** Um agente que conduz a jornada de contestação de fraude ponta-a-ponta (triagem → coleta de evidência → acionamento do MED → prestação de contas) sob mandato com escopo, limite e trilha auditável — para bancos/fintechs que hoje resolvem disputa no braço, com prazo longo e passivo regulatório crescente.

## 🎯 O gap que origina isto
- Jornada: Prevenção a fraude & disputas (SD: **Fraud Resolution**) · Nível atual (EMA-J): **L3** (regra + humano; MED em até 7 dias/contestação 80 dias) · Alvo: **L5** · Gap: **2**
- O de-para mostrou que a detecção comoditizou em L3–L4, mas a **resolução de disputa segue em L2–L3** em todo o piloto — é o SD mais atrasado da jornada e o de maior exposição (responsabilidade objetiva crescente no judiciário).

## 🏗️ Arquétipo e desenho
**Reimaginação agêntica (→L5).** O agente recebe a contestação, classifica o tipo de golpe, reúne a evidência (logs de sessão, device, rastro Pix entre contas-laranja), monta o dossiê do MED, executa o acionamento dentro do prazo regulatório e devolve ao humano só a exceção — cada passo com trilha auditável de quem/quando/por quê. Não substitui a decisão de mérito; industrializa a instrução do caso sob mandato explícito.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Corta custo e prazo da disputa, reduz perda no MED e passivo judicial; ancorado em R$ 6,5 bi de perda Pix/2025 |
| A — Aderência governança/soberania | 5 | 2,0 | Processo regulado (MED), auditabilidade nativa, residência de dado sensível, mandato explícito — o argumento inteiro é governança |
| L — Lastro técnico/viabilidade | 3 | 1,0 | Viável, mas dado sensível e integração com trilhos do BC/MED exigem cuidado; L5 real pede human-in-the-loop robusto |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | Caso-vitrine de Cohort: mandato de agente com escopo/limite/jurisdição/trilha |

**Score VALE = (4×1,5)+(5×2,0)+(3×1,0)+(5×1,0) = 24 / 27,5** → faixa: **≥20 — candidata a proposta agora**

## 🧪 Laboratório vivo
Cohort é o produto: demonstra o **mandato do agente** (escopo = só instrução de MED; limite = não decide mérito acima de X; jurisdição = dado fica no BR; trilha = tudo auditável). Veltrix entra no FinOps de inferência da instrução automática.

## ⚠️ Contraponto real
Disputa envolve dado sensível de vítima e decisão com efeito jurídico direto — erro do agente vira dano ao consumidor e risco reputacional/regulatório. O prazo do MED é do BC, não do agente: automatizar mal pode acelerar a decisão errada. Sem human-in-the-loop forte e sem trilha impecável, é passivo, não ativo. O custo de instrução automática por caso também precisa fechar contra o ganho.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** Insumo: este é o único arquétipo da jornada com gap 2 (L3→L5) e A=5 — alto valor E alta defensibilidade. É o candidato natural a virar oferta ligada a Cohort. Falta você dar a tese e o recorte de qual player/segmento (banco de varejo vs adquirente têm disputa diferente: MED vs chargeback).

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Prevenção a fraude & disputas]]
