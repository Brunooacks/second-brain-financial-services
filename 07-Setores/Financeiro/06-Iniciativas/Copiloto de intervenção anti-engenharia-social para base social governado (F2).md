---
tipo: iniciativa-ia
jornada: fraude
fase: 2
arquetipo: copiloto
maturidade_atual: L2
maturidade_alvo: L4
score_vale: 21.0
status: candidata
data: 2026-07-05
eixos: [financeiro, governanca, soberania, agentes]
tags: [iniciativa, backlog, vale, fraude, engenharia-social, copiloto, base-social, caixa, fase-2]
---

# 💡 Iniciativa — Copiloto de intervenção anti-engenharia-social para base social governado (Fase 2)

**Em uma frase:** Um copiloto que intervém em tempo real no cliente durante a tentativa de golpe (ligação suspeita, transação atípica, coação) — levado à **base social** (perfil da Caixa, 130 mi+), onde a engenharia social é a frente crítica e não há defesa de IA na ponta do cliente.

## 🎯 O gap que origina isto
- Jornada: Prevenção a fraude & disputas (Fase 2) · Nível atual (EMA-J): **L2** (Caixa; sem intervenção de IA ao cliente) · Alvo: **L4** (copiloto de intervenção human-in-the-loop) · Gap: 2 níveis
- O vale do de-para: o Santander shipou **Alerta de Segurança / Alerta em ligação** (intervenção ao cliente em tempo real); a Caixa (130 mi+, público mais visado por engenharia social) está no piso mínimo. A Zetta e o diretor de segurança do C6 apontam a **susceptibilidade da vítima** — não a quebra do sistema — como o problema real.

## 🏗️ Arquétipo e desenho
**Copiloto** (human-in-the-loop). Diferente do antideepfake do piloto (que olha a autorização): este olha o **contexto de engenharia social** no momento do risco:
1. **Detecta o padrão de golpe** — usuário no app durante uma ligação, transação fora do padrão para conta-destino nova/suspeita, urgência atípica.
2. **Interrompe e explica** em linguagem acessível ("você pode estar sendo enganado; nenhum funcionário pede isto") — desenhado para o público social, baixa fluência digital.
3. **Governa** — trilha do que foi alertado, sob LGPD, com residência de dado estatal; o copiloto avisa, o cliente decide (não bloqueia por conta própria).

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Engenharia social é a frente crítica do Pix (Zetta) e a base social é a mais vitimada (28 mi de vítimas, 53% com 50+). Impacto social alto, mas monetização sobre base social/estatal é difícil, por isso não é 5. |
| A — Aderência governança/soberania | 4 | 2,0 | LGPD + residência de dado estatal + trilha de intervenção sobre base social. Forte, mas é copiloto que avisa (não roteamento/mandato puro), por isso 4 e não 5. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | O Santander já provou a viabilidade (Alerta em ligação em produção); replicar para base social é adaptação de UX e integração, não pesquisa. |
| E — Encaixe Veltrix/Cohort | 3 | 1,0 | Cohort governa o mandato do copiloto e a trilha, mas o encaixe é parcial — é copiloto de aviso, não frota de agentes autônomos. |

**Score VALE = (4×1,5)+(4×2,0)+(4×1,0)+(3×1,0) = 6,0+8,0+4,0+3,0 = 21,0 / 27,5** → faixa: **candidata a proposta agora (≥20)**

## 🧪 Laboratório vivo
Cohort governa o mandato do copiloto (o que pode alertar, o que registra, o que nunca decide sozinho) e a trilha de conformidade; a residência de dado estatal demonstra soberania sobre a base mais sensível do país. Mostra que defesa na ponta do cliente pode ser governada e auditável, não caixa-preta.

## ⚠️ Contraponto real
Copiloto que alerta demais **cansa e é ignorado** (fadiga de alerta) — e o público social, menos fluente, pode se paralisar ou desconfiar do próprio banco. Pior: o golpista de engenharia social já instrui a vítima a ignorar avisos ("o banco vai mandar uma mensagem, pode ignorar"), então o copiloto compete com o roteiro do fraudador dentro da cabeça da vítima. Eficácia real depende de UX comportamental, não de modelo — e isso é difícil de provar antes de escalar.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina estruturou a candidata; a tese e o serviço são seus.)

---
**Liga com:** [[De-Para — Prevenção a fraude & disputas (Fase 2 · expansão)]] · [[Copiloto antideepfake na autorização conversacional]] (piloto) · [[Motor de pagamento conversacional governado para base social (Caixa) (F2)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]]
