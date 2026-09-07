---
tipo: moc
setor: financeiro
fase: 1
tags: [moc, financeiro]
---

# 🏦 MOC — Setor Financeiro (Fase 1)

> Meta da fase: ser **a** referência em PT sobre IA no setor financeiro. Eixos: risco/fraude/crédito, agentic commerce, banking AI-native, regulação aplicada (Bacen, LGPD, EU AI Act no contexto financeiro), economia de IA.

## 🎯 Teses vivas do setor
```dataview
TABLE status, maturidade
FROM "03-Ideas"
WHERE contains(eixos, "financeiro")
SORT maturidade DESC
```

## 📚 Reports & fontes do setor
```dataview
TABLE autor, data_publicacao
FROM "02-Sources"
WHERE contains(setor, "financeiro")
SORT file.cday DESC
```

## ⚠️ Sinais a monitorar
```dataview
LIST
FROM "04-Atencao"
WHERE contains(eixos, "financeiro") AND status != "resolvido"
```

---

## 📌 Dado citável de board (atualizar conforme leio reports)
<!-- Números que carrego pro board. Sempre com fonte + página. -->
- **Governança centralizada separa líderes de retardatários:** 65% dos líderes de IA em serviços financeiros seguem governança centralizada, vs. 36,1% dos laggards — gap de ~29 p.p., um dos maiores do dataset. *(NTT DATA, 2026 Global AI Report, p. 22)*
- **CAIO já é norma no setor:** 77,5% dos líderes têm um Chief AI Officer dedicado, vs. 70,3% dos demais. *(NTT DATA, p. 24)*
- **Comitê de IA virou table stakes:** ~55% líderes / 54% laggards têm steering committee — a presença não diferencia mais; o que diferencia é clareza de mandato e accountability. *(NTT DATA, p. 23)*
- **Deployment híbrido como estratégia regulatória:** 62,5% dos líderes usam modelo híbrido (plug-and-play + co-inovação), vs. 29,2% dos laggards. *(NTT DATA, p. 15)*
- **Arquitetura como exigência regulatória, não otimização:** 30% dos líderes priorizam stacks seguros e escaláveis. Soberania/private AI tratada como "o protetor" da stack. *(NTT DATA, p. 16)*
- **Governança de agentes é o gap aberto:** só 21% das empresas dizem ter modelo maduro de governança de agentes autônomos. *(NTT DATA, key findings, p. 20)*

## 🧱 Frameworks aplicáveis aqui
```dataview
LIST
FROM "05-Frameworks"
WHERE contains(eixos, "financeiro")
```

## 🔗 Mapa de subtemas
- [[Risco, fraude e crédito]]
- [[Agentic commerce]]
- [[Banking AI-native]]
- [[Regulação aplicada — Bacen, LGPD, EU AI Act]]
- [[Economia de IA no setor financeiro]]
