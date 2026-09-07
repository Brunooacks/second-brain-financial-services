---
tipo: moc
setor: industria
fase: 2
tags: [moc, industria]
---

# 🏭 MOC — Indústria (Fase 2)

> Fase 2 — multissetor.

## 🎯 Teses vivas
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "industria")
SORT maturidade DESC
```

## 📚 Reports & fontes
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "industria")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "industria") AND status != "resolvido"
```

## 🧱 Frameworks aplicáveis
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "industria")
```

## 📌 Dado citável de board
<!-- Preencher conforme leio reports do setor. Sempre fonte + página. -->
-
