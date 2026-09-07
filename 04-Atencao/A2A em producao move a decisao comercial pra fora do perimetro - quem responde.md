---
tipo: atencao
data: 2026-08-18
status: aberto
origem: auto-digest
fonte_daily: "[[2026-08-18]]"
horizonte: curto
eixos: [agentes, financeiro, governanca]
tags: [atencao, auto]
---

# ⚠️ A2A saiu do slide e entrou num trilho de pagamento real — quem responde quando dois agentes combinam uma condição que nenhuma das empresas aprovou?

## O sinal
A **Cielo** colocou em produção (Fórum E-Commerce Brasil 2026) uma jornada de pagamento agêntico sobre três protocolos: **AP2** (pagamento iniciado por agente), **A2A** (agentes de empresas diferentes negociando entre si) e **MCP** (o agente lendo catálogo, preço e estoque do lojista). É o primeiro caso brasileiro em que **A2A sai do slide e entra num trilho de pagamento real** ([Varejo S.A./CNDL](https://cndl.org.br/varejosa/pagamentos-por-agentes-de-ia-avancam-no-forum-e-commerce-brasil-2026/) · [Mobile Time](https://www.mobiletime.com.br/noticias/28/07/2026/assistente-de-compras/); daily 2026-08-18). Os ganhos anunciados — **-60% no checkout, -30% no abandono, +15% em vendas, -20% no custo por operação** — são **projeção de fornecedor, não realizado auditado**; tratar como hipótese a testar, não baseline.

## Por que monitorar
Enquanto o agente é interno, o perímetro de risco termina na borda da instituição. Com A2A, **o agente do lojista negocia com o agente do cliente** — e uma parte da decisão comercial passa a ocorrer numa conversa entre duas máquinas que nenhuma das duas instituições controla sozinha. A pergunta de comitê deixa de ser "o agente errou?" e vira "**quem responde quando dois agentes de empresas diferentes combinam uma condição que nenhuma das duas aprovou?**". Isso não é fraude (aquele eixo está em [[Verifiable Intent - quem arbitra a disputa do agente define quem paga a fraude]]) nem defesa de canal lateral ([[A defesa do agent estate saiu do perimetro para o canal lateral entre agentes]]) — é **responsabilidade em cadeia comercial A2A**, um vazio contratual que só aparece quando o protocolo vai a produção. E ele chega junto com a janela de consulta pública do BC ([[Bacen estuda risco de IA antes de regular - janela para definir o vocabulario]]).

## Gatilhos pra reavaliar
- Qualquer disputa/estorno originado numa negociação A2A entre agentes de empresas distintas → primeiro teste real de "de quem é o passivo".
- Bandeira, adquirente ou BC tipificar responsabilidade em cadeia A2A → muda o desenho de alçada do agente.
- Cielo (ou concorrente) publicar número **realizado auditado** do checkout agêntico → converter a projeção -60%/-20% em baseline ou descartar.
- Exigir que a alçada do agente esteja **no protocolo**, não no discurso — é a condição para auditar a negociação.

## Atualizações
- 2026-08-18: nota criada a partir da daily. Eixo distinto de fraude/identidade ([[Verifiable Intent - quem arbitra a disputa do agente define quem paga a fraude]]) e de registro fragmentado de agente ([[Num marketplace de multiagentes o ativo critico nao e o catalogo e o registro]]) — aqui o vazio é **responsabilidade comercial em cadeia A2A em produção**. Conecta a [[No pagamento agentico o agente decide a regra liquida - o trilho continua burro]].
