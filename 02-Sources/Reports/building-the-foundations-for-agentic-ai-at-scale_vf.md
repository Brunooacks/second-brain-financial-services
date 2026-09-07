---
tipo: source
classe: report
titulo: "Building the foundations for agentic AI at scale"
autor: Asin Tavakoli, Brian Goodman, Henning Soller, Kayvaun Rowshankish et al. (McKinsey Technology / QuantumBlack)
data_publicacao: 2026-04
data_captura: 2026-06-08
setor: [financeiro]
eixos: [agentes, governanca, risco, soberania]
tags: [source]
---

**Fonte/autor/data** — McKinsey Technology e QuantumBlack (AI by McKinsey), "Building the foundations for agentic AI at scale", abril 2026. Esforço coletivo de Asin Tavakoli (Düsseldorf), Brian Goodman e Kayvaun Rowshankish (NY), Henning Soller (Frankfurt), com Akshat Kumar, Carlos Barreto (São Paulo), Satyajit Parekh, Tancredi Litta Modignani e outros. Baseado no capítulo "No data architecture, no AI advantage" do livro *Rewired* (Wiley, 14 abr 2026).

**Tese central** — IA agêntica escala sobre dados fortes — "uma casa só é tão forte quanto sua fundação". O que separa quem extrai valor de quem não extrai não é número de pilotos, mas arquitetura de dados modular, qualidade contínua e operating model redesenhado para supervisão humano-agente.

**Achados-chave**
- Quase 2/3 das empresas já experimentaram agentes, mas menos de 10% os escalaram para valor tangível — gap brutal entre piloto e produção (pág 1-2).
- 8 em cada 10 empresas citam limitações de dados como o gargalo para escalar IA agêntica (pág 1).
- Sete princípios de arquitetura: tratar ingestão como produto; compartilhar significado (não só dados); uma fundação única para analytics e IA; confiança embutida por padrão (segurança, acesso, governança automáticas); interfaces estáveis (APIs); comportamento visível/mensurável; camada de execução controlada com guardrails (pág 3).
- Dois arquétipos: single-agent (um agente, múltiplas ferramentas em sequência) e multi-agent (agentes especializados via knowledge graphs e acesso fine-grained) — ambos quebram sem dados interoperáveis (pág 4).
- Quatro passos: agentificar poucos workflows de alto impacto; modernizar cada camada da arquitetura (evolutiva, não rebuild); qualidade de dados contínua em tempo real (não limpeza periódica); construir operating e governance model agêntico (pág 4-5).
- Modelo de governança federado: domínios de negócio governam o dia a dia (ontologias, modelos de domínio); times centrais de dados/IA mantêm plataformas, guardrails e oversight — equilíbrio entre autonomia e accountability enterprise (pág 9).

**Conexão** — É a peça de "como fazer" por trás da tese de governança agêntica. Detalha controles que conectam direto ao EU AI Act, NIST AI RMF e ISO 42001: lineage e auditabilidade automáticos, AI gateway controlando acesso a dados não-estruturados, telemetria built-in para logar toda ação de agente, guardrail agents monitorando comportamento, e identity-management como pré-requisito quando autonomia cresce. Para soberania, o ponto-chave é que governança "viaja com o dado" (lineage embarcado na pipeline, controle de acesso dinâmico por caso de uso/permissão) — habilitando residência por jurisdição. Cita protocolos de interoperabilidade emergentes: MCP, A2A e AP2 (pagamentos entre agentes). Fine-tuning de modelos menores e domésticos sobre dados próprios é apresentado como rota mais barata, resiliente e compliant.

**O que eu diria sobre isso num board** — O número que abre qualquer conversa é: 2/3 experimentaram, menos de 10% escalaram, e 80% culpam os dados. Isso reposiciona a discussão — não estamos atrasados em "comprar agentes", estamos atrasados em fundação de dados, e é aí que mora a vantagem defensável. O insight estratégico para o nosso núcleo (governança + soberania) é que governança não pode ser camada adicionada depois: a tese é "trust by default", governança que viaja embarcada no pipeline com lineage e auditabilidade automáticos — exatamente o que torna residência de dados por jurisdição auditável. Eu também levaria o argumento de fine-tuning doméstico: modelos menores sobre dados próprios são mais baratos E mais soberanos — alinha custo e controle, raro. Ressalva: é McKinsey/QuantumBlack promovendo o livro *Rewired* e o método "Rewired"; os sete princípios e quatro passos são bons como blueprint, mas genéricos — o trabalho duro de mapear nossos workflows e core legado bancário continua sendo nosso. O modelo federado (domínio governa, centro mantém guardrails) é o desenho organizacional que eu defenderia para o operating model de agentes.
