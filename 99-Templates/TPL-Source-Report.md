<%*
const titulo = await tp.system.prompt("Título da fonte/report");
const tipoFonte = await tp.system.suggester(
  ["Report (PDF)", "Newsletter", "Artigo", "Paper", "Podcast", "Thread/X"],
  ["report", "newsletter", "artigo", "paper", "podcast", "thread"]
);
const destino = tipoFonte === "report" ? "/02-Sources/Reports/" : "/02-Sources/";
const nomeArquivo = titulo.replace(/[\\/:*?"<>|]/g, "-");
await tp.file.rename(nomeArquivo);
await tp.file.move(destino + nomeArquivo);
-%>
---
tipo: source
classe: <% tipoFonte %>
titulo: "<% titulo %>"
autor:
data_publicacao:
data_captura: <% tp.date.now("YYYY-MM-DD") %>
setor: [financeiro]
eixos: []          # financeiro | governanca | soberania | economia-ia | agentes | seguranca | fronteira
fase:
url:
tags: [source]
---

# <% titulo %>

**Fonte / Autor / Data:**  ·  ·

## 🎯 Tese central
<!-- 2 linhas. Qual é a aposta deste material? -->

## 🔑 Achados-chave (com número + página)
<!-- 3 a 5. Cada um com o dado citável e a página. É o que cito num board. -->
1. **[dado]** — (p. )
2. **[dado]** — (p. )
3. **[dado]** — (p. )
4.
5.

## 🔗 Conexão com finanças / governança / soberania
<!-- Onde isto encaixa na minha tese de mercado? -->

## 🗣️ O que eu diria sobre isso
<!-- Minha interpretação. Não é resumo — é posição. Daqui sai tese de post. -->

---
**Liga com:** [[ ]]
