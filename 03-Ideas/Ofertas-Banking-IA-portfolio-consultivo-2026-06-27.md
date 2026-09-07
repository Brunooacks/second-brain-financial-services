---
tipo: oferta
data: 2026-06-27
status: madura
eixos: [governanca, soberania, financeiro, economia-ia, agentes, seguranca]
maturidade: 4
tags: [ofertas, go-to-market, banking, consultivo, perfis]
---

# 💼 Catálogo de Ofertas — Banking AI (portfólio consultivo NTT DATA)

> Base: síntese da semana 21–25/jun/2026 (edições One Banking AI Nº 12–15). Âncora: **portfólio consultivo**; Veltrix/Cohort entram como **aceleradores de entrega**, não como o produto vendido. Endereçamento em **dois níveis**: mensagem de board (quem assina) + aterrissagem por área (quem usa). *Uso interno — cruza com o estudo* Where To Play Banking · One Banking (MTP 27-29).

---

## 🎯 A leitura que sustenta o catálogo

A semana fechou uma tese: o setor financeiro BR saiu de "qual modelo" para "como governar a frota de agentes em produção". Os números de adoção já são manchete — Itaú entregando software em 14h (era 18 dias), Nubank com AI Private Banker para 15M de usuários, BB com 12 mil agentes, Bradesco com ~20 agentes por pessoa. O que **ninguém** ainda opera bem, e por isso é a dor vendável:

1. **Governança da frota** — agentes em produção sem mandato, trilha e curva de autonomia explícita (e a régua "controle comprovável" da CMN 5.274/BCB 538 migrando para IA).
2. **Economia da frota** — investimento em IA +61%, mas custo por agente/decisão não instrumentado (FinOps de inferência).
3. **Soberania** — "dependências comuns" (Comef) e risco de "kill switch" de modelo estrangeiro.
4. **Antifraude agêntica** — 89% das IFs viram fraude subir; 90% apontam IA agêntica como a próxima arma do crime; 83% não conseguem distinguir agente legítimo de hostil (BioCatch).
5. **Crédito AI-native auditável** — inadimplência de neobancos triplicou (7,71%→20,31%); decisão automatizada sujeita ao art. 20 da LGPD.

Cada oferta abaixo ataca uma dessas dores, em dois níveis, com passo a passo e modelo de comercialização.

---

## 🧭 Matriz dor → oferta (visão rápida)

| # | Oferta | Dor de board | Dor de área | Gatilho de venda desta semana |
|---|--------|--------------|-------------|-------------------------------|
| 1 | **AI Agent Governance & Mandate** | "Temos milhares de agentes e não sei quem responde por eles" | Time sem padrão de mandato/promoção a produção | BB 12 mil agentes; CMN 5.274 "controle comprovável" |
| 2 | **FinOps de IA (custo por agente/decisão)** | "Gastamos +61% em IA e não sei o ROI real" | Conta de inferência opaca, sem teto por caso de uso | Itaú −44% custo infra; orçamento R$ 47,8 bi |
| 3 | **Soberania & Continuidade de Modelo** | "Estamos reféns de um fornecedor de fora?" | Sem plano B de modelo por jurisdição | Comef "dependências comuns"; AI kill switch |
| 4 | **Antifraude Agêntica (defesa agente-vs-agente)** | "A IA virou arma contra nós?" | Funil agentic sem stress-test; sem identidade de agente | BioCatch 89%/90%/83%; agentic commerce |
| 5 | **Crédito AI-native Auditável (LGPD art. 20)** | "Nosso motor de crédito é defensável num pedido de revisão?" | Decisão automatizada sem trilha nem baseline | Inadimplência neobancos 7,71%→20,31% |

---

## 1) AI Agent Governance & Mandate Design

**Dor que resolve.** *Board:* "colocamos agentes em produção mais rápido do que conseguimos governá-los — e não sei quem responde por cada um." *Área:* engenharia/risco sem padrão para definir escopo, ponto de revisão humana e promoção de um agente a produção. A régua de cyber (CMN 5.274/BCB 538) já exige "controle comprovável"; o mesmo padrão probatório vai bater na camada de agente.

**O que é.** Diagnóstico + framework de governança da força de trabalho de agentes: catálogo de agentes (estate), mandato por agente (limite, escopo, jurisdição, trilha), desenho da **curva de autonomia** (o que roda autônomo × híbrido × humano), gates de promoção a produção e trilha de auditoria. Ancorado em NIST AI RMF e ISO 42001.

