---
tipo: plano
produto: One Banking Hub (nome provisório)
versao: 0.1
data: 2026-09-04
status: rascunho para decisão
horizonte: 2026-09-08 a 2026-12-04
tags: [plano, portal, formacao, banking, ecossistema]
---

# Estratégia e plano de 90 dias — One Banking Hub

> Companheiro do PRD v0.1. A estratégia responde "por que esse ecossistema e não um SharePoint"; o plano responde "o que acontece segunda-feira".

## 1. A estratégia em uma frase

Transformar o sistema pessoal que já roda (coleta automática → vault → digest → posts) em **função institucional da prática**, adicionando as duas peças que ele não tem: uma vitrine que qualquer pessoa consegue usar e uma trilha que forma quem chega. O portal não cria conteúdo novo; ele torna acessível e confiável o que a máquina já produz, e a trilha transforma esse acervo em capacidade do time.

## 2. O ecossistema completo — as seis camadas

Cada camada tem um dono, uma cadência e um artefato. A regra herdada do escritório de IA vale aqui: se uma camada não tem quem abre, que decisão muda e se é transferível, ela não existe.

| Camada | O que é | Estado | Dono / cadência |
|---|---|---|---|
| **1. Fontes** | Newsletters Tier A/B, reports, portais oficiais (BCB, Febraban, OFB, ANPD), X/Reddit | Rodando | Bruno · higiene quinzenal |
| **2. Coleta e destilação** | Rotinas Cowork: digest 6h, auto-digest 10h, weekly sexta, discovery noturno, ingestão de reports | Rodando; discovery sem alvo | Máquina · diária |
| **3. Acervo (vault)** | ~500 notas com frontmatter por tipo; ledgers; auditoria de proveniência | Rodando; 45 correções pendentes; iCloud sem git | Bruno + 2º curador · semanal |
| **4. Vitrine (portal)** | O front end: acervo, comparativos, news, regulatório, projetos, busca, chat | **A construir** | Time de produto (Bruno + 1 dev) · deploy diário |
| **5. Formação (trilha)** | 8 módulos, 40 lições, certificado interno; "o que mudou" ligado ao digest | **A construir** | Bruno (roteiro/tese) + máquina (vídeo/quiz) · 1 módulo a cada 2 semanas |
| **6. Comunidade e retorno** | Office hours quinzenal, clube de leitura de reports mensal, canal no Teams com o digest, "sugerir correção", perguntas sem resposta viram backlog de conteúdo | **A criar** | Bruno + líderes de conta · quinzenal |

O que fecha o loop é a camada 6: a pergunta que o portal não respondeu vira nota no vault na semana seguinte, e a correção sugerida por alguém da conta passa pela mesma auditoria de proveniência que o resto. É isso que faz o conhecimento "evoluir de forma contínua" sem depender de uma pessoa lembrar de atualizar.

**Antecipação** vem de duas mecânicas concretas, não de intenção: o radar regulatório com alerta 30 dias antes de cada prazo, e a aba "o que mudou desde que você estudou isso" em cada módulo, que cruza os eixos e players da lição com o digest do dia.

## 3. Por que app web e não SharePoint ou Notion

Você escolheu app web com backend. O que essa escolha compra, e o que cobra: compra progresso de trilha por pessoa, quiz com nota, selo de proveniência como dado (não como texto), busca com filtro por tipo de nota, chat com citação, e liberdade visual — nada disso existe de forma decente em SharePoint ou Notion. Cobra 4–8 semanas até a versão completa, um dev (ou você com o Cowork gerando o esqueleto), e uma decisão de hospedagem com a TI. O plano abaixo reduz a conta: o MVP de 3 semanas usa ingestão em build (sem backend complexo) e só o progresso da trilha e as sugestões de correção tocam o banco.

## 4. Roadmap de 90 dias

### Sprint 0 — semana de 08/09: decisões e fundação

Sem isso, nada abaixo começa.

- Decidir nome, hospedagem/SSO e a regra editorial sobre Veltrix/Cohort (três decisões suas; §11 do PRD).
- Aplicar (ou recusar) as 45 correções da auditoria de proveniência — uma sessão de 1 h. É pré-requisito para expor o acervo.
- Vault em git: "manter baixado nesta máquina" no iCloud, repositório privado, commit automático diário depois das rotinas. Sem PDFs no git; eles ficam no storage.
- Escolher 5 pessoas-piloto: 2 recém-chegadas, 1 líder de conta, 1 arquiteto, 1 líder da prática.
- Entregável: repositório do vault sincronizado, decisões registradas no PRD v0.2.

### Sprint 1 — 14/09 a 25/09: esqueleto do portal

- Pipeline de ingestão (parser de frontmatter, wikilinks, tabelas) → Postgres. Teste de aceitação: as 192 notas de Financeiro entram sem erro e todo wikilink resolve.
- App Next.js atrás de login: Home, Instituições, Produtos (matriz 11×8), Comparativos (6 jornadas De-Para), News (70 edições), Busca.
- Selo de proveniência lido da auditoria (afirmação → selo → fonte).
- Módulo 1 da trilha: roteiros das 5 lições escritos por você (tese sua, ~600 palavras cada), narração e vídeo gerados, 5 quizzes, 5 exercícios com o acervo.
- Entregável: URL funcionando para os 5 pilotos em 25/09.

### Sprint 2 — 28/09 a 09/10: validação e trilha

