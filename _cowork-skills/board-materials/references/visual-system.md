# Sistema visual — tokens, gráficos e QA

## Princípio que governa tudo: nomes de token estáveis, valores trocáveis

O material inteiro usa três cores categóricas, sempre pelos mesmos nomes de variável — `--blue` (série 1), `--orange` (série 2), `--aqua` (série 3) — independentemente de que cor elas de fato carregam na paleta escolhida. Os nomes viraram *papéis*, não descrições. Consequência prática: trocar a paleta de um dossiê de 30 páginas com 25 SVGs é editar cinco linhas de CSS.

**Regra absoluta: nunca escreva um hex dentro de um SVG de dado.** Hex literal só é aceitável dentro da camada de ilustração (`.art` de capa e aberturas), onde a composição é desenhada para aquela paleta específica.

## Paletas

### Editorial quente — recomendada quando o TEMA é tecnologia

Um estudo sobre IA, software ou dados feito em azul-marinho parece igual a todos os outros. A paleta quente sobre papel cria distância do assunto e lê como relatório impresso de consultoria.

```css
:root{
  --navy-900:#2a2118; --navy-800:#3b2e21; --navy-700:#7d3350; --navy-600:#a8482a;
  --blue:#c25434;   /* terracota — série 1 */
  --blue-300:#dd9070; --blue-150:#eec7b4; --blue-100:#f6ded2;
  --orange:#4f7a55; /* musgo — série 2 */
  --aqua:#d9962a;   /* ocre — série 3 */
  --wine:#7d3350;
  --ink:#1f1c17; --ink2:#5c554a; --muted:#968d7d; --grid:#e6ded0; --baseline:#cbc0ae;
  --surface:#fffdf8; --plane:#f7f3ec; --border:rgba(31,28,23,.13);
  --good:#4f7a55; --goodtext:#3a5c3f; --warn:#d9962a; --serious:#c07a35; --critical:#b23a26;
}
```

Note que `--navy-900` deixou de ser azul e virou espresso: é a cor de fundo dos cards escuros e das aberturas de parte. O nome permanece porque o CSS e os SVGs já o referenciam.

### Navy executiva — padrão sóbrio para temas não-técnicos

```css
:root{
  --navy-900:#0d366b;--navy-800:#104281;--navy-700:#184f95;--navy-600:#1c5cab;
  --blue:#2a78d6;--blue-300:#6da7ec;--blue-150:#b7d3f6;--blue-100:#cde2fb;
  --orange:#eb6834;--aqua:#1baf7a;--wine:#7a2f57;
  --ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--baseline:#c3c2b7;
  --surface:#fcfcfb;--plane:#f9f9f7;--border:rgba(11,11,11,.10);
  --good:#0ca30c;--goodtext:#006300;--warn:#fab219;--serious:#ec835a;--critical:#d03b3b;
}
```

### Verde-petróleo + cobre
`--plane:#f4f6f5` · `--navy-900:#123b3a` · `--blue:#b4693a` (cobre) · `--orange:#2a8f86` (turquesa) · `--aqua:#cfa96a` (areia) · tinta `--ink:#14201f`.

### Roxo-tinta + coral
`--plane:#fbfaf8` · `--navy-900:#2e1f5e` · `--blue:#e8623f` (coral) · `--orange:#23a9b8` (ciano) · `--aqua:#f0a838` (âmbar) · tinta `--ink:#171326`.

### Marca do usuário
Mapeie o hex principal para `--blue`, o secundário para `--orange`, e escolha um terceiro tom distinguível para `--aqua`. Mantenha tinta e estrutura neutras — nunca colora o texto corrido com a cor da marca. Valide: cada cor de série com contraste ≥3:1 contra `--surface`, ou rótulo direto legível em toda marca; pares adjacentes distinguíveis por quem tem daltonismo.

## Anatomia de página (A4 paisagem)

```
.page 297×210mm · .pad 11mm 13mm 13mm
eyebrow  → "NN · NOME DA SEÇÃO" (7.5pt, caps, tracking largo, cor accent)
h1.sec   → ACTION TITLE em frase (20pt/800) — afirma, não rotula
.lede    → 1-3 linhas de contexto (9pt, ink2)
corpo    → .flexrow de .card (border-radius 3.2mm, hairline border)
.pgfoot  → fontes da página à esquerda · número à direita (6.4pt muted)
```

Componentes: **stat tile** (número 16-23pt/800 + `.tiny` explicando, com fonte); **card com borda superior colorida** (`.tt`, `.tt-o`, `.tt-a`, `.tt-n` — 1mm) para categorizar blocos; **chips** (`.chip.v` verificado, `.chip.d` declarado, `.chip.g` lacuna); **card escuro** (`.darkcard`) para a resposta consolidada; **numlist** com badge circular numerado para conclusões enumeradas.

