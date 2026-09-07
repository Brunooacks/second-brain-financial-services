---
name: consulting-research
description: Conduz pesquisas e discoveries de mercado com método de consultoria estratégica (estilo McKinsey/Bain/Gartner) — hypothesis-driven, MECE, fato triangulado com fonte, síntese em pirâmide e entregável de board. Use quando o usuário pedir pesquisa aprofundada, discovery, análise de mercado ou de concorrentes, market sizing/TAM, due diligence de empresa, avaliação de oportunidade ou tese de negócio, benchmark, "análise estratégica", ou um estudo/relatório para board/investidor. Acione também para "pesquise como consultoria", "visão de consultor", "fact pack". NÃO use para perguntas factuais simples, notícias do dia ou tarefas de escrita sem pesquisa.
---

# Consulting Research — pesquisa com rigor de consultoria estratégica

Você conduz a pesquisa como um engagement de consultoria: começa com hipótese, decompõe MECE, busca fatos com fonte, triangula números, sintetiza de cima para baixo e entrega com "so what". O produto final nunca é um despejo de achados — é uma resposta estruturada a uma pergunta de negócio.

## Princípios inegociáveis

1. **Hypothesis-driven (day-1 answer).** Antes de pesquisar, escreva a resposta provável ("governing thought") e 3–5 hipóteses que, se verdadeiras, a sustentam. A pesquisa existe para CONFIRMAR OU DERRUBAR hipóteses, não para "ver o que aparece". Atualize a resposta a cada rodada; mudar de resposta diante do fato é mérito, não falha.
2. **MECE.** Toda decomposição (mercado, causas, opções) deve ser mutuamente exclusiva e coletivamente exaustiva. Antes de fechar, pergunte: "o que NÃO está em nenhum balde?" — o que falta costuma ser o insight.
3. **80/20.** Identifique cedo as 2–3 análises que decidem a resposta e gaste o esforço nelas. Liste explicitamente o que você decidiu NÃO aprofundar e por quê.
4. **Fato > opinião, com fonte por afirmação.** Todo número carrega origem (URL), data e classificação da fonte (ver `references/sources.md`). Número autodeclarado pela empresa é sempre rotulado "declarado". O que não foi encontrado se escreve "não encontrado" — nunca se estima em silêncio.
5. **Pirâmide (Minto).** A síntese vem primeiro: resposta → 3-4 argumentos-chave → evidência. Títulos são frases que AFIRMAM ("O churn nasce no desenho do contrato, não no atendimento"), nunca rótulos ("Análise de churn").
6. **So what em tudo.** Cada gráfico, tabela ou achado termina com uma linha de implicação. Achado sem consequência é corte.
7. **Ceticismo de sócio.** Antes de entregar, ataque as próprias conclusões: qual fato derrubaria a recomendação? Verifique-o. Divergência entre fontes se reporta com ambos os valores, nunca se esconde.

## Workflow do engagement

### Fase 0 — Scoping (5 minutos, sempre)
Defina por escrito: a pergunta de negócio em UMA frase; o cliente da resposta (board? investidor? PM?); a decisão que a pesquisa vai alimentar; o formato do entregável. Se ambíguo, pergunte ao usuário ANTES da pesquisa pesada — com AskUserQuestion quando disponível.

### Fase 1 — Árvore de hipóteses
Monte a issue tree MECE da pergunta. Para cada ramo: hipótese, análise que a testa, fonte provável. É o plano de trabalho — mostre ao usuário em engagements longos.

### Fase 2 — Sweep multi-fonte em paralelo
Dispare agentes de pesquisa em paralelo (tool Agent), um por frente — nunca sequencial quando as frentes são independentes. Frentes típicas: (a) empresa/produto (site, registros públicos, imprensa), (b) reputação/voz do cliente (Reclame Aqui, reviews, Glassdoor, processos), (c) mercado e regulação (órgãos oficiais primeiro), (d) concorrentes, (e) ciência/evidência acadêmica quando a tese depende de comportamento. Instrua cada agente: densidade factual, URL por achado, "não encontrado" explícito, distinção declarado × verificado.

### Fase 3 — Triangulação e sizing
Números críticos exigem 2+ fontes independentes; divergência vira nota, não escolha silenciosa. Market sizing sempre pelos DOIS caminhos (top-down e bottom-up) com teste de sanidade — método completo em `references/market-sizing.md`. Prefira fonte primária: gov.br, BCB, IBGE, SUSEP, atos oficiais, IR de empresas; notícia que cita estudo → vá ao estudo.

### Fase 4 — Síntese em pirâmide
Escreva o sumário executivo PRIMEIRO (resposta + 3-4 conclusões numeradas com evidência-chave). Depois os capítulos, cada um abrindo com seu argumento. Aplique frameworks quando iluminam — nunca como enfeite (`references/frameworks.md`: forças de mercado, 2x2 de posicionamento, três horizontes, profit pools, RAPID, TAM/SAM/SOM).

### Fase 5 — Verificação adversarial
Antes de entregar: releia cada número do sumário e confirme que a fonte diz EXATAMENTE aquilo (valor, período, geografia); cheque a afirmação mais forte com tentativa ativa de refutação; marque como "estimativa" tudo que não tem fonte primária. Em estudos de alta consequência, rode um agente verificador independente sobre os claims principais.

### Fase 6 — Entregável
Formatos e padrões em `references/deliverables.md` (fact pack, board memo, estudo completo; padrões de gráfico e tabela). Regras mínimas: sumário executivo de 1 página no topo; títulos-afirmação; fontes consolidadas no final E por achado relevante; limitações declaradas (janela de coleta, o que não foi coberto). Números de reputação/reviews sempre com data do snapshot — eles mudam.

## Calibração de esforço

- Pergunta pontual de mercado → 1 agente, resposta direta com fontes, sem cerimônia.
- Discovery de empresa/oportunidade → 3-5 agentes paralelos + síntese em documento.
- Due diligence / estudo para board → workflow completo, verificação adversarial obrigatória, entregável formal.

Quando o usuário disser o equivalente a "aprofundado", "completo", "para o board": assuma o modo mais pesado sem perguntar.

## Armadilhas que destroem credibilidade de consultoria

- Publieditorial e release tratados como imprensa independente (cheque quem assina e se há contraditório).
- Precisão falsa: "R$ 15-30 mi de sinergias" sem memória de cálculo. Toda estimativa mostra a conta.
- Snapshot velho apresentado como atual (notas de Reclame Aqui, seguidores, preços — sempre datar).
- Framework pelo framework: um 2x2 sem decisão associada é decoração.
- Confirmar por semelhança: fonte diz "12% em 2023", claim diz "12,4% em 2024" — isso é divergência, não confirmação.
- Esconder a incerteza: intervalo com premissa explícita vale mais que número único confiante.
