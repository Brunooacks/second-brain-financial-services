---
tipo: post
data: 2026-08-20
canal: medium
registro: executivo
status: rascunho
eixos: [agentes, financeiro, governanca]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-08-20-passivo-em-cadeia-a2a]]"
tags: [post, medium, 2026-W34]
---

# 📰 Medium — O passivo em cadeia entre agentes chegou antes do contrato

**Título:** O passivo em cadeia entre agentes chegou antes do contrato

**Dek:** Dois agentes de empresas diferentes já negociam condição comercial num trilho de pagamento brasileiro. Nenhum contrato diz de quem é o prejuízo quando eles combinam algo que ninguém aprovou.

---

## O número

O caso concreto é da Cielo, apresentado no Fórum E-Commerce Brasil 2026: uma jornada em que o consumidor pesquisa produto, compara alternativas e autoriza a transação dentro da própria conversa. Três peças sustentam isso — um protocolo que permite ao agente iniciar o pagamento (AP2), um que permite ao agente da empresa A conversar com o agente da empresa B (A2A) e um que dá ao agente acesso ao catálogo, preço e estoque do lojista (MCP). A parte que interessa a um conselho é a do meio: **é o primeiro caso brasileiro em que a negociação entre agentes de empresas distintas sai da demonstração e encosta num trilho de pagamento real.**

⚠️ conferir — as fontes divergem entre "apresentou no fórum" e "colocou em produção". Antes de citar em comitê, confirmar o estágio: demonstração controlada, piloto com lojista real ou produção com volume.

O que temos de número, e o que ele vale:

| Número | Valor | Natureza | Fonte |
|---|---|---|---|
| Redução do tempo de checkout | −60% | **Projeção de fornecedor** | Varejo S.A./CNDL, 29/07/2026 |
| Abandono de carrinho | −30% | **Projeção de fornecedor** | Varejo S.A./CNDL, 29/07/2026 |
| Vendas concluídas | +15% | **Projeção de fornecedor** | Varejo S.A./CNDL, 29/07/2026 |
| Custo por operação | −20% | **Projeção de fornecedor** | Mobile Time, 28/07/2026 |
| Intenção de comprar via agente (BR) | 76% | Pesquisa declarada | Iniciador, via Finsiders, 17/07/2026 |
| Intenção de comprar via agente (EUA) | 44% | Pesquisa declarada | Iniciador, via Finsiders, 17/07/2026 |
| Instituições que acham o cliente confortável com agente decidindo sozinho | 35% | Pesquisa | Adobe, *2026 AI and Digital Trends in FS* |
| Clientes que declaram esse conforto | 21% | Pesquisa | Adobe, *2026 AI and Digital Trends in FS* |
| Firmas financeiras rodando sobre modelo de terceiro | 63% | Levantamento | CCAF/Cambridge + WEF/BIS/FMI, *2026 Global AI in Financial Services Report*, **pág. 7–8** |

Método de leitura, porque isso muda a conclusão: as quatro primeiras linhas são **anúncio de fornecedor sobre resultado esperado**. Nenhuma delas passou por auditoria, nenhuma tem baseline público, nenhuma informa o denominador. Trate como hipótese a testar. As linhas seguintes são pesquisa com amostra declarada — imperfeitas, mas com método.

O contraste entre as duas metades da tabela é a tese inteira. **Do lado do benefício, projeção. Do lado da tolerância do cliente e da dependência estrutural, medição.** Quem aprova o projeto olhando só a metade de cima está aprovando expectativa contra risco medido.

E há o número que ainda não existe: **nenhuma das duas empresas envolvidas numa negociação entre agentes publicou qual é o limite de alçada do seu agente, em reais, por tipo de decisão.** É a variável que decide o tamanho do prejuízo, e ela não está em lugar nenhum.

## A exposição

Enquanto o agente é interno, o perímetro de risco da instituição é nítido: ele começa e termina dentro de casa. Quando o agente do lojista passa a negociar com o agente do cliente, **parte da decisão comercial migra para um espaço que nenhuma das duas empresas controla sozinha**.

