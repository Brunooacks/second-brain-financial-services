---
tipo: framework
data: 2026-06-21
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-06-21]]"
eixos: [agentes, governanca, soberania, financeiro]
tags: [framework, auto]
---

# 🧱 O Mandato do Agente (ELJT) — todo agente em produção precisa de um mandato verificável

## O problema que ele resolve
Quando o agente do cliente inicia um pagamento (AP2 com Pix como trilho) ou um agente interno decide em produção, o controle de risco sai da tela do app e vai para o protocolo do agente. Sem um mandato explícito, "temos agentes" vira um arquipélago de POCs sem régua. O mandato responde, antes de promover qualquer agente a produção, as quatro perguntas que um board faz.

## O framework
Todo agente em produção carrega um **mandato verificável** com quatro eixos — **ELJT**:

- **E — Escopo:** o que o agente pode fazer (e o que não pode). Ações permitidas, dados que toca, sistemas que aciona.
- **L — Limite:** até quanto. Teto de valor, volume, taxa de chamada, custo de inferência — o limite é também FinOps, não só risco.
- **J — Jurisdição:** onde executa e onde o dado reside. Qual modelo/sandbox roda o quê por jurisdição e sensibilidade (residência de dado como pré-condição, não nice-to-have).
- **T — Trilha:** registro auditável de cada decisão — quem decidiu, com que modelo, sob que mandato. Sem trilha, "soberania" é fé.

É o equivalente, na governança de agente, ao *mandato* assinado do AP2: uma credencial que diz o que o agente pode comprar, até quanto e por quanto tempo.

## Quando usar / quando NÃO usar
**Usar:** ao promover qualquer agente a produção em ambiente regulado; ao avaliar plataforma de agente de fornecedor (o mandato é portável entre Claude/GPT/Gemini?); ao desenhar onboarding/crédito/pagamento assistido por IA.
**Não usar:** em protótipo isolado sem acesso a dado sensível ou a movimento de valor — aí o mandato vira burocracia que mata a experimentação. O mandato é o portão piloto→produção, não o portão da ideação.

## Aplicado na prática
No **Cohort**, o mandato ELJT é o objeto de governança do *agent estate*: cada agente promovido recebe escopo/limite/jurisdição/trilha e fica auditável acima do provedor. No **Veltrix**, o eixo J (jurisdição) e o L (limite de custo) viram roteamento executável — qual modelo/sandbox atende por jurisdição e sensibilidade, com FinOps por agente. ELJT conecta os dois produtos: Cohort define o mandato, Veltrix o executa e mede.

## Como cito isto num board
"Nenhum agente vai a produção sem mandato: o que pode fazer, até quanto, onde, e com que trilha — ELJT. É o que separa um agent estate governado de uma coleção de POCs."

## Atualizações
- 2026-07-14 · **proposta de 5º eixo — F (Finalidade)**, a partir da daily [[2026-07-14]]: o ELJT governa *o que* o agente faz, mas não *sob qual finalidade declarada* ele consome cada fonte de dado. Roberta/Belvo (cobrança agêntica que lê **saldo via Open Finance** para escolher a hora de ligar: **−60% de custo por dívida recuperada**) e Pierre/CloudWalk (**R$ 800 mi** acompanhados via Open Finance) mostram o buraco: consentimento dado para *servir* (crédito melhor) alimentando agente que *age* (cobrar melhor) — limitação de finalidade (LGPD art. 6º, I). **F = finalidade declarada por fonte de dado que o agente consome**, verificável em código e ligada à trilha (T). Decisão sua: promover a **ELJT+F** ou manter finalidade como atributo do eixo E (Escopo). Contexto e tese em [[A proxima fronteira de governanca de dado nao e residencia - e finalidade]]; proveniência da fonte em [[Matriz de Proveniencia do Dado (PCT) - Proprio, Compartilhado, Terceiro]].
