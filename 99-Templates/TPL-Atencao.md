<%*
const t = await tp.system.prompt("O sinal/pergunta a monitorar");
const nome = t.replace(/[\\/:*?"<>|]/g, "-").slice(0, 80);
await tp.file.rename(nome);
await tp.file.move("/04-Atencao/" + nome);
-%>
---
tipo: atencao
data: <% tp.date.now("YYYY-MM-DD") %>
status: aberto      # aberto | monitorando | resolvido
horizonte: medio    # curto | medio | longo
eixos: []           # financeiro | governanca | soberania | economia-ia | agentes | seguranca | fronteira
tags: [atencao]
---

# ⚠️ <% t %>

## O sinal
<!-- O que estou vendo se mover? -->

## Por que monitorar
<!-- Hipótese: se isto evoluir, o que muda pro meu mercado/tese? -->

## Gatilhos pra reavaliar
<!-- O que precisa acontecer pra eu agir ou mudar de ideia. -->

## Atualizações
- <% tp.date.now("YYYY-MM-DD") %>:
