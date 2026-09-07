---
tipo: atencao
data: 2026-09-05
status: aberto
origem: auto-digest
fonte_daily: "[[2026-09-05]]"
horizonte: medio
eixos: [soberania, governanca, agentes, economia-ia]
tags: [atencao, auto]
---

# ⚠️ Multi-modelo não é multi-infra — dois fornecedores no mesmo control plane caem juntos

## O sinal
Na quinta (03/09), uma falha no Azure East US tirou do ar por ~90 min ChatGPT, Claude, Grok e Copilot ao mesmo tempo — >37 mil reports no Downdetector só do ChatGPT; o Gemini, em outra nuvem, ficou de pé (Axios · 03/09; Daily AI Digest · 04/09). Analistas descreveram como falha de plano de controle compartilhado (shared control plane). No mesmo intervalo, o BankID norueguês (4,2 mi de usuários, assinatura qualificada) ficou 30h fora por falha do fornecedor DXC — segundo incidente multi-dia desde 2021, testando na prática os prazos do DORA (TechTimes · 04/09). Os três hyperscalers concentram ~63% do gasto em nuvem; o Reino Unido já designou AWS, Google, Microsoft e Oracle como *Critical Third Parties* (jul/2026).

## Por que monitorar
Ter dois modelos não é ter dois fornecedores se os dois moram no mesmo prédio: OpenAI e Anthropic rodaram na mesma nuvem, e a nuvem caiu. Isso derruba a ilusão de failover que sustenta quase todo desenho "multi-modelo" de banco. E é pior para agente que para app: 90 min/ano é 99,98% de disponibilidade — ótimo para o app, errado para o agente. Um agente no meio de uma tarefa de 40 passos que perde o modelo por 90 min não "pausa"; ele falha em estado desconhecido. O report da CCAF (2026 Global AI in FS, pág 9) coloca privacidade como risco nº 1 para 74% da indústria — concentração de infraestrutura nem aparece na lista, e foi ela que parou o mercado esta semana. Cruza com o conector do PicPay (ed. 68), que empilha inferência e distribuição na mesma camada.

## Gatilhos pra reavaliar
- Failover de modelo entre fornecedores que **não compartilham** região nem control plane (regra de Veltrix): sair da tese e virar requisito de arquitetura.
- Bacen ou CVM tratarem concentração de nuvem como risco cibernético sistêmico (espelho do UK Critical Third Parties) — vira item de supervisão, não boa prática.
- Primeiro incidente documentado no Brasil de agente que falhou "em estado desconhecido" por outage de nuvem durante execução financeira.

## Atualizações
- 2026-09-05: nota criada a partir da daily. Conecta com [[O conector do banco empilha dependencia de distribuicao sobre a de inferencia no mesmo fornecedor]] e [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]] — roteamento por jurisdição precisa incluir roteamento por nuvem, e o failover de modelo precisa ser testado como se testa DR de core.
