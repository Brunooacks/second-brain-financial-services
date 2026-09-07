---
tipo: moc
setor: saude
fase: 2
tags: [moc, saude]
---

# 🩺 MOC — Saúde (Fase 2)

> Fase 2 — multissetor. Foco em pattern-matching com finanças e frameworks próprios.

## 🎯 Teses vivas
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "saude")
SORT maturidade DESC
```

## 📚 Reports & fontes
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "saude")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "saude") AND status != "resolvido"
```

## 🧱 Frameworks aplicáveis
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "saude")
```

## 📌 Dado citável de board
<!-- Preencher conforme leio reports do setor. Sempre fonte + página. -->
-
