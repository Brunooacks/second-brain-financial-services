# AI-Brain — como restaurar na máquina nova

Este repositório é o segundo cérebro (vault do Obsidian) + as skills customizadas do Cowork.
Backup criado em 2026-09-07. Origem na máquina antiga:
`~/Library/Mobile Documents/com~apple~CloudDocs/Head-Ai-Banking/AI-Brain/AI-Brain`

## O que está aqui
- `000-HOME.md`, `01-Daily/` … `99-Templates/` — o vault completo (notas, posts, frameworks, templates do Templater).
- `.obsidian/` — configuração do Obsidian, plugins Dataview e Templater já configurados (só `workspace.json` fica de fora, é estado de janela).
- `_cowork-skills/` — cópia das skills customizadas do Cowork: `arte-post`, `board-materials`, `caio-editorial-brain`, `consulting-research` (+ `manifest.json`).
  As skills também ficam sincronizadas na conta Claude; esta cópia é garantia.
- `RESTAURAR.md` — este guia.

## O que NÃO está aqui (e onde está)
- **Reports (PDFs)** — pasta `Head-Ai-Banking/Reports/` no iCloud Drive (sincroniza sozinha ao logar no iCloud na máquina nova). Cópia também no pendrive em `AI-Brain-backup/Reports/`.
- **Projeto "Referência em IA / CAIO"** (instruções, 27 docs, 19 PDFs) e **memória do Claude** — ficam na conta Claude, na nuvem. Nada a fazer.
- **Tarefas agendadas do Cowork** (digest diário 6h, ingestão de reports) — são do app Desktop; recriar na máquina nova com os prompts da seção 10 das instruções do Projeto.

## Passo a passo na máquina nova (15 min)
1. Logar no iCloud e esperar `Head-Ai-Banking/` sincronizar. Botão direito na pasta → "Manter baixado" (PDFs só-na-nuvem não são lidos pelo Cowork).
2. Instalar Obsidian e git (`xcode-select --install` já traz o git).
3. Clonar o vault. Duas opções:
   - **Mesmo lugar de antes (iCloud):**
     ```bash
     cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Head-Ai-Banking/AI-Brain
     mv AI-Brain AI-Brain-old-icloud   # se o iCloud já tiver trazido a pasta antiga
     git clone https://github.com/Brunooacks/second-brain-financial-services.git AI-Brain
     ```
   - **Fora do iCloud (recomendado, evita conflito iCloud × git):**
     ```bash
     git clone https://github.com/Brunooacks/second-brain-financial-services.git ~/AI-Brain
     ```
     Depois ajustar o caminho do vault nas tarefas agendadas do Cowork.
4. Abrir o Obsidian → "Open folder as vault" → apontar para a pasta clonada. Em Settings → Community plugins, desligar Restricted mode (Dataview e Templater já vêm no repo).
5. Abrir o Claude Desktop → Cowork → conectar a pasta do vault e recriar as duas tarefas agendadas.
6. Conferir: `000-HOME.md` abre, Dataview mostra as notas de `01-Daily/`, skills aparecem no Cowork.

## Rotina depois de restaurado
Uma vez por dia (ou deixar o Cowork fazer no fim do digest):
```bash
cd <pasta do vault> && git add -A && git commit -m "daily $(date +%F)" && git push
```
O pendrive é snapshot: repetir a cópia a cada troca de máquina ou a cada mês.
