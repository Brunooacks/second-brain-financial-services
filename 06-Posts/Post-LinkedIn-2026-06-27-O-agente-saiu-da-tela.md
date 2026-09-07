---
tipo: post
data: 2026-06-27
canal: linkedin
status: rascunho
eixos: [agentes, governanca, financeiro, economia-ia, soberania]
maturidade: 4
tags: [post, linkedin, semana, 2026-W26]
---

# 📝 Post LinkedIn — O agente saiu da tela (e a fraude foi atrás)

> Long-form (~1.150 palavras). Voz: Bruno, diretor de tecnologia . Storytelling + tese própria + fecho de board. Síntese da semana 21–25/jun/2026.

---

## O agente saiu da tela e foi para o balcão. A fraude foi atrás.

Esta semana, um pequeno comerciante no Brasil olhou para a maquininha, falou em voz alta o valor da venda e a cobrança foi disparada. Sem digitar. Sem app. A IA generativa do Itaú na nova Laranjinha+ chegou a todos os clientes que têm o equipamento, e a cobrança por comando de voz virou produto de prateleira no ponto de venda (TI Inside, 24/jun).

Parece um detalhe. Não é. É o momento em que o agente de IA deixou de ser uma caixinha de texto dentro de um app e passou a ser a interface — no balcão, no bolso, no código.

No mesmo banco, agentes especializados já escrevem software regulado: um ciclo de produto que levava 18 dias foi entregue em 14 horas no modo 100% autônomo (TI Inside, 03/jun). No Nubank, o "AI Private Banker" já está na mão de mais de 15 milhões de usuários ativos, aconselhando sobre dívida e crédito (Nu Videocast, 11/jun). O Banco do Brasil opera mais de 12 mil agentes em produção e colocou 36 mil funcionários em formação de IA agêntica. O Bradesco fala em algo como 20 agentes para cada colaborador.

E aí, na mesma semana, veio o outro número. A BioCatch entrevistou 100 líderes de instituições financeiras brasileiras: 89% viram a fraude aumentar em 2026 — acima da média global de 81% — e 90% disseram que a IA agêntica será a principal vulnerabilidade que o crime organizado vai explorar. O dado que me tirou o sono não foi nenhum desses. Foi o 83%: a fração de líderes que admite que será extremamente difícil distinguir uma ação legítima assistida por IA de uma ação maliciosa.

Junte as duas pontas e você tem a história da semana em uma frase: **a mesma camada de agente que virou o motor de receita virou o vetor de ataque.**

## O que mudou de verdade (e não é a velocidade)

A leitura preguiçosa desta semana é "os bancos brasileiros estão correndo em IA". Verdade, mas é a manchete, não a notícia.

A notícia é que a pergunta de board mudou. Por dois anos, a discussão foi "qual modelo usar" e "onde aplicar IA". Essa pergunta morreu. Quando o Itaú entrega em 18 dias, 5 dias ou 14 horas dependendo de quanto humano você deixa no circuito, o que diferencia as três opções não é a capacidade do agente — é a **política de supervisão**. Os 5 dias do modo híbrido não são ineficiência. São o preço explícito de manter alguém assinando onde a decisão é regulada.

Ou seja: o ativo competitivo deixou de ser o modelo e passou a ser a **curva de autonomia** — saber, tarefa por tarefa, o que roda sozinho, o que exige human-in-the-loop, e por quê. Isso é uma decisão de governança, não um toggle de tecnologia.

E há um segundo número que quase ninguém abre. O investimento em IA no setor bancário brasileiro subiu 61% (Pesquisa Febraban de Tecnologia Bancária), o orçamento de tecnologia chegou a R$ 47,8 bilhões. Todo mundo publica adoção. Quase ninguém publica o custo por agente, por decisão, por inferência. ROI de IA sem o denominador de custo é fé, não FinOps. Com 12 mil agentes rodando, um movimento de 10% no custo de inferência é material — e invisível para quem não instrumentou.

## A conta que a euforia não mostra

Deixe-me trazer o número que mais me incomoda, porque ele é o contrato implícito de toda essa corrida. A inadimplência em cartões de neobancos saltou de 7,71% para 20,31% entre 2021 e 2025 — quase triplicou — enquanto a base de clientes cresceu menos de 15% no mesmo período (Equifax Boa Vista, via Finsiders). O crédito AI-native cresceu a base e cresceu o calote mais rápido ainda.

