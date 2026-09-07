---
tipo: blueprint
setor: financeiro
fase: 1
status: ativo
data: 2026-06-29
eixos: [financeiro, governanca, soberania, agentes]
tags: [blueprint, produtos, mapeamento, banking, fintech, especificacao-funcional, vivo]
---

# 🗺️ Blueprint — Mapeamento de Produtos do Setor Financeiro BR

> Especificação funcional **viva** do setor: uma base de conhecimento de todos os produtos de bancos e fintechs brasileiros — telas, conteúdo, processos e jornadas documentados — para gerar conhecimento de produto/negócio dos clientes e comparar ofertas (prós, contras, diferenciais). **Automatizar a coleta, nunca o pensamento:** a máquina raspa e organiza; a tese de cada ficha é minha.

---

## 0. Por que isto existe (a tese antes do método)

Vendo consultoria de IA para banking. Para falar de board a board com um cliente, preciso saber o produto dele melhor do que o gerente de produto dele — e saber onde o concorrente o supera. Esta base é o **acervo defensável** que transforma "conheço IA" em "conheço o seu negócio e o seu mercado". Conecta direto ao catálogo de ofertas consultivas: cada lacuna de produto/jornada que eu mapear vira gancho de uma oferta (governança, FinOps, antifraude, crédito auditável).

**O que eu diria num board:** quem mapeia o setor inteiro de forma estruturada deixa de vender "capacidade técnica" e passa a vender "leitura de mercado". O ativo não é a tela raspada — é a **comparação com tese**: o slide que diz "o seu onboarding PJ tem 7 passos; o do concorrente tem 3, e é por isso que você perde ativação". Esse é o artefato que ninguém entrega.

---

## 1. Princípios

1. **Conteúdo público apenas.** Nada de login, dado pessoal, ou contornar autenticação. Telas logadas só por captura manual sua, com nota de governança (ver §8).
2. **Dado é rei.** Toda tarifa/número entra com **fonte + data de captura**. Preço de banco muda; sem data, vira boato.
3. **Tese, não dump.** Cada ficha fecha com "o que eu diria num board". Comparação sem opinião é planilha; comparação com tese é referência.
4. **Governança que eu mesmo vendo.** Pratico residência de dados, trilha de coleta e respeito a ToS/LGPD — é incoerente vender governança e raspar errado.
5. **Incremental e vivo.** A base nunca está "pronta"; ela tem changelog e cadência. Releitura semanal mata a desatualização.

---

## 2. Taxonomia — os 4 eixos de classificação

Toda peça de conhecimento é endereçada por **Instituição × Segmento × Processo × Jornada**.

### Eixo 1 — Instituição (o player)
Classes: `bancão` · `banco médio` · `fintech/neobanco` · `adquirente/sub-adquirente` · `cooperativa` · `BaaS/infra` · `gestora/corretora`.
Atributos: porte (ativos/faturamento), público (varejo PF / PME / corporate / private), modelo de negócio, licença (banco múltiplo, SCD, IP, etc.), maturidade digital.

### Eixo 2 — Segmento de produto (o quê)
Catálogo canônico de segmentos a cobrir:

- **Contas** — PF, PJ/MEI, conta global/internacional, conta-salário, menores/teen.
- **Cartões** — crédito, débito, pré-pago, múltiplo, benefícios (VR/VA), corporativo.
- **Crédito** — pessoal, consignado, CDC, capital de giro, antecipação de recebíveis, imobiliário, veículos, BNPL/parcelado.
- **Pagamentos & recebimentos** — Pix, maquininha/adquirência, boletos, link de pagamento, TEF, Pix Automático/garantido.
- **Investimentos** — renda fixa, fundos, corretagem (RV), tesouro, previdência, caixinhas/cofrinhos.
- **Seguros & assistências** — vida, residencial, cartão protegido, prestamista.
- **Câmbio & global** — conta internacional, remessas, cartão multimoeda.
- **Crypto / ativos digitais** — compra/venda, custódia, stablecoins.
- **Open Finance / BaaS / APIs** — compartilhamento, iniciação de pagamento, banking-as-a-service.
- **Fidelidade & benefícios** — pontos, cashback, shopping/marketplace.
- **Soluções AI-native** — copiloto financeiro, advisor, antifraude, atendimento por agente. ← *eixo da minha tese; sempre destacar*

### Eixo 3 — Processo (o como, por dentro)
`onboarding/KYC` · `autenticação & login` · `originação de crédito` · `transação/pagamento` · `cobrança` · `atendimento/suporte` · `prevenção a fraude` · `encerramento/portabilidade`. Cada processo é onde mora a **dor vendável** (ex.: KYC lento = oferta de IA de onboarding).

