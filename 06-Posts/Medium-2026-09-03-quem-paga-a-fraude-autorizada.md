---
tipo: post
data: 2026-09-03
canal: medium
registro: executivo
status: rascunho
eixos: [financeiro, governanca, agentes]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-09-03-quem-paga-a-fraude-autorizada]]"
tags: [post, medium, executivo, 2026-W36]
---

# 📰 Medium — Quem paga a fraude autorizada

**Título:** No Brasil, a fraude que o cliente autoriza ainda não tem dono

**Dek:**
Quarenta por cento dos indícios de fraude do país não deixam anomalia técnica, porque quem digitou foi o titular.
O MED devolve, o antifraude não vê e o jurídico chega depois — e nenhuma das três áreas assina a perda.

---

## O número

Três séries precisam ser lidas juntas. Separadas, cada uma vira slide de painel; juntas, viram linha de exposição.

| O que mede | Número | Fonte |
|---|---|---|
| Indícios de fraude financeira no Brasil, 1º sem/2026 | **9 milhões** (+10,26% sobre o 2º sem/2025) | Quod, via Agência Brasil/EBC, 22/08/2026 |
| Parcela de engenharia social | **3,6 milhões — 40%** | idem |
| Canal e trilho do golpe | **78%** celular · **85%** Pix | idem |
| Perfil da vítima | **3,1 mi** de pessoas · **49,06%** entre 18 e 34 anos · **58%** até 2 salários mínimos · **799 mil** vitimadas duas ou mais vezes | idem |
| Intenção × entrega da defesa | **75%** planejam IA antifraude · **80%** travam em qualidade de dado · **12%** colhem valor em produção | EY + IIF, 101 bancos em 31 países |
| Ganho por campo de visão | recuperação de **<10% para até 46%** das solicitações; **R$ 40 bi/mês** monitorados | Data Rudder / Núclea (operação pendente de aprovação do BC) |
| Não devolvido em Pix, 2024 | **R$ 4,941 bi** ⚠️ conferir | Sindpd / WeLiveSecurity, 2026 — fonte secundária, sem página |
| Volume mensal do MED | **2,7 a 2,8 mi de pedidos/mês** ⚠️ conferir | registrado em daily do vault, sem link primário |

**Como o número foi apurado — e o que ele não diz.** Os 40% da Quod são *indícios*, não perdas confirmadas: incluem casos suspeitos e confirmados. É uma medida de incidência, não de prejuízo. Ninguém publica, no Brasil, a série de perda líquida por tipologia de fraude — e essa ausência é parte da tese: não se governa o que não se segmenta. Os 12% da EY/IIF são autorrelato de executivos sobre "extrair valor de projetos em produção", sem baseline de custo — o tipo de número que eu trataria como direção, não como magnitude.

O dado regulatório é o único que não admite interpretação. O **MED 2.0** — Mecanismo Especial de Devolução, **Resolução BCB nº 493/2025**, em vigor desde **02/02/2026** — fixa **80 dias** para a contestação do cliente, **11 dias úteis** para a devolução após a confirmação de fraude, e rastreamento em cadeia. Isso é um relógio no seu processo, com data de partida.

## A exposição

A categoria tem nome na literatura internacional: *authorized push payment fraud* — a fraude que a vítima autoriza. O criminoso não invade: convence. Do ponto de vista do sistema, tudo confere. Dispositivo conhecido, geolocalização habitual, horário normal, credencial correta, biometria comportamental compatível.

O antifraude transacional procura **anomalia**. Aqui não há anomalia a encontrar. A sensibilidade não é baixa por má calibragem; é baixa por construção. Cinco anos de investimento em score sobre a transação compraram cobertura excelente para a metade do problema que está encolhendo em participação relativa, e cobertura estrutural nula para os 40% que crescem.

Onde isso aparece no balanço:

**1. No prazo.** O MED 2.0 transfere ônus e relógio para a instituição. Quando o cliente contesta, o banco corre contra 11 dias úteis e precisa provar a cadeia. Cada novo canal de execução — Pix por voz, WhatsApp, agente autônomo — é um novo vetor de contestação com o cronômetro já rodando.

