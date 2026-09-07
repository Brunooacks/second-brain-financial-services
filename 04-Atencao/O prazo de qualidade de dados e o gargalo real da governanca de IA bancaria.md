---
tipo: atencao
data: 2026-08-20
status: aberto
origem: auto-digest
fonte_daily: "[[2026-08-20]]"
horizonte: curto
eixos: [governanca, financeiro, soberania]
tags: [atencao, auto]
---

# ⚠️ O prazo da Resolução Conjunta nº 18 é o gargalo real da governança de IA bancária

## O sinal
A **Resolução Conjunta nº 18** obriga as instituições financeiras a implementar **política de qualidade de dados (data quality) até o fim de 2026** — e o prazo, não a norma, virou o maior risco ([Finsiders](https://finsidersbrasil.com.br/regulamentacao/resolucao-conjunta-no-18-prazo-vira-o-maior-risco-da-qualidade-de-dados/)). Isso corre em paralelo a um setor que vai gastar **R$ 50,4 bilhões** em tecnologia em 2026 (+8% a/a, +58% em cinco anos), com **GenAI e cloud prioridade para 84%** das instituições ([Pesquisa Febraban de Tecnologia Bancária 2026 / Deloitte, 34ª ed., vol. 1, jun/2026](https://cmsarquivos.febraban.org.br/Arquivos/documentos/PDF/Pesquisa%20Febraban%20de%20Tecnologia%20Banca%CC%81ria%202026%20-%20Vol1.pdf)). O descompasso: bilhões indo para o modelo antes de o prazo do **insumo** fechar.

## Por que monitorar
Governança de dado é **pré-requisito** de governança de IA, nessa ordem — não o inverso. Um score antifraude, um modelo de crédito ou um agente em produção herdam a qualidade do dado que os alimenta; sem linhagem, residência e qualidade auditáveis, "IA auditável" é retórica. Se este prazo escorregar ou for cumprido só no papel (política de PDF, não configuração), o setor entra em 2027 com modelos em produção rodando sobre uma base que o próprio regulador já considera não conforme. É o mesmo padrão que vi no BC virando **operador de modelo** ([[Score de fraude centralizado do BC cria monocultura de risco antifraude]]): a régua regulatória chega pela via setorial (Bacen), antes do marco legal ([[PL 2338 vira modelo sancionatorio - SIA e sancao de ate R 50 mi enquanto os pilotos ja rodam]]).

## Gatilhos pra reavaliar
- Bacen sinalizar prorrogação, fiscalização ou primeira sanção ligada ao prazo de fim de 2026 → muda o horizonte e a urgência do backlog.
- Pesquisa Febraban/Deloitte de 2027 mostrar quanto dos R$ 50,4 bi foi para governança de dado vs. para modelo → confirma ou derruba a hipótese do descompasso.
- Cruzamento com a **Resolução Conjunta** de qualidade e o novo **score de fraude do Pix** (SPI/DICT): se o BC exigir qualidade de dado como condição de participação no score, o prazo deixa de ser interno e vira porta de acesso à infraestrutura.
- Contraponto a vigiar: pode-se argumentar que IA de fronteira tolera dado imperfeito e que exigir data quality completa antes de qualquer piloto é atrasar o setor. Reavaliar se surgir evidência de que modelos em produção degradam de forma tolerável — mas o ônus da prova é de quem afirma isso a um comitê de risco.

## O que eu diria num board
O gasto em IA é um número de **entrada**; o prazo da Resolução Conjunta nº 18 é o número de **saída** que ninguém coloca no slide. Antes de aprovar mais orçamento de modelo, eu perguntaria uma coisa: temos política de qualidade de dados versionada, com linhagem e residência por classe de dado, pronta para auditoria em dezembro? Se a resposta for "está em andamento", o backlog de conformidade dos próximos doze meses já existe — só não foi orçado. É onde o **Veltrix** ajuda por construção (proveniência e roteamento por jurisdição/sensibilidade dão o rastro do dado que a política exige).

## Atualizações
- 2026-08-20: nota criada a partir da daily (item "No Radar" sub-trabalhado; destilada na run de 2026-08-21 por fallback — a daily de hoje ainda não havia sido gerada).
