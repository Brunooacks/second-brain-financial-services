---
tipo: post
data: 2026-08-18
canal: medium
registro: tecnico
status: rascunho
eixos: [economia-ia, financeiro, governanca]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-08-18-contrato-de-IA-na-unidade-errada]]"
tags: [post, medium, 2026-W34]
---

# 📰 Medium — Custo por tarefa concluída: a unidade que falta no seu contrato de IA

**Título:** Custo por tarefa concluída: a unidade que falta no seu contrato de IA

**Dek:** Dois modelos com preço de tabela parecido resolveram as mesmas tarefas com consumo quatro vezes diferente. O problema não é o preço — é a unidade em que ele foi negociado.

---

Em agosto de 2026 a Artificial Analysis fez uma mudança editorial pequena e consequente: passou a publicar, junto com os benchmarks de qualidade, o **custo por tarefa concluída** (cost per completed task). Não o preço por milhão de tokens — o custo de levar uma tarefa agêntica até o fim.

Essa mudança de unidade é o assunto deste texto, porque ela desmonta a forma como praticamente todo contrato de fornecimento de IA foi assinado nos últimos três anos.

## O número

No AA-Briefcase, benchmark de tarefas agênticas, dois modelos de fronteira entregaram qualidade próxima com perfis de consumo muito distintos:

| | Turnos por tarefa | Tokens de entrada (total do benchmark) | Custo publicado |
|---|---|---|---|
| Grok 4.6 | ~53 | 0,5 bi | **US$ 0,84 / tarefa concluída** |
| Claude Opus 5 Max | ~103 | 2,0 bi | não publicado |

*Fonte: Artificial Analysis, 13/08/2026; anúncio do Grok 4.6 por x.ai em 12/08/2026.*

Duas honestidades sobre esta tabela, antes de qualquer conclusão:

**Primeira:** a Artificial Analysis publicou o valor por tarefa para o Grok 4.6. Não publicou o equivalente para o Opus 5 Max. A razão de 4x entre os consumos de entrada (2,0 bi contra 0,5 bi) indica ordem de grandeza, não um preço. Eu não vou multiplicar 0,84 por quatro e apresentar o resultado como dado — seria exatamente o tipo de número sem lastro que este texto critica.

**Segunda:** qualidade "próxima" não é qualidade igual. Se o modelo mais caro por tarefa entrega taxa de acerto materialmente superior no *seu* caso de uso, ele pode continuar sendo a escolha certa. A tese aqui não é "use o mais barato". É "meça na unidade certa antes de decidir".

## O mecanismo: onde o dinheiro realmente sai

Numa carga agêntica o modelo não responde uma vez e encerra. Ele entra num laço: chama uma ferramenta, lê o retorno, decide o próximo passo, chama de novo. Cada volta é uma requisição faturada — e o histórico acumulado viaja junto.

Isso cria três multiplicadores que a tabela de preço não captura.

### 1. Turnos por tarefa

O negócio contrata "tarefa resolvida". O fornecedor cobra token. Entre as duas unidades existe um número — turnos — que não aparece em nenhuma cláusula. Ele varia por modelo, por qualidade do prompt, por qualidade das ferramentas expostas ao agente, e por quão bem o caso de uso foi decomposto.

### 2. Reenvio de contexto

Este é o item que mais surpreende quem vê a fatura pela primeira vez.

A cada turno, o modelo precisa do histórico da tarefa. Sem cache de prefixo, esse histórico é reenviado inteiro. O custo de entrada, portanto, não cresce proporcionalmente ao número de turnos — cresce **mais rápido**:

```
tokens_entrada ≈ Σ (contexto_base + incremento × n)  para n = 1..N turnos
              ≈ O(N²)
```

É por isso que dobrar o número de turnos (53 → 103) quadruplicou o consumo de entrada (0,5 bi → 2,0 bi), e não apenas dobrou. Quem projeta orçamento assumindo relação linear entre complexidade e custo vai errar para menos, sempre.

**Consequência prática:** cache de contexto (prompt caching) deixa de ser otimização de latência e vira alavanca de custo de primeira ordem. Vale medir taxa de acerto de cache por caso de uso antes de trocar de modelo.

### 3. Retries

