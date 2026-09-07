---
name: board-materials
description: Cria materiais executivos de alto nível — PDFs ilustrados para board, estudos estratégicos, dossiês para investidor, relatórios visuais com gráficos e ilustração editorial — SEMPRE começando por um briefing interativo com o usuário (formato, paleta, densidade visual vs. profundidade, estilo de ilustração e molde de consultoria McKinsey/Bain/Gartner). Use quando o usuário pedir "material para o board", "PDF ilustrado", "relatório visual", "apresentação executiva", "estudo em PDF", "dossiê", "material de alto nível", ou quando um trabalho de pesquisa precisar virar entregável apresentável. Combina com a skill consulting-research (pesquisa primeiro, material depois). NÃO use para documentos simples de texto ou respostas em chat.
---

# Board Materials — materiais executivos ilustrados com briefing interativo

Você produz o material como um estúdio de consultoria: entende o que a pessoa precisa (briefing), organiza o conteúdo em storyline, constrói com sistema visual consistente e ilustração autoral, e SEMPRE verifica o resultado olhando cada página antes de entregar.

## Etapa 1 — BRIEFING INTERATIVO (obrigatória, nunca pule)

Pergunte com AskUserQuestion (1 chamada, até 4 perguntas). Se o usuário já especificou algo no pedido, não re-pergunte esse item.

1. **Formato e uso:** PDF paisagem para apresentar ao board (padrão) · Documento de estudo para leitura profunda · Deck editável (pptx) · One-pager.
2. **Paleta:** ofereça as opções com `preview` mostrando os hex e a ideia da capa — o preview é o que faz o usuário escolher bem. Opções em `references/visual-system.md`: **Editorial quente** (creme/terracota/ocre/musgo — recomendada quando o TEMA é tecnologia, justamente para o material não parecer genérico) · **Navy executiva** · **Verde-petróleo + cobre** · **Roxo-tinta + coral** · **Cores da marca do usuário** (peça os hex e valide contraste).
3. **Densidade:** Visual-first · Equilibrado (padrão) · Estudo denso.
4. **Ilustração:** Diagramas conceituais autorais (padrão) · Ilustração editorial + diagramas (capa ilustrada e aberturas de parte) · Só gráficos, mais limpos.

Em sessão não assistida, use os padrões e declare-os na entrega.

## Etapa 2 — CONTEÚDO ANTES DE FORMA

Pesquisa primeiro, formato depois. Se o conteúdo não existe, rode `consulting-research` (hipóteses → agentes paralelos por frente → triangulação → síntese em pirâmide). Nunca abra o template antes de ter os fatos.

Monte a storyline pelos **action titles**: a sequência deles deve contar o argumento inteiro sem abrir as páginas. Estrutura de estudo longo (20–35 páginas): capa → [abertura de parte] → sumário executivo → método e leitura dos números → diagnóstico com evidência → mecanismo central → dinâmica competitiva → recorte geográfico ou setorial → ceticismo (o que derrubaria a tese) → implicações → limitações e lacunas → fontes.

**Em estudos acima de ~15 páginas, use aberturas de parte.** Elas dão respiro entre seções densas, orientam o leitor e são onde a ilustração editorial mora. Cada abertura traz: rótulo da parte, título-tese, um parágrafo e o índice dos capítulos daquela parte.

## Etapa 3 — CONSTRUÇÃO (pipeline HTML → PDF)

Detalhes em `references/visual-system.md` (tokens, gráficos, QA), `references/illustration.md` (gramática de ilustração, receitas de capa e abertura) e `references/assembly.md` (build multiarquivo e renumeração automática). Esqueleto pronto em `assets/template.html`.

1. HTML autocontido, páginas A4 paisagem (`@page{size:A4 landscape}`, `.page` de 297×210mm).
2. Fontes Inter via `npm i @fontsource/inter`; copie os woff2 **latin e latin-ext** para `fonts/` (sem latin-ext, acentos quebram). Fallback `system-ui`.
3. **CSS por tokens, com nomes de variável estáveis.** Isto é o que torna a re-tematização barata: mantenha `--blue` / `--orange` / `--aqua` como *série 1 / 2 / 3* e troque só os VALORES. Um material inteiro, com dezenas de SVGs, muda de paleta editando cinco linhas. Nunca escreva hex direto dentro de um SVG de dado.
4. Gráficos SVG inline autorais, uma mensagem por gráfico, rótulo direto na marca, cor seguindo a ENTIDADE.
5. Ilustração: camada `<svg class="art">` em full-bleed atrás do conteúdo na capa e nas aberturas de parte.
6. **Documentos longos: escreva em arquivos-parte e monte com script** (`references/assembly.md`). Inserir um capítulo no meio sem isso obriga a renumerar tudo à mão — é a maior fonte de erro do formato.
7. Renderize com Chromium headless: `chromium --headless --disable-gpu --no-sandbox --print-to-pdf=out.pdf --no-pdf-header-footer --virtual-time-budget=15000 file://$PWD/doc.html`. Em ambientes com Playwright, o binário costuma estar em `/opt/pw-browsers/chromium-*/chrome-linux/chrome`.
8. **QA visual obrigatório:** `pdftoppm -png -r 48 out.pdf pg` e **olhe cada página**. Corrija e re-renderize até limpar. A lista de falhas recorrentes está em `references/visual-system.md` — confira contra ela, não improvise.
9. Todo número com fonte: rodapé da página + página final de fontes. Métricas voláteis sempre datadas.

Para pptx ou docx, use as skills nativas, mantendo a mesma storyline e o mesmo sistema visual.

## Etapa 4 — ENTREGA E ITERAÇÃO

Entregue com 1-2 frases de resumo — nunca re-descreva o documento. Ofereça no máximo UMA melhoria concreta. Ao receber ajustes, **edite o HTML fonte e re-renderize; nunca reconstrua do zero**. Correções de dado: aplicar direto, sem página de "de/para".

Quando o usuário pedir "outras cores" ou disser que está "tudo muito parecido": o problema quase nunca é a saturação — é que a paleta escolhida é a mesma que o assunto já evoca (azul para tecnologia, verde para finanças, roxo para IA). Ofereça uma paleta **contra-intuitiva ao tema** e uma capa com ilustração geométrica grande. É o que muda a percepção de qualidade mais rápido.

## Assinaturas de qualidade dos moldes

- **McKinsey:** títulos são frases-tese; quem lê só os títulos entende tudo. Zero gráfico decorativo. "So what" sob cada exhibit.
- **Bain:** primeira página responde; última é plano com dono, prazo e métrica. Corte tudo que não muda uma decisão.
- **Gartner:** todo 2x2 com critérios de eixo declarados e um "espaço vazio" marcado; comparação de players com coluna "lacuna comum"; previsões como premissas numeradas com horizonte.

## Armadilhas

- Pular o briefing e adivinhar formato ou paleta — causa nº 1 de retrabalho.
- Hex direto dentro de SVG de dado — inviabiliza a troca de paleta.
- Texto de chat colado em página; material executivo tem prosa reescrita para leitura em 10 segundos.
- Gráfico sem mensagem no título; paleta nova a cada página; número sem fonte.
- Ilustração decorativa que não deriva da estrutura do conteúdo (ver `references/illustration.md`).
- Entregar sem ter olhado o raster de **todas** as páginas.
- Página de fontes e página de limitações esquecidas quando o material vai para board ou investidor.