### Eixo 4 — Jornada (o como, pela ótica do cliente)
`descoberta → aquisição → ativação → uso recorrente → expansão/cross-sell → retenção → churn`. Cada etapa recebe **telas de evidência** (screenshots públicos) e métrica de atrito (nº de passos, campos, tempo). É aqui que a comparação fica visual e citável.

---

## 3. Arquitetura de pastas (Obsidian)

```
07-Setores/Financeiro/
├── 00-Blueprint-Mapeamento-Produtos-Banking-BR.md   (este doc)
├── 01-Instituicoes/        1 ficha por player (perfil, licença, porte, estratégia)
├── 02-Produtos/            1 ficha funcional por produto  ← coração da base
│   └── <Instituição> — <Produto>.md
├── 03-Comparativos/        1 nota por segmento (matriz prós/contras/diferenciais)
│   └── Comparativo — Conta PJ.md
├── 04-Jornadas/            jornadas documentadas com telas (por processo)
├── 05-Telas/               evidência visual (screenshots públicos, datados)
└── _Indice-Produtos.md     MOC com Dataview (catálogo navegável)
```

Telas ficam em `05-Telas/<instituicao>/<produto>/AAAA-MM-DD-<etapa>.png` e são linkadas na ficha — nunca coladas soltas.

---

## 4. Esquema de dados — a ficha funcional de produto

Frontmatter padronizado (alimenta o Dataview da comparação):

```yaml
tipo: produto
instituicao: <nome>
classe_inst: <bancão|banco-médio|fintech|adquirente|cooperativa|baas>
segmento: <conta|cartão|crédito|pagamentos|investimento|seguro|câmbio|crypto|open-finance|ai-native>
produto: <nome comercial>
publico: [PF|PJ|MEI|PME|corporate|private]
status: <ativo|descontinuado|beta>
data_captura: AAAA-MM-DD
fontes: [url1, url2]
maturidade: 1-5
eixos: [financeiro, ...]
tags: [produto, <segmento>, <instituicao>]
```

Seções obrigatórias da ficha (ver template `TPL-Produto-Financeiro`):
1. **Identificação & posicionamento** (uma frase: "o que é e pra quem").
2. **Proposta de valor** (a promessa central).
3. **Funcionalidades** (lista do que faz).
4. **Tarifas & preços** — *cada linha com fonte + data*.
5. **Requisitos & elegibilidade**.
6. **Processo & jornada** (passo a passo por etapa; nº de passos/atrito).
7. **Telas** (links datados em `05-Telas/`).
8. **Tecnologia & IA embarcada** (o ângulo da minha tese).
9. **Governança / regulação / dados** (LGPD, Bacen, residência, autenticação).
10. **Prós / Contras**.
11. **Diferenciais vs concorrentes**.
12. **Matriz comparativa** (tabela do segmento).
13. **O que eu diria num board** (a tese).
14. **Fontes**.

---

## 5. Pipeline de coleta (scraping de conteúdo público)

Abordagem em camadas, da mais barata/legal para a mais manual:

| Camada | O que coleta | Como | Automação |
|--------|--------------|------|-----------|
| **A. Páginas institucionais** | Proposta de valor, features, tarifários, T&C | `WebSearch` + `web_fetch` (HTML estático). Se a página for client-side (JS), escalar para o navegador (Claude in Chrome) que renderiza | Alta |
| **B. Tarifários & docs regulatórios** | Tabelas de tarifas (Bacen exige publicação), CET, contratos | Fetch direto de PDF/HTML do tarifário público | Alta |
| **C. App stores** | Descrição, changelog, reviews, screenshots oficiais | Fetch das páginas Play/App Store | Média |
| **D. Telas de jornada pública** | Fluxos de aquisição até a parede de login | Captura manual (print) das telas públicas, datada | Manual |
| **E. Telas logadas** | Onboarding interno, dashboards | **Só captura manual sua**, com nota de governança. A máquina documenta, não acessa | Manual (humano) |

**Regras técnicas de coleta:** respeitar `robots.txt`; rate-limit (sem martelar servidor); identificar-se quando aplicável; nunca burlar paywall/login; cachear a fonte com data. Quando `web_fetch` retornar shell vazio (página JS), usar o navegador para renderizar — não tentar contornar por outro caminho.

---

## 6. Camada de comparação (onde nasce o diferencial)

