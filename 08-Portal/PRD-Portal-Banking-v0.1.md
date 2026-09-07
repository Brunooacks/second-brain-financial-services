---
tipo: prd
produto: One Banking Hub (nome provisório)
versao: 0.1
data: 2026-09-04
status: rascunho para decisão
autor: Bruno
eixos: [financeiro, governanca, formacao]
tags: [prd, portal, formacao, banking]
---

# PRD — One Banking Hub

> Portal interno da prática de Banking: o lugar fidedigno de informação do setor financeiro, com acervo navegável, comparativos, news diária e trilha de formação para quem chega ao setor. Versão 0.1, para decisão. Sexta-feira, 04/09/2026.

## 1. O problema

A prática de Banking já produz um acervo de conhecimento raro no mercado: 11 instituições mapeadas em 8 categorias de produto, 6 jornadas comparadas com nível de maturidade agêntica, 36 iniciativas priorizadas com placar, 19 frameworks próprios, 22 reports destilados com página citada, 70 edições de digest diário e uma auditoria de proveniência que já derrubou 28 de 88 "ganhos" copiados de fonte secundária. Nada disso é acessível para quem não abre o Obsidian de uma pessoa. Hoje esse conhecimento chega ao time por PDF no e-mail, por conversa ou não chega.

O segundo problema é a base. A prática recebe pessoas de tecnologia sem formação no setor. Elas aprendem o que é SPI, DICT, MDR, suitability ou Res. 4.893 no meio do projeto, com o cliente, e cada uma aprende de um jeito. Não existe onboarding bancário — só onboarding de conta.

O terceiro é a confiabilidade. O mercado repete número sem fonte; a auditoria de proveniência do próprio acervo mostrou que 32% das afirmações herdadas não paravam em pé contra documento primário. Um portal que só junte conteúdo repete o problema; um portal fidedigno precisa mostrar o lastro de cada dado.

## 2. Visão e princípios

**Visão.** Um único lugar onde qualquer pessoa da prática entende o setor, compara players, acompanha o que mudou hoje e se forma de maneira contínua — com cada afirmação ligada à sua fonte.

Princípios de produto, na ordem em que desempatam decisões:

1. **Proveniência visível.** Todo número exibe selo: *fonte primária* · *declarado pela instituição* · *imprensa secundária* · *sem fonte*. É o diferencial do portal e o que o torna citável em proposta.
2. **O vault é a fonte, o portal é a vitrine.** Nenhum conteúdo nasce no portal; nasce em nota com frontmatter e entra por pipeline. Isso preserva a regra "automatizar a coleta, nunca o pensamento" e evita dois acervos divergentes.
3. **Amigável antes de completo.** Quem abre pela primeira vez precisa responder "o que é Pix por aproximação e quem já faz" em menos de um minuto, sem tutorial.
4. **Formação encadeada com a notícia.** Cada módulo da trilha tem uma aba "o que mudou desde que você estudou isso", alimentada pelo digest. É assim que a evolução fica contínua e antecipada, e não um curso que envelhece.
5. **Tom consultivo.** O portal descreve o estado do mercado; não julga instituição nomeada. Vale para ficha, comparativo e news.

## 3. Personas e jobs

| Persona | Quem é | O que precisa fazer | Sucesso |
|---|---|---|---|
| **Recém-chegada** (prioridade 1) | Dev, analista ou PM que entrou na prática sem base bancária | Entender o setor em 30 dias; parar de perguntar o básico | Completa módulos 1–4 em 4 semanas e passa no quiz com ≥ 80% |
| **Líder de conta / pré-venda** | Conhece o cliente, precisa do mercado | Comparar o cliente com os pares, achar o número com fonte para a proposta, saber o que mudou na semana | Cita o portal numa proposta; leva ≤ 3 min para achar o comparativo |
| **Arquiteto / engenheiro** | Está desenhando solução no cliente | Ver a jornada em BIAN, o nível EMA-J do player, a iniciativa de referência e o frame regulatório aplicável | Usa a ficha de iniciativa como ponto de partida do desenho |
| **Liderança da prática** | Decide portfólio e alocação | Ver placar VALE, backlog de iniciativas, radar regulatório com prazos | Abre o portal antes do comitê em vez de pedir slide |
| **Curador** (Bruno + 1) | Mantém o acervo | Ver o que está desatualizado, sem fonte ou sem tese; aprovar correções | Fila de curadoria zerada semanalmente |

