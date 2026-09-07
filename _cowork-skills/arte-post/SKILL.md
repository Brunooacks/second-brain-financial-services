---
name: arte-post
description: "Gera a arte 4:5 dos posts de LinkedIn e das capas de Medium do Bruno no sistema visual Registro Húmido — ilustração de nanquim e aguada sobre papel envelhecido, silhueta pequena, um único acento cromático, tipografia editorial com a tese e o dado. Use quando ele pedir a arte do post técnico (terça) ou executivo (quinta), a capa de um artigo, 'gera a arte', 'ilustra esse post', 'a imagem da semana', ou quando um post estiver pronto em 06-Posts e faltar a peça visual."
---

# Arte do post — sistema Registro Húmido

A máquina desenha; a tese é do Bruno. **A ilustração encena o desconforto que a tese nomeia.** Se a imagem serviria para qualquer post de IA, ela está errada.

## Antes de desenhar

1. Leia o post em `~/.../AI-Brain/06-Posts/` (ou peça a tese colada, se o arquivo estiver como placeholder do iCloud).
2. Extraia: **a tese em duas linhas**, **o eixo**, **o dado com fonte e página**. Sem dado verificado, não invente — use a linha de framework como referência.
3. Escolha a cena pelo que a tese *dói*, não pelo assunto.

## A gramática travada

Papel envelhecido com fibra, poeira e bordas absorvidas. Nanquim `#161615`. Massas construídas por camadas de aguada, com veios claros de dry-brush por dentro. Silhueta humana **sem rosto, ≤ 6% da altura**, sempre fora do centro. Linha de repouso em ~60% da altura separa imagem de texto. Um **único acento cromático**, sempre menos de 8% do quadro.

Tipografia: `Gloock` na tese, `GeistMono` no índice, `DMMono` no dado, `InstrumentSans` no rodapé. Duas linhas de tese, no máximo duas de dado. Nada encosta na margem.

**Nunca:** robô, cérebro de circuito, rede neural brilhante, cadeado, paleta azul-ciano de tecnologia, render 3D, look vetorial limpo, texto dentro da ilustração.

## Banco de cenas

| Cena | Encena | Usar quando a tese fala de |
|---|---|---|
| `cena_arquivo` | sistema vasto e uniforme, um módulo tocado | governança, auditoria, explicabilidade, inventário, rastreabilidade |
| `cena_ponte` | travessia feita, estrutura que sustenta o peso | agentes em produção, passivo, trilho de pagamento, responsabilidade |
| `cena_balao` | o que sobe sem que ninguém segure o custo | economia de IA, FinOps, ROI, custo por tarefa, inferência |

Cena nova só quando nenhuma das três encena a tese — e aí ela entra na biblioteca, não vira peça avulsa.

## Acento por eixo

| Eixo | Acento | |
|---|---|---|
| financeiro | `#B94E32` laranja-queimado | |
| governança | `#2E5484` azul guache | |
| soberania | `#2F5D4F` verde-garrafa | |
| economia de ia | `#A9782B` ocre | |
| agentes | `#7B3B4A` vinho | |
| segurança | `#8C3A2E` tijolo | |
| fronteira | `#4A3B6B` roxo-tinta | |

Um acento por peça. Duas peças da mesma semana nunca repetem acento.

## Como rodar

Edite a lista `PECAS` em `scripts/cenas.py` e execute:

```bash
python3 scripts/cenas.py
```

Cada entrada da lista:

```python
dict(arq="2026-08-25-tecnico", cena=cena_balao, semente=19, acento=(169,120,43),
     indice="02", eixo="economia de ia",
     tese=["ROI de IA sem custo de", "inferência é fé, não FinOps."],
     dados=["tokens · contexto · cache · latência · volume",
            "o que não medimos, não otimizamos"],
     fonte="NTT DATA · 2026 GLOBAL AI REPORT · P. 22")
```

**Duas variações por post:** rode a mesma cena com duas sementes diferentes e entregue as duas. A semente muda a aguada, a deriva e o respingo — a composição permanece.

Saída: PNG 1080×1350. Salve em `06-Posts/assets/` com o nome do post e sufixo `-a` / `-b`.

## Técnico × executivo

Mesma gramática, ênfases diferentes.

- **Técnico (terça):** a cena mostra o **mecanismo** — onde o sistema é medido ou onde falha. As linhas de dado nomeiam o ponto de instrumentação.
- **Executivo (quinta):** a cena mostra a **consequência** — quem carrega o peso. As linhas de dado trazem o número de balanço ou o prazo regulatório.

## Se houver modelo de imagem disponível

Quando existir crédito de geração, a mesma cena pode ser briefada como prompt em inglês, mantendo a gramática: *ink-wash and charcoal on aged textured paper, small faceless silhouette seen from behind, vast architecture, drifting geometric fragments, watercolour bleeds and dry-brush, deep blacks and warm greys, single accent colour under eight percent of the frame, no text, no logos, no robots, no circuitry, no glowing networks, no blue tech palette, no 3D render.* A ilustração entra como imagem e a faixa tipográfica é montada por cima.
