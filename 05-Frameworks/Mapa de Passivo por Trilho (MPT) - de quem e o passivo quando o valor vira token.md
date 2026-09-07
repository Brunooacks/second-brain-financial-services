---
tipo: framework
data: 2026-07-05
status: rascunho
origem: auto-digest
fonte_daily: "[[2026-07-05]]"
eixos: [soberania, financeiro, governanca, economia-ia]
tags: [framework, auto]
---

# 🧱 Mapa de Passivo por Trilho (MPT) — de quem é o passivo quando o valor vira token

> Um one-pager que impede a decisão de "entrar em token/cripto" de ser tomada como integração técnica quando é, na verdade, escolha de modelo de negócio.

## O problema que ele resolve
Quando o banco cogita tocar valor tokenizado — stablecoin de terceiro, depósito tokenizado (tokenized deposit) próprio, Drex — a discussão tende a cair no colo da TI como "qual blockchain / qual integração". É a pergunta errada. A pergunta que decide se o banco continua banco é **de quem é o passivo no trilho onde o valor liquida** (ver [[O campo de soberania bancaria nao e o app e de quem e o passivo no trilho onde o deposito vira token]]). O **[[Roteamento de Trilho do Agente de Pagamento (SRC)]]** decide por qual trilho o *agente* paga; o MPT é a camada acima — decide se o banco **emite ou aluga** o trilho, olhando o balanço, não a experiência de pagamento.

## O framework
Para cada forma de valor tokenizado que o banco cogita tocar, uma linha respondendo quatro perguntas — **P-L-F-R**, legíveis por um board em 30 segundos:

- **P — Passivo:** de quem é o passivo? Depósito tokenizado = passivo do banco regulado (dentro do seguro de depósito). Stablecoin = passivo de emissor privado. Drex = passivo/infra do Bacen.
- **L — Lastro (quem quebra):** quem quebra se o lastro falhar? No depósito tokenizado, o próprio banco sob supervisão; na stablecoin, o emissor e sua reserva 1:1; no Drex, o desenho central do BC.
- **F — Funding:** quem fica com o funding? É a pergunta de sobrevivência: se o cliente move dinheiro em stablecoin de terceiro, o funding do banco migra para outro balanço; no depósito tokenizado, permanece.
- **R — Regulador:** qual regulador manda? Bacen/CVM (BR), lei de stablecoin dos EUA (licenciamento jan/2027, lastro 1:1, KYC/AML), ou a régua do Drex/Open Finance.

A saída é uma matriz simples (forma de valor × P × L × F × R), que expõe a decisão real: **emitir o próprio trilho tokenizado vs alugar o de um terceiro** — e o custo de soberania de cada opção.

## Quando usar / quando NÃO usar
**Usar:** quando o board debater "entrar em cripto/stablecoin/token", ao avaliar parceria com emissor de stablecoin, ao definir postura frente ao Drex, ou ao desenhar o radar estratégico de 24 meses. **Não usar:** para valor que não é tokenizado (Pix/TED comum já têm passivo e regulador óbvios) nem como política de *roteamento* de um pagamento específico — para isso o portão é o SRC. O MPT é decisão de arquitetura de funding, não de transação.

## Aplicado na prática
É o princípio do **Veltrix** levado ao dinheiro: assim como roteamos inferência por jurisdição e sensibilidade e sabemos build-vs-buy auditável, o MPT roteia a *decisão de trilho de valor* por passivo e soberania. No BR, ele mostra por que a resposta soberana é participar da definição do Drex enquanto ele é escrito (trilho público, neutro) em vez de montar um trilho tokenizado privado que colida com ele — a diferenciação vira o que se constrói **em cima** do trilho.

## Como cito isto num board
"Antes de decidir se entramos em token, cada forma de valor passa pelo MPT — Passivo, Lastro, Funding, Regulador. É o que impede a escolha entre continuar banco e virar prateleira de ser tomada como integração técnica."
