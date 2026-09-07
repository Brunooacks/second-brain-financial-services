---
tipo: framework
data: 2026-08-13
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-08-13]]"
eixos: [economia-ia, financeiro]
tags: [framework, auto]
---

# 🧱 Matriz Adoção × Eficiência de IA (A×E)

## O problema que ele resolve
Board olha "gasto com IA" como número solto e tira a conclusão errada: fatura baixa parece disciplina, fatura alta parece desperdício. Os dois enganam. Falta um par de eixos que separe **adoção real** de **eficiência de execução** — porque cada métrica sozinha mente.

## O framework
Duas medidas, quatro quadrantes:
- **Eixo X — Adoção:** tokens de saída por usuário ativo. Proxy mais honesto de uso real (ninguém queima inferência por vaidade em escala). Baseline de referência: frontier firms geram **8,3x** mais que a empresa típica, contra 2,6x um ano atrás ([OpenAI, 12/08](https://openai.com/index/how-enterprises-put-ai-to-work/); daily 2026-08-13).
- **Eixo Y — Eficiência:** custo por tarefa concluída (cost per completed task), que soma turnos, tokens e retries até o fim — ex.: **US$ 0,84/tarefa** do Grok 4.6 ([Artificial Analysis](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis)).

Quadrantes:
- **Baixa adoção / baixa eficiência — "Piloto cego":** ninguém usa, e o pouco que roda é caro. Diagnóstico: ainda não saiu do laboratório.
- **Alta adoção / baixa eficiência — "Queima cara":** usa muito e desperdiça em turnos/retries. Maior risco de fatura; é onde re-roteamento e escolha de modelo pagam sozinhos.
- **Baixa adoção / alta eficiência — "Eficiente e subutilizado":** arquitetura boa, adoção travada. Problema é change management, não tecnologia.
- **Alta adoção / alta eficiência — "Maturidade real":** o quadrante-alvo. Usa muito e resolve barato.

## Quando usar / quando NÃO usar
Usar em revisão executiva de portfólio de IA e antes de renegociar contrato de fornecedor. **Não** usar para carga curta e determinística (tarefa de um turno), onde o custo por tarefa colapsa no preço por token e o eixo Y perde resolução.

## Aplicado na prática
Veltrix instrumenta os dois eixos por operação: tokens/usuário (adoção) e custo por tarefa com telemetria de turnos/retries (eficiência). Move o caso "Queima cara" para "Maturidade real" via re-roteamento por preço/qualidade — sem re-arquitetar o produto.

## Como cito isto num board
"Nossa IA está no quadrante 'queima cara': adoção alta, mas pagando o dobro de turnos por tarefa — o ganho está em roteamento, não em cortar uso."