**2. No litígio.** Fraude autorizada é o campo onde o registro do banco diz apenas "houve autorização" e a peça do cliente diz "houve indução". Quem não consegue reconstruir o contexto da autorização não perde por mérito; perde por ausência de prova. E há precedente de responsabilidade difusa se materializando no próprio trilho: o Banco Central já figura como réu solidário em ações sobre marcação de fraude no MED.

**3. Na organização — e é aqui que dói mais.** A exposição não tem dono porque está partida em três:

| Etapa | Área que responde | O que ela mede |
|---|---|---|
| Detecção | Time de fraude / CISO | taxa de detecção agregada |
| Devolução | Operações / ouvidoria | cumprimento do prazo de 11 dias |
| Perda e litígio | Jurídico | provisão, meses depois |

Nenhuma das três é cobrada pela pergunta que importa: *em quantos casos conseguimos distinguir autorização de indução?* É uma métrica de ninguém. Métrica de ninguém é exposição de todos.

**4. No agente.** O ponto que ainda não entrou em nenhum comitê brasileiro. Hoje o golpista precisa convencer uma pessoa a executar. Amanhã ele convence uma pessoa a **instruir um agente**, e o agente executa sem a fricção residual de quem hesita antes de confirmar. Tratamos o humano no meio (*human-in-the-loop*) como controle de segurança. Os 40% dizem o contrário: o humano no loop é o componente com a maior taxa de comprometimento da cadeia. Remover a hesitação não é ganho de eficiência neutro — é remoção de controle.

## O contraponto

O melhor argumento contra tudo isso é jurídico e curto: **o cliente autorizou**. Não há, no ordenamento brasileiro, regime de repartição obrigatória de perda em fraude autorizada. Engenharia social é problema de cultura e educação do consumidor, e a instituição não controla a cultura — o levantamento Certta/Nexus mostra que só 11% das menções públicas sobre golpes tratam de prevenção. Instrumentar o contexto pré-transacional, por sua vez, esbarra em LGPD e em custo de falso positivo: ninguém quer bloquear a conta de um cliente porque ele recebeu uma ligação.

O segundo contraponto é metodológico: os 12% da EY/IIF podem ser imaturidade de curva, não falha estrutural. Três anos atrás o número seria zero.

Aceito os dois. Nenhum deles muda quem paga.

Educar reduz incidência; não redistribui responsabilidade. Com 85% dos golpes passando pelo Pix e o MED rodando na casa dos milhões de pedidos por mês, o prejuízo e o passivo estão no balanço da instituição, não na educação do titular. Quanto ao custo de falso positivo: o mesmo argumento foi usado contra biometria comportamental em 2020, e hoje ela é padrão de mercado. A pergunta nunca foi *se* a janela de detecção recua; é quem chega primeiro com base legal defensável.

E há um teste simples para o argumento "o cliente autorizou": ele funciona até o dia em que o executor não é mais o cliente, e sim um agente com mandato assinado pela instituição. Nesse dia, a defesa vira acusação.

## O que eu faria

Quatro movimentos, na ordem, e nenhum deles é comprar o próximo score.

**1. Segmentar a métrica antes de discutir orçamento.** Peça a taxa de detecção por tipologia, não agregada. Se o relatório do comitê só traz o consolidado, a instituição não sabe se está cega em 40% do problema — e ninguém consegue provar o contrário. Isso é uma reunião, não um projeto.

**2. Instrumentar o estado da decisão, não o fato dela.** Para toda autorização de risco, registrar **quem instruiu, sob que contexto, com que mandato e com que limite** — o suficiente para reconstruir, depois do fato, se houve autorização ou indução. Métrica de board: *% de autorizações de risco com trilha de contexto reconstruível vs. % que só registram o fato*. É barato agora e impossível de reconstruir depois: o contexto não fica gravado retroativamente.

