---
tipo: ideia
data: 2026-08-25
status: crua
origem: auto-digest
fonte_daily: "[[2026-08-25]]"
eixos: [financeiro, governanca]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Todo banco loga a oferta negada; nenhum loga a oferta que nunca foi exibida — e é aí que a recomendação por IA vira acesso diferencial a crédito

## A tese
Quando a recomendação por IA vira o canal de distribuição de crédito para 100% de uma base, o risco regulatório não está na decisão de crédito (que todo banco já loga) — está na camada *a montante* (upstream): a oferta que o modelo deixou de exibir. **Exposição diferencial é, na prática, acesso diferencial** — e é exatamente o que ninguém está registrando.

## Por que eu acredito nisso
O novo App BB foi liberado em 24/08 com migração de **100% da base até o fim de setembro** e IA que "interpreta contexto, apoia atendimento e recomenda produtos e serviços" — tela, menus e ofertas variam por perfil (*[Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/banco-do-brasil-lanca-novo-aplicativo-com-foco-em-ia-e-personalizacao)*, *[Diário do Comércio](https://diariodocomercio.com.br/negocios/banco-brasil-novo-app-ia/)*). Nenhum comunicado usou a palavra risco. Enquanto isso o **PL 2338** — que copia a lógica de faixas de risco do AI Act e coloca crédito/serviços essenciais na faixa alta — dorme na Câmara: aprovado no Senado em 10/12/2024, remetido em março/2025, votação prevista **só para dezembro**, com SIA e sanção de até **R$ 50 mi** (*[DIAP](https://www.diap.org.br/index.php/noticias/noticias/92249-pl-2338-23-votacao-do-projeto-sobre-inteligencia-artificial-esta-prevista-apenas-para-dezembro)*, *[Senado](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233)*). O setor está construindo a arquitetura de recomendação agora e vai descobrir a obrigação depois — sobre um log que hoje ninguém escreve.

## Quem discordaria — e por quê
O contraponto jurídico é forte e provavelmente vence hoje: recomendar não é decidir; o art. 20 da LGPD trata de decisões com efeitos jurídicos, e exibir (ou não) um banner não é uma delas; personalização de vitrine sempre foi marketing. Aceito o argumento — mas ele não resolve o problema de prova: daqui a dois anos, se um supervisor perguntar se o modelo sistematicamente deixou de oferecer crédito a um recorte, a resposta terá que vir de um registro que não está sendo criado.

## O que eu faria / recomendaria
Instrumentar a camada de recomendação **antes** de escalá-la. Um **ledger de recomendação** com três campos por evento: **o que foi exibido**, **o que foi suprimido** e **versão do modelo que decidiu**, agregado por segmento. É barato agora e impossível de reconstruir depois. Nos meus produtos: [[Veltrix]] mede custo por chamada de recomendação, por jornada e por jurisdição; [[Cohort]] carrega o mandato do agente de recomendação (quais produtos pode empurrar, para quem, sob qual base legal). Distinção importante frente ao [[MRR - Matriz de Rastreabilidade da Recomendacao]]: a MRR prova a adequação da recomendação *emitida*; esta tese cobre o outro lado — o **não-evento**, a oferta suprimida agregada por segmento, que a MRR não vê. Adjacente, sem duplicar: [[O ativo que o banco perde primeiro para a IA nao e o produto e a camada de aconselhamento]] e [[Explicabilidade de credito virou requisito de arquitetura, nao compliance]].

## Lastro
- [Agência Brasil — Novo app do BB com foco em IA e personalização (24/08/2026)](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/banco-do-brasil-lanca-novo-aplicativo-com-foco-em-ia-e-personalizacao)
- [Diário do Comércio — Novo App BB: IA, personalização e autonomia (24/08/2026)](https://diariodocomercio.com.br/negocios/banco-brasil-novo-app-ia/)
- [DIAP — PL 2338/23: votação prevista apenas para dezembro](https://www.diap.org.br/index.php/noticias/noticias/92249-pl-2338-23-votacao-do-projeto-sobre-inteligencia-artificial-esta-prevista-apenas-para-dezembro)
- [Senado — PL 2338/2023 (tramitação)](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233)

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança (soberania da decisão de crédito)  ·  **Setor:** financeiro
