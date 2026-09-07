---
tipo: ideia
data: 2026-06-21
status: crua
origem: auto-digest
fonte_daily: "[[2026-06-21]]"
eixos: [governanca, soberania, agentes]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Governança de agente que importa pra banco regulado é a que fica ACIMA do provedor — neutra e portável

## A tese
Quando os três grandes (Google, OpenAI, Anthropic) passam a vender a *camada de governança de agente*, comprar a governança embutida do mesmo lab que fornece o modelo recria o lock-in que a soberania deveria evitar. Para banco regulado, a régua do agente não pode depender de quem fornece o agente: governança defensável é a que fica acima do provedor, portável entre Claude/GPT/Gemini.

## Por que eu acredito nisso
Os três convergiram para vender controle, não só inteligência: Google (Gemini Enterprise + A2A em produção, 200+ modelos incluindo Claude), OpenAI (Codex/Frontier chegando a 3 mi de usuários semanais de agentes enterprise) e Anthropic (Managed Agents com MCP tunnels e sandboxes self-hosted). O gargalo do mercado migrou de "modelo bom" para "camada de controle" — e a EY (AI Pulse Survey Wave 3, pág 10–12, biblioteca) já mostrava 64% construindo in-house exatamente para não entregar o dado sensível ao modelo de terceiro. Se a governança vem amarrada ao provedor, terceiriza-se o controle a quem mais interessa que você não saia.

## Quem discordaria — e por quê
Quem defende governança nativa do provedor: ela é mais profunda, mais barata, integra-se sem fricção e entrega no dia 1; uma "camada neutra acima de todos" é abstração que cobra imposto de performance e fica sempre atrás das features nativas. Em volume único de fornecedor, lock-in é trade-off aceitável por velocidade. É um contraponto real — a tese só se sustenta para quem é multi-provedor por mandato regulatório ou de soberania.

## O que eu faria / recomendaria
Posicionar o Cohort como governança soberana *acima* do provedor — mandato de agente (limite, escopo, jurisdição, trilha) portável entre modelos — e o Veltrix como o roteamento/FinOps que torna a política de residência auditável por jurisdição e sensibilidade. No pitch, contrastar de frente "governança embutida do provedor" (amarra) vs "governança soberana portável" (opcionalidade). Banco regulado não pode ter a régua do agente refém do fornecedor do agente.

## Lastro
- [[2026-06-21]] — clusters 🤖 Agentes & Força de Trabalho e 🌐 Soberania da Informação
- Bloomberg (Google agentes), CNBC (coding models), llm-stats (jun/2026)
- Anthropic — Claude Managed Agents (self-hosted sandboxes, MCP tunnels)
- EY AI Pulse Survey Wave 3 (64% in-house · pág 10–12, biblioteca)

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** governança/soberania  ·  **Setor:** Financeiro