## 4. Escopo por módulo

### 4.1 Módulos do MVP (semanas 1–3)

**Home.** Três pontos de atenção da semana (do digest), termômetro do dia, "novo no acervo" (últimas notas por tipo), o progresso da pessoa na trilha e uma busca única no topo.

**Instituições.** Uma página por player (23 hoje: 5 bancões, 4 fintechs, 3 adquirentes, 10 concorrentes de consultoria) com ficha, produtos, posição em cada jornada e as notícias em que aparece. As fichas atuais têm ~860 bytes — o MVP aceita ficha curta e marca "ficha em enriquecimento".

**Produtos.** Matriz 11 players × 8 categorias (Conta PF, Conta PJ, Cartão, Crédito, Investimentos, Seguros, Pagamentos/Pix, Adquirência) com a nota por célula e o comparativo por categoria.

**Comparativos.** As 6 jornadas (Onboarding & KYC · Originação de crédito · Pagamentos & Pix · Fraude & disputas · Atendimento & cobrança · Investimentos & advisor) como tabela De-Para com nível EMA-J L1–L5 por player e por Service Domain BIAN, com filtro por player e exportação para slide.

**News.** As edições do One Banking AI (70 em .md, com HTML já renderizado) navegáveis por data, seção e eixo, com busca no arquivo e assinatura por e-mail já existente.

**Formação — Módulo 1 (SFN e papéis das instituições).** Cinco lições com vídeo, leitura curada, exercício e quiz; progresso salvo por pessoa. É o único módulo produzido no MVP; os demais entram como "em breve" com a ementa visível.

**Busca.** Full-text sobre todo o acervo com filtro por tipo (`tipo` do frontmatter), eixo, player, data e selo de proveniência.

### 4.2 Módulos da fase seguinte (semanas 4–12)

**Regulatório.** Registro estruturado: uma entrada por norma (número, órgão, data, prazo de adequação, a quem se aplica, impacto em IA/dados, status de verificação, link oficial) e um radar com os prazos dos próximos 12 meses. Não existe hoje como estrutura — só espalhado nas notas de refresh.

**Grandes projetos do setor.** Páginas vivas de Pix (Automático, por aproximação, iniciação sem redirecionamento), Open Finance (fases, diretório, certificação), Drex (como caso histórico 2021–2025, com a reorientação de nov/2025), Open Insurance, cadastro positivo, tokenização. Não existe hoje.

**Iniciativas e ofertas.** As 36 fichas com placar VALE, filtro por jornada, fase e player-alvo; a nota de portfólio consultivo de ofertas como página-mãe.

**Frameworks.** Os 19 frameworks como páginas com o diagrama dos eixos, exemplo aplicado e quais iniciativas os usam.

**Reports.** Biblioteca com as 22 notas destiladas (tese, achados com página, "o que eu diria num board") e o PDF original em anexo.

**Formação — Módulos 2 a 8.** Ver §7.

**Clientes.** Ficha viva de conta (padrão de compra, decisores públicos, o que já foi entregue, iniciativas candidatas). Existe hoje só como dossiê no projeto; precisa nascer como notas no vault e passar por revisão de confidencialidade antes de aparecer.

**Pergunte ao acervo.** Chat com recuperação (RAG) sobre as notas, sempre respondendo com as fontes e o selo de proveniência. Entra depois da busca, não antes: sem busca boa, o chat esconde as lacunas.

**Glossário.** Termo, definição em 2 linhas, termo original em inglês, onde aparece no acervo. Não existe hoje; deve ser gerado a partir dos módulos da trilha.

