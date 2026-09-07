---
tipo: moc
setor: varejo
fase: 2
tags: [moc, varejo]
---

# 🛍️ MOC — Varejo (Fase 2)

> Fase 2 — multissetor. Agentic commerce cruza com finanças.

## 🎯 Teses vivas
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "varejo")
SORT maturidade DESC
```

## 📚 Reports & fontes
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "varejo")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "varejo") AND status != "resolvido"
```

## 🧱 Frameworks aplicáveis
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "varejo")
```

## 📌 Dado citável de board
<!-- Preencher conforme leio reports do setor. Sempre fonte + página. -->
-
