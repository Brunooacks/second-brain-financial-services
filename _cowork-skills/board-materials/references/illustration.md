# Ilustração editorial — gramática, receitas e limites

Ilustração aqui não é enfeite: é o que impede um estudo de 30 páginas de parecer uma planilha longa, e é o que faz um material sobre tecnologia não parecer todo material sobre tecnologia. Mas ela só ganha o direito de existir quando **a geometria deriva da estrutura do próprio conteúdo**.

## A regra única

Antes de desenhar qualquer coisa, responda: *que forma o argumento desta seção tem?* Um afunilamento? Uma convergência? Camadas empilhadas? Duas forças opostas? Um ciclo? A ilustração é essa forma, desenhada em grande. Se a resposta for "não sei", não ilustre — use um card.

Formas que funcionam, e o que cada uma diz:

| Forma | Diz | Onde usei bem |
|---|---|---|
| Arcos concêntricos | Camadas de um mercado, do amplo ao específico | capa, abertura de parte |
| Blocos empilhados decrescentes | Stack de produto, hierarquia, precedência | capa |
| Funil de retângulos decrescentes com guias | Denominador → público real | abertura da parte geográfica |
| Linhas convergindo para um nó | Muitos fornecedores, um ponto de agregação | abertura da parte sobre API |
| Blocos quadrados sobrepostos em diagonal | Tabuleiro competitivo, players disputando espaço | abertura da parte competitiva |
| Node-link escalonado | Encadeamento de conclusões | abertura da parte de conclusões |
| Grade de pontos decrescente | Dispersão, cauda longa, perda ao longo do funil | textura de apoio na capa |

## Camada `.art` — como se monta

Capa e aberturas de parte têm duas camadas: um `<svg class="art">` em full-bleed e o conteúdo por cima.

```css
.cover{background:var(--plane);color:var(--ink);position:relative}
.cover .art{position:absolute;inset:0;z-index:1}
.cover .inner{position:relative;z-index:2;padding:19mm 22mm;height:100%;display:flex;flex-direction:column}
.div{background:var(--navy-900);color:#fff;position:relative}
.div .art{position:absolute;inset:0;z-index:1}
.div .inner{position:relative;z-index:2;padding:24mm;height:100%;display:flex;flex-direction:column;justify-content:center}
```

O SVG usa `viewBox="0 0 1122 794"` com `preserveAspectRatio="none"` — proporção A4 paisagem em px, o que permite pensar em coordenadas absolutas sem converter milímetros.

**Nesta camada, e só nela, hex literal é permitido**, porque a composição é desenhada para uma paleta específica e não precisa sobreviver a re-tematização automática.

## Receita 1 — capa em papel com bloco de arte lateral

A capa mais forte e mais reutilizável: dois terços de papel com a tipografia, um terço de campo de cor com a composição.

```
1. rect full-bleed na cor --plane
2. <g transform="translate(660,0)"> abre o painel direito
3. rect 462×794 num tom levemente mais escuro que o papel (#efe7d9 sobre #f7f3ec)
4. três arcos concêntricos ancorados na borda direita, do escuro ao claro:
   <path d="M462,120 A300,300 0 0,0 462,720 Z" fill="terracota"/>
   <path d="M462,196 A224,224 0 0,0 462,644 Z" fill="terracota clara"/>
   <path d="M462,272 A148,148 0 0,0 462,568 Z" fill="terracota mais clara"/>
5. quatro blocos empilhados decrescentes no canto superior esquerdo do painel (as camadas do assunto)
6. círculo vazado + círculo cheio + círculo pequeno no canto inferior (contraponto de forma)
7. grade de pontos triangular em --baseline (textura, sugere cauda longa)
8. três faixas horizontais decrescentes no rodapé esquerdo, nas três cores da paleta
```

A tipografia da capa fica em quatro linhas curtas, 34–36pt/800, `max-width` de ~168mm para nunca invadir o painel.

## Receita 2 — abertura de parte sobre fundo escuro

```
1. rect full-bleed em --navy-900
2. composição temática à direita ou embaixo, ocupando ~40% da área, nas 3 cores + vinho
3. textura discreta em #4a3d2c (linhas ou círculos concêntricos) no lado oposto — ela existe
   para o fundo não parecer vazio, nunca para competir com o título
4. faixa de 8px no rodapé, na cor-tema daquela parte (dá identidade a cada divisor)
5. conteúdo: rótulo da parte (tracking .3em, cor --aqua) · título 30pt/800 ·
   parágrafo de 9.6pt · índice horizontal dos capítulos com número em --aqua
```

**Cuidado que custa caro:** a composição gráfica e o texto ocupam a mesma página. Antes de escolher onde ancorar as formas, calcule a caixa que o texto ocupa — `padding` de 24mm mais `max-width` do título — e mantenha toda forma fora dela. O erro típico é um node-link atravessando a segunda linha do título; só aparece no raster.

## Receita 3 — diagrama conceitual dentro de página de conteúdo

Diferente da arte de abertura: aqui a forma carrega dado e precisa de rótulo.

- **Comparação de duas leituras do mesmo mercado:** dois painéis lado a lado com fundo `#efe7d9`, um sinal `≠` grande em `--wine` entre eles, e a barra proporcional dentro de cada painel. Comunica "mesma coisa, medidas opostas" mais rápido que qualquer gráfico.
- **Composição de receita:** barra empilhada de 500 unidades de largura com os segmentos rotulados por dentro, e a linha de leitura embaixo com o número derivado em destaque.
- **Cadeia de funil:** barras decrescentes alinhadas à esquerda com o valor à direita e a razão total no pé.
- **Tabela de verificação:** quando o achado é "verifiquei três fornecedores e o resultado é heterogêneo", a tabela vence o diagrama. Não force ilustração onde a evidência é textual.

## Quando NÃO ilustrar

- Página de fontes, de limitações e de método: densidade textual é a mensagem.
- Quando o dado é uma tabela de comparação com mais de três colunas.
- Quando a forma escolhida não deriva do conteúdo — a decoração genérica (ondas, malhas, gradientes de circuito) baixa a percepção de rigor exatamente no público que você quer impressionar.