### 4.3 Não-objetivos (v1)

Não é ferramenta de CRM nem de pipeline comercial. Não hospeda dado de cliente (contratos, volumes, nomes de pessoas do cliente). Não é rede social interna: comentários existem só como "sugerir correção" que vai para a fila de curadoria. Não substitui o Obsidian como local de escrita. Não tem versão pública na v1 — a linha editorial externa (marca CAIO) permanece separada.

## 5. Requisitos funcionais

| ID | Requisito | Prioridade |
|---|---|---|
| RF-01 | Login por SSO corporativo (Entra ID/SAML); nenhuma página pública | MVP |
| RF-02 | Ingestão do vault: parser de frontmatter YAML, wikilinks e tabelas; sincronização diária (após o digest das 6h) e sob demanda | MVP |
| RF-03 | Cada nota vira página com tipo, eixos, data, status, maturidade, links de entrada e saída | MVP |
| RF-04 | Selo de proveniência por afirmação numérica, herdado da nota de auditoria; filtro "só com fonte primária" | MVP |
| RF-05 | Busca full-text com filtros; resultado mostra tipo e trecho | MVP |
| RF-06 | Matriz Produtos × Players e tabela De-Para de jornadas com filtros e exportação PNG/CSV | MVP |
| RF-07 | News: lista por data, leitura de edição, busca no arquivo, link para assinatura por e-mail | MVP |
| RF-08 | Trilha: módulos → lições (vídeo, leitura, exercício, quiz); progresso por pessoa; certificado interno ao concluir módulos 1–4 | MVP (mód. 1) |
| RF-09 | "Sugerir correção" em qualquer página, com campo de fonte; vai para fila de curadoria | MVP |
| RF-10 | Painel de curadoria: notas sem fonte, sem tese, sem atualização há 90 dias, sugestões pendentes | Fase 2 |
| RF-11 | Radar regulatório com linha do tempo de prazos e alerta por e-mail 30 dias antes | Fase 2 |
| RF-12 | "O que mudou" por módulo da trilha, cruzando eixos/players da lição com o digest | Fase 2 |
| RF-13 | Chat "pergunte ao acervo" com citação obrigatória | Fase 2 |
| RF-14 | Analytics de uso por módulo e por página (sem rastrear indivíduo além do progresso de trilha) | Fase 2 |

## 6. Requisitos não funcionais e restrições

**Confidencialidade.** Conteúdo interno da empresa. Hospedagem em ambiente aprovado pela TI (a decidir: Azure corporativo ou cloud pessoal com SSO). Nada de dado pessoal de cliente. As páginas de concorrentes de consultoria são internas por natureza.

**Conflito de interesse declarado.** O acervo cita Veltrix e Cohort como laboratório. No portal da empresa, essas menções passam por regra editorial explícita (manter como referência de arquitetura, sem posicionamento comercial) e o conflito fica declarado por escrito antes do lançamento — é pendência já registrada no plano do escritório.

**Fonte de verdade.** O vault vive no iCloud, e nesta máquina 441 de 462 notas e todos os PDFs estão como placeholder (não baixados). O pipeline precisa de uma cópia sempre baixada — o caminho mais simples é um repositório git do vault (sem os PDFs) sincronizado por commit, e o portal lendo do git, não do iCloud.

**Desempenho.** Página de nota em < 1 s; busca em < 500 ms para o acervo atual (~500 notas, crescendo ~5/dia).

**Acessibilidade.** WCAG 2.1 AA; vídeos com legenda (a narração gerada já entrega o texto).

## 7. Trilha de formação — currículo v0.1

Público: pessoa de tecnologia sem base bancária. Formato de cada lição: vídeo de 4–6 min (roteiro próprio, narração e imagem gerados por IA, legenda automática), uma leitura curada de fonte oficial, um exercício aplicado ao acervo e um quiz de 8 questões. Cada módulo fecha com um "desafio de campo": uma conversa com alguém da conta usando o que aprendeu. Certificado interno "Banking Foundations" ao concluir os módulos 1–4; "Banking + IA" ao concluir os 8.

