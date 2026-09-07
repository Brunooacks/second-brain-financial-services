---
tipo: moc
tags: [moc, jornadas, depara, benchmarking]
---

# 🗂️ MOC — De-Para de Jornadas

> Índice das jornadas mapeadas (jornada × players). Cada nota usa [[TPL-Jornada-DePara]]. Ver plano: [[00b-Plano-Discovery-Jornadas-para-Iniciativas]].

## Jornadas da Fase 1 (financeiro)
- [x] Onboarding & KYC *(Semana 1)* — 🖼️ aguardando captura
- [x] Originação de crédito *(Semana 2)* — 🖼️ aguardando captura
- [ ] Pagamentos & Pix / agentic *(Semana 3)*
- [ ] Prevenção a fraude & disputas *(Semana 4)*
- [ ] Atendimento & cobrança *(Semana 5)*
- [ ] Investimentos & advisor *(Semana 6)*

## Catálogo automático (Dataview)
```dataview
TABLE jornada, players, data_captura
FROM "07-Setores/Financeiro/03-Comparativos"
WHERE tipo = "jornada-depara"
SORT jornada ASC
```

## Matriz de cobertura (jornada × player)
```dataview
TABLE jornada, players
FROM "07-Setores/Financeiro/03-Comparativos"
WHERE tipo = "jornada-depara"
```
