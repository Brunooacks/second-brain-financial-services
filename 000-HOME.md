---
tipo: home
tags: [home, moc]
---

# 🧠 AI-Brain — Segundo Cérebro CAIO

> **Princípio que rege tudo: automatizar a coleta, nunca o pensamento.** A máquina junta, organiza e traduz. A tese é minha.

## Mapa
| Pasta | O que vive aqui |
|---|---|
| `00-Inbox/` | capturas soltas, pra triar |
| `01-Daily/` | digest automático + minhas peripécias do dia |
| `02-Sources/` | 1 nota por fonte que vale guardar |
| `02-Sources/Reports/` | notas destiladas dos PDFs/relatórios |
| `03-Ideas/` | ideias atômicas, cada uma com uma TESE |
| `04-Atencao/` | watch-list, perguntas em aberto, sinais a monitorar |
| `05-Frameworks/` | meus frameworks próprios (material citável) |
| `06-Posts/` | consolidação semanal → rascunho → publicado |
| `07-Setores/` | MOCs: [[MOC-Financeiro]], Saúde, Jurídico... |
| `99-Templates/` | templates do Templater |

**Índice mestre:** [[Fontes-Perfis-CAIO]]

## ⚙️ Setup (uma vez)
1. Instalar plugins da comunidade: **Templater** e **Dataview**.
2. Templater → *Template folder location* = `99-Templates`.
3. (Opcional) Templater → *Trigger on new file creation* e atalhos por template.
4. Dataview → ativar *Enable JavaScript Queries* não é necessário (uso só DQL).
5. Reports locais: manter "sempre baixar nesta máquina" em
   `~/Library/Mobile Documents/com~apple~CloudDocs/Head-Ai-Banking - reports/`.

## 🔁 O loop
- **Diário (~60–90 min):** Coletar (auto, Cowork) → Pensar (15 min, só eu) → Publicar.
- **Semanal (sexta):** Weekly Review → escolher as teses → rascunhos automáticos → editar → publicar.
- **A sexta tem que acontecer.** A automação mata o atrito, não a disciplina.

### 📆 Esteira semanal de publicação
A Weekly de sexta rende **3 peças de LinkedIn + 2 artigos de Medium** — três teses distintas, nunca três versões do mesmo texto.

| Dia | Peça | Tese | Rotina |
|---|---|---|---|
| terça | LinkedIn **técnico** (500–700 pal.) | candidata nº 2 | `post-tecnico-semanal` |
| quarta | Medium técnico (1.400–2.000) | expansão | (mesma rotina) |
| quinta | LinkedIn **executivo** (400–600) | candidata nº 3 | `post-executivo-semanal` |
| sexta | Medium executivo (1.200–1.600) | expansão | (mesma rotina) |
| sábado | LinkedIn **long-form** (900–1.300) | candidata nº 1 | `post-semanal-linkedin` |

**Técnico** responde *como funciona e onde quebra* — se não nomeia **onde medir**, é opinião.
**Executivo** responde *quanto custa e quem responde* — se não nomeia **quem responde**, é notícia.
**Não-canibalização:** teses não se repetem entre as peças da semana. Semana fraca → "sem tese nova", não recorte.

Regras completas em [[_CAIO-Brain]] (seções 11–14). Arte em [[Identidade-Visual-Editorial]].
Templates: [[TPL-Post-Tecnico]] · [[TPL-Post-Executivo]] · [[TPL-Medium]]

---

## 📋 Prompts do Cowork (colar no Cowork)

### Digest diário
> Todo dia útil às 6h, gere meu briefing de IA com foco no setor financeiro. Leia as newsletters recebidas no Gmail nas últimas 24h com a query `from:(swyx+ainews@substack.com OR swyx@substack.com OR bigtechnology@substack.com OR pkriaris@substack.com OR samboboev@substack.com OR theneuron@newsletter.theneurondaily.com OR emergingai@substack.com) newer_than:1d` e busque na web os principais debates do dia no Reddit (r/MachineLearning, r/LocalLLaMA), Medium e X sobre IA aplicada a finanças. Para cada item relevante: (1) o que mudou, (2) por que importa, (3) o que eu diria sobre isso num board. Destaque no topo os 3 "pontos de atenção" da semana. Cruze com a biblioteca de reports quando houver conexão. Escreva em PT (síntese, nunca tradução integral) e salve como nota em `~/AI-Brain/01-Daily/` no formato AAAA-MM-DD.md.

### Ingestão de reports
> Leia todos os PDFs novos em `~/Library/Mobile Documents/com~apple~CloudDocs/Head-Ai-Banking - reports/`. Para cada um, gere uma nota em português em `~/AI-Brain/02-Sources/Reports/` com: fonte/autor/data, tese central, 3–5 achados-chave com números e número da página, conexão com IA em finanças/governança/soberania, e "o que eu diria sobre isso". Não copie trechos longos — sintetize. Ignore PDFs que já tenham nota correspondente.

---

## 🎯 Métricas de sucesso (não "quanto li")
Inbound qualificado · convites pra falar/participar · negócios gerados · densidade do acervo de notas com tese.
