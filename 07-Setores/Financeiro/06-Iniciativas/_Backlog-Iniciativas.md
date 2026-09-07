---
tipo: moc
tags: [moc, iniciativas, backlog, vale]
---

# 🎯 Backlog de Iniciativas de IA

> Funil saído do de-para. Cada nota usa [[TPL-Iniciativa-IA]] e recebe [[Placar VALE — Priorizacao de Iniciativa de IA]]. Ordena por score. Ver plano: [[00b-Plano-Discovery-Jornadas-para-Iniciativas]].

## Ranking automático (Dataview)
```dataview
TABLE arquetipo, jornada, maturidade_atual, maturidade_alvo, score_vale, status
FROM "07-Setores/Financeiro/06-Iniciativas"
WHERE tipo = "iniciativa-ia"
SORT score_vale DESC
```

## Faixas
- **≥ 20** — proposta de serviço agora (vira one-pager)
- **14–19** — backlog quente (falta dado/PoC)
- **< 14** — parking lot

## Por arquétipo
```dataview
TABLE rows.file.link AS iniciativas
FROM "07-Setores/Financeiro/06-Iniciativas"
WHERE tipo = "iniciativa-ia"
GROUP BY arquetipo
```
