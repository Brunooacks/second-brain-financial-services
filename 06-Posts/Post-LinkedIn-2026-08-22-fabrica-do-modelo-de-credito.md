---
tipo: post
data: 2026-08-22
canal: linkedin
status: rascunho
eixos: [financeiro, governanca, agentes]
maturidade: 4
tags: [post, linkedin, semana, 2026-W34]
---

# 🧵 Long-form — Quem vai testemunhar como o modelo de crédito nasceu?

> Tese da semana W34. Origem: [[Quando o agente constroi o modelo de credito o objeto regulado vira o processo nao o modelo]] · lastro de calendário em [[O prazo de qualidade de dados e o gargalo real da governanca de IA bancaria]].
> Distinta de [[Post-LinkedIn-2026-08-15-explicabilidade-arquitetura-anpd]] (lá o objeto é a **decisão** de crédito; aqui é a **fábrica** que produz o modelo) e de [[Post-LinkedIn-2026-08-18-contrato-de-IA-na-unidade-errada]] (unidade de contrato).

---

## Quem vai testemunhar como o modelo de crédito nasceu?

Imagine a cena daqui a dezoito meses.

Uma sala de auditoria. Do outro lado da mesa, alguém pede a descrição do modelo de estimativa de renda que negou crédito a um cliente. O banco entrega a documentação: variáveis, pesos, métricas de performance, relatório de impacto algorítmico. Está tudo lá. Impecável.

Aí vem a segunda pergunta, que é sempre a que dói: **por que essa variável e não aquela?**

E a resposta honesta é que ninguém na sala sabe. Não por má-fé. Porque a decisão foi tomada por um agente, dentro de um pipeline, num dia de 2026 em que o time comemorava — com razão — ter reduzido de dez semanas para menos de uma o tempo de construir um modelo.

Essa cena não é ficção especulativa. Ela já tem endereço.

---

### O número

O Bradesco aplicou arquitetura agêntica à criação de modelos de estimativa de renda no **RendaBRA 5.0**. O resultado divulgado: o processo ficou **16x mais rápido** e passou a ser conduzido por **1 especialista em vez de 10**, inclusive lidando com informação incompleta (inovabra/Startups, 14/08/2026).

Leia esse número duas vezes, porque ele carrega duas notícias e o mercado só está comentando uma.

A primeira é a que está no press release: ganho de produtividade brutal numa das funções mais caras e mais lentas do banco. É real, é defensável, e qualquer diretor de risco que despreze isso vai perder a corrida.

A segunda notícia não está em slide nenhum: **uma redução de ~90% no número de pessoas capazes de testemunhar como aquele modelo nasceu.**

Documentação e testemunho não são a mesma coisa. Documentação responde "o que foi feito". Testemunho responde "por que não foi feito o contrário" — e é essa a pergunta de uma auditoria adversarial, de um processo administrativo, de uma ação civil pública. Dez especialistas discordando entre si ao longo de dez semanas produzem, como subproduto, um registro distribuído de alternativas descartadas. Um especialista revisando a saída de um agente em três dias produz aprovação, não deliberação.

---

### O calendário

Nada disso seria urgente se o relógio regulatório estivesse parado. Não está.

O **PL 762/2026** propõe **certificação e registro prévios** para sistemas de IA aplicados a crédito, com **12 meses** de adaptação após a publicação (Plugged Ninja, 09/07/2026). Certificação prévia é uma expressão com consequência de arquitetura: não se certifica previamente aquilo que não se consegue descrever.

Em paralelo, a **Resolução Conjunta nº 18** exige política de qualidade de dados implementada **até o fim de 2026** — e o prazo, mais do que a norma, virou o risco (Finsiders Brasil). No mesmo ano em que o setor vai gastar **R$ 50,4 bilhões** em tecnologia, com GenAI e nuvem como prioridade para **84%** das instituições (Pesquisa Febraban de Tecnologia Bancária 2026 / Deloitte, 34ª ed., vol. 1, jun/2026).

Junte as três coisas e o desenho aparece: bilhões indo para o modelo, com o prazo do insumo ainda aberto e a régua da fábrica chegando logo atrás.

---

### A tese

**Quando o agente participa da construção do modelo, o objeto regulado deixa de ser o modelo e passa a ser o processo que o produz.**

A Avaliação de Impacto Algorítmico que descreve apenas o modelo final está descrevendo metade do sistema. A outra metade — seleção de variável, tratamento de dado faltante, engenharia de atributos (*feature engineering*), redação da própria documentação — passou a ser executada por um componente não-determinístico que, na maioria dos bancos, não tem identidade própria, não tem mandato escrito e não deixa trilha vinculada ao artefato que produziu.

O detalhe que fecha o argumento é que o Bradesco fez o certo: a plataforma **AgentiX** roda internamente, mas delega identidade, segurança e auditoria à **Bridge** (600+ casos de uso desde abr/2024). O rastro existe por desenho. A tese não é sobre quem tem uma Bridge. É sobre os oitenta e tantos por cento do mercado que estão copiando o ganho de produtividade sem copiar a camada de identidade que o torna auditável.

---

### O contraponto honesto

Um head de risco de modelo competente me responderia duas coisas, e as duas são boas.

**Primeira:** nenhum regulador do mundo impôs, até hoje, avaliação de impacto sobre o *processo* de construção. A obrigação sempre recaiu sobre o modelo e sua saída. Exigir descrição dos agentes que o construíram é sobre-especificação — e sobre-especificação atrasa banco.