A tarefa que "concluiu" na terceira tentativa custou três vezes. As duas primeiras não produziram resultado, então não aparecem em nenhum relatório de valor entregue — mas apareceram na fatura.

É o custo mais invisível dos três, porque hoje, na maioria das arquiteturas, **consumo com resultado e consumo sem resultado são indistinguíveis no log**.

## Onde isso quebra na prática

**Na renegociação.** Você entra na mesa com dólar por milhão de tokens e sai com 12% de desconto. A fatura não se move, porque o gasto é governado por turnos e retries, não pela tabela.

**No roteamento.** Rotear a carga para o modelo mais barato por token pode *aumentar* a conta se ele precisar do dobro de turnos. Regra de roteamento escrita sobre preço de tabela é uma regra que pode andar para trás — e, pior, andar para trás silenciosamente, porque o dashboard de preço unitário vai continuar mostrando melhora.

**No business case.** Piloto roda com carga curta e supervisionada; produção roda com carga longa e autônoma. O custo por tarefa entre um e outro não escala — ele muda de regime.

## O contraponto

O argumento contrário é bom e merece ser dito inteiro.

Para carga curta e determinística — classificar um documento, extrair campos, resumir um texto — o preço por token continua sendo um proxy razoável do custo real, e é muito mais simples de contratar, auditar e comparar entre fornecedores. Trocar a unidade do contrato por uma métrica composta introduz complexidade de governança que nem toda operação precisa.

E há o contraponto que vem do próprio dado: **benchmark de eficiência é fotografia.** O Grok 4.7 já foi anunciado; o ranking vira. Quem re-arquiteta a esteira a cada release gasta mais em engenharia do que economiza em token — e ainda desestabiliza o que estava funcionando.

Os dois argumentos são válidos, e nenhum dos dois derruba a tese. A conclusão não é "persiga o modelo mais eficiente do mês". É: **pare de assinar contrato numa unidade que não mede o que você paga.** Trocar a unidade de medida é barato e permanente. Trocar de modelo é caro e temporário.

## O que eu faria

Três métricas, todas coletadas no proxy de inferência — o único ponto onde se mede sem instrumentar cada aplicação separadamente:

**1. Turnos por tarefa concluída — p50 e p95, por caso de uso.**
A média esconde exatamente a cauda que estoura a fatura. O p95 é o número que se leva para a renegociação.

**2. Taxa de retry e tokens queimados em tentativa perdida.**
Definição operacional: toda sequência que não atingiu o critério de conclusão do caso de uso conta como perdida, e seus tokens entram numa linha separada. Sem essa separação, não existe custo por tarefa *concluída* — existe custo por tentativa.

**3. Custo por tarefa concluída por rota.**
O mesmo caso de uso medido em cada modelo disponível, com a mesma definição de conclusão. Sem essa comparação pareada, roteamento é palpite com dashboard.

Com as três, trocar de fornecedor vira decisão operacional com número em cima da mesa. Sem elas, vira projeto — e projeto não se aprova no meio do trimestre, que é justamente quando o preço muda.

Essa é a razão de existir do **Veltrix**: medir custo por tarefa e tratar re-roteamento como operação corrente, não como iniciativa. Quando o fornecedor muda de posição de preço a cada quatro semanas, a camada que permite responder em dias deixou de ser otimização e virou **hedge**.

---

**Frameworks citados:** [[Matriz Adocao x Eficiencia de IA (AxE) - adocao vs custo por tarefa]] · [[Demonstracao de Resultado de IA (VCAT) - Valor, Custo, Atribuicao, Trilha]]
**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-08-18-contrato-de-IA-na-unidade-errada]]
**Notas relacionadas:** [[Custo por tarefa concluida substituiu o preco por token como unidade da IA]] · [[Integracao vertical dos labs derruba o preco por token - contrato fixo envelhece mal]]

## Fontes
1. Artificial Analysis — *Grok 4.6 benchmarks and analysis* (13/08/2026) — https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis
2. x.ai — *Grok 4.6* (12/08/2026) — https://x.ai/news/grok-4-6
3. VentureBeat — desempenho comparado do Grok 4.6 (13/08/2026)
4. Daily [[2026-08-13]] — via The Neuron e AINews
