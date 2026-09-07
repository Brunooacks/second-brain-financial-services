---
tipo: moc
setor: fronteira
fase: 3
tags: [moc, fronteira]
---

# 🚀 MOC — Fronteira / Geral (Fase 3)

> Fase 3 — arquiteturas GenAI, segurança/alignment, AGI, quântica, geopolítica e soberania de dados.

## 🎯 Teses vivas
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "fronteira")
SORT maturidade DESC
```

## 📚 Reports & fontes
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "fronteira")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "fronteira") AND status != "resolvido"
```

## 🧱 Frameworks aplicáveis
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "fronteira")
```

## 📌 Dado citável de board
<!-- Preencher conforme leio reports do setor. Sempre fonte + página. -->
-
