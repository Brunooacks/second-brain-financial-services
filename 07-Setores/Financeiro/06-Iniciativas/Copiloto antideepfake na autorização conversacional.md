---
tipo: iniciativa-ia
jornada: fraude
arquetipo: copiloto
maturidade_atual: L3
maturidade_alvo: L4
score_vale: 21
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, agentes, economia-ia]
tags: [iniciativa, backlog, vale, fraude, deepfake, autorizacao, copiloto]
---

# 💡 Iniciativa — Copiloto antideepfake na autorização conversacional

**Em uma frase:** Um copiloto de segurança em tempo real no ato de autorizar pagamento por voz/texto/imagem, que detecta deepfake de voz, engenharia social automatizada e conta-destino suspeita antes de o Pix sair — para o momento em que a interface conversacional (voz/texto/imagem) já é padrão e multiplicou a superfície de fraude.

## 🎯 O gap que origina isto
- Jornada: Prevenção a fraude & disputas (SD: **Transaction Authorization**) · Nível atual (EMA-J): **L3** (biometria/comportamento na autorização) · Alvo: **L4** (copiloto GenAI na ponta) · Gap: **1**
- Cruza com [[De-Para — Pagamentos & Pix]]: a categoria toda chegou a L4 em Pix conversacional (10 mi MAU Nubank, 20 mi canal WhatsApp BB) — e cada nova interface natural abre porta para deepfake/engenharia social (ataques +126%/+140% em 2025).

## 🏗️ Arquétipo e desenho
**Copiloto/assistência (→L4).** No passo de autorização, um copiloto cruza sinais: cadência de voz (deepfake?), coerência da narrativa (engenharia social?), reputação da conta-destino, e apresenta ao cliente um alerta acionável em tempo real ("esta voz pode ser sintética" / "esta conta tem denúncias") — human-in-the-loop, a decisão fica com o usuário. É o Alerta Pix (Itaú, 80% de detecção) generalizado para a era conversacional.

## 📊 Placar VALE
| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Ataca o vetor que mais cresce (deepfake/personificação); benchmark de valor: Alerta Pix do Itaú já pega 80% dos golpes |
| A — Aderência governança/soberania | 4 | 2,0 | Dado sensível na autorização; auditabilidade da decisão; menos "soberania pura" que as outras duas, mais segurança de IA |
| L — Lastro técnico/viabilidade | 4 | 1,0 | Modelos de detecção de deepfake e reputação de conta já existem (Itaú tem modelo próprio); integração na autorização é factível |
| E — Encaixe Veltrix/Cohort | 3 | 1,0 | Encaixe médio: FinOps de inferência por checagem (Veltrix), mas não é caso-vitrine de mandato como as outras |

**Score VALE = (4×1,5)+(4×2,0)+(4×1,0)+(3×1,0) = 21 / 27,5** → faixa: **≥20 — candidata a proposta agora**

## 🧪 Laboratório vivo
Veltrix mede o **custo de inferência por checagem antifraude** — cada "manda 50 pro Fulano" por voz dispara um ou mais modelos; roteamento por custo/latência é FinOps de segurança. Ângulo de economia de IA embutido na defesa.

## ⚠️ Contraponto real
Detecção de deepfake é corrida armamentista: o mesmo avanço de GenAI melhora o ataque e a defesa simultaneamente — a vantagem é temporária e cara de manter. Excesso de alerta gera fadiga e o cliente ignora (o Alerta Pix funciona porque é seletivo). Custo de inferência por transação pode inviabilizar em volume de Pix se o roteamento não for eficiente. E é o de menor A da jornada — mais segurança de IA que soberania.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** Insumo: é a iniciativa mais "shippável" da jornada (L=4, modelos existem) e a que mais conversa com o de-para de Pagamentos — bom gancho para ligar as duas jornadas num post. Mas é a de menor defensibilidade das três (A=4, corrida armamentista): boa como copiloto de entrada, não como núcleo defensável.

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Prevenção a fraude & disputas]] · [[De-Para — Pagamentos & Pix]]