### O card escuro exige regra própria de negrito

`b{color:var(--ink)}` é global, então um `<b>` dentro de um card de fundo escuro renderiza tinta escura sobre escuro e some. Sempre inclua:

```css
.darkcard b{color:#fff}
.darkcard i{color:var(--blue-100);font-style:italic}
```

e aplique `class="card darkcard"` em todo card com `background:var(--navy-900)`. É um bug silencioso — só aparece no raster, nunca no HTML lido.

## Regras de gráfico (SVG inline autoral)

1. **Um gráfico = uma mensagem**, escrita no `.klabel` acima dele. Dois insights, dois gráficos.
2. **Rótulo direto na marca** (valor na ponta da barra, nome dentro ou ao lado). Legenda só com ≥2 séries sem rótulo direto possível.
3. **Barras:** cantos 4px arredondados, base no eixo; baseline 1.5px (`--baseline`); gridlines hairline (`--grid`); texto de eixo 8–8.5px (`--muted`).
4. **Cor segue a entidade** em TODOS os gráficos do material, nunca a posição. Máximo 3 cores categóricas.
5. **Status colors** só para semântica real de risco/estado, sempre acompanhadas de texto.
6. **Linha de referência** (`dasharray 4 4`, `--muted`) com rótulo quando existir benchmark.
7. **Dispersão/2x2:** eixos com setas de leitura, bandas nomeadas, destaque de espaço vazio com anel tracejado, no máximo ~12 pontos rotulados.
8. **Derivações declaradas:** número anualizado, estimado ou derivado ganha asterisco e nota de memória de cálculo.
9. **Séries temporais com poucos pontos** (3-4 waves de um estudo) funcionam melhor como linhas com marcador e rótulo de valor nas pontas do que como barras agrupadas.

## Pipeline de renderização e QA

```bash
# fontes (uma vez) — latin E latin-ext, senão acentos quebram
npm i @fontsource/inter
cp node_modules/@fontsource/inter/files/inter-latin{-ext,}-{400,600,700,800,900}-normal.woff2 fonts/

# render
chromium --headless --disable-gpu --no-sandbox --print-to-pdf=out.pdf \
  --no-pdf-header-footer --virtual-time-budget=15000 file://$PWD/doc.html
# ambientes com Playwright: /opt/pw-browsers/chromium-*/chrome-linux/chrome

# QA visual (OBRIGATÓRIO — olhe TODAS as páginas)
pdftoppm -png -r 48 out.pdf pg
pdftoppm -png -r 110 -f N -l N out.pdf z   # zoom em região densa; crop com PIL se preciso
```

## Falhas recorrentes — confira contra esta lista antes de entregar

Estas são as que efetivamente aparecem, em ordem de frequência:

1. **Rótulo dentro de barra transbordando a barra** e colidindo com o número à direita. Correção: encurte o rótulo, quebre em duas linhas dentro da barra (título 9pt + qualificador 7.6pt), ou empurre o número. Nunca resolva encolhendo a fonte para menos de 8px.
2. **`text-anchor="end"` com rótulo longo saindo pela esquerda do viewBox.** Correção: mova o eixo para a direita (`x1` maior) e recalcule as larguras das barras proporcionalmente.
3. **Texto de anotação atravessando uma caixa de destaque** (o quadro tracejado de "espaço vazio" em 2x2 é o caso clássico). Correção: mova a caixa para uma faixa vertical que nenhum rótulo ocupa, ou quebre a anotação em linhas curtas.
4. **`<b>` invisível em card escuro** — ver regra `.darkcard` acima.
5. **Coluna transbordando o rodapé da página.** Sempre a coluna com mais cards ou o card de fechamento no pé. Correção: encurte a prosa (não reduza padding) ou promova `.small` para `.tiny` no bloco de fechamento.
6. **Rótulo de banda de quadrante colidindo com o rótulo de um ponto** perto do canto. Correção: ancore a banda no canto oposto ao ponto.
7. **Numeração dessincronizada após inserir capítulo** — resolvido estruturalmente pelo build de `references/assembly.md`.
8. **Referência cruzada obsoleta** ("ver página 21") depois de inserções. Prefira referenciar **capítulo** e não página, e revise no fim.

## Edição incremental

O HTML é a fonte da verdade; o PDF é build. Nunca edite o PDF. Para inserir páginas em documento longo, use o build multiarquivo — inserir à mão obriga a renumerar eyebrows, rodapés e índices das aberturas de parte, e algo sempre escapa.
