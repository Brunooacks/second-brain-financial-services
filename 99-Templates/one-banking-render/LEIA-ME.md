# One Banking AI — renderizador (sistema Registro Húmido)

Gera o e-mail e o PDF da edição a partir da nota diária `01-Daily/AAAA-MM-DD.md`, sem mudar o conteúdo.

```bash
pip install weasyprint pillow numpy   # uma vez
python3 render.py ../../01-Daily/2026-09-05.md ../../01-Daily/
```

Saída em `01-Daily/`: `One-Banking-AI-<data>-email.html` (e-mail, tabelas + estilo inline, fontes de sistema),
`One-Banking-AI-<data>.html` (versão para impressão) e `One-Banking-AI-<data>.pdf` (WeasyPrint, A4, fontes embutidas)
e `One-Banking-AI-<data>-assunto.txt` (linha de assunto sugerida).

## O sistema
- Papel `#E9E5DB` · papel escuro `#D8D2C5` · nanquim `#161615` · cinza `#58544C` · mudo `#8C867C`
- Acento em tons de azul (decisão de 06/09): azul guache `#2E5484` principal, azul profundo `#1F3A5C` (selo de impacto), azul claro `#8FB0D1` sobre fundo escuro, azul acinzentado `#6F8BA6` (contexto). Nunca ciano de tecnologia.
- Tipografia: Gloock (títulos, lede, números), DM Mono (rótulos, fontes, rodapé), Instrument Sans (texto corrido).
  No e-mail: Georgia / Courier New / Helvetica como equivalentes de sistema.
- Cabeçalho ilustrado (`cabecalho.png`) e textura de papel (`papel.jpg`) são gerados por `masthead.py`; para trocar a cena, rode `python3 masthead.py`.

## Estrutura da nota que o parser espera
`# One Banking AI · data · Edição Nº N` → blockquote com curadoria + lede → `## 📌 Como ler` → `## ⚠️ Os 3 pontos` (lista numerada)
→ `## 🌡️ Termômetro` (tabela de 3 colunas) → `## ⚡ A leitura de hoje` → seções `##` com itens `###` (selos no início do título)
→ `## 🔭 No Radar` (lista) → `## 📊 Gráfico do dia` (tabela de 2 colunas com %) → `## 🎓 Aprendizado` → `## 📚 Fontes`.
Blocos `*O que eu diria num board:*` e `*Pra usar amanhã:*` viram caixas próprias.

## Paginação (o que estava quebrando)
Título de seção nunca fica sozinho no pé da página (`break-after: avoid`); termômetro, "pra usar amanhã", gráfico e aprendizado
não quebram no meio; o bloco escuro da leitura pode quebrar (é maior que uma página) mas mantém rótulo + primeiro parágrafo juntos.