**3. Nomear o dono antes do incidente.** Uma linha só, num documento de governança: quem assina a classificação "autorizado" versus "induzido", e sob que evidência. Enquanto for de três áreas, é de nenhuma.

**4. Escrever o mandato do agente antes do primeiro pagamento agêntico em produção.** Qual agente, sobre qual dado, autorizado por quem, com que teto, com que trilha, em qual jurisdição — e com data de revalidação. É onde o [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] e a [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]] deixam de ser diagrama e viram cláusula. O lado técnico do custo e da jurisdição da inferência é o terreno do Veltrix; o mandato e o ciclo de vida do agente pagador é o do Cohort.

Se eu tivesse uma frase para deixar na ata: **quem só tem devolução tem custo; controle é conseguir provar, em 11 dias úteis, a diferença entre um cliente que decidiu e um cliente que foi conduzido.**

---

**Frameworks citados:** [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] · [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]] · [[Mapa de Passivo por Trilho (MPT) - de quem e o passivo quando o valor vira token]]
**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-09-03-quem-paga-a-fraude-autorizada]]
**Notas de lastro:** [[O proximo ciclo de antifraude nao e outro score - e instrumentar a decisao]] · [[MED 2.0 poe cronometro de 11 dias na fraude com deepfake - deteccao vira requisito de conformidade com prazo]] · [[A cadeia de responsabilidade do Rufra e o proximo litigio - antes do PL 2338]] · [[Verifiable Intent - quem arbitra a disputa do agente define quem paga a fraude]] · daily [[2026-08-23]]
**Capa:** 16:9 conforme [[Identidade-Visual-Editorial]] — mesmo motivo do card (guichê vasto, papel assinado, acento vermelhão apenas na assinatura), recomposto na horizontal com o vazio à direita.

## Fontes

1. [Agência Brasil/EBC — Engenharia social responde por 40% das fraudes financeiras no Brasil (22/08/2026)](https://agenciabrasil.ebc.com.br/geral/noticia/2026-08/engenharia-social-responde-por-40-das-fraudes-financeiras-no-brasil) — pesquisa Quod; levantamento Certta/Nexus; declarações de José Oliveira (CTO da Certta).
2. [Let's Money — 3 em cada 4 bancos querem IA contra crimes financeiros (09/07/2026)](https://www.letsmoney.com.br/noticias/bancos-ia-crimes-financeiros/) · [EY newsroom — EY/IIF survey](https://www.ey.com/en_gl/newsroom/2026/02/banks-race-to-adapt-as-traditional-risks-rebound-and-new-threats-accelerate-ey-and-iif-survey-shows) — 101 bancos, 31 países.
3. [Let's Money — Núclea anuncia compra da antifraude Data Rudder](https://www.letsmoney.com.br/noticias/nuclea-compra-data-rudder-antifraude/) — R$ 40 bi/mês monitorados; meta de recuperação de <10% para até 46%.
4. [Banco Central — Resolução BCB nº 501 (compartilhamento de indícios de fraude / Rufra)](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=501).
5. Resolução BCB nº 493/2025 — MED 2.0, em vigor desde 02/02/2026: 80 dias para contestação, 11 dias úteis para devolução, rastreamento em cadeia. ⚠️ **conferir link direto do normativo no site do BC antes de publicar.**
6. R$ 4,941 bi não devolvidos em Pix (2024) e volume mensal do MED (2,7–2,8 mi de pedidos): Sindpd / WeLiveSecurity, 2026 — ⚠️ **conferir fonte primária.**

---
## ✅ Checklist antes de publicar
- [x] Acrescenta algo que **não estava** no post de LinkedIn? (tabela de séries, método de apuração, mapa das três áreas, o teste do "cliente autorizou")
- [x] Título é afirmação e cabe em 12 palavras?
- [x] Linka o post de origem e as notas de `05-Frameworks/`?
- [ ] Fontes com link, não só nome? — itens 5 e 6 pendentes de link primário
- [x] O card de LinkedIn promete "análise completa no Medium" — esta análise existe?