**Step-by-step (6–10 semanas).**
1. *Discovery (1 sem):* inventário do estate de agentes e mapeamento de quem "é dono" hoje.
2. *Diagnóstico (2 sem):* gap contra NIST AI RMF / ISO 42001 e contra o padrão "controle comprovável" do Bacen.
3. *Desenho (2 sem):* template de mandato de agente + curva de autonomia por classe de tarefa + matriz human-in-the-loop.
4. *Piloto (2–3 sem):* aplicar a 2–3 fluxos críticos (ex.: agente de atendimento, agente de código, agente de crédito).
5. *Operacionalização (1–2 sem):* runbook de promoção a produção + painel de trilha (acelerador: **Cohort**).

**Como comercializar.** Porta de entrada: um *Agent Governance Assessment* de 2 semanas, preço fixo (foot-in-the-door). Sponsor: CRO/CISO/Head de Risco de Modelo. Gatilho: "o BB já opera 12 mil agentes; quantos dos seus têm dono, escopo e log?". Expansão natural: do assessment para o framework e depois para o managed service de governança.

**Perfis que entregam.** AI Governance Lead · AI Risk & Compliance Specialist (Bacen/LGPD) · Responsible AI Architect · AgentOps Engineer.

**O que eu diria num board.** Escala de agentes sem mandato é passivo de auditoria esperando acontecer. O entregável não é um documento de política — é a capacidade de provar quem aprovou o quê, com qual escopo, em produção.

---

## 2) FinOps de IA — custo por agente e por decisão

**Dor que resolve.** *Board:* "aumentamos 61% o investimento em IA e não consigo dizer o ROI real por caso de uso." *Área:* conta de inferência opaca, sem teto por agente, sem build-vs-buy auditável. ROI de IA sem custo de inferência é fé, não FinOps.

**O que é.** Implantação de uma disciplina de FinOps de IA: instrumentação de custo por inferência, por agente e por decisão; painel de unit economics ("custo de IA por interação atendida"); política de teto/alerta por caso de uso; decisão build-vs-buy auditável e roteamento por custo/sensibilidade. Acelerador: **Veltrix** (proxy de LLM com observabilidade, método CARO).

**Step-by-step (6–8 semanas).**
1. *Baseline (1–2 sem):* levantar o gasto atual de IA por fornecedor, caso de uso e área.
2. *Instrumentação (2 sem):* proxy/observabilidade para capturar custo por inferência e atribuir por agente/decisão.
3. *Unit economics (1 sem):* definir e calcular o indicador de board (custo por interação/decisão atendida).
4. *Política (1 sem):* tetos, alertas e gates de aprovação por caso de uso.
5. *Otimização (1–2 sem):* roteamento por modelo/jurisdição/sensibilidade; relatório de economia comprovada.

**Como comercializar.** Porta de entrada: *AI Cost Audit* de 3 semanas que devolve "quanto você gasta hoje e onde está o desperdício", com economia estimada. Sponsor: CFO/COO + Head de Plataforma de IA. Gatilho: "o Itaú cortou 44% de custo de processamento com arquitetura certa; você sabe seu custo por agente?". Modelo: fixo no audit, recorrente no managed FinOps (% da economia comprovada como upside).

**Perfis que entregam.** FinOps de IA / AI Cost Engineer · Plataforma/MLOps Engineer · Arquiteto de Soluções de IA.

**O que eu diria num board.** O número fiduciário não é "quanto investimos em IA", é "quanto cada agente custa por decisão". Quem instrumentar primeiro transforma "gastamos em IA" em "sabemos o que cada agente nos custa" — e o resto vira corte defensável.

---

## 3) Soberania & Continuidade de Modelo

**Dor que resolve.** *Board:* "se um fornecedor de fora desligar o modelo, nossa decisão de crédito/antifraude para?" *Área:* nenhum plano B de modelo por jurisdição; residência de dados mal mapeada. O Comef nomeou "dependências comuns" como risco sistêmico; o "kill switch" de export control deixou de ser hipótese.

**O que é.** Assessment de risco de concentração de modelo + arquitetura de continuidade: mapa de dependência por caso de uso crítico, roteamento por jurisdição/sensibilidade, residência de dados, e ao menos uma alternativa soberana pronta para assumir. Enquadrado como **hedge de continuidade**, não compliance. Acelerador: **Veltrix** (roteamento por jurisdição com log).

