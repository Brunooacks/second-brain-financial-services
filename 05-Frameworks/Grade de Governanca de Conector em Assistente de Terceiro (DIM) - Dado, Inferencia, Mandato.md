---
tipo: framework
data: 2026-09-04
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-09-04]]"
eixos: [soberania, governanca, agentes, financeiro]
tags: [framework, auto]
---

# 🧱 Grade DIM — Governança de Conector em Assistente de Terceiro (Dado · Inferência · Mandato)

## O problema que ele resolve
Quando um banco pluga saldo, fatura e transações num assistente de terceiro (PicPay no Claude e no ChatGPT, 03/09), a decisão costuma ser tratada como feature de canal. Não é: é decisão de arquitetura de distribuição que abre três exposições que ninguém precifica no go-live. A Grade DIM força as três perguntas *antes* de o conector entrar no ar, cada uma com um dono de risco e um teste objetivo.

## O framework
Três eixos, avaliados por conector e por jornada:

- **D — Dado que sai.** O que efetivamente trafega: só o campo respondido, ou o histórico que o modelo precisa *ler* para responder? Ler 12 meses de transação para dizer "quanto gastei com delivery?" é **inferência**, e inferência sobre dado transacional é finalidade nova sob LGPD, não a "consulta" consentida. Teste: mapear payload real, não o payload declarado.
- **I — Inferência (onde e sob que contrato).** Em qual jurisdição roda o raciocínio e sob que contrato de residência? O conector autentica no Brasil, mas o raciocínio pode acontecer fora, sob a política de privacidade do *plano do cliente* — sem contrato corporativo por trás. Teste: existe roteamento por jurisdição para o **canal**, não só para o backend? (é o que o **Veltrix** faz por chamada).
- **M — Mandato (quem decide quando consulta vira transação).** Hoje é leitura-apenas; "movimentar dinheiro não está no escopo" — *ainda*. Quem vira essa chave é o roadmap de conectores do fornecedor. Teste: há mandato escrito que limite valor, contraparte e horário quando consulta virar transação? (é o mandato de agente do **Cohort**).

Regra de leitura: um conector só é governado quando os três eixos têm dono e resposta. D sem I é dado solto; I sem M é canal sem freio.

## Quando usar / quando NÃO usar
**Usar:** avaliação de qualquer conector/OAuth de banco em assistente de terceiro (Claude, ChatGPT, Gemini), integração de Open Finance com big tech, ou plugin que exponha dado de cliente a modelo externo. **Não usar:** para IA interna sobre modelo contratado por API (aí a exposição é de inferência, coberta pela [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]]); a DIM é específica do caso em que a *distribuição* migra para fora do perímetro.

## Aplicado na prática
Conector PicPay-no-Claude pela DIM: **D** = fatura e transações do cartão (histórico lido, não campo isolado) → finalidade de inferência, revisar base legal. **I** = raciocínio na infraestrutura/jurisdição do fornecedor, sob termo de uso do cliente → sem contrato de residência corporativo (gap). **M** = "não está no escopo" é decisão do fornecedor, sem mandato escrito do banco (gap). Diagnóstico: leitura-apenas hoje, mas dois dos três eixos sem dono — o conector está no ar antes de estar governado. Veltrix cobre o I; Cohort cobre o M.

## Como cito isto num board
"Antes de qualquer conector em assistente de terceiro, respondemos três perguntas — que dado sai, onde a inferência roda e quem decide quando consulta vira transação. Se dois ficam sem dono, não é canal: é exposição que a gente não controla."
