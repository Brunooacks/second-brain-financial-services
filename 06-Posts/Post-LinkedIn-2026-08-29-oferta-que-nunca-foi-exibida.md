---
tipo: post
data: 2026-08-29
canal: linkedin
status: rascunho
eixos: [financeiro, governanca, soberania]
maturidade: 4
tags: [post, linkedin, semana, 2026-W35]
---

# 🧵 Long-form — O app não decide seu crédito. Decide se você chega até ele.

> Tese da semana W35. Origem: [[A oferta que nunca foi exibida vira acesso diferencial a credito]] · lastro de calendário em [[ANPD agendou 20 fiscalizacoes de IA para 2026-2027 - compliance virou calendario]] · lastro de trilho em [[2026-08-25]].
> Distinta de [[Post-LinkedIn-2026-08-15-explicabilidade-arquitetura-anpd]] (lá o objeto é a **decisão** de crédito) e de [[Post-LinkedIn-2026-08-22-fabrica-do-modelo-de-credito]] (lá é a **fábrica** do modelo). Aqui o objeto é a camada **a montante**: quem chega até a decisão.
> **Nota de execução:** rodada em 31/08 (segunda) — o gatilho de sábado não pegou o app aberto.

---

## O app não decide seu crédito. Decide se você chega até ele.

Um cliente em Manaus abre o app do banco. Tela inicial montada para ele, menus na ordem que o modelo achou melhor, uma área de ofertas com o que faz sentido para o seu perfil. Não aparece crédito consignado. Não aparece antecipação de recebível. Não porque alguém analisou e negou — porque o motor de recomendação, olhando o perfil, decidiu que não valia o espaço da tela.

Não existe negativa. Não existe protocolo. Não existe log.

Guarde essa ausência, porque ela é a peça inteira.

---

### O que aconteceu esta semana

O **novo App BB** foi liberado na segunda-feira, **24/08**, com migração de **100% da base até o fim de setembro**. O que mudou não é a interface: é a camada de decisão. Tela inicial, menus e atalhos passam a variar conforme perfil e contexto; a IA é usada para interpretar contexto, apoiar atendimento e **recomendar produtos e serviços**; a área "Meu BB" concentra ofertas personalizadas. O próprio banco descreve o canal como ferramenta de relacionamento e **distribuição de produtos financeiros** (*Agência Brasil* e *Diário do Comércio*, 24/08/2026).

Nenhum comunicado usou a palavra risco. E não usou porque, tecnicamente, não precisava.

Na mesma semana, a **200 metros dali**, no Febraban Tech, o Banco Central apresentou os números do trilho onde isso tudo vai rodar: **86% da população brasileira** usa Pix; o **Pix Automático** fechou o primeiro ano com estoque de **20 milhões de autorizações**, e os recebedores saíram de **mil em dezembro de 2025 para 14 mil em agosto de 2026**. Márcia Vicari nomeou os próximos capítulos: duplicata escritural, pagamentos internacionais e **uso de fluxo futuro de recebimento via Pix como garantia para oferta de crédito** (*Convergência Digital*, 24/08/2026).

No mesmo painel, Lauro Gonzalez (FGV-SP) apresentou a *Geografia do Pix*: **Amazonas com 48** transações por usuário, **Norte/Nordeste com 40**, **Sul abaixo de 30**. Quem tem menos renda usa mais o trilho. E deixou a frase de governança da semana — que, repare, não veio de um comitê de risco, veio de um economista num painel de pagamentos: **"nem toda inclusão é automaticamente boa para o incluído."**

Junte as três coisas: trilho soberano com penetração quase universal, fluxo futuro virando garantia, e IA de recomendação na tela de toda a base. Isso é **oferta de crédito na velocidade da transação**. É a maior conquista de infraestrutura financeira que este país fez — com uma camada de decisão plugada em cima que nenhuma das duas pontas auditou em conjunto.

---

### A tese

A pergunta regulatória óbvia é "o app decide crédito?". Não decide. E é por isso que é a pergunta errada.

A que eu levaria ao board é outra: **o app decide quem chega até o crédito.**

Recomendação é camada *a montante* (upstream) da decisão — e é exatamente a montante que não existe trilha. Todo banco loga a proposta negada: motivo, política, versão do modelo, direito de revisão. **Nenhum banco loga a oferta que nunca foi exibida.**

