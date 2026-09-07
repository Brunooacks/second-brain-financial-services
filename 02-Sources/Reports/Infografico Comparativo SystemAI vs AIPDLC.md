---
tipo: source
classe: report
titulo: "Duas escolas, uma virada — System AI como disciplina de engenharia × AI PDLC operacional"
autor: NTT DATA
data_publicacao: 2026
data_captura: 2026-06-08
setor: [multissetor]
eixos: [agentes, governanca, economia-ia]
tags: [source]
---

**Fonte/autor/data** · NTT DATA, infográfico comparativo (PT, 1 pág). Confronta duas escolas sobre a virada agêntica: "System AI como disciplina de engenharia" (base Gartner/McKinsey) × "AI PDLC como modelo operacional 24h" (StartSe). É peça de posicionamento NTT.

**Tese central**
Mesma virada, duas profundidades. A escola A trata IA agêntica como **disciplina de engenharia** (auditável, com SLO e custo controlado); a escola B trata como **transformação operacional/cultural** (times se reorganizam, throughput acelera). NTT se posiciona como quem entrega a A — "narrativa de palco mobiliza desejo; disciplina de engenharia entrega produção".

**Achados-chave (as duas escolas)**
- **Escola A — System AI (engenharia):** foco em como sustentar IA agêntica em ambiente crítico/auditável; vocabulário Gartner rastreável (ADLC, AI TRiSM, Harness Engineering, Knowledge/Forward-Deployed Engineer); 4 perfis cravados (Arquiteto IA, Spec-Driven Engineer, SRE de IA, PO de IA), squad 3-5 humanos + frota de agentes. Evidência com fonte: **17% deployed, 60% planejando até 2027, 40% cancelados até 2027** (CIO Survey 2026, Hype Cycle Agentic AI).
- **Escola B — AI PDLC (operacional 24h):** foco cultural; vocabulário próprio + McKinsey (Day/Night Cadence, Digital Agent Factory, Spec-Driven); 6-8 papéis em 3 horizontes (PM→Product Definer, Dev→Product Builder, QA→AgentOps); escada de maturidade Vibe Coding → AI-Assisted → Augmented → Agentic Workflow → Digital Agent Factory. Métricas **sem fonte auditável**: 70→15 dias, -36% failed changes, 6x experimentos, +30% produtividade.
- **Os 5 pontos de convergência (consenso de mercado):** (1) humanos orquestram, agentes executam; (2) times menores + agentes especializados; (3) spec executável > prompt isolado; (4) métricas em tempo real como sistema operacional; (5) **governança desde o dia zero**.

**Conexão (governança / Veltrix / Cohort)**
A convergência é o mapa de produto do Bruno. "Métricas em tempo real como SO" + "ambiente auditável com SLO e custo controlado" = Veltrix (observabilidade/FinOps de LLM). "Humanos orquestram, agentes executam" + "governança desde o dia zero" = Cohort (governança de força de trabalho de agentes). O contraste A×B também é uma ferramenta de qualificação de fornecedor: quem só traz a narrativa B (métricas de palco sem fonte) está vendendo desejo, não produção.

**O que eu diria sobre isso num board**
O número que eu levaria é o da escola A, porque tem fonte: Gartner projeta **40% dos projetos agênticos cancelados até 2027**. Isso transforma a conversa — a pergunta do board não é "vamos adotar agentes?", é "como ficamos no lado certo dos 40%?". E a resposta está nos 5 pontos de convergência, com destaque para "governança desde o dia zero" e "métricas em tempo real" — exatamente os controles que justificam Veltrix e Cohort. O contraste honesto que eu faria: as métricas espetaculares (6x experimentos, +30% produtividade) vêm da escola sem citação auditável; em banco, eu não cito número sem fonte. Disciplina de engenharia, não narrativa de palco.
