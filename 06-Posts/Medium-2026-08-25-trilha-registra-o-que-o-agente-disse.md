---
tipo: post
data: 2026-08-25
canal: medium
registro: tecnico
status: rascunho
eixos: [agentes, governanca, seguranca, financeiro]
maturidade: 3
origem_linkedin: "[[Post-LinkedIn-2026-08-25-trilha-registra-o-que-o-agente-disse]]"
tags: [post, medium, 2026-W35]
---

# 📰 Medium — A trilha de auditoria de agente cobre a mensagem, não o canal

**Título:** A trilha de auditoria de agente cobre a mensagem, não o canal

**Dek:**
A detecção de coordenação encoberta entre agentes cai de 0,993 para 0,854 quando os modelos são de fornecedores diferentes — que é a descrição literal de qualquer frota bancária.
E a pressão que empurra o handoff para fora do texto não é ataque: é economia de token.

---

## O número

O trabalho que origina este texto é um preprint publicado no arXiv em 19/08/2026 — *Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication* (arXiv:2608.19161), assinado por pesquisadores do SRI International, MIT Media Lab e University of Florida. **Preprint, sem revisão por pares** — registro isso antes de citar qualquer número, porque a força do argumento não depende da precisão do decimal.

O que os autores fizeram: montaram um canal em que o **estado oculto do último token** (last-token hidden state) do agente emissor é convertido em vetor e injetado diretamente na entrada do receptor, sem jamais passar por texto. Depois construíram um monitor — **VLA (Verifiable Latent Alignments)** — treinado **apenas com tráfego legítimo**, sem exemplos de ataque, e mediram a capacidade dele de flagrar coordenação encoberta.

| Configuração | Métrica | Valor |
|---|---|---|
| Agentes da **mesma família** de modelo | AUROC do monitor | **0,993** |
| Agentes de **famílias diferentes** (par heterogêneo) | AUROC do monitor | **0,854** |
| Leilão-cartel, 25–100 licitantes (NandaTown) | Redução do lance colusivo após intervenção | **47,3 p.p.** |
| Modo caixa-branca | Recuperação da mensagem latente | 100% *(teste de sanidade, não eficácia)* |

**Como ler a tabela.** AUROC é a probabilidade de o monitor ranquear um caso positivo acima de um negativo escolhido ao acaso. 0,993 é praticamente resolvido. 0,854 é um detector que erra o suficiente para não sustentar uma decisão de bloqueio sozinho — e é o número do cenário heterogêneo.

A distância entre os dois não é ruído estatístico. É estrutural: o monitor aprende a geometria do espaço de representação do emissor. Quando emissor e receptor compartilham família, essa geometria é a mesma. Quando não compartilham, o monitor está lendo um idioma que não é o seu.

**A série que importa não é a do paper — é a da frota.** Estes são os números públicos de escala de agentes no banking brasileiro em ago/2026:

| Instituição | Escala declarada | Fonte |
|---|---|---|
| Banco do Brasil | 12 mil agentes Copilot · 1.200 modelos em produção | Let's Money, ago/2026 ⚠️ conferir |
| Santander | 280+ agentes (crédito, fraude, KYC, operações) · meta de € 200 mi de valor em 2026 | Let's Money, ago/2026 ⚠️ conferir |
| Itaú | 1,3 mil modelos em uso · **−65%** de custo de GenAI desde 2022 | Mobile Time, 09/03 e 27/07/2026 ⚠️ autorrelato sem baseline |
| Bradesco | b.ia com 74 mi de interações no 1S26 | Consumidor Moderno, 06/08/2026 |

Quatro unidades de medida diferentes, nenhuma comparável — e **nenhuma delas é uma métrica do canal**. Todas contam agentes, modelos ou interações. Nenhuma conta arestas, e é na aresta que este risco mora.

## O mecanismo

### Como o handoff funciona hoje

Dois agentes conversam por texto. O emissor comprime seu estado interno em linguagem — uma mensagem, um JSON, uma chamada de ferramenta. O receptor lê e reconstrói. Sobre esse tráfego, os protocolos que o mercado adotou (A2A, MCP) e a instrumentação que os bancos estão construindo funcionam bem: há uma mensagem, ela tem carimbo de tempo, ela entra no log.

Duas coisas são verdadeiras ao mesmo tempo sobre esse desenho. É auditável. E é caro.

Caro porque a compressão em linguagem é lossy nas duas pontas e verbosa no meio: o emissor gasta token para dizer o que já sabia, o receptor gasta token para reler, e a informação que sobrevive é menor que a que existia. Numa arquitetura com dezenas de saltos por tarefa, isso aparece na conta.

