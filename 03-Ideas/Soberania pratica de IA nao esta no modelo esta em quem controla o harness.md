---
tipo: ideia
data: 2026-06-27
status: crua
origem: auto-digest
fonte_daily: "[[2026-06-25]]"
eixos: [soberania, economia-ia, governanca]
maturidade: 1
candidata_post: true
tags: [ideia, tese, auto]
---

# 💡 Soberania prática de IA não está no modelo — está em quem controla o harness portável

## A tese
Soberania de IA defensável não se conquista escolhendo "o modelo certo", e sim controlando a camada de orquestração (harness) e mantendo-a portável: quem trata o harness como produto versionável e independente de fornecedor troca o foundation model por baixo sem reescrever a operação. Sem isso, o "plano B soberano" é PowerPoint — existe no comitê, não na produção.

## Por que eu acredito nisso
A daily de 25/jun trouxe o sinal direto: Databricks liberou o **Omnigent** (meta-harness sob licença **Apache 2.0**, 16/jun) que envolve agentes de código existentes e os torna interoperáveis — "o ecossistema da fronteira precisa ser aberto" (Zaharia/Xin, Latent Space). A tese lida de cima é hedge de soberania: se a orquestração é aberta e portável, o banco escapa do lock-in dos três foundation models de jurisdição única (OpenAI/Google/Anthropic) que o *Global AI in FS 2026* já mostra concentrando a indústria. E o argumento econômico fecha: **53% das firmas gastam menos de US$ 100 mil/ano em IA e ainda relatam alta maturidade** (*Global AI in FS 2026*, pág 7) — vantagem é de quem otimiza a conta e mantém opcionalidade, não de quem casa com um provedor. O aprendizado da própria daily: "quem controla o harness controla o agente — e pode trocar o modelo por baixo sem refazer a operação".

## Quem discordaria — e por quê
Um arquiteto pragmático diria que manter um harness próprio e portável é overhead caro: você paga em complexidade e velocidade para comprar uma opcionalidade que talvez nunca exerça, enquanto o concorrente que casou com um provedor entrega mais rápido. E há o contraponto mais fino: o harness pode virar o novo lock-in — abstrair três modelos atrás de uma camada que só a sua engenharia entende é trocar a dependência do fornecedor pela dependência de você mesmo. A tese só se sustenta se a portabilidade for testada de verdade (failover real), não declarada.

## O que eu faria / recomendaria
Adotar "portabilidade do harness" como critério explícito de arquitetura em toda decisão de build vs buy: *consigo trocar o modelo por trás dos agentes sem reescrever o fluxo, e isso já foi ensaiado?* É exatamente o terreno do **Veltrix** — roteamento por jurisdição/sensibilidade + prova, por log, de que a alternativa soberana está pronta e foi exercida. A métrica de board não é "qual modelo usamos", é "% de casos de uso críticos com modelo alternativo testado em produção". Conecta-se a [[Soberania de modelo virou risco de continuidade, nao tese]] (esta é o mecanismo que torna aquele hedge executável) e a [[Governanca de agente que importa pra banco fica acima do provedor]] (governança e harness acima do provedor são a mesma disciplina).

## Lastro
- Databricks Omnigent (meta-harness, Apache 2.0, 16/jun) · Latent Space — "Frontier Ecosystem must be Open": https://www.latent.space/
- *Global AI in Financial Services 2026*, pág 7 (53% gastam <US$ 100 mil/ano com alta maturidade; concentração em 3 foundation models de jurisdição única)
- AINews/Smol AI — "Meta-Harness Summer" (harness engineering como disciplina)
- Daily-fonte: [[2026-06-25]] (clusters 🌐 Soberania da Informação · 📊 Economia de IA & FinOps · 🎓 Aprendizado do dia)

---
**Candidata a post?** ☑  ·  **Eixo CAIO:** soberania / economia-ia  ·  **Setor:** financeiro