Para cada **segmento**, uma nota `03-Comparativos/Comparativo — <segmento>.md` com:
- **Matriz mestre** (linhas = instituições; colunas = critérios: tarifa, Pix, rendimento, atrito de onboarding, crédito, IA embarcada…).
- **Prós/contras por player** (3 bullets cada).
- **Diferenciais reais** (o que só um faz).
- **Lacuna vendável** (onde o produto perde → conecta a uma oferta consultiva).
- **O que eu diria num board.**

O Dataview do `_Indice-Produtos.md` gera o catálogo automático:
```dataview
TABLE instituicao, segmento, publico, data_captura
FROM "07-Setores/Financeiro/02-Produtos"
SORT segmento ASC, instituicao ASC
```

---

## 7. Rotina (a cadência viva)

- **Diária (automatizável, ~15 min):** raspar 1–2 produtos novos OU atualizar tarifário de 1 player; registrar no changelog. Pode virar tarefa agendada do Cowork (como o digest), cruzando com a daily.
- **Semanal (eu, ~30 min):** escolher 1 segmento e fechar/atualizar o comparativo com tese. É a peça que vira post/material de cliente.
- **Mensal:** revisão de frescor — qualquer ficha com `data_captura` > 60 dias entra na fila de re-coleta (preço de banco envelhece rápido).

**Gatilho de qualidade:** ficha sem tese ("o que eu diria num board") não conta como pronta — é dump, não referência.

---

## 8. Governança legal & de dados (não-negociável)

Esta base **é** uma demonstração da governança que vendo. Regras:

- **Só conteúdo público.** Tarifários (publicação obrigatória por Bacen), páginas de produto, app stores, T&C. Zero dado pessoal de cliente; zero scraping atrás de login.
- **Respeito a ToS e `robots.txt`.** Coleta para conhecimento interno/competitive intelligence; não republicar conteúdo de terceiros como meu, não reproduzir marca/figura protegida fora de uso analítico interno.
- **LGPD.** A base não trata dado pessoal — apenas informação de produto/empresa. Telas com qualquer dado pessoal (mesmo o seu, em testes) são anonimizadas antes de arquivar.
- **Residência & trilha.** Arquivos ficam nos meus folders (iCloud/local), com data de captura e URL-fonte em cada item — trilha de proveniência, igual ao que exijo de um cliente.
- **Marca registrada.** Nomes e telas dos bancos são deles; uso é análise comparativa interna, não material de venda redistribuível sem cuidado jurídico.

**O que eu diria num board:** se eu raspar errado para vender governança, perco o argumento. A coleta limpa, datada e só-pública é parte do pitch — "olha como a gente trata até a inteligência de mercado".

---

## 9. Roadmap de execução (farol → escala)

**Fase A — Validar o método (agora):** mix farol de ~5–6 instituições (2 bancões + 2 fintechs + 1 banco médio) em **1 segmento** (Conta PJ) → fecha o primeiro comparativo. *Entregue junto deste blueprint: ficha-exemplo Nu Empresas + comparativo Conta PJ.*

**Fase B — Profundidade por segmento:** rodar os 5–6 players em todos os segmentos de varejo (contas, cartões, crédito, pagamentos, investimentos).

**Fase C — Amplitude de players:** expandir para os ~15–20 maiores (todos os bancões, principais fintechs, 5–6 bancos médios) no segmento-farol.

**Fase D — Jornadas & telas:** documentar jornada visual (descoberta→ativação) dos top produtos, com telas datadas.

**Farol sugerido (Fase A):** Itaú, Bradesco (bancões) · Nubank, Inter (fintechs) · BTG Empresas (médio/digital de porte). Ajustável.

---

## 10. Métricas de sucesso

Não é "quantas fichas". É: **cobertura** (% dos segmentos × top players preenchidos), **frescor** (% de fichas com captura < 60 dias), **densidade de tese** (% de fichas com "o que eu diria num board"), e — a que importa — **uso comercial** (quantos comparativos viraram gancho de oferta ou material de cliente).

---

## 11. Próximos passos

- Aprovar o **template** (`99-Templates/TPL-Produto-Financeiro.md`) e a **ficha-exemplo** (Nu Empresas).
- Definir a lista farol final de 5–6 instituições.
- Decidir se a coleta diária vira tarefa agendada do Cowork (recomendo começar manual 1 semana, depois agendar).
- Ao fechar o 1º comparativo (Conta PJ), escolher a **lacuna vendável** e ligar a uma oferta do catálogo consultivo.

---

**Liga com:** [[Ofertas-Banking-IA-portfolio-consultivo]] · [[MOC-Financeiro]] · [[TPL-Produto-Financeiro]]