### O que o canal latente muda

O caminho latente elimina a linguagem do meio. O estado do emissor entra no receptor como vetor. Menos token, menos perda, menos round-trip.

E nada disso produz uma mensagem.

O ponto que interessa a quem desenha arquitetura não é o cartel do experimento. É a assimetria: **o observador do sistema passou a ver a ação sem ver o estado que a produziu**. O log de conversas continua íntegro, completo, assinado — e cego para uma classe inteira de troca. Ele não está errado. Ele está cobrindo o canal errado.

Isso conversa diretamente com uma tese que já defendo aqui: [[O scratchpad exposto e feature de fornecedor nao trilha de auditoria de agente]]. Lá, o problema é que o rascunho **mostrado** pelo fornecedor não é prova do que decidiu. Aqui, o problema é anterior: existe um caminho que **nunca é mostrado**, porque nunca foi texto. Visibilidade não é verificabilidade, e agora nem a visibilidade está garantida.

### Por que isso chega pela porta do FinOps

Este é o parágrafo que eu levaria a um comitê de arquitetura antes de qualquer outro.

O Itaú reporta **−65%** no custo de IA generativa desde 2022, e o caminho declarado é explícito: gestão inteligente de tokens, plataforma única centralizada, governança de consumo (Mobile Time, 27/07/2026). É a disciplina correta — é literalmente o argumento que sustento com o Veltrix. E é exatamente essa disciplina, funcionando bem, que cria a pressão.

Numa casa que já cortou 65% apertando token, "comprimir o handoff entre agentes" não chega como proposta de risco. Chega como otimização. Passa por code review, não por comitê. E a primeira versão vai ser inocente: um cache de embedding, um estado compartilhado entre dois passos do mesmo pipeline, um "por que serializar isso em JSON se os dois modelos são do mesmo provedor?".

O risco não entra pela porta do adversário. Entra pela porta da eficiência — e a eficiência tem patrocínio executivo.

## O contraponto

Formulo o melhor argumento contrário, porque ele é bom.

**Primeiro:** o modelo de ameaça do paper é artificial em três frentes que os próprios autores declaram. O código de coordenação encoberta é fixo e previamente otimizado; o agente receptor é **instruído** sobre a existência do canal; o ambiente é um leilão controlado com regras conhecidas. Isso não é um adversário adaptativo — é um demonstrador. E a recuperação de 100% no modo caixa-branca prova que o canal existe, não que o monitor funciona.

**Segundo:** ninguém em produção bancária está passando hidden state entre agentes hoje. O tráfego real é texto sobre protocolo. Instrumentar contra um vetor de ataque sem incidência é o tipo de gasto que a segurança de IA precisa parar de fazer, num ano em que há prazo de qualidade de dados fechando em dezembro e fiscalização da ANPD agendada.

**Concordo com as duas premissas. Discordo da conclusão** — por uma razão de custo, não de medo.

O que estou propondo não é uma defesa. É um **rótulo**. Classificar o tipo de payload de cada aresta do grafo de agentes é trabalho de instrumentação, não de segurança; custa próximo de zero enquanto o grafo é textual e enquanto ele é pequeno. O que custa caro é o inverso: descobrir em auditoria — ou numa consulta do regulador sobre uma decisão específica — que existe uma classe de troca fora da trilha, e não conseguir dizer **desde quando**. Retrofit de rastreabilidade em 12 mil agentes não é projeto de segurança; é arqueologia com prazo.

E há um detalhe do cenário do paper que não é decorativo: **supressão coordenada de lance tem nome no direito concorrencial**. O dia em que dois agentes de instituições diferentes convergirem para uma condição comercial sem transcrição que explique a convergência, a pergunta não vai ser técnica. Vai ser a mesma que abri em [[Post-LinkedIn-2026-08-20-passivo-em-cadeia-a2a]] — quem responde — só que sem material para responder.

## O que eu faria

Três pontos de medição, na ordem. Nenhum deles exige comprar produto novo.

**1. Inventário de aresta, não de agente.**
Toda comunicação agente→agente classificada em `texto` · `estruturado` · `representação` (embedding/estado interno).
→ Métrica: **% de arestas com payload não-textual**.
Se o time não consegue responder isso em uma semana, o problema já não é o canal latente — é que o grafo de agentes não está inventariado. O placar de frota ([[Placar do Parque de Agentes (FMC) - Frota, Mandato, Custo]]) mede agente e custo; esta coluna é o que falta nele.

