---
tipo: atencao
data: 2026-08-01
status: aberto
origem: auto-digest
fonte_daily: "[[2026-08-01]]"
horizonte: curto
eixos: [governanca, soberania, financeiro]
tags: [atencao, auto]
---

# ⚠️ A partir de 02/08 o risco regulatório do EU AI Act para o banco não está no que o banco faz — está no que seu fornecedor de GPAI faz

## O sinal
Amanhã (02/08/2026) entram em vigor os **poderes de enforcement do Capítulo V** do EU AI Act sobre provedores de GPAI (general-purpose AI): a Comissão Europeia passa a poder requisitar documentação, conduzir avaliações, exigir medidas corretivas (mitigação, restrição de mercado, **recall do modelo**) e multar em até **3% do faturamento global ou €15 mi, o que for maior** (*artificialintelligenceact.eu · ComplianceHub · AccuroAI*). As obrigações dos labs existem desde 08/2025; o que muda agora é o **poder de punir**. Na direção oposta, o **Digital Omnibus** (acordo provisório de 07/05/2026) adiou as obrigações de alto risco do Annex III — que inclui **credit scoring** — para **02/12/2027**.

## Por que monitorar
Leia os dois prazos juntos: o regulador europeu decidiu apertar primeiro **os labs** e dar fôlego **aos usuários corporativos**. Para um banco, o risco regulatório imediato não é a sua própria conformidade — é a **cadeia de fornecimento**: se meu provedor de GPAI for multado, restringido ou forçado a recall, minha operação herda a interrupção sem ter sido a infratora. Isso reclassifica cláusula de continuidade contratual e plano de fallback multi-modelo de "luxo de arquitetura" para **mitigação de risco de terceiros**. E o adiamento do credit scoring para dez/2027 não é perdão — é tempo de arrumar a casa com a norma já conhecida, não desculpa para adiar. Distinto de [[Art 50 do EU AI Act em vigor 02-08 vira o benchmark de facto de transparencia no Brasil]] (que trata da obrigação de transparência do próprio banco) e de [[Soberania de modelo virou risco de continuidade, nao tese]] (indisponibilidade por export control/kill switch de outra jurisdição): aqui o gatilho é **enforcement regulatório sobre o lab** virando risco de continuidade a jusante.

## Gatilhos pra reavaliar
- Primeira ação pública de enforcement da Comissão contra um provedor de GPAI usado por instituição financeira (documentação exigida, medida corretiva ou multa).
- Primeiro caso de recall/restrição de um modelo que roda caso de uso crítico de banco BR.
- Bacen, ANPD ou regulador prudencial citando risco de fornecedor de GPAI / continuidade como risco operacional.
- Contratos de LLM de banco BR passando a incluir cláusula explícita de "provedor sob medida de enforcement".
- Sinal de que o prazo de dez/2027 (credit scoring) volta a ser antecipado ou é novamente adiado.

## Atualizações
- 2026-08-01: nota criada a partir da daily [[2026-08-01]]. Enforcement do Cap. V (GPAI) em vigor 02/08; multas de até 3% do faturamento global ou €15 mi; credit scoring (Annex III) adiado para 02/12/2027 via Digital Omnibus. Ângulo de risco de fornecedor/continuidade herdada, distinto das notas de transparência (Art. 50) e de kill switch. Conecta a [[Banco no board do fornecedor de IA transforma concentracao em risco competitivo]] pelo eixo de dependência de provedor único.
- 2026-08-02: **enforcement ativou hoje** (daily [[2026-08-02]]). "Ontem o assunto era prazo; hoje é operação." Janela assimétrica confirmada: até 12/2027 o custo pesado de conformidade está no fornecedor, não no banco — momento de negociar contrato barato (cláusula de "evidência de conformidade AI Act sob demanda" espelhando o que a Comissão pode pedir ao lab). Ação prática: cláusula de continuidade + fallback multi-provider = mitigação regulatória, não luxo de arquitetura. Novo ângulo derivado hoje (fronteira porosa provider/deployer): [[Fine-tuning substancial rebaixa o banco de deployer a provider no EU AI Act]].