| # | Módulo | Lições (5 cada) | Leitura curada de fonte oficial | Exercício com o acervo |
|---|---|---|---|---|
| 1 | **SFN e papéis das instituições** | CMN/BCB/CVM/Susep; bancos, IPs, cooperativas; o que é ser "regulado"; como o dinheiro se move (SPB); história curta do BC | Composição do SFN (BCB); Coursera FIA "Estrutura e Funcionamento do Mercado" mód. 1–2; playlist "BC te Explica" | Classificar os 11 players do acervo por tipo de licença |
| 2 | **Produtos bancários de varejo** | Conta PF/PJ; cartão; crédito (consignado, CDC, rotativo); investimentos e suitability; seguros | Programa detalhado da antiga CPA-10 (ainda público); Cadernos CVM; Meu Bolso em Dia | Ler 3 notas de produto e apontar onde o comparativo diverge |
| 3 | **Meios de pagamento e cartões** | Portador, emissor, bandeira, credenciadora, sub; MDR e intercâmbio; chargeback; antecipação de recebíveis; registradoras | Guia Prático Abecs (28 p.); Pesquisa Febraban 2026 | Mapear a cadeia de uma compra no cartão com os players do acervo |
| 4 | **Pix e Open Finance** | Arquitetura do Pix (SPI, DICT, participantes); Pix Automático e por aproximação (Res. BCB 406/24); MED; Open Finance (fases, consentimento, TPP/PISP); Drex como caso histórico | Relatório de Gestão do Pix; Onboarding Open Finance Brasil; Referências básicas do Drex | Percorrer a jornada "Pagamentos & Pix" no comparativo e explicar os níveis EMA-J |
| 5 | **Crédito, risco e fraude** | Ciclo de crédito; scoring e bureaus; provisão e Basileia em 1 slide; PLD/FT e KYC; engenharia social e fraude autorizada | Programa detalhado da antiga CPA-20 (risco); FAQ Pix/MED do BCB | Ler a iniciativa de originação agêntica e listar os controles regulatórios que ela cita |
| 6 | **Regulação, supervisão e cibersegurança** | Como nasce uma norma (consulta pública → resolução → IN); Res. CMN 4.893 e 5.274/25; Res. BCB 538/25; sandbox regulatório; o que o supervisor pede numa inspeção | Normativos BCB; artigo Febraban Tech "Novas regras para a segurança digital em 2026" | Preencher uma entrada do registro regulatório com fonte oficial |
| 7 | **Dados, LGPD e IA no setor** | LGPD art. 20 e decisão automatizada; ANPD (NT 12/2025, Radar Tecnológico); residência de dados e transferência internacional; explicabilidade; EU AI Act no contexto financeiro (Anexo III em 02/12/2027) | Documentos técnicos ANPD; nota do acervo "Residência de Dados e Explicabilidade nos 11 Players" | Auditar 5 afirmações do acervo contra fonte primária (é o exercício mais formador que existe) |
| 8 | **IA aplicada: os frameworks da prática** | EMA-J, VALE, VCAT, Mandato do Agente, SJC (roteamento por jurisdição); como ler uma ficha de iniciativa; como levar isso a um board | Os 19 frameworks; 3 reports destilados | Pontuar uma iniciativa nova com o placar VALE e defender em 3 minutos |

Fontes públicas que embasam a curadoria: hub Cidadania Financeira do BCB, curso "Gestão de Finanças Pessoais" (BCB/Enap, 20 h, gratuito), playlist "BC te Explica" (188 vídeos), Museu de Valores (tour virtual), portal e área do desenvolvedor do Open Finance Brasil, Portal do Investidor e AVA da CVM, plataforma Meu Bolso em Dia (Febraban), Guia Prático da Abecs, Pesquisa Febraban de Tecnologia Bancária 2026, ANBIMA Edu. Aviso registrado: as certificações CPA-10/20/CEA foram substituídas em jan/2026 por CPA, C-Pro R e C-Pro I; os programas antigos seguem públicos e servem como ementa. Links completos no anexo A.

