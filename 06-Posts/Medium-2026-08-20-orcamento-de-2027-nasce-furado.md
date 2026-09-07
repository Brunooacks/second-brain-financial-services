---
tipo: post
data: 2026-08-20
canal: medium
registro: executivo
status: rascunho
eixos: [economia-ia, financeiro, soberania]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-08-20-orcamento-de-2027-nasce-furado]]"
tags: [post, medium, 2026-W34]
---

# 📰 Medium — O preço de inteligência artificial parou de ser previsível

**Título:** O preço de inteligência artificial parou de ser previsível

**Dek:** Em 14 de agosto, um fornecedor cortou preço pela metade e outro subiu dez vezes. O orçamento de 2027 aprovado com a tabela de hoje já nasce furado.

---

Existe uma premissa que sustenta silenciosamente quase todo business case de inteligência artificial aprovado desde 2024: **o custo só cai**. Ela era razoável. Ela deixou de ser verdade em 14 de agosto de 2026.

## O número

No mesmo dia, dois movimentos em direções opostas:

| Fornecedor | Movimento | Entrada (US$/mi tokens) | Saída (US$/mi tokens) |
|---|---|---|---|
| Google — Gemini 3.7 Flash | corte de 50% | 0,75 | 3,75 |
| Google — Gemini 3.7 Flash **a partir de 01/01/2027** | **+100%** | **1,50** | **7,50** |
| DeepSeek — V4-Pro | alta acima de 10x | — | — |

*Fontes: InfoWorld e VentureBeat, 14/08/2026.*

O detalhe que quase nenhum business case registrou está na segunda linha: **o preço do Flash é promocional até 31/12/2026.** Em 1º de janeiro ele dobra. A DeepSeek, no sentido contrário, subiu o V4-Pro em mais de dez vezes alegando pressão de capacidade.

Não é uma tendência. São dois pontos, no mesmo dia, em direções opostas. O que morreu não foi o preço baixo — foi a **previsibilidade**.

## A exposição

Vale separar o que é notícia de fornecedor do que é exposição de balanço.

**O cenário que preocupa não exige nenhuma decisão nova.** Uma instituição que migrou carga para o preço promocional durante o segundo semestre de 2026 aprova o orçamento de 2027 com a tabela vigente. Em janeiro, o consumo é idêntico — mesmas cargas, mesmos casos de uso, mesmo volume — e a conta dobra na parcela apoiada naquele preço. Não há o que "otimizar": o gasto não cresceu por uso, cresceu por contrato.

**Preço promocional tem uma segunda função.** Além de vender, ele move carga. Barato para migrar; caro depois que a migração aconteceu. Desfazer o movimento custa engenharia, tempo e risco de regressão — é aprisionamento ao fornecedor, com a diferença de que aqui o gatilho tem data marcada no calendário.

**E há o problema de titularidade.** Na maioria das casas, o custo de inferência entra na conta de tecnologia como despesa de nuvem, diluído entre centros de custo, sem responsável nomeado. Quando dobrar, aparecerá numa reconciliação de fechamento — meses depois de ter começado a dobrar. Custo sem dono não é gerenciado; é descoberto.

Para uma instituição financeira com esteira de agentes indo a produção, a exposição real não é o preço de hoje. É **a diferença entre o preço de tabela pós-promoção e o preço sobre o qual o orçamento foi construído**, multiplicada pela parcela da carga que depende dele.

## O contraponto

O argumento contrário é sólido e vem de gente experiente.

Um diretor financeiro diria: a curva de longo prazo do custo de inferência é claramente de queda — mais eficiência de hardware, mais competição, mais modelos abertos. Reprovisionar orçamento por causa da tabela de um fornecedor específico é microgestão, e ainda cria despesa de governança para administrar volatilidade que se resolve sozinha em dois trimestres.

Concordo com a curva. Discordo da conclusão, por dois motivos.

Primeiro: a curva agregada não paga a fatura de janeiro. Entre a tendência e o fluxo de caixa existe um trimestre, e é nele que o comitê de orçamento vive.

Segundo — e mais importante: o que se pede aqui não é previsão de preço. É **medida de exposição**. Nenhuma tesouraria prevê câmbio; toda tesouraria sabe qual percentual da sua posição está exposto e quanto custaria neutralizá-la. A disciplina já existe na casa, aplicada a moeda e a concentração de fornecedor. Falta apenas apontá-la para uma linha de custo que, até dois anos atrás, não existia.

## O que eu faria

**No próximo comitê, três perguntas — e não sair da sala sem resposta:**

**1.** Que percentual do gasto previsto de IA em 2027 está apoiado em preço promocional com data de expiração? *Se ninguém souber responder, essa já é a resposta — e o número a levantar antes da próxima reunião.*

**2.** Quem é o dono nomeado da linha de custo de inferência? Nome de pessoa, não nome de área. Sem titular, não há quem responda pela variação.

**3.** Quanto tempo e quanto custa mover a maior carga de IA para outro fornecedor? *Se a resposta for "seria um projeto", não existe alternativa — existe dependência.*

**E uma mudança de instrumento, que vale mais que as três perguntas juntas:** toda proposta de investimento em IA passa a exigir uma **coluna de preço pós-promoção**, com a data de expiração explícita ao lado. É uma linha a mais na planilha. É também a diferença entre descobrir a exposição em agosto e descobri-la em fevereiro.

O **Veltrix** existe para tornar essa segunda pergunta respondível: quando custo por tarefa e troca de provedor são operação corrente e não projeto, a expiração de uma promoção vira um ajuste de rota — não uma surpresa de orçamento.

---

**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-08-20-orcamento-de-2027-nasce-furado]]
**Notas relacionadas:** [[Preco de IA virou imprevisivel - promo expira e orcamento de 2027 nasce furado]] · [[Integracao vertical dos labs derruba o preco por token - contrato fixo envelhece mal]]
**Frameworks citados:** [[Demonstracao de Resultado de IA (VCAT) - Valor, Custo, Atribuicao, Trilha]] · [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]]

## Fontes
1. InfoWorld — corte de preço do Gemini 3.7 Flash e expiração da promoção em 31/12/2026 (14/08/2026)
2. VentureBeat — reajuste do DeepSeek V4-Pro por pressão de capacidade (14/08/2026)
3. Daily [[2026-08-14]]