**2. Vínculo estado-recebido → ação-pública.**
Identificador de correlação ligando a entrada que moldou a decisão à saída registrada. Quando a entrada for vetorial, registrar `hash + dimensão + modelo de origem` — não o vetor (guardar o vetor cria um problema de dado pessoal onde não havia).
→ Métrica: **% de ações de agente com entrada vinculada**, contando entrada não-textual no denominador.
No [[Mandato do Agente - escopo, limite, jurisdicao, trilha]], isso pertence à dimensão **trilha**: é parte do mandato, não log de aplicação. É a diferença entre "temos observabilidade" e "temos prova".

**3. Heterogeneidade medida em par, não em fornecedor.**
Não "quantos fornecedores temos", e sim **% de decisões executadas em par emissor-receptor de fornecedores diferentes**.
→ É o denominador do 0,854. E é a exigência contratual que decorre disso: qualquer monitor de comportamento de agente que você contratar precisa reportar performance **no par heterogêneo**, nunca a média agregada. A média esconde exatamente o cenário que você opera — o mesmo erro de leitura que já apontei em ranking de IA e em orçamento de tecnologia: a média esconde a concentração.

**E um gatilho de contrato, não de arquitetura.** Vigiar se plataformas que hospedam agentes passam a expor **interface de auditoria de ativações/estado latente**. No dia em que a primeira expuser, isso sai do backlog de engenharia e vira cláusula de fornecedor — e quem já tiver a coluna do item 1 preenchida negocia com dado, não com hipótese.

---

**Frameworks citados:** [[Mandato do Agente - escopo, limite, jurisdicao, trilha]] · [[Placar do Parque de Agentes (FMC) - Frota, Mandato, Custo]] · [[Matriz de Execucao do Agente (VCAP) - Valor, Canal, Autenticacao, Prova]]
**Post de LinkedIn de origem:** [[Post-LinkedIn-2026-08-25-trilha-registra-o-que-o-agente-disse]]
**Notas internas:** [[Agentes coordenam em estado latente e a auditoria de texto registra o que o agente disse nao o que sabia]] · [[O scratchpad exposto e feature de fornecedor nao trilha de auditoria de agente]] · [[2026-08-21]] · [[Weekly-2026-08-22]]
**Capa:** 16:9 conforme [[Identidade-Visual-Editorial]] — mesma cena do post (corredor de arquivos etiquetados; o cano sem inspeção rente ao rodapé, em vermelhão), reenquadrada com mais corredor à esquerda e a silhueta deslocada para o terço direito.

## Fontes

1. **arXiv:2608.19161**, 19/08/2026 — *Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication* (SRI International · MIT Media Lab · University of Florida) · https://arxiv.org/abs/2608.19161 · ⚠️ **conferir**: preprint sem revisão por pares
2. **Plugged Ninja**, 20/08/2026 — Agentes de IA podem combinar ações fora do registro público · https://www.plugged.ninja/2026/08/agentes-de-ia-conluio-latente-deteccao-vla/
3. **Mobile Time**, 27/07/2026 — Itaú reduziu 65% o custo com IA generativa desde 2022 · https://www.mobiletime.com.br/noticias/27/07/2026/itau-custo-ia-generativa/ · ⚠️ **conferir**: autorrelato sem baseline auditável (variação, não nível)
4. **Mobile Time**, 09/03/2026 — Itaú tem mais de 1,3 mil modelos de IA em uso · https://www.mobiletime.com.br/noticias/09/03/2026/itau-modelos-ia/
5. **Let's Money**, ago/2026 — Banco do Brasil: 12 mil agentes Copilot, 1.200 modelos em produção · https://www.letsmoney.com.br/noticias/banco-do-brasil-academia-bb-ia-agentica · ⚠️ **conferir**: imprensa secundária, sem documento primário do banco
6. **Let's Money**, ago/2026 — Santander: 280+ agentes, meta de € 200 mi em 2026 · https://www.letsmoney.com.br/noticias/santander-libera-ia-185-mil-funcionarios-200-milhoes/ · ⚠️ **conferir**
7. **Consumidor Moderno**, 06/08/2026 — Bradesco: b.ia com 74 mi de interações no 1S26 · https://consumidormoderno.com.br/meu-bradesco-novo-ecossistema-solucoes-ia-cx/

---
## ✅ Checklist antes de publicar
- [x] Acrescenta algo que **não estava** no post de LinkedIn? (tabela de AUROC com leitura da métrica, tabela de escala da frota BR, seção de por que o risco entra pela porta do FinOps, distinção rótulo × defesa)
- [x] Título é afirmação e cabe em 12 palavras? (10)
- [x] Linka o post de origem e as notas de `05-Frameworks/`?
- [x] Fontes com link, não só nome?
- [x] O card de LinkedIn promete "análise completa no Medium" — esta análise existe?