## 8. Arquitetura

```
Fontes (newsletters, web, reports) ──► rotinas Cowork ──► Vault Obsidian (iCloud)
                                                              │  commit automático
                                                              ▼
                                                     Repositório git do vault
                                                              │  webhook / cron 6h30
                                                              ▼
                                   Pipeline de ingestão (parser MD + YAML + wikilinks)
                                                              │
                     ┌────────────────────────────────────────┼─────────────────────┐
                     ▼                                        ▼                     ▼
             Postgres (notas, tipos,               Índice de busca            Storage de mídia
             links, proveniência,                  (pg full-text +            (vídeos, PDFs,
             progresso de trilha)                  pgvector p/ RAG)           artes)
                     └────────────────────────────────────────┬─────────────────────┘
                                                              ▼
                                        App web (Next.js, SSR) atrás de SSO
                                    Home · Acervo · Comparativos · News · Formação · Busca
```

Stack proposta: Next.js + TypeScript, Postgres (com pgvector), autenticação via NextAuth/Entra ID, storage de objetos para vídeo, deploy em container. Modelo de dados central: `nota` (id, tipo, título, slug, data, status, maturidade, eixos[], players[], corpo HTML, corpo texto) · `link` (origem, destino) · `afirmacao` (nota, texto, valor, selo_proveniencia, fonte_url, verificada_em) · `modulo` / `licao` / `quiz` / `progresso` · `sugestao_correcao`. O `tipo` do frontmatter (daily, ideia, atencao, post, source, framework, iniciativa, instituicao, produto, jornada) mapeia direto para as seções do portal — o vault já foi desenhado com templates por tipo, o que reduz o trabalho de modelagem quase a zero.

## 9. O que falta no acervo (complementos)

| Lacuna | Situação hoje | O que criar | Esforço |
|---|---|---|---|
| Fichas de instituição rasas | ~860 bytes cada | Template ampliado: licença, porte, estratégia de IA declarada, padrão de compra, decisores públicos, fontes | 2 semanas, rotina noturna reaproveitada |
| Registro regulatório estruturado | Espalhado em notas de refresh | `08-Regulatorio/` com uma nota por norma e o radar de prazos | 1 semana + curadoria contínua |
| Grandes projetos do setor | Inexistente | `09-Projetos-Setor/` (Pix, Open Finance, Drex, Open Insurance, tokenização) | 1 semana |
| Glossário | Inexistente | Gerado dos módulos; ~150 termos | Sai junto com cada módulo |
| Fichas de cliente | Só no projeto (dossiê) | Migrar para o vault com revisão de confidencialidade | 1 semana + aval |
| Trilha de formação | Inexistente | 8 módulos × 5 lições (40 vídeos, 40 quizzes) | Módulo 1 em 2 semanas; 1 módulo/2 semanas depois |
| Correções da auditoria de proveniência | 45 correções aguardando aval | Aplicar antes de expor o acervo | 1 sessão de decisão do Bruno |
| Vault não baixado / sem git | 441 placeholders | Repositório git + "manter baixado" | 1 dia |
| 3 reports sem nota (New-reports) | Sem destilação | Rodar a ingestão de reports | Automático |

## 10. Métricas de sucesso

Adoção: ≥ 60% da prática com login no primeiro mês; ≥ 30% de usuários semanais no terceiro. Formação: ≥ 80% das pessoas novas concluem o módulo 1 em 2 semanas; nota média de quiz ≥ 80%. Valor comercial: ≥ 3 propostas por mês citando página do portal; tempo para achar um comparativo ≤ 3 min em teste com 5 pessoas. Confiabilidade: 100% dos números na Home com selo; fila de correções zerada semanalmente. Antecipação: alertas regulatórios enviados ≥ 30 dias antes de todo prazo do radar.