- Teste com os pilotos: 3 tarefas cronometradas (achar um comparativo, responder "quem já faz Pix por aproximação", concluir a lição 1). Meta: ≤ 3 min por tarefa sem ajuda.
- Motor da trilha completo: progresso, quiz com nota, certificado interno ao fechar módulos 1–4.
- "Sugerir correção" com fila de curadoria.
- Módulo 2 (Produtos de varejo).
- Entregável: relatório de validação de 1 página + decisão go/no-go para abrir à prática inteira.

### Sprint 3 — 12/10 a 23/10: abertura e estrutura nova

- Abrir para toda a prática (com o digest anunciando).
- Registro regulatório (`08-Regulatorio/`, uma nota por norma) e radar de prazos com alerta.
- Grandes projetos do setor (`09-Projetos-Setor/`: Pix, Open Finance, Drex, Open Insurance, tokenização).
- Módulo 3 (Meios de pagamento) e glossário v1 (termos dos módulos 1–3).
- Primeiro office hours e primeiro clube de leitura (report escolhido: Pesquisa Febraban 2026).

### Sprint 4 — 26/10 a 06/11: iniciativas, frameworks, reports

- Páginas de Iniciativas (36, com placar VALE), Frameworks (19) e Reports (22 + 3 pendentes).
- Fichas de instituição enriquecidas (rotina noturna reaproveitada — ela está sem alvo desde julho).
- Módulo 4 (Pix e Open Finance). Primeiras pessoas com certificado "Banking Foundations".

### Sprint 5 — 09/11 a 20/11: antecipação e clientes

- Aba "o que mudou" por módulo, cruzando eixos e players com o digest.
- Fichas de cliente no vault (migração do dossiê, com revisão de confidencialidade e aval).
- Módulo 5 (Crédito, risco e fraude).
- Painel de curadoria: sem fonte, sem tese, sem atualização há 90 dias.

### Sprint 6 — 23/11 a 04/12: pergunte ao acervo e balanço

- Chat com recuperação sobre o acervo, resposta sempre com fontes e selo.
- Módulo 6 (Regulação e cibersegurança). Módulos 7 e 8 ficam para janeiro.
- Balanço de 90 dias contra as métricas do PRD §10; decisão sobre o segundo curador e sobre a versão 2027.

## 5. Como a trilha é produzida — a linha de montagem

A produção segue o princípio da casa: **a máquina monta, a tese é sua**.

1. **Ementa** (feita, PRD §7) → você ajusta o que quer que a pessoa saiba dizer ao final de cada módulo.
2. **Roteiro** — você escreve ou dita 600 palavras por lição, com a leitura curada e o exercício. O Cowork rascunha a partir do acervo e das fontes oficiais; a opinião ("o que eu diria num board") é sua. Passa pelo pente anti-slop antes de gravar.
3. **Vídeo** — narração e cenas geradas por IA a partir do roteiro, com legenda extraída do próprio texto; identidade visual do portal, não a editorial pessoal.
4. **Quiz e exercício** — 8 questões por lição geradas do roteiro e revisadas por você; exercício sempre aponta para uma nota real do acervo.
5. **Publicação** — a lição vira nota no vault (`10-Formacao/M01/L01.md` com frontmatter `tipo: licao`), e o pipeline a leva ao portal como qualquer outra nota.

Ritmo sustentável: um módulo (5 lições) a cada duas semanas exige cerca de 4 h suas por quinzena para roteiro e revisão. Se isso não couber, o módulo atrasa — não se pula a revisão.

## 6. Papéis

| Papel | Quem | Horas/semana |
|---|---|---|
| Dono do produto e curador-chefe | Bruno | 4–6 |
| Dev (Next.js/Postgres) | 1 pessoa da prática ou Cowork gerando o esqueleto com revisão sua | 15–20 nas sprints 1–2; 8 depois |
| Segundo curador | A escolher até a sprint 3 | 2–3 |
| Pilotos | 5 pessoas | 1 na sprint 2 |
| Comunicação/compliance | Consulta pontual (voz sintética, hospedagem) | Pontual |

## 7. Riscos e como reduzi-los

Dependência de uma pessoa: o segundo curador é meta da sprint 3, não desejo. Acervo com erro exposto: correções antes do MVP, selo de proveniência em tudo, "sugerir correção" desde o dia 1. TI corporativa bloquear hospedagem: MVP em ambiente próprio com SSO e migração planejada; nada de dado de cliente até migrar. Vídeos sintéticos rejeitados: o roteiro é o ativo; regravar com voz humana custa uma tarde. Ninguém usar: o digest já tem leitores — o portal nasce dentro dele (todo item linka a página do acervo), e a trilha entra no onboarding oficial da prática como etapa, não como sugestão.

## 8. O que eu diria sobre isso num board

A prática de Banking tem um ativo que os concorrentes de consultoria não têm: um acervo auditado do mercado brasileiro, com proveniência, produzido todo dia por máquina e revisado por gente. Hoje ele está preso num Obsidian. O portal e a trilha custam um dev por dois meses e quatro horas semanais de curadoria; o retorno é medível em duas linhas — propostas que citam o acervo e tempo de rampa de quem entra. Se em 90 dias nenhuma proposta citar o portal e menos da metade dos novos concluir o módulo 1, o problema não é o portal, é a prática não ter decidido que conhecimento do setor é obrigação de todos. Nesse caso, encerra-se e o acervo continua servindo ao digest como antes.

## Segunda-feira, 08/09 — as três primeiras ações

1. Sessão de 1 h: aplicar as 45 correções da auditoria de proveniência.
2. iCloud "manter baixado" + repositório git do vault.
3. Responder as três decisões do PRD §11 (nome, hospedagem/SSO, regra Veltrix/Cohort) e escolher os 5 pilotos.