Quando a personalização deixa de ser vitrine e vira o **canal de distribuição** de produto de crédito para dezenas de milhões de pessoas, exposição diferencial vira, na prática, **acesso diferencial**. E acesso diferencial sem registro é a única forma de discriminação que não deixa vítima identificável — porque a pessoa nunca soube que existia a oferta.

---

### O contraponto honesto (e ele provavelmente vence hoje)

Um jurídico competente me responde duas coisas, e as duas são boas.

**Primeira:** recomendar não é decidir. O **art. 20 da LGPD** trata de decisões automatizadas com efeitos jurídicos ou que afetem interesses do titular; exibir — ou não exibir — um banner não é uma delas. Personalização de vitrine sempre foi marketing, e vitrine é livre.

Aceito o argumento. Ele é sólido e, na régua de hoje, vence. Mas ele não resolve o problema de **prova**: daqui a dois anos, se um supervisor perguntar se o modelo sistematicamente deixou de oferecer crédito a um recorte, a resposta terá que vir de um log que hoje ninguém está escrevendo. E log de não-evento é impossível de reconstruir retroativamente. Não existe backfill de ausência.

**Segunda, e essa é a melhor:** registrar toda oferta suprimida é registrar o infinito — e pior, para agregar por segmento você precisa **inferir e armazenar atributo sensível** que hoje o banco deliberadamente não guarda. Ou seja: o controle de discriminação cria um dataset de discriminação.

Esse é o dilema real, e não tem saída elegante. Minha posição: não se registra o infinito. Registra-se o **conjunto elegível** — quem passou no filtro de política e mesmo assim não viu a oferta —, agregado, com atributo derivado de proxy geográfico e de comportamento que o banco já tem, sem criar coleta nova. Isso não é privacidade perfeita. É a escolha entre um risco que você desenha e um risco que você descobre em audiência pública.

---

### Por que isso não é assunto de 2028

Porque a fiscalização já tem data, ainda que a lei não tenha.

O **PL 2338** — que copia a lógica de faixas de risco do AI Act e coloca **crédito e acesso a serviços essenciais na faixa alta** — foi aprovado no Senado em **10/12/2024**, está na Câmara desde março de 2025 e tem votação prevista **apenas para dezembro**, com SIA e sanção de até **R$ 50 milhões** por infração (*DIAP*; *Senado*).

Só que a **ANPD** não está esperando: incluiu IA no Mapa de Prioridades e programou **20 fiscalizações específicas de IA para 2026–2027**, no desenho de reguladora residual dos setores sem norma própria (*Plugged.ninja*; *ANPD/gov.br*). Quem está esperando o PL 2338 para começar a documentar está esperando a regra errada — a LGPD já regula o que interessa.

O atraso do marco legal parece fôlego e é dívida. Cada mês sem regra é um mês em que o banco desenha arquitetura sob hipótese própria do que será "alto risco" — e a norma, quando vier, vale para o que **já está rodando**. Retrofit de trilha em motor de recomendação vivo custa uma ordem de grandeza a mais que instrumentar no dia zero.

---

### O que eu diria num board

Três perguntas, nessa ordem:

**1.** Nosso motor de recomendação distribui produto de crédito? Se a resposta for sim — e em todo grande banco brasileiro já é —, ele é infraestrutura de acesso, não de marketing, e não pode continuar reportando para a mesma governança de campanha.

**2.** Conseguimos responder, com dado, se um recorte de clientes elegíveis viu menos oferta de crédito no último trimestre? Se a resposta for "não temos esse log", esse é o item mais barato do backlog hoje e o mais caro daqui a dezoito meses.

**3.** Qual a nossa **inadimplência por origem de jornada** — recomendado pelo modelo, buscado pelo cliente, assistido por humano? Sem esse corte, não dá para dizer se a personalização está incluindo ou empurrando. E a resposta do Gonzalez à fricção não é fricção: é observabilidade.

A ação concreta: um **ledger de recomendação** com três campos por evento — **o que foi exibido**, **o que foi suprimido dentro do conjunto elegível**, e **a versão do modelo que decidiu** —, agregado por segmento, com retenção definida. Barato agora. Impossível depois.

