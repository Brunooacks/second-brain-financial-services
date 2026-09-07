---
tipo: atencao
data: 2026-07-22
status: aberto
origem: auto-digest
fonte_daily: "[[2026-07-21]]"
horizonte: medio
eixos: [financeiro, governanca, agentes]
tags: [atencao, auto]
---

# ⚠️ Nenhum bancão publica taxa de proveniência do core traduzido por agente — monitorar quem será o primeiro (ou o primeiro incidente)

## O sinal
Bradesco e Banco do Brasil já reportam **percentual de velocidade** em código gerado/traduzido por agente (Bradesco: até 80% em engenharia reversa de Cobol; BB: +12 mil agentes Copilot, +1.200 modelos) — mas **nenhum publicou taxa de validação/proveniência** (audit trail) sobre esse código, especialmente na tradução de *core banking* Cobol → nuvem (daily [[2026-07-21]], No Radar). Ou seja: o mercado tem o KPI do ganho, ainda não tem o KPI do risco.

## Por que monitorar
Engenharia reversa por IA em core transacional é o ponto onde ROI e risco sistêmico se sobrepõem. Um erro de *semântica* financeira (regra de juros, compensação, arredondamento) numa tradução automática não aparece no benchmark de velocidade nem no teste de sanidade — aparece na conciliação meses depois. O primeiro bancão a publicar taxa de proveniência ganha um selo de governança que vira argumento de board; o primeiro *incidente público* de "regra mal traduzida por agente em produção" muda o custo regulatório do caso de uso para todo o setor (e antecipa cobrança de TCU em banco público).

## Gatilhos pra reavaliar
- Qualquer bancão divulgar **% de código traduzido por agente com validação humana + trilha** (não só % de velocidade) → mover para tese/framework.
- Primeiro incidente público de erro semântico em core traduzido por IA → elevar horizonte para curto e conectar a risco prudencial.
- Bacen ou ANPD mencionarem "proveniência de código gerado por IA" em orientação → vira exigência, não boa prática.

## Atualizações
- 2026-07-22: nota criada a partir da daily [[2026-07-21]]. Sinal levantado no "No Radar" da edição Nº 35. Par com a Ideia [[ROI de IA na engenharia sem proveniencia troca divida visivel por invisivel]].