## 11. Riscos e decisões em aberto

1. **Hospedagem e SSO** — depende da TI da empresa. Sem decisão, o MVP roda em cloud pessoal com convite por e-mail e migra depois. *Decisão do Bruno até 11/09.*
2. **Conflito Veltrix/Cohort** — declarar antes do lançamento. *Decisão do Bruno.*
3. **Nome** — "One Banking Hub" herda a marca do digest já conhecida no time. Alternativas: "Banking Brain", "Casa Banking". *Decisão do Bruno.*
4. **Vídeos gerados por IA** — validar com a área de comunicação/compliance se voz sintética é aceita em material interno. Alternativa: narração própria a partir do mesmo roteiro.
5. **Dependência de uma pessoa** — o acervo tem um curador. O portal precisa de um segundo curador até o fim do trimestre, ou vira o key-person risk que o próprio acervo critica.
6. **Correções pendentes** — expor o acervo antes de aplicar as 45 correções contradiz o princípio 1.

## Anexo A — Fontes públicas verificadas (04/09/2026)

BCB: curso Gestão de Finanças Pessoais (Enap) https://www.escolavirtual.gov.br/curso/170 · Cidadania Financeira https://www.bcb.gov.br/cidadaniafinanceira · Composição do SFN https://www.bcb.gov.br/estabilidadefinanceira/sfn · Pix https://www.bcb.gov.br/estabilidadefinanceira/pix · Relatório de Gestão do Pix https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2023.pdf · Drex referências básicas https://www.bcb.gov.br/content/estabilidadefinanceira/real_digital_docs/drex_referencias_basicas_nov2023.pdf · Museu de Valores https://www.bcb.gov.br/acessoinformacao/museu/tourvirtual/ · Playlist BC te Explica https://www.youtube.com/playlist?list=PLhqfgkxuHXh5tlmhzGpwjnucUPn06XLtk · Dados Abertos https://dadosabertos.bcb.gov.br/organization/sistema-financeiro-nacional
Febraban: Pesquisa de Tecnologia Bancária 2026 https://cmsarquivos.febraban.org.br/Arquivos/documentos/PDF/Pesquisa%20Febraban%202026.pdf · Meu Bolso em Dia https://meubolsoemdia.com.br/ · Infi https://febrabaneducacao.com.br/
Open Finance Brasil: onboarding https://openfinancebrasil.org.br/onboarding/ · área do desenvolvedor https://openfinancebrasil.atlassian.net/wiki/spaces/OF
ANBIMA: transição das certificações https://www.anbima.com.br/pt_br/noticias/anbima-apresenta-regras-de-transicao-das-atuais-para-as-novas-certificacoes-profissionais-de-distribuicao.htm · ANBIMA Edu https://anbimaedu.com.br/certificacoes
CVM: hub de educação https://www.gov.br/cvm/pt-br/assuntos/educacao · Portal do Investidor https://www.investidor.gov.br/
Abecs: Guia Prático de Meios de Pagamento https://api.abecs.org.br/wp-content/uploads/2019/11/Cartilha-da-Abecs-sobre-o-Mercado-de-Meios-de-Pagamento.pdf
Coursera FIA: https://www.coursera.org/learn/estrutura-e-funcionamento-do-mercado
ANPD: documentos técnicos https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos
Regulação (cópias/análises; confirmar texto oficial em normativos.bcb.gov.br antes de citar): Res. CMN 5.274/2025 e Res. BCB 538/2025 (adequação 01/03/2026) · Res. BCB 406/2024 (iniciação sem redirecionamento) · Res. CMN 4.893/2021 · LGPD https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

Pontos ainda não verificados nesta rodada: páginas do bcb.gov.br listadas acima foram obtidas por busca, não abertas (o domínio bloqueou o acesso automatizado); catálogo atual do Infi; nota oficial do BCB sobre a reorientação do Drex (nov/2025); carga horária dos cursos gratuitos da FGV.
