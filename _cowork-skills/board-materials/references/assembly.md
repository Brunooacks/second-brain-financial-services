# Build multiarquivo e renumeração automática

Materiais acima de ~12 páginas não devem viver em um único HTML. Não por tamanho de arquivo, mas porque **inserir um capítulo no meio** — o que sempre acontece — obriga a renumerar eyebrows, rodapés e índices das aberturas de parte. Feito à mão, algo sempre escapa, e o erro só aparece no raster.

## Estrutura

```
projeto/
  fonts/            woff2 latin + latin-ext
  p1.html           <head> + CSS + capa + abertura I + capítulos 01–07
  papi.html         abertura II + capítulos da parte II
  div3.html         abertura III
  p2.html           capítulos da parte III
  div4.html         abertura IV
  p3.html           capítulos da parte IV
  p4.html           abertura V + capítulos finais + </body></html>
  build.py
  doc.html          gerado — nunca editar
```

O primeiro arquivo carrega `<!DOCTYPE>`, `<head>` e o CSS; o último fecha `</body></html>`. Os do meio são só sequências de `<div class="page">`. Nenhum deles é HTML válido isolado, e tudo bem: a fonte da verdade é o conjunto.

## O script

```python
import re

# ordem de montagem — inserir um capítulo é inserir um item nesta lista
parts = ['p1.html','papi.html','div3.html','p2.html','div4.html',
         'p3.html','pbrapi.html','p3b.html','div5.html','p4.html']
doc = ''.join(open(f).read() for f in parts)

# 1) renumera os eyebrows sequencialmente (só páginas de conteúdo; divisores usam .pt)
c = [0]
def eb(m):
    c[0] += 1
    return '<div class="eyebrow">%02d &middot;' % c[0]
doc = re.sub(r'<div class="eyebrow">\d+ &middot;', eb, doc)

# 2) renumera o rodapé pela posição física da página
pages = [m.start() for m in re.finditer(r'<div class="page', doc)]
def foot(m):
    n = sum(1 for p in pages if p <= m.start())
    return '<span>%02d</span></div>' % n
doc = re.sub(r'<span>\d+</span></div>', foot, doc)

open('doc.html','w').write(doc)
print('capítulos:', c[0], '| páginas:', len(pages))
```

Duas linhas de saída que valem como verificação: se o número de capítulos ou de páginas não for o esperado, algo não entrou na montagem.

## Precisa dividir um arquivo no meio para inserir?

Não crie um arquivo novo à mão — corte pelo comentário-marcador do capítulo seguinte:

```python
marker = '<!-- ================= 16 BRASIL ECONOMIA ================= -->'
a, b = open('p3.html').read().split(marker, 1)
b = marker + b
# monta ... a, novo_capitulo, b ...
```

Por isso todo capítulo começa com um comentário `<!-- ===== NN NOME ===== -->`: ele é o ponto de corte estável. O número dentro do comentário não precisa ser atualizado — ele é apenas rótulo humano; quem numera é o script.

## O que o script NÃO resolve

- **Índices das aberturas de parte** (`<div class="idx">` com os números dos capítulos daquela parte). São escritos à mão. Depois de inserir um capítulo, confira que os números das aberturas ainda batem com a numeração gerada — é a verificação final antes de entregar.
- **Referências cruzadas no texto** ("ver página 21"). Prefira referenciar capítulo e não página, e revise no fim.

## Ciclo de trabalho

```bash
python3 build.py
chromium --headless --disable-gpu --no-sandbox --print-to-pdf=out.pdf \
  --no-pdf-header-footer --virtual-time-budget=18000 file://$PWD/doc.html
pdftoppm -png -r 48 out.pdf pg      # e olhe cada página
```

Ao corrigir: edite o arquivo-parte correspondente e rode os três comandos de novo. O ciclo inteiro leva segundos, então itere até o raster estar limpo em vez de tentar acertar de primeira. Em documento longo, rasterize só as páginas que você mexeu (`-f N -l N`) nas rodadas intermediárias, e faça uma varredura completa antes da entrega final.
