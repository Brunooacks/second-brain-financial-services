# 🧠 AI-Brain — Second Brain · IA no Setor Financeiro

> **Princípio que rege tudo: automatizar a coleta, nunca o pensamento.**
> A máquina junta, organiza e traduz o material bruto todo dia. A tese é minha.

Segundo cérebro de um diretor em trajetória de **Chief AI Officer (CAIO)**, focado em IA aplicada ao setor financeiro brasileiro — risco, fraude, crédito, pagamentos agênticos, regulação (Bacen, LGPD, EU AI Act, PL 2338), FinOps de inferência e **soberania de dados**. É um vault do [Obsidian](https://obsidian.md) alimentado por automações do Claude Cowork e mantido por um loop diário de coleta → tese → publicação.

Snapshot deste repositório: **setembro/2026** · ~490 notas Markdown · 63 edições do briefing *One Banking AI* · 17 frameworks próprios · 11 instituições financeiras mapeadas produto a produto.

---

## 🗺️ Mapa do vault

| | Pasta | O que vive aqui | Volume |
|---|---|---|---|
| 🏠 | `000-HOME.md` | Página inicial: mapa, setup, o loop e os prompts das automações | 1 nota |
| 📅 | `01-Daily/` | Digest diário gerado às 6h (newsletters + web, filtrados pela lente financeira) e as edições do briefing **One Banking AI** em HTML/PDF | 72 digests · 63 edições |
| 📚 | `02-Sources/Reports/` | Uma nota destilada por relatório de mercado (McKinsey, PwC, EY, Stanford AI Index, NTT DATA, MIT…): tese central, achados com número e página, conexão com finanças/governança e "o que eu diria sobre isso" | 22 notas |
| 💡 | `03-Ideas/` | Ideias atômicas — **cada nota é uma tese**, não um resumo. Matéria-prima dos posts | 54 notas |
| 👁️ | `04-Atencao/` | Watch-list: sinais regulatórios, movimentos de mercado e riscos a monitorar, cada um com o gatilho que o torna acionável | 51 notas |
| 🧩 | `05-Frameworks/` | Frameworks próprios, nomeados e citáveis — o material que torna alguém referência | 17 frameworks |
| ✍️ | `06-Posts/` | Esteira de publicação: Weekly Review → rascunhos → posts publicados (LinkedIn técnico, executivo, long-form e artigos de Medium) + ganchos e artes | 12 weeklies · 17 posts · 6 Medium |
| 🏦 | `07-Setores/` | MOCs por setor. O de **Financeiro** é um acervo completo: instituições, produtos, comparativos, jornadas de-para e iniciativas de IA | ~190 notas |
| 🖥️ | `08-Portal/` | PRD e plano de 90 dias do portal de conhecimento de Banking | 2 notas |
| 🧬 | `99-Templates/` | Templates do Templater (daily, ideia, framework, atenção, ficha de instituição, produto, jornada, iniciativa, posts, Medium, weekly, report) + render do One Banking AI | 14 templates |
| 🛠️ | `_cowork-skills/` | Cópia das skills customizadas do Claude Cowork que operam o sistema | 4 skills |
| 🔁 | `RESTAURAR.md` | Guia de restauração em máquina nova | — |

---

## 🏦 O acervo do setor financeiro (`07-Setores/Financeiro/`)

O núcleo do vault. Construído com método de discovery de consultoria e auditado por proveniência (cada ganho citado tem fonte rastreável).

```
07-Setores/Financeiro/
├── 00-Blueprint-Mapeamento-Produtos-Banking-BR.md   ← método e escopo do mapeamento
├── 00b-Plano-Discovery-Jornadas-para-Iniciativas.md
├── 01-BIAN-Espinha-Dorsal.md                        ← taxonomia BIAN como espinha do acervo
├── 01-Instituicoes/        🏛️ 11 players em 4 grupos
│   ├── Bancoes/            Itaú · Bradesco · Santander · Banco do Brasil · Caixa
│   ├── Fintechs-e-Neobancos/  Nubank · Inter · C6 Bank · PicPay
│   ├── Adquirentes-e-Pagamentos/  Stone · PagBank · Mercado Pago
│   └── Concorrentes-Consultoria/  McKinsey · BCG · Accenture · Deloitte · EY · KPMG · PwC · IBM · CI&T · Dimensa
├── 02-Produtos/            💳 8 famílias × 11 players (~90 fichas)
│   Conta-PF · Conta-PJ · Cartão · Crédito · Investimentos · Seguros · Pagamentos-Pix · Adquirência
├── 03-Comparativos/        ⚖️ comparativos por produto + jornadas de-para
│   ├── Produtos/           8 comparativos transversais
│   └── Jornadas/           Onboarding & KYC · Originação de crédito · Pagamentos & Pix ·
│                           Investimentos & advisor · Prevenção a fraude · Atendimento & cobrança
├── 06-Iniciativas/         🚀 ~40 iniciativas de IA governada (Fase 1 + Fase 2), com backlog priorizado
└── 2026-08-31 … 09-03      📋 refreshes trimestrais e auditorias de proveniência do acervo
```

Os outros MOCs (Saúde, Jurídico, Varejo, Indústria, Govtech, Fronteira) estão abertos para a Fase 2 do plano (multissetor).

---

## 🧩 Frameworks próprios (`05-Frameworks/`)

Cada framework tem sigla, eixos e um caso de uso no setor financeiro. São o material citável em board e em posts.

| Sigla | Framework | Pergunta que responde |
|---|---|---|
| **SJC** | Matriz de Roteamento de Inferência — Sensibilidade, Jurisdição, Custo | Para onde cada chamada de LLM pode ir? |
| **VCAT** | Demonstração de Resultado de IA — Valor, Custo, Atribuição, Trilha | Como provar ROI de IA sem hype? |
| **FMC** | Placar do Parque de Agentes — Frota, Mandato, Custo | Quantos agentes têm mandato e quem orquestra? |
| **VCAP** | Matriz de Execução do Agente — Valor, Canal, Autenticação, Prova | Quando o agente pode mover dinheiro? |
| **ASE** | Matriz de Interrupção do Agente — Acionador, SLA, Estado | Quando o humano entra no loop, e a que custo? |
| **MPT** | Mapa de Passivo por Trilho | De quem é o passivo quando o valor vira token? |
| **SRC** | Roteamento de Trilho do Agente de Pagamento | Pix, cartão ou stablecoin — quem decide? |
| **PCT** | Matriz de Proveniência do Dado — Próprio, Compartilhado, Terceiro | Que dado pode treinar/alimentar o quê? |
| **RSJA** | Censo do Corpus Exposto — Repositório, Sensibilidade, Jurisdição, Autorização | O que o agente lê e com que autorização? |
| **DCS** | Construir-Comprar-Parcear do Ativo de IA — Dado, Custo, Soberania | Onde vale construir e onde comprar? |
| **DIM** | Grade de Governança de Conector em Assistente de Terceiro — Dado, Inferência, Mandato | O que um assistente de big tech pode fazer com a conta? |
| **ESR** | Exposição à Portabilidade Agêntica — Exposição, Sobrevivência, Retenção | Que produto o agente do cliente porta primeiro? |
| **SIR** | Mapa de Captura da Advice Layer — Segmento, Interface, Receita | Quem fica com a camada de aconselhamento? |
| **AxE** | Matriz Adoção × Eficiência de IA | Adoção alta com custo por tarefa alto é sucesso? |
| **BIH** | Régua de Produtividade Agêntica — Baseline, Inferência, Human-in-the-loop | O ganho de produtividade sobrevive ao custo? |
| **MRR** | Matriz de Rastreabilidade da Recomendação | O que o advisor de IA recomendou e por quê? |
| **EMA-J** | Escala de Maturidade Agêntica de Jornada | Em que degrau de autonomia está cada jornada? |
| **VALE** | Placar de Priorização de Iniciativa de IA | Qual iniciativa entra primeiro no roadmap? |
| — | Mandato do Agente — escopo, limite, jurisdição, trilha | O contrato mínimo antes de um agente ir a produção |

---

## 🔁 O loop que mantém o vault vivo

```
 06:00  📥 COLETAR (100% automático — Cowork)
        Gmail (newsletters Tier A) + Reddit/Medium/X → filtro pela lente financeira
        → síntese em PT-BR → "o que eu diria num board" → nota em 01-Daily/
        → briefing One Banking AI (HTML + PDF) para a prática de Banking

 manhã  🧠 PENSAR (100% humano, ~15 min)
        Ler o digest no Obsidian → jogar teses em 03-Ideas/ e sinais em 04-Atencao/
        A única etapa que exige o autor — e é de propósito: aqui nasce a autoridade.

 sexta  ✍️ PUBLICAR (semi-automático)
        Dataview varre a semana → Weekly Review em 06-Posts/ → 3 teses distintas
        → terça: LinkedIn técnico · quinta: LinkedIn executivo · sábado: long-form
        → quarta/sexta: expansão em Medium · arte no sistema visual "Registro Húmido"
```

**Regras editoriais que valem para tudo:** tese, não resumo · síntese de 3–5 linhas, nunca tradução integral · termo técnico original entre parênteses quando não há equivalente em PT · toda peça fecha com "o que eu faria/recomendaria" · tom consultivo — descrever o estado do mercado, não julgar instituições nomeadas.

---

## 🛠️ Skills do Cowork (`_cowork-skills/`)

As automações que operam o sistema. Ficam sincronizadas na conta Claude; esta cópia é garantia de restauração.

| Skill | O que faz |
|---|---|
| 🧭 **caio-editorial-brain** | Aplica a lente editorial a qualquer síntese, nota, gancho ou rascunho: tese própria, foco financeiro + governança/soberania, dado com fonte, fechamento de board |
| 🎨 **arte-post** | Gera a arte 4:5 dos posts e capas de Medium no sistema visual *Registro Húmido* (nanquim e aguada sobre papel envelhecido, um acento cromático) |
| 📊 **board-materials** | Materiais executivos ilustrados — PDFs para board, dossiês, estudos — a partir de um briefing de formato, paleta e densidade |
| 🔍 **consulting-research** | Discovery e pesquisa de mercado com método de consultoria: hypothesis-driven, MECE, fato triangulado, síntese em pirâmide |

---

## ⚙️ Stack

| Camada | Ferramenta |
|---|---|
| Notas e grafo | Obsidian · plugins **Dataview** (consultas e Weekly Review) e **Templater** (notas padronizadas em `99-Templates/`) |
| Coleta e síntese | Claude Cowork (tarefas agendadas) + skills acima |
| Fontes | Newsletters Tier A (AINews, Latent Space, Big Technology, Kriaris, Boboev, The Neuron), Emerj, The Financial Brand, American Banker, Import AI, Interconnects, One Useful Thing, Exponential View, Stratechery |
| Biblioteca de reports | PDFs em iCloud (`Head-Ai-Banking/Reports/`) — **fora deste repo por tamanho**; notas destiladas em `02-Sources/Reports/` |
| Versionamento | Este repositório (push diário) + snapshot em SSD externo |

---

## 🚀 Uso rápido

```bash
# clonar (de preferência fora do iCloud, para evitar conflito iCloud × git)
git clone https://github.com/Brunooacks/second-brain-financial-services.git ~/AI-Brain

# abrir no Obsidian: "Open folder as vault" → ~/AI-Brain
# Settings → Community plugins → desligar Restricted mode (Dataview e Templater já vêm no repo)

# rotina diária
cd ~/AI-Brain && git add -A && git commit -m "daily $(date +%F)" && git push
```

Restauração completa em máquina nova, incluindo reports e tarefas agendadas: ver [`RESTAURAR.md`](RESTAURAR.md).

---

## 📏 Métricas de sucesso

Não é "quanto li". É **inbound qualificado · convites para falar/participar · negócios gerados · densidade do acervo de notas com tese**.

---

<sub>Repositório privado. Conteúdo em PT-BR. Mantido por Bruno Oliveira · 2026.</sub>
