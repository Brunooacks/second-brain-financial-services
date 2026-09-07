---
tipo: framework
nome: Identidade Visual Editorial — Toulmé/Kafka
descricao: Spec visual única para toda arte de post (LinkedIn e Medium). Paleta, traço, repertório de motivos, grid do carrossel e prompts reutilizáveis.
versao: 1.0
data: 2026-08-15
eixos: [financeiro, governanca, soberania, economia-ia, agentes]
tags: [framework, identidade, visual, arte, post]
---

# 🎨 Identidade Visual Editorial

> **Leia junto com [[_CAIO-Brain]].** O texto carrega a tese; a arte carrega o *estado emocional* da tese. Se a imagem pudesse ilustrar qualquer post sobre IA, ela está errada.

## 1. A tese visual

A ilustração não decora o post — ela **encena o desconforto que a tese nomeia**. A referência é o encontro de dois registros:

- **Fabien Toulmé** (quadrinho documental): traço solto de nanquim, aguada, figura humana pequena e vulnerável, gesto cotidiano, cor usada com parcimônia extrema. Humaniza o assunto árido.
- **Franz Kafka** (registro narrativo, não gráfico): a instituição vasta e ilegível, o limiar que não se atravessa, o processo do qual não se vê o fim, a figura minúscula diante do aparato. Dá o peso.

O cruzamento dos dois é o nosso território: **um humano em escala pequena diante de uma arquitetura institucional que ele não controla — desenhado com a mão trêmula do quadrinho, não com o vetor limpo do corporativo.** É exatamente a posição de quem senta num board para responder por um sistema que decide sozinho.

## 2. Paleta

| Papel | Hex | Uso |
|---|---|---|
| Papel envelhecido | `#EFE8DC` | fundo de toda ilustração |
| Papel claro (bloco de texto) | `#F4F2EE` | faixa inferior do card |
| Nanquim | `#1A1A1A` | traço, massa, silhuetas |
| Grafite médio | `#5A5A58` | aguadas, sombra, corpo de texto |
| Cinza frio | `#9A9A96` | textura, profundidade, elementos secundários |
| **Vermelhão queimado** | `#C7472A` | **acento único** |
| Vermelhão claro | `#E0714D` | apenas em degradê do acento |

**Regra do acento:** uma só cor quente por peça, ocupando **menos de 8% da área**. O vermelhão marca *o ponto onde a tese dói* — nunca é enfeite. Se há dois focos vermelhos, a composição tem duas ideias e precisa ser cortada.

**Proibido:** azul tecnológico, ciano neon, degradê roxo-azul, verde "dado", qualquer paleta que pareça dashboard.

## 3. Traço e textura

- Nanquim aplicado a pincel seco: bordas irregulares, falhas, respingo, escorrido.
- Aguada (wash) para volume — nunca sombreamento uniforme.
- Grão de papel visível em toda a área. A peça deve parecer **impressa e um pouco gasta**, não renderizada.
- Hachura fina para superfícies grandes (piso, parede, ponte).
- Silhuetas humanas **sem rosto** e sem detalhe de roupa. A pessoa é qualquer um — inclusive quem lê.

## 4. Composição

1. **Figura pequena, espaço grande.** A silhueta humana ocupa no máximo 12% da altura. O vazio ao redor é o argumento.
2. **Um único evento visual.** Uma porta, uma ponte, um balão, uma escada. Não empilhe metáforas.
3. **Linha de horizonte baixa** ou ponto de fuga alto: a arquitetura domina, o humano não.
4. **Dispersão como motivo recorrente:** quadrados/fragmentos soltos no ar = a decisão que se fragmenta e não se reconstrói. É a assinatura da série — use quando o tema for trilha, auditoria ou rastreabilidade.
5. **Respiro.** Pelo menos 30% da ilustração é papel vazio.

## 5. Repertório de motivos (mapa tese → imagem)

