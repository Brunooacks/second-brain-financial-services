---
tipo: framework
data: 2026-09-01
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-09-01]]"
eixos: [agentes, governanca, financeiro, soberania]
tags: [framework, auto]
---

# 🧱 Matriz de Interrupção do Agente (ASE) — Acionador, SLA, Estado da transação em voo

## O problema que ele resolve
"Kill switch" virou item de slide de governança de agente — o BB nomeou os três controles (interrupção de agente, autonomia faseada, restrição de dado sensível) e vai virar benchmark. Mas **dizer que se pode parar o agente é diferente de provar, depois do incidente, em que estado o sistema ficou.** Sem SLA de acionamento e sem definição do estado da transação interrompida, o mecanismo de interrupção é botão de PowerPoint. Nenhum framework do acervo cobre a interrupção em si: [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] (ELJT) governa a credencial de entrada; [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]] governa a autenticação da ordem; nenhum governa a saída de emergência.

## O framework
Para cada agente que executa em produção, três colunas obrigatórias:

- **A — Acionador:** quem pode interromper (cliente, operador, comitê de risco, sistema automático) e sob qual gatilho. Se ninguém sabe quem aperta o botão, não há botão.
- **S — SLA de acionamento:** em quanto tempo a interrupção se efetiva — **medido, não prometido**. Kill switch com latência desconhecida é declaração.
- **E — Estado da transação em voo:** o que acontece com a transação já iniciada — **reverte, compensa ou permanece** —, definido por tipo de transação, nunca genérico.

## Quando usar / quando NÃO usar
Usar antes de promover a produção qualquer agente que **execute** (Pix por linguagem natural, cobrança, pagamento, otimização de saldo). NÃO usar como substituto do mandato: a ASE governa a saída de emergência, não a credencial de entrada — ela compõe o ELJT, não o troca. Para agente que só sugere/consulta, a ASE é leve; o peso está em quem executa.

## Aplicado na prática
No **App 5.0 do BB** já se pede Pix por linguagem natural dentro da mesma jornada. ASE desse agente: **A** = cliente + antifraude; **S** = o número que hoje ninguém publica; **E** = Pix é irreversível, então o estado só pode ser "permanece" ou "compensa via MED 2.0" — **nunca "reverte"**. Isso redesenha o kill switch: num trilho irreversível, interromper o agente não desfaz a transação, só impede a próxima. É a fronteira do **Cohort** (emite, escopa, revoga **e interrompe** o mandato) medida pelo **Veltrix** (custo e latência do acionamento por chamada e por jornada).

## Como cito isto num board
"Para cada agente que executa, quero três coisas provadas: **quem aperta o botão, em quanto tempo ele responde e o que acontece com a transação que estava em voo.** Sem as três, não temos kill switch — temos slide."
