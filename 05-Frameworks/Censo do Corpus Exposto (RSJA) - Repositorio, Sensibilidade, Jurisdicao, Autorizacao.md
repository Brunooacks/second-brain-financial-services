---
tipo: framework
data: 2026-07-16
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-16]]"
eixos: [soberania, governanca, financeiro]
tags: [framework, auto]
---

# 🧱 Censo do Corpus Exposto (RSJA) — Repositório, Sensibilidade, Jurisdição, Autorização

## O problema que ele resolve
Quando a casa liga busca por IA de terceiro sobre um repositório de conhecimento (Slack, Notion, Drive, Confluence), o valor não está no modelo — está no **acervo** que ele passa a indexar e tornar consultável. Terceirizar o modelo é reversível (troca-se de fornecedor); terceirizar a residência do acervo cria dependência estrutural. Quase ninguém governa essa camada — a **soberania de conhecimento** (knowledge sovereignty), um degrau acima da soberania de modelo. O RSJA transforma "temos IA na colaboração" em um censo auditável do que já saiu de casa.

## O framework
Para **cada repositório de conhecimento**, preencha quatro colunas:

1. **R — Repositório**: qual acervo (Slack, Notion, Drive, Confluence, e-mail, wiki de engenharia).
2. **S — Sensibilidade**: classificação do conteúdo indexado (contratos, decisões de risco, arquitetura, PII → alta; documentação pública → baixa).
3. **J — Jurisdição**: onde reside o índice gerado pela IA de terceiro — país/fornecedor e sob qual regime de acesso.
4. **A — Autorização**: existe mandato escrito de que aquele acervo podia ser indexado e sair de casa? Quem assinou? (coluna vazia = soberania cedida por default).

Lógica de leitura: qualquer linha com **S=alta + J=fora + A=vazia** é uma exposição de soberania não-governada — prioridade de comitê.

## Quando usar / quando NÃO usar
**Usar:** antes ou logo depois de ativar qualquer indexação por IA de terceiro sobre repositório interno; em due diligence de fornecedor de SaaS colaborativo; quando o board pergunta "onde mora o nosso conhecimento operacional?".
**Não usar** como controle de fluxo de query/prompt em tempo real — isso é a [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]] (governa a inferência que *sai*). O RSJA é inventário do **estoque** de acervo exposto, não do fluxo. Também não confundir com a [[Matriz de Proveniencia do Dado (PCT) - Proprio, Compartilhado, Terceiro]] (classifica a *origem* do dado, não a exposição do corpus à indexação).

## Aplicado na prática
Caso Nubank (135 mi de clientes): ao tornar o Slackbot da Salesforce a "camada operacional", o acervo de contratos, aprovações de orçamento e avaliações de risco entra como **R=Slack, S=alta, J=fornecedor americano, A=?**. Se a coluna A estiver vazia, o RSJA mostra ao board em 30s que a residência do corpus foi decidida pela conveniência da ferramenta, não pela política do banco. A instrumentação da coluna J (roteamento por jurisdição/sensibilidade) é terreno da **Veltrix**; a coluna A (mandato escrito) é o que o **Cohort** formaliza.

## Como cito isto num board
"Antes de comemorar a IA na colaboração, me mostrem o RSJA: para cada repositório, quão sensível é o que ele guarda, sob qual jurisdição o índice reside e quem autorizou a saída — se a coluna Autorização estiver vazia, a soberania já foi cedida no varejo."