**Step-by-step (5–7 semanas).**
1. *Mapa de dependência (1–2 sem):* para cada caso crítico, qual modelo/fornecedor/jurisdição.
2. *Análise de risco (1 sem):* exposição a kill switch, preço, dado e disponibilidade.
3. *Arquitetura (2 sem):* roteamento por jurisdição, residência de dados, plano B soberano.
4. *Prova (1 sem):* simulação de failover de modelo + log auditável.
5. *Painel de board (1 sem):* "% de carga em jurisdição estrangeira" e "plano B por caso de uso".

**Como comercializar.** Porta de entrada: *Model Concentration Risk Review* de 2 semanas → um slide de risco que o board nunca viu. Sponsor: CRO/Comitê de Risco + CISO. Gatilho: "para cada decisão crítica, qual seu plano B se o modelo sair do ar amanhã?". Expansão: do review para a implantação de roteamento e managed continuity.

**Perfis que entregam.** Sovereign AI Architect · AI Risk Specialist · Arquiteto de Dados (residência/jurisdição) · Security/Compliance Lead.

**O que eu diria num board.** Soberania de IA não é nacionalismo — é o "dependências comuns" do Comef lido como risco de continuidade. Roteamento por jurisdição e uma alternativa soberana são hedge contratável, não linha de compliance.

---

## 4) Antifraude Agêntica — defesa agente-contra-agente

**Dor que resolve.** *Board:* "a IA virou arma contra o banco?" *Área:* funil de agentic commerce sem stress-test; impossível separar ação legítima assistida por IA de ataque. BioCatch: 89% das IFs viram fraude subir, 90% apontam IA agêntica como próxima arma do crime, 83% não conseguem distinguir legítimo de malicioso.

**O que é.** Programa de defesa para a era agêntica: identidade e mandato do agente como controle antifraude, stress-test do funil agentic contra fraude sintética, desenho do SOC com agentes (o que detecta autônomo × o que exige human-in-the-loop), e métrica de "% de ações iniciadas por agente com identidade verificável". Cruza com a régua "controle comprovável" da cyber.

**Step-by-step (8–12 semanas).**
1. *Threat model agêntico (2 sem):* mapear onde voz/pagamento/crédito por agente ampliam a superfície.
2. *Stress-test (2–3 sem):* funil agentic contra fraude sintética; medir taxa de não-distinção (o 83%).
3. *Identidade de agente (2 sem):* desenho de mandato/identidade como gate antifraude.
4. *SOC agêntico (2 sem):* curva de autonomia da defesa + custo por varredura (FinOps cruzado).
5. *Operação (2 sem):* runbook + indicadores de board + trilha por correção.

**Como comercializar.** Porta de entrada: *Agentic Fraud Readiness* de 3 semanas com um red-team do funil agentic. Sponsor: Head de Fraude/Prevenção a Perdas + CISO. Gatilho: "90% dos seus pares já dizem que a IA agêntica é a próxima arma do crime — seu funil de 'faça por mim' foi testado contra isso?". Modelo: fixo no readiness, recorrente no programa.

**Perfis que entregam.** Agentic Fraud Architect · AI Security Engineer (prompt injection / tool exfiltration) · Fraud Data Scientist · Identity/Access Architect.

**O que eu diria num board.** A defesa migra de "detectar comportamento anômalo" para "provar identidade e mandato do agente". Sem identidade de agente, não dá para separar o "faça por mim" do cliente do "faça por mim" do fraudador.

---

## 5) Crédito AI-native Auditável (LGPD art. 20 + Open Finance)

**Dor que resolve.** *Board:* "nosso motor de crédito por IA é defensável quando um cliente pedir revisão humana?" *Área:* decisão automatizada sobre Open Finance sem trilha por decisão nem baseline de inadimplência provisionado. Inadimplência de neobancos saltou 7,71%→20,31% (2021–2025): crédito AI-native cresceu base e calote junto.

**O que é.** Governança do ciclo de vida do modelo de crédito: trilha por decisão (art. 20 LGPD — caminho de revisão humana registrado), baseline e monitoramento de inadimplência por safra, explicabilidade da negativa, e controle de viés. Posiciona governança publicada como diferencial de marca (benchmark: Guia de IA Ética do BB).

**Step-by-step (8–10 semanas).**
1. *Diagnóstico (2 sem):* onde a IA nega crédito sem caminho de revisão registrado.
2. *Trilha por decisão (2 sem):* fluxo auditável de revisão humana (art. 20) + logging.
3. *Baseline de risco (2 sem):* inadimplência por safra, provisionamento do erro de modelo.
4. *Explicabilidade & viés (2 sem):* razão da negativa + testes de viés documentados.
5. *Pacote de evidência (1–2 sem):* dossiê "controle comprovável" pronto para regulador/auditoria.

