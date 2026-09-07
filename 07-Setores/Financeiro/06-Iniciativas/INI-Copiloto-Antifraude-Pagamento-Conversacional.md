---
tipo: iniciativa-ia
jornada: pagamentos-pix
arquetipo: copiloto
maturidade_atual: L4
maturidade_alvo: L4
score_vale: 23
status: candidata
data: 2026-07-03
eixos: [financeiro, governanca, seguranca-ia]
tags: [iniciativa, backlog, vale, pagamentos, pix, fraude, deepfake, veltrix]
---

# 💡 Iniciativa — Copiloto antifraude para pagamento conversacional (voz/imagem)

**Em uma frase:** Um copiloto de fraude em tempo real na etapa de autorização do Pix conversacional — quando o pagamento entra por voz, texto ou imagem (foto de chave manuscrita) — para conter a superfície de risco nova que a interface natural abre: engenharia social, deepfake de voz e adulteração de imagem, com trilha explicável.

## 🎯 O gap que origina isto
- Jornada: Pagamentos & Pix · Nível atual (EMA-J): **L4** (Pix por voz — Nubank/Bradesco/Itaú; por imagem — BB) · Alvo: **L4** (mesmo nível, blindado) · Gap de segurança: quanto mais natural a interface, maior a superfície de fraude. BB lê foto de papel manuscrito (adulterável); voz é clonável. O Bacen apertou regras de segurança/rastreio de fraude do Pix em 2026. Ver [[De-Para — Pagamentos & Pix]].

## 🏗️ Arquétipo e desenho
**Copiloto (human-in-the-loop).** Na confirmação do pagamento conversacional, o copiloto avalia sinais de fraude específicos do canal — voz sintética, imagem forjada, padrão atípico de intenção, engenharia social ("manda pra essa nova chave urgente") — e devolve um score explicável + recomendação (aprovar, desafiar, bloquear) antes de o Pix sair. Não substitui o antifraude transacional; cobre a lacuna que a **interface natural** cria e que o antifraude clássico (baseado em dispositivo/comportamento) não vê.

## 📊 Placar VALE
Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Fraude é custo direto e reputacional; valor é defensivo (perda evitada), não receita nova — nota honesta 4 |
| A — Aderência governança/soberania | 5 | 2,0 | Segurança de IA + trilha explicável; alinhado à agenda do Bacen de rastreio de fraude no Pix; governança é o núcleo |
| L — Lastro técnico/viabilidade | 3 | 1,0 | Detecção de deepfake de voz e imagem forjada é fronteira real (falsos positivos travam pagamento legítimo) — barreira técnica honesta |
| E — Encaixe Veltrix/Cohort | 4 | 1,0 | Veltrix observa e roteia; a explicabilidade do score de fraude encaixa na observabilidade, mas não é o caso canônico |

**Score VALE = (4×1,5)+(5×2,0)+(3×1,0)+(4×1,0) = 23 / 27,5** → faixa: **≥20 — Proposta agora (one-pager)**

## 🧪 Laboratório vivo
Veltrix dá a observabilidade e a explicabilidade do score de fraude (por que bloqueou); a trilha conversa com a governança de mandato do Cohort quando o pagamento for agêntico. É o par natural da iniciativa [[Pix agêntico governado sob mandato]]: mandato governa o "pode pagar"; copiloto governa o "é seguro pagar".

## ⚠️ Contraponto real
⏳ **para o Bruno.** (Insumos: falso positivo em fraude trava pagamento legítimo e destrói experiência — o custo do erro é assimétrico; detecção de deepfake é corrida armamentista; risco de sobreposição com o antifraude que o player já tem. Se não fecha o contraponto, é slogan.)

## 🗣️ O que eu diria num board
⏳ **para o Bruno.**

---
**Liga com:** [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]] · [[De-Para — Pagamentos & Pix]] · [[INI-Pix-Agentico-Governado-Mandato]] · [[Copiloto anti-deepfake com liveness explicável]]
