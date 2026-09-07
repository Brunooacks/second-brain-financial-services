---
tipo: framework
data: 2026-07-04
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-04]]"
eixos: [agentes, governanca, financeiro, seguranca]
tags: [framework, auto]
---

# 🧱 Matriz de Execução do Agente (VCAP) — Valor, Canal, Autenticação, Prova

## O problema que ele resolve
Quando o agente passa de recomendar para **executar** (Pix por voz da BIA, cobrança do Mercado Pago), a pergunta de board deixa de ser "a resposta foi boa?" e vira **"quem autorizou, e como vocês provam que foi o cliente?"**. O [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] (ELJT) diz *o que o agente pode fazer*; falta a camada que diz *quando exigir step-up e como provar a autenticidade da ordem no canal aberto* — o território que a fraude turbinada por IA (deepfake de voz) ataca primeiro.

## O framework
Para **cada ação executável** que um agente pode disparar (Pix, transferência, contratação de crédito), preencher quatro colunas:
- **V — Valor:** teto até o qual o agente executa **sem 2º fator**. Acima dele, obrigatório step-up.
- **C — Canal:** onde a ação é permitida (app blindado, WhatsApp, voz) e onde é bloqueada — o canal aberto sobe o nível de exigência.
- **A — Autenticação (step-up):** o gatilho de reautenticação (biometria, 2º fator, confirmação fora de banda) por combinação valor × canal.
- **P — Prova:** o que fica na trilha auditável — quem autorizou, quando, por qual fator — para responder ao Bacen e ao jurídico.

Regra de ouro do desenho: achar o **teto de valor por confirmação**, não bloquear tudo — fricção demais mata a conveniência que justifica o canal.

## Quando usar / quando NÃO usar
- **Usar:** ao promover qualquer agente de recomendação para execução que mova dinheiro ou contrate; ao abrir um canal novo (voz/WhatsApp); no one-pager de risco antes do go-live.
- **NÃO usar:** para agentes que só informam/recomendam (aí vale [[MRR - Matriz de Rastreabilidade da Recomendacao]]); não substitui o ELJT — VCAP é a camada de **autenticação da ordem**, ELJT é a **credencial do agente**.

## Aplicado na prática
Pix por voz da BIA no WhatsApp: V = teto R$ X sem step-up; C = WhatsApp/voz classificado como canal aberto (nível +1); A = biometria de voz + confirmação fora de banda acima do teto; P = trilha de quem autorizou, canal e fator. Operacionalmente, é o **Cohort** aplicando o mandato por ação e o **Veltrix** medindo o custo de inferência de cada verificação em escala de 20 mi de clientes.

## Como cito isto num board
"Para cada coisa que o agente executa sozinho, a VCAP responde quatro perguntas em 30 segundos: até quanto sem 2º fator, em que canal, quando exige step-up, e como provamos quem autorizou."