| Eixo da tese | Motivo | Leitura |
|---|---|---|
| Governança / trilha | Porta monumental aberta para o escuro; fragmentos escapando | a decisão passou e não deixou rastro |
| Soberania de dados | Ponte sobre água; a outra margem fora do quadro | jurisdição é distância, não bandeira |
| Economia de IA / FinOps | Balão preso a um novelo emaranhado; figura segurando o fio | o custo sobe, o controle fica no chão |
| Preço / orçamento | Escada que desce e se inverte para cima | o que caía voltou a subir |
| Agentes / autonomia | Multidão de silhuetas idênticas, uma só com sombra vermelha | escala sem mandato |
| Segurança / ataque | Corredor de portas repetidas, uma entreaberta | o canal lateral que ninguém observa |
| Explicabilidade | Figura diante de um muro liso; do outro lado, estrutura exposta | fachada × arquitetura |
| Concentração de fornecedor | Coluna única sustentando uma laje enorme | dependência comum |

**Nunca use:** robô humanoide, cérebro de circuito, mão de androide tocando mão humana, rede neural em nós brilhantes, cadeado azul, gráfico de barras genérico. São o oposto exato desta identidade.

## 6. Grid do card

**Formato:** 1200×1500 (4:5, o que mais ocupa feed no LinkedIn) ou 1080×1080 quando for carrossel de 3.

```
┌──────────────────────────────┐
│                              │
│      ILUSTRAÇÃO              │  62% da altura
│      (sangra nas 3 bordas)   │
│                              │
├──────────────────────────────┤
│ 01.            ← vermelhão   │
│ Manchete em duas linhas.     │  33% da altura
│ Bold, nanquim, ~44pt         │
│                              │
│ Corpo em 4–5 linhas curtas,  │
│ grafite médio, ~22pt         │
├──────────────────────────────┤
│ ▪ marca · autor · M · in     │  5% — faixa nanquim
└──────────────────────────────┘
```

- **Tipografia:** grotesk neutra (Inter, Söhne, Helvetica Now). Nunca serifada, nunca display.
- **Numeral do card** (`01.`) sempre no acento vermelhão — é o que cria a série.
- **Manchete:** máximo 8 palavras, quebrada manualmente em 2 linhas. Termina em ponto final.
- **Corpo:** frases curtas, uma por linha, sem bullet. Cada linha é uma unidade de sentido.
- **Rodapé fixo:** `Conteúdo semanal sobre IA no setor financeiro — governança, soberania e economia de agentes.` · `Compilado, analisado e escrito por Bruno Acks.` · ícones Medium + LinkedIn.

## 7. Prompts reutilizáveis

**Bloco de estilo (colar sempre, sem alterar):**

```
Editorial illustration in the style of French documentary comics — loose brush-and-ink
linework with watercolor wash, visible paper grain, aged cream paper background (#EFE8DC),
deep black india ink, muted warm greys. ONE single accent colour: burnt vermillion (#C7472A),
used on less than 8% of the frame. A small faceless human silhouette, no more than 12% of
the frame height, dwarfed by a vast institutional architecture. Kafkaesque mood: bureaucratic
immensity, threshold, quiet unease. Generous empty space. Hand-drawn imperfection, dry-brush
edges, ink splatter, slight bleed. NO text, NO letters, NO numbers, NO logos.
NO robots, NO circuit boards, NO neural networks, NO blue tech palette, NO glowing lines.
```

**Bloco de cena (varia por post):** uma frase, um evento visual, extraída do motivo da tabela 5.

| Tipo de post | Cena |
|---|---|
| Técnico | privilegie mecanismo: escada, engrenagem de pedra, corredor, estrutura exposta |
| Executivo | privilegie consequência: limiar, ponte, sala vasta, assinatura, cadeira vazia |
| Long-form | privilegie a cena narrativa da abertura do texto |

**Ajustes de saída:** `aspect ratio 4:5` para card único, `1:1` para carrossel, `16:9` para capa de Medium.

## 8. Checklist antes de publicar

- [ ] A imagem só serve para **esta** tese? (se serve pra qualquer post de IA, refaça)
- [ ] Um único foco vermelho, abaixo de 8% da área?
- [ ] A figura humana está pequena e sem rosto?
- [ ] Tem grão de papel e imperfeição de traço?
- [ ] Zero texto dentro da ilustração?
- [ ] O rodapé de marca está idêntico ao das peças anteriores?

---

**Ligações:** [[_CAIO-Brain]] · [[000-HOME]]
