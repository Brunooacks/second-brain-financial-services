---
tipo: framework
data: 2026-07-12
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-12]]"
eixos: [soberania, governanca, financeiro, economia-ia]
tags: [framework, auto]
---

# 🧱 Matriz de Proveniência do Dado (PCT) — Próprio, Compartilhado, Terceiro

## O problema que ele resolve
A regra do BC contra revenda no Open Finance criou estoques de dado com **destinos regulatórios opostos**, e confundi-los custa caro: um modelo de IA que bebe de dado compartilhado herda um risco regulatório que um modelo sobre dado próprio não tem. "Estratégia de dado para IA" sem esse corte é slide, não tese. Faltava um one-pager que lesse, **por modelo**, o moat competitivo e o risco regulatório ao mesmo tempo.

## O framework
Para cada modelo de IA em produção ou roadmap, classifique a proveniência do dado que o alimenta em três classes — **PCT**:

- **P — Próprio (1ª mão).** Dado transacional/comportamental gerado dentro do banco. Moat alto, ativo mais livre. (agente de investimentos do Itaú; NuFormer do Nubank.)
- **C — Compartilhado (Open Finance).** Dado que o cliente autoriza portar. Poderoso para nivelar o jogo, mas entrando em **uso cercado**: proibição de revenda, contrato de parceria obrigatório, disputa BC × ANPD sobre governança.
- **T — Terceiro (comprado/enriquecido).** Dado de fornecedor externo. Se o fornecedor se abastece, direta ou indiretamente, do Open Finance, vira **passivo de compliance** quando a regra entrar.

Leitura da matriz: quanto mais um modelo depende de **P**, maior o moat e menor o risco regulatório; **C** e **T** carregam risco crescente e exigem cláusula de proveniência antes de escalar.

## Quando usar / quando NÃO usar
Usar no inventário de dado para IA e na **due diligence de fornecedor** (auditar se algum contrato de dado/enriquecimento se abastece do Open Finance). **Não** confundir com o [[Matriz Construir-Comprar-Parcear do Ativo de IA (DCS) - Dado, Custo, Soberania]] — o DCS decide a *origem do ativo* (construir/comprar/parcear); o PCT classifica a *origem do dado* de um modelo já existente, para ler risco e moat. Também não é ranking de prioridade (isso é o [[Placar VALE — Priorizacao de Iniciativa de IA]]).

## Aplicado na prática
Agente de investimento tipo Itaú: **P** alto → moat + baixo risco regulatório. Enriquecimento de crédito via fornecedor que puxa dado do Open Finance: **T** apoiado em **C** → passivo de compliance à espera da regra. O **Veltrix** operacionaliza: rotular a proveniência de cada dado que entra na inferência (roteamento por origem/sensibilidade) transforma o PCT de planilha em controle auditável.

## Como cito isto num board
"Cada modelo em produção passa pelo PCT — Próprio, Compartilhado, Terceiro: num slide, o board vê onde está o moat de IA e onde mora o risco regulatório da nova regra do Open Finance. Sem esse corte, não sabemos qual modelo herda passivo quando a norma do BC entrar."