Isso cria uma categoria de prejuízo que os manuais atuais não cobrem. Considere uma condição comercial fechada nessa conversa — um desconto, um parcelamento, uma garantia estendida — fora da política de qualquer uma das partes. Quando o caso chega à mesa de disputa, ele não se encaixa em nenhuma das três gavetas existentes:

- **Não é fraude.** Ninguém se passou por ninguém. Os dois agentes estavam autorizados a agir em nome de quem agiram. (O eixo de fraude é outro, e está mapeado em [[Verifiable Intent - quem arbitra a disputa do agente define quem paga a fraude]].)
- **Não é falha de sistema.** Todos os componentes funcionaram exatamente como projetados. Não há incidente para abrir.
- **Não é decisão humana.** Não há quem chamar para explicar. Não há gravação, não há testemunha, não há gerente que autorizou.

Sobra a quarta gaveta, que ninguém construiu: **responsabilidade em cadeia comercial entre agentes.** Um passivo real, com valor em reais, sem dono contratual.

Compare com a situação que ele substitui. Um vendedor de loja que concede desconto fora da política também cria prejuízo — mas cria com dono: existe um nome, um gerente, uma política escrita e um limite. A empresa sabe a quem perguntar. A automação preserva o prejuízo e apaga o dono.

Três agravantes brasileiros:

**Escala e velocidade.** Alçada informal erra uma venda por vez. Automatizada, erra o dia inteiro, em silêncio, e o erro aparece na conciliação — semanas depois.

**Demanda concentrada aqui.** 76% contra 44% não é uma curiosidade cultural. Significa que o Brasil é onde a compra por agente escala primeiro, e portanto onde a lacuna contratual encontra volume primeiro.

**Dependência estrutural.** 63% das instituições financeiras já rodam sobre modelos de terceiros (pág. 7–8). O agente que negocia em nome da sua empresa raramente é um sistema seu de ponta a ponta — o que significa que o prejuízo tem pelo menos três candidatos a dono, e nenhum deles assinou nada.

Há uma janela regulatória aberta. A expectativa declarada do mercado é de **consulta pública do Banco Central sobre pagamento agêntico entre meados de setembro e meados de outubro de 2026** (Pagos, via Finsiders). ⚠️ conferir — expectativa de mercado, não edital publicado; o que está confirmado é que o BC colocou "estudar riscos e impactos da IA nas instituições financeiras" como meta formal da agenda regulatória 2025/2026. Consulta pública é o único momento em que uma instituição escreve, de fato, a regra que vai cumprir pelos dez anos seguintes — e é o momento que quase todo mundo delega ao jurídico na última semana do prazo.

## O contraponto

O melhor argumento contrário é este, e ele tem bons defensores: **a Cielo não inventou risco nenhum — automatizou o que o vendedor de loja sempre fez com alçada informal.** E alçada informal é muito pior de auditar do que uma negociação entre agentes, que ao menos deixa registro estruturado. Trocar um processo opaco por um processo logado é melhoria de governança, não deterioração. Quem exige contrato antes de qualquer experimento está pedindo que a inovação espere o jurídico — e o jurídico nunca chega primeiro.

Aceito a premissa e recuso a conclusão, por dois motivos.

O primeiro é que registro não é o mesmo que responsabilidade. Ter o log de uma negociação diz **o que** aconteceu; não diz **quem paga**. São duas coisas distintas, e a segunda é a que aparece na conciliação. Um processo perfeitamente auditável com passivo indefinido produz exatamente um resultado: disputa entre duas empresas que ambas acham que a outra deveria absorver.

O segundo é o comportamento em escala. O erro do vendedor humano é auto-limitado por cansaço, por volume e por testemunha. O erro automatizado é replicável e persistente — se a regra estiver mal desenhada, ela erra igual em todas as transações do dia.

Por isso a recomendação não é frear. É separar duas decisões que o mercado está tratando como uma só: **experimentar a jornada** (rápido, aprova-se agora) e **escrever a alçada e a cadeia de responsabilidade** (antes do primeiro estorno, não depois).

## O que eu faria

Quatro passos, na ordem, todos executáveis antes do fim de setembro:

