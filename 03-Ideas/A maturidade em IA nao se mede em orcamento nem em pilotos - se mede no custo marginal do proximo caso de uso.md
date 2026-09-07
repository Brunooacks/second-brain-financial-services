---
tipo: ideia
data: 2026-07-13
status: crua
origem: auto-digest
fonte_daily: "[[2026-07-13]]"
eixos: [economia-ia, financeiro, governanca, soberania]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 A maturidade em IA não se mede em orçamento nem em pilotos — se mede no custo marginal do próximo caso de uso

## A tese
Enquanto o board perguntar "quanto vamos investir em IA?", ele está medindo a coisa errada. A única régua de maturidade que sobrevive a uma pergunta hostil é: **quanto custa (em dias e em R$) colocar o próximo caso de uso em produção — e esse custo está caindo?** Se não está caindo, não existe plataforma; existem projetos. E projeto artesanal não absorve capital, absorve gente.

## Por que eu acredito nisso
O dado do dia desmonta a narrativa de subinvestimento. Na **Pesquisa Febraban de Tecnologia Bancária 2026 (Deloitte, divulgada 26/06/2026)**, os bancos BR executaram **R$ 46,8 bi em tecnologia em 2025 e destinaram apenas R$ 826 mi à IA — 1,8%** (cloud: R$ 3,9 bi). No mesmo levantamento, **GenAI é prioridade alta/média para 84%** e, ainda assim, **56% seguem "em fase de testes e construção de casos de uso"**. A distância entre 84% de prioridade e 56% de piloto não se explica por verba — se explicasse, o dinheiro já teria entrado.

A explicação está em quem saiu do piloto. O **Bradesco** tem **600+ casos de GenAI em produção**, **~70 mi de interações da BIA em 18 meses com 87% de resolutividade** e **~1.000 pull requests revisados por IA/mês** — e o diretor de tecnologia Leandro Marçal credita a escala a um **barramento interno** (AI gateway) que centraliza o acesso a modelo com **governança embutida na infraestrutura, não como auditoria posterior**. O **Itaú** exibe a versão financeira do mesmo argumento: **+2.099% de deploys entre 2018 e 2025 com −34% de custo de infraestrutura** — velocidade e custo deixam de ser trade-off quando a plataforma é a certa. O **NTT DATA Banking AI Leaders' Playbook 2026 (pág. 4-5)** dá o número que fecha a conta pro board: **84,1% das organizações com estratégia de IA plenamente alinhada reportam ≥5% de uplift de lucro, contra 58,3% das não alinhadas**.

O mecanismo é simples: sem camada única (roteamento, política de dado, custo por caso de uso, trilha de auditoria), **cada iniciativa refaz do zero integração, compliance e controle de custo — o custo marginal do segundo caso é quase igual ao do primeiro.** Com barramento, ele tende a zero. Daí 600 casos num, piloto eterno em 56% dos outros. E não dá pra contar com o mercado resolver: com a **escassez de memória até 2030 e contratos de DRAM +63% no 2T26** (SK Hynix), o custo unitário de inferência tem **piso**. A alavanca que sobra é arquitetural.

## Quem discordaria — e por quê
Três contrapontos honestos. (1) **O CFO:** o R$ 826 mi subestima o real — parte do gasto de IA está embutida em cloud e software, então "1,8%" é artefato de taxonomia contábil. Justo — mas mesmo corrigido, o gap 84% × 56% permanece. (2) **O arquiteto cético:** um **barramento proprietário pode virar o próximo legado** — ponto único de gargalo que atrasa a adoção de modelo de fronteira enquanto a plataforma homologa. Verdadeiro, e é o teste que eu faria no Bradesco: **quanto tempo leva pra um modelo novo entrar no barramento?** Se for trimestre, virou burocracia com outro nome. (3) **O head de negócio:** o gargalo é *data readiness* e caso de uso, não plataforma — barramento só organiza a fila. Contra-argumento: dado ruim não explica por que quem tem barramento roda 600 casos com o mesmo dado do resto do mercado.

## O que eu faria / recomendaria
Trocar a pergunta de orçamento por uma pergunta de arquitetura no comitê: **"qual é hoje o custo, em dias e em R$, de colocar o próximo caso de uso de IA em produção — e ele é menor que no caso anterior?"** Se ninguém souber responder, o diagnóstico está feito. Em seguida, decompor o gasto de IA nas três linhas que ninguém consolida — **inferência (tokens), plataforma (camada de acesso) e trabalho humano de integração**; a terceira costuma ser a maior, e é exatamente a que o barramento mata. Para o **Veltrix**, isso é o melhor evento de categoria do ano: o maior banco privado do país acabou de validar em produção a arquitetura (roteamento + política de dado + custo por caso de uso + trilha) e chamou de "barramento". Não é produto procurando problema — é a categoria que 56% do mercado ainda não tem. O pitch deixa de ser "economize tokens" e passa a ser **"derrube o custo marginal do próximo caso de uso"**, que é a frase que o board entende.

## Lastro
- Pesquisa Febraban de Tecnologia Bancária 2026 / Deloitte (26/06/2026, via Valor e Let's Money): R$ 50,4 bi previstos p/ 2026; R$ 46,8 bi executados em 2025; IA R$ 826 mi (1,8%); cloud R$ 3,9 bi; 56% em testes; GenAI prioridade p/ 84%.
- TI Inside / Let's Money: Bradesco — 600+ casos de GenAI, barramento com governança embutida, BIA ~70 mi de interações / 87% de resolutividade, ~1.000 PRs/mês.
- NeoFeed / Itaú Day: Itaú — 1,9 mil iniciativas, 70% da plataforma modernizada, +2.099% de deploys, −34% de custo de infra, eficiência 39% → ~30%.
- NTT DATA — *Banking AI Leaders' Playbook 2026*, pág. 4-5: 84,1% × 58,3% (≥5% de uplift de lucro).
- SK Hynix / Tom's Hardware (jul/2026): escassez de memória até 2030; DRAM +63% no 2T26.
- Vizinhas no vault: [[A escala chegou a conta ninguem reporta - custo por inferencia e o ponto cego do agent estate]] (o denominador ausente — aqui a tese é o *custo marginal*, não o custo unitário) · [[Matriz Construir-Comprar-Parcear do Ativo de IA (DCS) - Dado, Custo, Soberania]] · [[Matriz de Roteamento de Inferencia (SJC) - Sensibilidade, Jurisdicao, Custo]]

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** economia-ia / governança  ·  **Setor:** financeiro (bancos BR)
