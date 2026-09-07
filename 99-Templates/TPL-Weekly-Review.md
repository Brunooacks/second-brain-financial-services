<%*
const data = tp.date.now("YYYY-MM-DD");
const nome = "Weekly-" + data;
await tp.file.rename(nome);
await tp.file.move("/06-Posts/" + nome);
-%>
---
tipo: weekly
data: <% tp.date.now("YYYY-MM-DD") %>
semana: <% tp.date.now("gggg-[W]ww") %>
tags: [weekly, review]
---

# 🗓️ Weekly Review — semana <% tp.date.now("gggg-[W]ww") %>

> Sexta-feira. O Dataview varre o que marquei; eu escolho **uma** tese; o Cowork rascunha na minha voz; eu edito e publico. **A sexta tem que acontecer.**

---

## 💡 Ideias da semana (das mais maduras pras mais cruas)
```dataview
TABLE status, maturidade, eixos
FROM "03-Ideas"
WHERE file.cday >= date(today) - dur(7 days)
SORT maturidade DESC
```

## 📅 Dailies da semana
```dataview
LIST
FROM "01-Daily"
WHERE date(data) >= date(today) - dur(7 days)
SORT data DESC
```

## ⚠️ Pontos de atenção em aberto
```dataview
TABLE status, eixos, file.mtime AS "atualizado"
FROM "04-Atencao"
WHERE status != "resolvido"
SORT file.mtime DESC
```

## 📚 Fontes/reports destilados na semana
```dataview
TABLE autor, classe, eixos
FROM "02-Sources"
WHERE file.cday >= date(today) - dur(7 days)
SORT file.cday DESC
```

## 🧩 Tudo que marquei como #tese esta semana
```dataview
LIST
WHERE contains(file.tags, "#tese") AND file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

## 🪝 Ganchos da semana (alimentados pela rotina diária)
<!-- A rotina "criao-de-notas" acumula aqui, todo dia, os ganchos das notas candidatas a post. É a lista curta de onde sai a escolha da semana. -->
![[_Ganchos-Semana.md]]

## 🌱 Sementes geradas pela máquina nesta semana
<!-- Notas-rascunho (status crua/aberto/rascunho) que a rotina destilou das dailies. Maturar a escolhida; arquivar/limpar o resto. -->
```dataview
TABLE tipo, status, eixos, file.cday AS "criada"
FROM "03-Ideas" OR "04-Atencao" OR "05-Frameworks"
WHERE origem = "auto-digest" AND file.cday >= date(today) - dur(7 days)
SORT file.cday DESC
```

---

## ✅ A escolha da semana
**Tese escolhida pra virar peça:**
<!-- UMA. A que tem mais lastro e mais a minha cara. -->

**Por que esta:**

**Ângulo / gancho:**

**Onde publica:** ☐ LinkedIn ☐ Newsletter ☐ X ☐ outro:

---

## 📝 Rascunho (Cowork ajuda → eu edito)
<!-- Cowork puxa a tese escolhida + lastro e rascunha NA MINHA VOZ. Eu fecho. -->

---

## 📈 Métricas (não "quanto li")
- Inbound qualificado:
- Convites pra falar/participar:
- Negócios gerados / movimentados:
- Densidade do acervo (notas novas com tese):