**1. Inventário de agentes que falam para fora.** Lista de todo agente que já conversa — ou está previsto para conversar — com sistema automatizado de outra empresa. Se a lista não existir, esse é o primeiro achado: ninguém sabe quantos agentes agem em nome da casa. É o objeto que o **Cohort** trata como cidadão de primeira classe: o agente como entidade registrável, com identidade, dono, escopo e limite — não como integração.

**2. Alçada escrita no sistema, não no slide.** Para cada agente da lista, preencher a [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]]: até que valor ele fecha sozinho, em que canal, quando exige confirmação humana e o que fica na trilha. A regra de desenho é achar o teto por confirmação, não bloquear tudo — fricção demais mata a conveniência que justifica o canal. O [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] é a credencial; a VCAP é a autenticação da ordem.

**3. Cláusula de cadeia nos contratos comerciais.** Uma cláusula que responda, em texto simples: quando uma condição é fechada em negociação automatizada entre agentes das duas partes, quem absorve o prejuízo, em que faixa de valor, e qual registro serve de prova. Sem isso, cada disputa vira negociação do zero — com a relação comercial de refém.

**4. Contribuição à consulta pública, pronta antes do edital.** Três posições defendidas com dado próprio: limite de alçada do agente, identidade do agente e responsabilidade em cadeia. O custo de se preparar para uma consulta que não vem é baixíssimo. O custo de não estar pronto para uma que vem é a regra escrita por outro.

E a pergunta única, se só couber uma na pauta: **de quem é o prejuízo quando dois agentes combinam uma condição que nenhuma das duas empresas aprovou?** Se a resposta for "cairia no caso a caso", a casa não tem contrato — tem sorte. Sorte é uma posição defensável enquanto o volume é pequeno. Com 76% de intenção declarada de compra por agente no Brasil, o volume não vai ficar pequeno.

---

**Frameworks citados:** [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]] · [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] · [[Roteamento de Trilho do Agente de Pagamento (SRC)]] · [[Mapa de Passivo por Trilho (MPT) - de quem e o passivo quando o valor vira token]]

**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-08-20-passivo-em-cadeia-a2a]]

**Capa:** 16:9 conforme [[Identidade-Visual-Editorial]] — duas salas idênticas separadas por parede espessa; no vão, uma mesa pequena com um contrato assinado e ninguém por perto; silhuetas minúsculas de costas em cada sala; a assinatura em vermelhão.

## Fontes

1. Varejo S.A./CNDL — *Pagamentos por agentes de IA avançam no Fórum E-Commerce Brasil 2026* (29/07/2026) · https://cndl.org.br/varejosa/pagamentos-por-agentes-de-ia-avancam-no-forum-e-commerce-brasil-2026/
2. Mobile Time — *Cielo lança assistente de compras com IA* (28/07/2026) · https://www.mobiletime.com.br/noticias/28/07/2026/assistente-de-compras/
3. Central do Varejo — *Cielo lança pagamentos por agentes de IA com Google Cloud* · https://centraldovarejo.com.br/cielo-lanca-pagamentos-por-agentes-de-ia-com-google-cloud/
4. Finsiders — *Pagamentos por IA ganham força e colocam BC sob pressão* (17/07/2026) · https://finsidersbrasil.com.br/tecnologia-para-fintechs/pagamentos-por-ia-ganham-forca-e-colocam-bc-sob-pressao/
5. Adobe — *2026 AI and Digital Trends in Financial Services* · https://business.adobe.com/resources/reports/financial-services-digital-trends.html
6. CCAF/Cambridge com WEF, BIS, FMI, IDB, CGAP, AMF — *2026 Global AI in Financial Services Report*, **pág. 7–8** (628 organizações, 151 jurisdições) · acervo `02-Sources/Reports/`
7. Convergência Digital — *BC prioriza Pix, Open Finance, IA e tokenização* · https://convergenciadigital.com.br/governo/bc-prioriza-pix-open-finance-inteligencia-artificial-e-tokenizacao/
8. Vault: daily [[2026-08-18]] · [[A2A em producao move a decisao comercial pra fora do perimetro - quem responde]] · [[O otimismo de quem constroi o agente excede em 14 pontos a confianca do cliente]] · [[No pagamento agentico o agente decide a regra liquida - o trilho continua burro]] · [[Bacen estuda risco de IA antes de regular - janela para definir o vocabulario]]
