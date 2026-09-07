<%*
const tese = await tp.system.prompt("A TESE em uma frase (vira o título)");
const nomeArquivo = tese.replace(/[\\/:*?"<>|]/g, "-").slice(0, 80);
await tp.file.rename(nomeArquivo);
await tp.file.move("/03-Ideas/" + nomeArquivo);
-%>
---
tipo: ideia
data: <% tp.date.now("YYYY-MM-DD") %>
status: crua        # crua | madura | publicada
eixos: []           # financeiro | governanca | soberania | economia-ia | agentes | seguranca | fronteira
maturidade: 1       # 1-5: quão pronta pra virar post
tags: [ideia, tese]
---

# 💡 <% tese %>

## A tese
<!-- Uma frase forte e defensável. Se não dá pra discordar, não é tese. -->

## Por que eu acredito nisso
<!-- O raciocínio. Evidência, padrão observado, dado de report, o que vi no Veltrix/Cohort. -->

## Quem discordaria — e por quê
<!-- Antecipa o contra. Tese sem contraponto é slogan. -->

## O que eu faria / recomendaria
<!-- A virada acionável. É isto que diferencia referência de comentarista. -->

## Lastro
<!-- Notas, reports, dados que sustentam. -->
- [[ ]]

---
**Candidata a post?** ☐  ·  **Eixo CAIO:**  ·  **Setor:**
