---
tipo: moc
setor: juridico
fase: 2
tags: [moc, juridico]
---

# ⚖️ MOC — Jurídico (Fase 2)

> Fase 2 — multissetor. Pattern-matching entre setores.

## 🎯 Teses vivas
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "juridico")
SORT maturidade DESC
```

## 📚 Reports & fontes
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "juridico")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "juridico") AND status != "resolvido"
```

## 🧱 Frameworks aplicáveis
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "juridico")
```

## 📌 Dado citável de board
<!-- Preencher conforme leio reports do setor. Sempre fonte + página. -->
-
