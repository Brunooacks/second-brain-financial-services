---
tipo: ideia
data: 2026-07-22
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-21]]"
eixos: [financeiro, governanca, agentes, economia-ia]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 O ROI de IA no banco já é real, mas migrou para a engenharia — e sem proveniência a velocidade vira dívida técnica invisível

## A tese
O primeiro ROI de IA com denominador nos bancões brasileiros não apareceu no chatbot — apareceu na engenharia, reescrevendo o core. E é exatamente por isso que o ganho de "até 80% menos tempo" só é ganho *líquido* se vier com trilha de proveniência (audit trail): sem ela, o banco troca uma dívida técnica visível (Cobol legado, mas conhecido) por uma dívida técnica invisível (Java gerado por agente, rápido, mas de semântica financeira não auditada).

## Por que eu acredito nisso
Por meses o setor vendeu IA pela vitrine (concierge, agente de investimentos). O número que virou o jogo esta semana está no backoffice: o **Bradesco** relatou **até 80% de ganho de tempo** em engenharia reversa e tradução de Cobol → nuvem e **+25% de eficiência em código novo** (via BEX e BIATech; Mobile Time, 20/07). O **Banco do Brasil** dá a escala: **+12 mil agentes Copilot, +1.200 modelos, 2 mil soluções catalogadas no 1º tri/2026** (TI Inside/Convergência Digital). Isso é IA agêntica *dentro da usina de código do banco*, não assistente de call center. E o contraponto de risco é medível pelo próprio dado: o NTT DATA já põe soberania/privacidade cross-geography como preocupação de board para **62,5% dos líderes** (Banking AI Leaders' Playbook 2026, pág. 5) — eu acrescentaria "proveniência de código gerado por agente" à mesma lista, porque uma regra de juros mal traduzida não falha no benchmark de velocidade; falha em silêncio no balanço seis meses depois.

## Quem discordaria — e por quê
Um engenheiro competente diria: "os testes automatizados pegam o erro — exigir proveniência total de cada trecho reintroduz o gargalo que a IA acabou de remover". É um contraponto real: em geração de código *nova* a aposta é baixa e o teste unitário basta. O furo do argumento é a assimetria — engenharia reversa de *core banking* é o caso de ROI máximo E de superfície de risco máxima ao mesmo tempo; um erro de semântica (não de sintaxe) numa regra de compensação passa no teste de velocidade e no de sanidade, e só aparece na conciliação. Proveniência não é o gargalo; é o seguro do ganho.

## O que eu faria / recomendaria
Levar ao comitê de tecnologia a pergunta de proveniência, não a de velocidade: **"de todo código que agentes reescreveram ou traduziram neste trimestre, qual % passou por validação humana com trilha, e conseguimos reconstruir quem (agente) mudou o quê, a partir de qual entrada e sob qual mandato?"** Se a resposta for "medimos a velocidade, não a proveniência", o diagnóstico está feito: falta a camada de mandato e trilha do *agent estate* de engenharia (**Cohort**) e falta medir o custo de inferência dessa frota (**Veltrix**). ROI sem proveniência é dívida técnica com juros de governança.

## Lastro
- Bradesco / engenharia reversa Cobol, até 80% e +25% (Mobile Time, 20/07/2026)
- Banco do Brasil — +12 mil agentes Copilot, +1.200 modelos, 2 mil soluções 1º tri (TI Inside; Convergência Digital)
- NTT DATA — Banking AI Leaders' Playbook 2026, pág. 5 (62,5%)
- Daily [[2026-07-21]] · Aprendizado do dia: "proveniência de código gerado por IA" (AI code provenance)

## Conexões
- [[Contar agentes e vaidade - o numero de board e quantos tem mandato e quem orquestra]]
- [[Mandato do Agente - escopo, limite, jurisdicao, trilha]]
- [[Placar do Parque de Agentes (FMC) - Frota, Mandato, Custo]]
- [[FMI - risco migra do balanco para o codigo e governanca do codigo vira eixo de soberania]]
- [[Cobol traduzido por agente sem proveniencia publicada - o sinal a monitorar]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança / agentes  ·  **Setor:** financeiro (bancos BR)