**Como comercializar.** Porta de entrada: *Credit Model Governance Gap* de 2 semanas. Sponsor: CRO + Head de Crédito + DPO. Gatilho: "a inadimplência AI-native quase triplicou; seu modelo tem baseline provisionado e trilha de revisão?". Expansão: do gap para a esteira de governança de modelo de crédito.

**Perfis que entregam.** AI Risk & Model Governance Lead · Credit Risk Data Scientist · DPO/Privacy Counsel (LGPD) · MLOps Engineer.

**O que eu diria num board.** Modelo de crédito sem baseline de inadimplência e sem trilha de revisão é fé, não risco gerido. Governança publicada é diferenciação barata — vira confiança vendável antes de virar compliance obrigatório.

---

## 👥 Perfis que podemos ofertar (staffing / squad-as-a-service)

Além dos projetos, há demanda para **alocação de perfis** escassos. Pacote sugerido — "AI Governance & Economics Squad":

- **AI Governance Lead** — desenha mandato, curva de autonomia e gates de produção.
- **FinOps de IA / AI Cost Engineer** — instrumenta e otimiza custo por inferência/agente.
- **AI Risk & Compliance Specialist (Bacen/LGPD/EU AI Act)** — traduz regra em controle comprovável.
- **Sovereign AI Architect** — roteamento por jurisdição, residência de dados, plano B de modelo.
- **Agentic Fraud / AI Security Engineer** — defesa agente-vs-agente, identidade de agente.
- **Responsible AI Architect** — NIST AI RMF / ISO 42001, explicabilidade, viés.
- **AgentOps / MLOps Engineer** — promoção a produção, observabilidade, trilha.

**Como comercializar perfis.** Entrada por projeto (o assessment abre a porta), saída por squad alocado ou managed service. Diferencial: perfis que falam board e área ao mesmo tempo — raro no mercado, e exatamente o que a curva de autonomia exige.

---

## 🚀 Go-to-market — sequência land-and-expand

1. **Land (porta de entrada barata e rápida):** um assessment de 2–3 semanas, preço fixo, por dor (governança, custo, soberania, fraude ou crédito). Entrega sempre **um artefato de board** (um slide/indicador que o executivo nunca viu).
2. **Prove (piloto):** aplicar a 2–3 fluxos críticos reais, com métrica antes/depois e trilha auditável.
3. **Expand (recorrência):** managed service (governança contínua, FinOps recorrente, defesa agêntica operada) e/ou squad alocado.
4. **Anchor (board):** trimestralmente, levar ao comitê os 3 indicadores fiduciários — % de agentes com mandato, custo de IA por decisão, % de carga em jurisdição estrangeira. São as métricas que ninguém reporta hoje e que prendem o relacionamento no nível executivo.

**Sequência de pitch (90 segundos):** "Vocês já têm os agentes [adoção é manchete]. O que vocês ainda não têm é prova de quem fez o quê, a que custo, sob qual jurisdição [a dor]. A régua do Bacen já saiu de 'ter política' para 'provar que funciona' [urgência]. Começamos com um assessment de 2 semanas que devolve um indicador que o board nunca viu [land]."

---

## ✅ Próximos passos sugeridos

- Escolher **1–2 ofertas-farol** para empacotar primeiro (recomendo #1 Governança e #2 FinOps — são as dores mais transversais e com gatilho mais quente esta semana).
- Transformar cada assessment num **one-pager de board** + deck de 6 slides.
- Definir a **tabela de preço de entrada** (assessment fixo) e o modelo de recorrência.
- Mapear, no estudo *Where To Play Banking (MTP 27-29)*, quais contas-alvo casam com cada dor.

---

**Fontes da semana (insumo):** One Banking AI Nº 12–15 (21–25/jun/2026); Itaú agentes 18d→14h e Laranjinha+ (TI Inside); Nubank AI Private Banker 15M MAU (Nu Videocast); BB 12 mil agentes / 36 mil em formação (TI Inside; Convergência); Bradesco ~20 agentes/pessoa (Convergência); BioCatch 89%/90%/83% (Let's Money; Biometric Update); inadimplência neobancos (Equifax Boa Vista via Finsiders); investimento IA +61% / R$ 47,8 bi (Febraban via Dock); Comef "dependências comuns" (Ata 65ª via Finsiders); CMN 5.274/BCB 538 (Matera; NDM); soberania/kill switch (CFR; AI Weekly).
