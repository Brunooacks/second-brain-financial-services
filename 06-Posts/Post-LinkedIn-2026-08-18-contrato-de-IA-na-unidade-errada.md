---
tipo: post
data: 2026-08-18
canal: linkedin
registro: tecnico
status: rascunho
eixos: [economia-ia, financeiro, governanca]
maturidade: 3
medium: "[[Medium-2026-08-18-contrato-de-IA-na-unidade-errada]]"
tags: [post, linkedin, tecnico, 2026-W34]
---

# 🔧 Post Técnico — O seu contrato de IA está precificado na unidade errada

> Piloto do formato técnico. Tese da candidata nº 2 da [[Weekly-2026-08-14]]. Distinta de [[Post-LinkedIn-2026-08-01-custo-por-conversa]] (lá o tema é roteamento e custo variável da interface; aqui é a **unidade do contrato**).

---

## O seu contrato de IA está precificado na unidade errada.

Dois modelos com preço de tabela parecido acabaram de resolver o mesmo conjunto de tarefas com consumo quatro vezes diferente.

No AA-Briefcase, benchmark agêntico, o Grok 4.6 fechou as tarefas em **~53 turnos e 0,5 bilhão de tokens de entrada**. O Claude Opus 5 Max fechou as mesmas tarefas, com qualidade próxima, em **~103 turnos e 2,0 bilhões**. A Artificial Analysis parou de deixar essa conta implícita e passou a publicar a métrica direta: **US$ 0,84 por tarefa concluída** (Artificial Analysis, 13/08/2026).

Comparar fornecedor por dólar por milhão de tokens é comparar o preço do litro sem saber o consumo do carro.

### O mecanismo: o custo não mora no token, mora no turno

Numa carga agêntica, o modelo não responde uma vez. Ele entra num laço: chama ferramenta, lê o retorno, decide o próximo passo. Cada volta é uma nova requisição — e o histórico acumulado vai junto.

São três multiplicadores que a tabela de preço não enxerga:

**Turnos por tarefa.** A unidade que o negócio contrata é "tarefa resolvida". A unidade que o fornecedor cobra é token. Entre as duas existe um número que ninguém coloca no contrato.

**Reenvio de contexto.** O histórico volta inteiro a cada turno. O custo de entrada não cresce linearmente com o número de turnos — cresce mais rápido que isso. É por isso que 103 turnos consumiram 4x os tokens de 53, e não 2x.

**Retries.** A tarefa que "concluiu" na terceira tentativa custou três vezes. As duas primeiras não aparecem em lugar nenhum, porque não geraram resultado — só fatura.

### Onde quebra

Quebra na renegociação: você entra na mesa com dólar por milhão de tokens, sai com 12% de desconto num número que não governa o seu gasto, e a fatura não se move.

E quebra no roteamento. Mandar a carga para o modelo mais barato por token pode **aumentar** a conta, se ele precisar do dobro de turnos para fechar a mesma tarefa. Regra de roteamento escrita sobre preço de tabela é uma regra que pode andar para trás sem avisar.

### O contraponto honesto

Para carga curta e determinística — classificar, extrair, resumir um documento — o preço por token continua sendo um proxy razoável, e é muito mais simples de contratar. E benchmark de eficiência é fotografia: o Grok 4.7 já foi anunciado, o ranking vira. Quem re-arquiteta a cada release gasta mais em engenharia do que economiza em token.

Por isso a conclusão não é perseguir o modelo mais eficiente do mês. É parar de assinar contrato numa unidade que não mede o que você paga.

### O que eu instrumentaria primeiro

Três métricas, todas no proxy de inferência — o único ponto onde dá para medir sem instrumentar cada aplicação uma por uma:

1. **Turnos por tarefa concluída**, p50 e p95, segmentado por caso de uso. A média esconde exatamente a cauda que estoura a fatura.
2. **Taxa de retry e tokens queimados em tentativa perdida.** É o custo invisível: consumo sem resultado, hoje indistinguível de consumo com resultado.
3. **Custo por tarefa concluída por rota** — o mesmo caso de uso medido em cada modelo. Sem essa comparação, roteamento é palpite com dashboard.

Com as três, "trocar de fornecedor" vira uma decisão operacional com número. Sem elas, vira projeto — e projeto ninguém aprova no meio do trimestre. É exatamente isso que o **Veltrix** existe para medir: custo por tarefa e re-roteamento como operação, não como iniciativa.

---

*Escrevo sobre IA aplicada ao setor financeiro — governança, soberania de dados e a economia de rodar agentes em produção.*

**Brief de arte:** motivo de mecanismo — *um corredor de pedra imenso com duas portas idênticas ao fundo; do lado esquerdo um caminho curto e reto até a porta, do lado direito o mesmo trajeto desdobrado em dezenas de voltas sobre si mesmo. Uma silhueta minúscula no início do trajeto longo. O batente de uma das portas em vermelhão.* Conforme [[Identidade-Visual-Editorial]].

**Expansão Medium:** [[Medium-2026-08-18-contrato-de-IA-na-unidade-errada]]

**Fontes:**
- Artificial Analysis — benchmarks Grok 4.6, custo por tarefa concluída (13/08/2026) · https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis
- x.ai — anúncio Grok 4.6 (12/08/2026) · https://x.ai/news/grok-4-6
- VentureBeat — desempenho comparado
- Daily [[2026-08-13]] · nota [[Custo por tarefa concluida substituiu o preco por token como unidade da IA]]

> **Ganchos de variação (para testar):**
> - Dado-first: abrir em "53 contra 103 turnos. Mesmo resultado. Quatro vezes o custo."
> - Provocação: "Você negociou 12% de desconto numa unidade que não governa a sua fatura."
> - Analogia: abrir pelo preço do litro sem o consumo do carro e descer para o benchmark.