É a fronteira exata entre os meus dois produtos: **Veltrix** mede custo por chamada de recomendação, por jornada e por jurisdição; **Cohort** carrega o mandato do agente de recomendação — quais produtos pode empurrar, para quem, sob qual base legal.

---

O Brasil construiu o trilho de pagamento mais invejado do mundo e está prestes a plugar nele a decisão de quem enxerga crédito.

A pergunta que eu faria ao seu comitê não é se o modelo é justo. É mais simples: **se ele não for, vocês conseguiriam provar?**

---

## Ganchos de variação (teste A/B)

1. **[Cena]** Um cliente em Manaus abre o app. O crédito consignado não aparece. Não porque alguém negou — porque o modelo achou que não valia o espaço da tela. Não existe negativa, não existe protocolo, não existe log.

2. **[Número seco]** 100% da base do BB migrada até setembro, com IA recomendando produto financeiro. 86% do país no Pix. Fluxo futuro virando garantia de crédito. Três fatos da mesma semana — e nenhum log da oferta que não foi exibida.

3. **[Provocação de comitê]** Seu banco loga toda proposta de crédito negada. Consegue me dizer quantos clientes elegíveis simplesmente nunca viram a oferta? Se não consegue, você tem um canal de distribuição de crédito operando como campanha de marketing.

---

## Fontes

- **Agência Brasil, 24/08/2026** — Banco do Brasil lança novo app com foco em IA e personalização; migração de 100% da base até o fim de setembro. https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/banco-do-brasil-lanca-novo-aplicativo-com-foco-em-ia-e-personalizacao
- **Diário do Comércio, 24/08/2026** — Novo App BB: IA, personalização e autonomia. https://diariodocomercio.com.br/negocios/banco-brasil-novo-app-ia/
- **Convergência Digital, 24/08/2026** — BC no Febraban Tech: 86% da população no Pix; Pix Automático com 20 mi de autorizações e 1.000 → 14.000 recebedores; fluxo futuro como garantia de crédito; estudo *Geografia do Pix* (Lauro Gonzalez, FGV-SP): AM 48, N/NE 40, Sul <30. https://convergenciadigital.com.br/governo/banco-central-pix-sera-cada-vez-mais-integrado-a-outros-meios-de-pagamentos/
- **DIAP** — PL 2338/23: votação prevista apenas para dezembro; SIA; sanção de até R$ 50 mi. https://www.diap.org.br/index.php/noticias/noticias/92249-pl-2338-23-votacao-do-projeto-sobre-inteligencia-artificial-esta-prevista-apenas-para-dezembro
- **Senado — PL 2338/2023 (tramitação)** — aprovado no plenário do Senado em 10/12/2024; na Câmara desde março/2025. https://www25.senado.leg.br/web/atividade/materias/-/materia/157233
- **Plugged.ninja, jul/2026 · ANPD/gov.br** — ANPD inclui IA no Mapa de Prioridades: 20 fiscalizações específicas de IA para 2026–2027; desenho de reguladora residual. https://www.plugged.ninja/2026/07/pl-762-2026-pl-704-2026-anpd-fiscalizacao-ia-brasil-pl-2338-julho/
- **LGPD, art. 20** — decisão automatizada e direito à revisão.

---

**Notas de edição (Bruno):**
- O contraponto nº 2 (o ledger cria dataset de atributo sensível) é o mais forte do texto e é onde alguém vai me atacar. Está respondido com "conjunto elegível + proxy que o banco já tem" — se quiser blindar mais, vale citar a técnica em nota, mas encompridar aqui mata o ritmo do feed.
- O BB aqui é **exemplo**, não alvo. Se soar como acusação ao banco, a tese perde: o alvo é a arquitetura que todo grande banco brasileiro está subindo ao mesmo tempo. Considerar trocar "novo App BB" por "um dos maiores bancos do país" se quiser tirar o nome.
- Veltrix/Cohort estão em um parágrafo só, perto do fim. Se soar comercial demais, corte inteiro — a tese sobrevive.
- O número "74 mi de transações" (BIA/b.ia) foi deliberadamente deixado de fora: aparece atribuído a duas instituições diferentes e não está confirmado em fonte primária.
