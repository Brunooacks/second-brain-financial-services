<%*
const nomeF = await tp.system.prompt("Nome do framework");
const nome = nomeF.replace(/[\\/:*?"<>|]/g, "-");
await tp.file.rename(nome);
await tp.file.move("/05-Frameworks/" + nome);
-%>
---
tipo: framework
data: <% tp.date.now("YYYY-MM-DD") %>
status: rascunho    # rascunho | testando | publicado
eixos: []
tags: [framework]
---

# 🧱 <% nomeF %>

> Frameworks tornam alguém citável. Este precisa de nome, sigla, e um diagrama que um board entenda em 30 segundos.

## O problema que ele resolve
<!-- Que decisão difícil ele simplifica? -->

## O framework
<!-- As etapas/eixos. Dê nome a cada um. Se couber sigla (estilo CARO), melhor. -->

## Quando usar / quando NÃO usar
<!-- Limites. Honestidade vira autoridade. -->

## Aplicado na prática
<!-- Exemplo real — de preferência via Veltrix ou Cohort. -->

## Como cito isto num board
<!-- A frase de uma linha que entrega o framework inteiro. -->
