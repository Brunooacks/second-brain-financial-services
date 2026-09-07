---
tipo: iniciativa-ia
jornada: credito
fase: 2
arquetipo: modernizacao
maturidade_atual: L3
maturidade_alvo: L4
score_vale: 25.0
status: candidata
data: 2026-07-04
eixos: [financeiro, governanca, soberania, economia-ia]
tags: [iniciativa, backlog, vale, credito, finops, roteamento, multi-fornecedor, veltrix]
---

# 💡 Iniciativa — Camada FinOps + roteamento de inferência de crédito em ambiente multi-fornecedor

**Em uma frase:** Uma camada que fica entre o motor de crédito e os múltiplos fornecedores de LLM (OpenAI/AWS/Google), medindo custo de inferência, roteando por jurisdição e gerando a trilha de explicabilidade que o Bacen exige — modernização governada para quem já rodou crédito/risco sobre GenAI multi-fornecedor (perfil Santander).

## 🎯 O gap que origina isto
- Jornada: Originação de crédito (F2) · Nível atual (EMA-J): **L3** (sinal L4 emergente) · Alvo: **L4** · Gap vs líder do piloto: 1
- Vale do de-para: Santander roda crédito/risco/cobrança sobre **plataforma agnóstica multi-fornecedor** (OpenAI + AWS + Google), sem camada pública de FinOps de inferência nem roteamento por jurisdição. Quanto mais GenAI entra na modelagem de risco, maior o custo de inferência e a dívida de explicabilidade.

## 🏗️ Arquétipo e desenho
**Modernização (com viés de insight/observabilidade).** Proxy entre o motor de crédito e os LLMs: (a) contabiliza custo por chamada, por modelo e por decisão (FinOps — método CARO); (b) roteia a inferência pelo fornecedor/região conforme a jurisdição do dado (residência); (c) registra prompt, modelo, versão e resposta como trilha auditável para a explicabilidade regulatória. Não troca o motor de risco — governa o consumo de inferência em volta dele.

## 📊 Placar VALE
Notas 1–5. Ver [[Placar VALE — Priorizacao de Iniciativa de IA]].

| Eixo | Nota (1–5) | Peso | Justificativa |
|------|-----------|------|---------------|
| V — Valor de negócio | 4 | 1,5 | Reduz custo de inferência num parque multi-fornecedor e destrava conformidade; valor real, porém indireto (não é receita nova de crédito). |
| A — Aderência governança/soberania | 5 | 2,0 | Roteamento por jurisdição + residência de dado + trilha de explicabilidade Bacen no núcleo. Máxima aderência. |
| L — Lastro técnico/viabilidade | 4 | 1,0 | O parque multi-fornecedor já existe (Santander declara OpenAI/AWS/Google); proxy de LLM é padrão maduro. |
| E — Encaixe Veltrix/Cohort | 5 | 1,0 | **É exatamente o Veltrix** (proxy de LLM com FinOps e observabilidade, método CARO). Demonstração viva direta. |

**Score VALE = (4×1,5)+(5×2,0)+(4×1,0)+(5×1,0) = 6,0+10,0+4,0+5,0 = 25,0 / 27,5** → faixa: **≥ 20 — candidata a proposta agora**

## 🧪 Laboratório vivo
Veltrix é o produto: mede custo de inferência por decisão de crédito, roteia por jurisdição e gera a observabilidade/trilha. O caso Santander (crédito sobre 3 fornecedores de LLM) é o argumento de que FinOps + roteamento deixam de ser luxo e viram controle de custo e de conformidade simultâneos.

## ⚠️ Contraponto real
⏳ **para o Bruno.** Insumos: (1) é venda de "encanamento" — valor indireto, ROI mais difícil de mostrar num board do que uma feature de crédito; (2) depende do banco expor o tráfego de inferência à camada, o que esbarra em segurança e em contratos existentes com os hyperscalers; (3) risco de ser visto como reinventar o observability stack que AWS/Google já vendem — a diferenciação tem que ser o **roteamento por jurisdição**, não a métrica de custo isolada.

## 🗣️ O que eu diria num board
⏳ **para o Bruno.** (A máquina propôs e pontuou; a tese e o serviço são seus.)

---
**Liga com:** [[De-Para — Originação de crédito (Fase 2 · expansão)]] · [[00b-Plano-Discovery-Jornadas-para-Iniciativas]] · [[Placar VALE — Priorizacao de Iniciativa de IA]] · [[EMA-J — Escala de Maturidade Agentica de Jornada]]