Concordo com o diagnóstico e discordo da conclusão. "Nenhum regulador impôs ainda" é uma janela, não uma defesa. E a janela é estreita: certificação prévia mais 12 meses de adaptação é um horizonte de decisão de arquitetura, não de compliance.

**Segunda:** o agente documenta melhor que o humano. Verdade. Um pipeline agêntico registra cada transformação com uma consistência que dez pessoas cansadas jamais tiveram. Mas documentação perfeita do caminho percorrido não é o mesmo que registro do caminho **não** percorrido — e é o segundo que sustenta a defesa quando alguém alega discriminação por proxy. Registro de execução não é registro de deliberação.

---

### O que eu diria num board

Todo banco tem inventário de modelos. Nenhum banco que eu conheça tem inventário de **onde há agente dentro do ciclo de vida de modelo regulado**. É esse o item que eu levaria.

Três perguntas, nessa ordem:

**1.** Quais dos nossos modelos em produção tiveram agente de IA em alguma etapa da construção — e nós rastreamos isso hoje? Se a resposta for "não rastreamos", esse é o item mais caro do backlog de conformidade dos próximos doze meses, e ele ainda não foi orçado.

**2.** O agente que participou tinha mandato escrito — escopo, limite, jurisdição, trilha — ou herdou a credencial de um humano? Agente que roda com credencial de gente não deixa rastro próprio: deixa rastro do gente.

**3.** Se a certificação prévia entrar em vigor, quanto tempo levamos para reconstruir a narrativa de construção de um modelo de crédito de 2026? Meça em dias. Se não souber medir, já é a resposta.

E uma recomendação prática: **antes de escalar agente na fábrica de modelos, escale a identidade do agente.** Ganho de velocidade sem proveniência é dívida técnica trocando de nome — sai do balanço da engenharia e entra no balanço do risco.

É exatamente aqui que o **Cohort** entra: mandato do agente por etapa, com trilha e alçada de promoção a produção. E é a outra metade da pergunta que o **Veltrix** responde: quanto custou e sob que jurisdição rodou cada chamada que produziu aquele modelo.

---

Dezesseis vezes mais rápido é uma conquista. Noventa por cento menos testemunhas é uma decisão — e decisão não anunciada é decisão não governada.

Se o seu banco está acelerando a fábrica de modelos: quem, hoje, consegue explicar como o último modelo de crédito nasceu?

---

## Ganchos de variação (teste A/B)

1. **[Cena]** Uma sala de auditoria, dezoito meses à frente. A documentação do modelo está impecável. Aí vem a pergunta que dói: *por que essa variável e não aquela?* E ninguém na sala sabe.

2. **[Número seco]** O Bradesco construiu modelo de renda 16x mais rápido, com 1 especialista em vez de 10. O press release conta essa metade. A outra: 90% menos gente capaz de testemunhar como o modelo nasceu.

3. **[Provocação de comitê]** Seu banco tem inventário de modelos. Tem inventário de onde há **agente** dentro do ciclo de vida desses modelos? Porque o PL 762 fala em certificação prévia — e não se certifica o que não se descreve.

---

## Fontes

- **inovabra / Startups, 14/08/2026** — Bradesco, RendaBRA 5.0, AgentiX e Bridge (16x mais rápido; 1 especialista vs. 10; 600+ casos de uso desde abr/2024). https://startups.com.br/branded-content/bradesco-e-reconhecido-no-premio-valor-inovacao-2026/
- **Convergência Digital** — Bradesco tem agentes de IA em todos os lugares. https://convergenciadigital.com.br/governo/bradesco-tem-agentes-ia-em-todos-os-lugares/
- **Plugged Ninja, 09/07/2026** — PL 762/2026: certificação e registro prévios para IA de crédito; 12 meses de adaptação. https://www.plugged.ninja/2026/07/pl-762-2026-pl-704-2026-anpd-fiscalizacao-ia-brasil-pl-2338-julho/
- **Finsiders Brasil** — Resolução Conjunta nº 18: política de qualidade de dados até o fim de 2026; prazo vira o maior risco. https://finsidersbrasil.com.br/regulamentacao/resolucao-conjunta-no-18-prazo-vira-o-maior-risco-da-qualidade-de-dados/
- **Pesquisa Febraban de Tecnologia Bancária 2026 / Deloitte, 34ª ed., vol. 1, jun/2026** — R$ 50,4 bi em tecnologia em 2026; GenAI e cloud prioridade para 84%. https://cmsarquivos.febraban.org.br/Arquivos/documentos/PDF/Pesquisa%20Febraban%20de%20Tecnologia%20Banca%CC%81ria%202026%20-%20Vol1.pdf

---

**Notas de edição (Bruno):**
- Checar se o "~90% menos testemunhas" fica melhor como afirmação direta ou como pergunta — hoje está como afirmação, é o ponto mais atacável e o mais memorável.
- O parágrafo do Bradesco/Bridge é elogio real, não ironia. Se soar como crítica ao banco, a tese perde — o alvo é quem copia o ganho sem a camada de identidade.
- Veltrix/Cohort estão em um parágrafo só, perto do fim. Se soar comercial demais para o feed, corte o parágrafo inteiro; a tese sobrevive sem ele.
