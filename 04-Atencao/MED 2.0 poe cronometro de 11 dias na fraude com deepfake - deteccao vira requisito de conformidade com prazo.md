---
tipo: atencao
data: 2026-07-05
status: aberto
origem: auto-digest
fonte_daily: "[[2026-07-05]]"
horizonte: curto
eixos: [governanca, financeiro, seguranca]
tags: [atencao, auto]
---

# ⚠️ MED 2.0 põe cronômetro de 11 dias na fraude com deepfake — detecção adaptativa deixa de ser boa prática e vira requisito de conformidade com prazo

## O sinal
O dado novo não é tecnológico, é regulatório. **42,5% das fraudes financeiras no Brasil já usam IA**, o uso de deepfakes cresceu **830%** (2024→2025) e o golpe do Pix por deepfake subiu **148%** em 2025 (voz clonada a partir de ~15s de áudio público); ~28 mi de brasileiros teriam sido vítimas, com **R$ 4,941 bi** não devolvidos só em Pix em 2024 (WeLiveSecurity; Sindpd, 2026). Do lado da régua, o **MED 2.0** (Mecanismo Especial de Devolução — Resolução BCB 493/2025, **em vigor desde 02/02/2026**) fixa **80 dias para o cliente contestar**, **devolução em até 11 dias úteis** após confirmação de fraude e **rastreamento em cadeia**.

## Por que monitorar
O MED 2.0 desloca o ônus e o relógio para a instituição: quando um cliente contesta um Pix fraudado por deepfake, o banco corre contra **11 dias úteis** e precisa provar a cadeia. Isso converte detecção adaptativa de "boa prática" em **requisito de conformidade com prazo cravado**. E o vetor se agrava com a leitura da semana: estamos empurrando pagamento para canais (voz, WhatsApp, agente) que a IA generativa tornou mais fáceis de falsificar — **cada novo canal de execução é um novo vetor de contestação com cronômetro regulatório rodando**. O elo mais fraco segue sendo a ponta terceirizada (o rastro tipo C&M), território de due diligence de fornecedor do **NIST AI RMF (ação GOVERN)**.

## Gatilhos pra reavaliar
- Primeiro caso público de banco que estoura o prazo de 11 dias por não conseguir provar a cadeia — vira benchmark de exposição.
- Bacen endurecer ou detalhar o rastreamento em cadeia do MED 2.0 (responsabilidade solidária na cadeia de instituições).
- Lançamento de canal de pagamento por voz/agente em produção sem métrica de detecção de deepfake acoplada — entra direto na conta de contestação.
- Aliança/compartilhamento de dado de fraude entre instituições com a ANPD na mesa — cruza soberania de dado com combate à fraude.

## Atualizações
- 2026-07-05: nota criada a partir da daily [[2026-07-05]] (cluster 🛡️ Governança & Risco). Ação pra board: cruzar o inventário de canais de execução (Pix por voz, WhatsApp, agente) com o prazo de 11 dias — cada canal novo entra na conta antes de ir ao ar, não depois. Conecta a [[Contra fraude agentica a defesa migra de detectar comportamento para provar identidade do agente]] (mesma virada "provar > detectar") e a [[Rombo de R 800 mi da C&M entra pela ponta terceirizada - risco de IA e due diligence de fornecedor nao do core]] (o elo fraco é o fornecedor).