Não estou dizendo que a IA causou isso. Estou dizendo que o motor de crédito por IA sobre Open Finance é, ao mesmo tempo, a maior promessa de inclusão e a maior superfície de risco do sistema. E aqui o regulador já se mexeu: o Comef colocou em ata a hipótese de modelos de IA explorarem sozinhos vulnerabilidades do sistema financeiro, nomeando o risco de "dependências comuns" — a concentração que transforma a falha de um fornecedor em risco de todos. As resoluções CMN 5.274 e BCB 538 já trocaram "ter política de segurança" por "provar que ela funciona", com evidência, teste independente e rastreabilidade.

Esse padrão — o "controle comprovável" — é o ensaio do que vem para a IA. Sai o compliance de papel, entra o compliance demonstrável. Quem opera agente em produção vai precisar do mesmo: trilha de quem aprovou, evidência de teste, rastreabilidade da decisão.

## A tese que eu defendo

Por isso minha leitura para um board é direta, e ela tem um contraponto real — então é tese, não slogan.

**Quem vence a próxima fase do banking não terá o melhor modelo. Terá a melhor governança e a melhor economia da frota de agentes.** Mandato por agente (escopo, limite, jurisdição, trilha), curva de autonomia desenhada de propósito, custo de inferência medido por decisão, e opcionalidade soberana de modelo para quando — não se — um fornecedor de fronteira sair do ar.

O contraponto honesto: há quem diga que o modelo ainda é o fosso, que quem tiver o melhor foundation model e o melhor dado proprietário (como o Nubank, com 135 milhões de clientes) vence por capacidade bruta. É um argumento forte. Mas dado proprietário sem trilha por decisão é passivo regulatório esperando acontecer, e capacidade bruta sem FinOps é margem evaporando em silêncio. O fosso do dado é real; ele só não dispensa a governança — ele a torna mais urgente.

A boa notícia para quem está construindo agora é que a janela está aberta. A régua brasileira de IA ainda é "estudo", não "regra". Quem montar trilha de agente, residência de dados e custo por inferência hoje chega ao regulador como referência, não como alvo. E quando a Febraban escolhe "Agentes Inteligentes, Liderança Humana" como tema do evento do ano, com os cinco maiores CEOs no palco, o establishment bancário acabou de validar exatamente essa pauta — meses antes do evento.

## O que eu faria na segunda-feira

Se eu sentasse num comitê executivo amanhã, faria três perguntas e não sairia da sala sem resposta:

Primeiro: quantos dos nossos agentes em produção têm dono, escopo e log? Não "quantos agentes temos" — isso é adoção. "Quantos têm mandato" — isso é governança.

Segundo: qual o nosso custo de IA por interação atendida, e como ele se move trimestre a trimestre? Se ninguém souber responder, não temos FinOps de IA; temos uma conta aberta.

Terceiro: para cada decisão crítica — crédito, antifraude, defesa cibernética — qual o nosso plano B de modelo em outra jurisdição se o atual sair do ar? Soberania não é nacionalismo; é gestão de risco de continuidade.

A camada de agente já é o produto e já é o risco. A diferença entre os bancos que vão liderar e os que vão virar trilho burro não está em adotar IA — todo mundo vai adotar. Está em quem consegue provar quem fez o quê, com qual escopo e a que custo.

O resto é manchete.

---

*Curadoria e tese: Bruno Oliveira · Escrevo sobre IA aplicada ao setor financeiro — governança, soberania de dados e a economia de rodar agentes em produção. Se a sua área já tem mais agentes do que gente, vale conversar sobre como torná-los auditáveis antes que o regulador peça.*

> **Ganchos de variação (para testar):**
> - Versão dado-first: abrir com "89% / 90% / 83%" (BioCatch) e descer para o balcão do Itaú.
> - Versão provocação: "Seu banco tem mais agentes do que gente. Quantos têm dono?"
> - Versão soberania: abrir pelo "kill switch" de modelo e o risco de continuidade.

**Fontes:** Itaú Laranjinha+ (TI Inside, 24/jun); Itaú agentes 18d→14h (TI Inside, 03/jun); Nubank AI Private Banker, 15M MAU (Nu Videocast, 11/jun); BB 12 mil agentes / 36 mil em formação (TI Inside; Convergência Digital); BioCatch — 89%/90%/83% (Let's Money; Biometric Update); inadimplência neobancos 7,71%→20,31% (Equifax Boa Vista via Finsiders); investimento em IA +61% / R$ 47,8 bi (Pesquisa Febraban de Tecnologia Bancária via Dock); Comef/Bacen — "dependências comuns" (Ata 65ª Comef via Finsiders); CMN 5.274/BCB 538 (Matera; NDM); Febraban Tech 2026.
