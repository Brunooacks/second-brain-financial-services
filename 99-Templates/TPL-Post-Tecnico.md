---
tipo: post
data: <% tp.date.now("YYYY-MM-DD") %>
canal: linkedin
registro: tecnico
status: rascunho
eixos: []
maturidade: 3
medium: nao-publicado
tags: [post, linkedin, tecnico, <% tp.date.now("YYYY-[W]WW") %>]
---

# 🔧 Post Técnico — <% tp.file.title %>

> 500–700 palavras · leitor: arquiteto, head de engenharia, staff, CISO · pergunta que responde: **como isso funciona e onde quebra?**
> Regra: se não nomear **onde medir**, é opinião. Corte e reescreva.

## Gancho (1–2 frases)

*Abra por um mecanismo, um número de arquitetura ou um trade-off — nunca por manchete.*

## O mecanismo

*Como a coisa realmente funciona. O caminho que a decisão percorre. Onde estão as fronteiras do sistema.*

## Onde quebra

*O ponto de falha que o release note não menciona. Escala, jurisdição, custo, latência, rastreabilidade.*

## O número

*Um dado de sistema com fonte: turnos, custo por tarefa, latência p95, taxa de erro, tokens. Fonte + página.*

## O contraponto honesto

*O que um engenheiro competente responderia a isso. Se não consegue formular, a tese não está madura — marque `status: crua`.*

## O que eu instrumentaria primeiro

1.
2.
3.

*(2–3 pontos de medição concretos, com o nome da métrica.)*

---

**Assinatura:**
*Escrevo sobre IA aplicada ao setor financeiro — governança, soberania de dados e a economia de rodar agentes em produção.*

**Arte:** motivo de mecanismo (escada, engrenagem de pedra, corredor, estrutura exposta) conforme [[Identidade-Visual-Editorial]].

**Expansão Medium:** [[ ]]

**Fontes:**
-

---
## ✅ Checklist antes de publicar
- [ ] Nomeia **onde medir**?
- [ ] Todo número tem fonte (e página, se for report)?
- [ ] Tem contraponto real declarado?
- [ ] NÃO virou tutorial?
- [ ] Tese distinta das outras peças da semana?
