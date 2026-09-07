#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One Banking AI — renderizador em Registro Húmido.
Uso: python3 render.py <nota.md> <pasta-saida>
Gera: One-Banking-AI-<data>-email.html · One-Banking-AI-<data>.html · One-Banking-AI-<data>.pdf"""
import os, re, sys, html, base64, datetime, glob
from parse_daily import parse, inline
import masthead

# ---------------------------------------------------------------- sistema
PAPEL, PAPEL_S, PAPEL_F = "#E9E5DB", "#D8D2C5", "#F1EEE6"
TINTA, CINZA, MUDO, LINHA = "#161615", "#58544C", "#8C867C", "#C9C3B5"
# Acento do One Banking: tons de azul (pedido do Bruno, 06/09/2026) — azul guache, nunca ciano de tecnologia
ACENTO   = "#2E5484"                     # azul guache — acento principal
ACENTO_E = "#1F3A5C"                     # azul profundo — selo de impacto, ênfases
ACENTO_C = "#8FB0D1"                     # azul claro — acento sobre fundo escuro (bloco da leitura)
ACENTO_M = "#6F8BA6"                     # azul acinzentado — contexto, secundários
SELO = {                                  # etiquetas de leitura — mantidas, em tons de azul
    "impacto":  ("⚠️", "Impacto direto no negócio", "#1F3A5C"),
    "primeira": ("✦", "Primeira mão", "#2E5484"),
    "contexto": ("🌐", "Contexto", "#6F8BA6"),
}
HERE = os.path.dirname(os.path.abspath(__file__))
FONTES = os.path.join(HERE, "fonts") if os.path.exists(os.path.join(HERE, "fonts", "Gloock-Regular.ttf")) else next((p for p in glob.glob("/mnt/skills/**/canvas-fonts", recursive=True) + glob.glob("/root/.claude/skills/**/canvas-fonts", recursive=True) if os.path.exists(os.path.join(p, "Gloock-Regular.ttf"))), "")

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
DIAS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

def data_extenso(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{DIAS[d.weekday()]} · {d.day:02d} de {MESES[d.month-1]} de {d.year}"

def selos_no_titulo(t):
    """Extrai os selos do início de um título (✦ Primeira mão — ⚠️ Impacto direto — Título)."""
    found = []
    while True:
        m = re.match(r"^\s*(?:(✦)\s*Primeira mão|(⚠️)\s*Impacto direto(?: no negócio)?|(🌐)\s*Contexto)\s*(?:—|–|-|·)?\s*", t)
        if not m:
            break
        found.append("primeira" if m.group(1) else "impacto" if m.group(2) else "contexto")
        t = t[m.end():]
    return found, t.strip()

def selos_inline(t):
    found = []
    if "⚠️" in t: found.append("impacto")
    if "✦" in t: found.append("primeira")
    if "🌐" in t: found.append("contexto")
    return found

def split_board(text):
    """Parágrafo com '*O que eu diria num board:*' no meio → duas partes."""
    m = re.search(r"\*O que eu diria num board:\*\s*", text)
    if m and m.start() > 0:
        return [("p", text[:m.start()].strip()), ("board", text[m.end():].strip())]
    return [("p", text)]

def numero_tabela(cell):
    return re.sub(r"\*\*", "", cell)

# ---------------------------------------------------------------- blocos comuns
def pct(v):
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*%", v)
    return float(m.group(1).replace(",", ".")) if m else None

class Base:
    email = False
    def a(self, s):  # links
        return inline(s, links=True)
    def selo(self, k):
        e, t, c = SELO[k]
        return (f'<span style="display:inline-block;font-family:{self.MONO};font-size:9.5px;letter-spacing:1.4px;text-transform:uppercase;'
                f'color:{c};border:1px solid {c};padding:2px 7px 1px;margin:0 6px 4px 0;white-space:nowrap;">{e}&nbsp;{t}</span>')
    def selos(self, ks):
        return "".join(self.selo(k) for k in ks)

# ---------------------------------------------------------------- E-MAIL (tabelas, estilo inline, fontes de sistema)
class Email(Base):
    email = True
    def a(self, s):
        return inline(s, links=True).replace('<a href=', f'<a style="color:{TINTA};text-decoration:underline;" href=')
    SERIF = "Georgia,'Times New Roman',serif"
    MONO = "'Courier New',Courier,monospace"
    SANS = "Helvetica,Arial,sans-serif"

    def p(self, text, size=14, color=TINTA, lh=1.55, italic=False, mb=10, serif=False):
        st = f"font-family:{self.SERIF if serif else self.SANS};font-size:{size}px;line-height:{lh};color:{color};margin:0 0 {mb}px;{'font-style:italic;' if italic else ''}"
        return f'<p style="{st}">{self.a(text)}</p>'

    def rotulo(self, txt, color=MUDO, mb=6):
        return f'<div style="font-family:{self.MONO};font-size:10px;letter-spacing:2.2px;text-transform:uppercase;color:{color};margin:0 0 {mb}px;">{txt}</div>'

    def board(self, text):
        return (f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:6px 0 12px;"><tr>'
                f'<td width="3" bgcolor="{ACENTO}" style="width:3px;background:{ACENTO};"></td>'
                f'<td style="padding:2px 0 2px 14px;">{self.rotulo("O que eu diria num board", ACENTO, 4)}'
                f'{self.p(text, 13.5, TINTA, 1.55, mb=0)}</td></tr></table>')

    def amanha(self, text):
        return (f'<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{PAPEL_S}" style="background:{PAPEL_S};margin:0 0 14px;"><tr>'
                f'<td style="padding:12px 14px;">{self.rotulo("Pra usar amanhã", CINZA, 4)}{self.p(text, 13, CINZA, 1.5, mb=0)}</td></tr></table>')

    def termometro(self, head, rows):
        cells = []
        for r in rows:
            num, leitura, fonte = (r + ["", "", ""])[:3]
            cells.append(f'<td width="25%" valign="top" style="padding:0 6px 0 0;">'
                         f'<div style="border-top:2px solid {TINTA};padding-top:8px;">'
                         f'<div style="font-family:{self.SERIF};font-size:22px;line-height:1.05;color:{TINTA};">{numero_tabela(num)}</div>'
                         f'<div style="font-family:{self.SANS};font-size:10.5px;line-height:1.4;color:{CINZA};margin-top:6px;">{self.a(leitura)}</div>'
                         f'<div style="font-family:{self.MONO};font-size:9px;line-height:1.4;color:{MUDO};margin-top:6px;">{self.a(fonte)}</div>'
                         f'</div></td>')
        # e-mail: 2×2 para caber em 640/mobile
        linhas = [cells[i:i+2] for i in range(0, len(cells), 2)]
        trs = "".join("<tr>" + "".join(c.replace('width="25%"', 'width="50%"') for c in l) + "</tr>" for l in linhas)
        return f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 6px;">{trs}</table>'

    def grafico(self, head, rows, nota):
        maxv = max((pct(r[1]) or 0) for r in rows) or 1
        trs = ""
        for i, r in enumerate(rows):
            v = pct(r[1]) or 0
            w = int(100 * v / maxv)
            cor = TINTA if i == 0 else CINZA
            trs += (f'<tr><td style="padding:0 0 4px;font-family:{self.SANS};font-size:11px;color:{CINZA};">{self.a(r[0])}</td></tr>'
                    f'<tr><td style="padding:0 0 12px;"><table cellpadding="0" cellspacing="0" width="100%"><tr>'
                    f'<td width="{w}%" bgcolor="{cor}" style="background:{cor};height:10px;font-size:1px;line-height:10px;">&nbsp;</td>'
                    f'<td style="padding-left:8px;font-family:{self.MONO};font-size:12px;color:{TINTA};white-space:nowrap;">{html.escape(r[1])}</td>'
                    f'<td width="{max(0, 100 - w - 12)}%"></td></tr></table></td></tr>')
        out = f'<table width="100%" cellpadding="0" cellspacing="0">{trs}</table>'
        if nota: out += self.p(nota, 12, MUDO, 1.5, italic=True)
        return out

    def lista(self, items, ordered=False):
        out = ""
        for i, it in enumerate(items):
            marca = f"{i+1}." if ordered else "—"
            out += (f'<tr><td valign="top" width="22" style="font-family:{self.MONO};font-size:12px;color:{ACENTO};padding:0 0 9px;">{marca}</td>'
                    f'<td style="padding:0 0 9px;">{self.p(it, 13.5, TINTA, 1.5, mb=0)}</td></tr>')
        return f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 6px;">{out}</table>'

    def blocos(self, blocks, fontes=False):
        out = ""
        for b in blocks:
            if b["t"] == "p":
                for k, t in split_board(b["text"]):
                    out += self.board(t) if k == "board" else self.p(t, 12 if fontes else 13.5, MUDO if fontes else "#2A2825")
            elif b["t"] == "board": out += self.board(b["text"])
            elif b["t"] == "amanha": out += self.amanha(b["text"])
            elif b["t"] == "ol": out += self.lista(b["items"], True)
            elif b["t"] == "ul": out += self.lista(b["items"])
            elif b["t"] == "table":
                if len(b["head"]) >= 3: out += self.termometro(b["head"], b["rows"])
                else: out += "<!--grafico-->"
        return out

    def item(self, it, n):
        ks, t = selos_no_titulo((it["emoji"] + " " + it["title"]).strip())
        return (f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 18px;border-top:1px solid {LINHA};"><tr><td style="padding:14px 0 0;">'
                f'{self.selos(ks)}'
                f'<div style="font-family:{self.SERIF};font-size:17px;line-height:1.3;color:{TINTA};margin:4px 0 10px;">{self.a(t)}</div>'
                f'{self.blocos(it["blocks"])}</td></tr></table>')

    def secao(self, s, idx):
        t = s["title"]; blocks = s["blocks"]
        head = f'<div style="margin:26px 0 12px;"><div style="font-family:{self.MONO};font-size:10px;letter-spacing:2.4px;color:{MUDO};text-transform:uppercase;">Seção {idx:02d}</div>' \
               f'<div style="font-family:{self.SERIF};font-size:22px;line-height:1.15;color:{TINTA};margin-top:4px;border-bottom:2px solid {TINTA};padding-bottom:8px;">{s["emoji"]} {self.a(t)}</div></div>'
        if t.startswith("Como ler"):
            return (f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 18px;border:1px solid {LINHA};"><tr><td style="padding:12px 14px;">'
                    f'{self.rotulo(s["emoji"] + " Como ler este briefing", MUDO)}' + "".join(self.p(b["text"], 12, CINZA, 1.5, mb=6) for b in blocks if b["t"] == "p") + '</td></tr></table>')
        if t.startswith("Os 3 pontos"):
            return (f'<div style="margin:0 0 22px;">{self.rotulo(s["emoji"] + " " + t, ACENTO, 10)}{self.blocos(blocks)}</div>')
        if t.startswith("Termômetro"):
            return f'<div style="margin:0 0 24px;">{self.rotulo(s["emoji"] + " " + t, MUDO, 12)}{self.blocos(blocks)}</div>'
        if t.startswith("A leitura de hoje"):
            ks = selos_inline(t)
            return (f'<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{TINTA}" style="background:{TINTA};margin:0 0 26px;"><tr><td style="padding:22px 22px 16px;">'
                    f'{self.rotulo(s["emoji"] + " A leitura de hoje", PAPEL_S, 10)}{self.selos(ks).replace(SELO["impacto"][2], "#8FB0D1").replace(SELO["primeira"][2], "#B7CBDD")}'
                    + "".join(self._dark(b) for b in blocks) + "</td></tr></table>")
        if t.startswith("Gráfico"):
            tb = next((b for b in blocks if b["t"] == "table"), None)
            nota = next((b["text"] for b in blocks if b["t"] == "p"), "")
            return head + (self.grafico(tb["head"], tb["rows"], nota) if tb else "")
        if t.startswith("Aprendizado"):
            return (head + f'<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{PAPEL_S}" style="background:{PAPEL_S};margin:0 0 10px;"><tr><td style="padding:14px 16px;">'
                    + "".join(self.p(b["text"], 13.5, TINTA, 1.55, mb=0) for b in blocks if b["t"] == "p") + "</td></tr></table>")
        if t.startswith("Fontes"):
            return head + self.blocos(blocks, fontes=True)
        return head + self.blocos(blocks) + "".join(self.item(it, i) for i, it in enumerate(s["items"]))

    def _dark(self, b):
        return self._dark0(b).replace(f'<a style="color:{TINTA};', f'<a style="color:{PAPEL_F};')
    def _dark0(self, b):
        if b["t"] == "p":
            return self.p(b["text"], 15, PAPEL_F, 1.5, serif=True)
        if b["t"] == "board":
            return (f'<table width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 12px;"><tr><td width="3" bgcolor="{ACENTO}" style="background:{ACENTO};"></td>'
                    f'<td style="padding:2px 0 2px 14px;">{self.rotulo("O que eu diria num board", "#8FB0D1", 4)}{self.p(b["text"], 13.5, PAPEL_S, 1.55, mb=0)}</td></tr></table>')
        if b["t"] == "amanha":
            return (f'<div style="border-top:1px solid #3A3936;padding-top:10px;">{self.rotulo("Pra usar amanhã", PAPEL_S, 4)}{self.p(b["text"], 13, PAPEL_S, 1.5, mb=0)}</div>')
        return ""

    def render(self, doc):
        sec_html = ""
        idx = 0
        for s in doc["sections"]:
            t = s["title"]
            if not any(t.startswith(k) for k in ("Como ler", "Os 3 pontos", "Termômetro", "A leitura", "Gráfico", "Aprendizado", "Fontes", "No Radar")):
                idx += 1
            sec_html += self.secao(s, idx)
        lede = doc["lede"]
        curadoria = re.sub(r"\*\*", "", lede[0]) if lede else ""
        resumo = lede[1] if len(lede) > 1 else ""
        data = data_extenso(doc["data"])
        preheader = html.escape(re.sub(r"\*\*", "", resumo)[:160])
        assunto = f"One Banking AI · Ed. {doc['edicao']} · {re.sub(r'[*]', '', resumo)[:90]}"
        return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(doc['title'])}</title>
<style>body{{margin:0;padding:0;background:{PAPEL_S};}} a{{color:{TINTA};text-decoration:underline;text-decoration-color:{LINHA};}} img{{border:0;}}
@media only screen and (max-width:640px){{ .w{{width:100%!important;}} .pad{{padding-left:18px!important;padding-right:18px!important;}} }}</style></head>
<body style="margin:0;padding:0;background:{PAPEL_S};">
<div style="display:none;max-height:0;overflow:hidden;font-size:1px;color:{PAPEL_S};">{preheader}</div>
<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{PAPEL_S}" style="background:{PAPEL_S};"><tr><td align="center" style="padding:18px 0 30px;">
<table class="w" width="640" cellpadding="0" cellspacing="0" bgcolor="{PAPEL}" style="width:640px;max-width:640px;background:{PAPEL};">
<tr><td class="pad" style="padding:30px 36px 0;">
  <table width="100%" cellpadding="0" cellspacing="0"><tr>
    <td style="font-family:{self.MONO};font-size:10px;letter-spacing:2.4px;text-transform:uppercase;color:{MUDO};">Briefing diário · IA no setor financeiro</td>
    <td align="right" style="font-family:{self.MONO};font-size:10px;letter-spacing:2.4px;text-transform:uppercase;color:{MUDO};">Edição Nº {doc['edicao']}</td></tr></table>
  <div style="font-family:{self.SERIF};font-size:40px;line-height:1;letter-spacing:-0.5px;color:{TINTA};margin:16px 0 6px;">One Banking <span style="color:{ACENTO};">AI</span></div>
  <div style="font-family:{self.MONO};font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:{CINZA};">{data}</div>
  <table width="100%" cellpadding="0" cellspacing="0" style="margin:18px 0 0;"><tr><td height="2" bgcolor="{TINTA}" style="height:2px;background:{TINTA};font-size:1px;line-height:2px;">&nbsp;</td></tr>
  <tr><td height="1" style="height:1px;font-size:1px;line-height:1px;">&nbsp;</td></tr>
  <tr><td height="1" bgcolor="{TINTA}" style="height:1px;background:{TINTA};font-size:1px;line-height:1px;">&nbsp;</td></tr></table>
</td></tr>
<tr><td class="pad" style="padding:22px 36px 0;">
  {self.p(resumo, 17, TINTA, 1.5, mb=8, serif=True)}
  <div style="font-family:{self.MONO};font-size:10px;letter-spacing:1.6px;text-transform:uppercase;color:{MUDO};margin:0 0 24px;">{html.escape(curadoria)}</div>
  {sec_html}
</td></tr>
<tr><td class="pad" style="padding:26px 36px 30px;">
  <table width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid {TINTA};"><tr>
    <td style="padding-top:12px;font-family:{self.MONO};font-size:9.5px;letter-spacing:1.8px;text-transform:uppercase;color:{MUDO};line-height:1.7;">One Banking AI · Edição Nº {doc['edicao']} · {doc['data']}<br>Uso interno e confidencial · cruza com o estudo Where To Play Banking · One Banking (MTP 27-29)</td>
    <td align="right" valign="top" style="padding-top:12px;font-family:{self.MONO};font-size:9.5px;letter-spacing:1.8px;text-transform:uppercase;color:{ACENTO};white-space:nowrap;">Team Sector Banking</td></tr></table>
</td></tr>
</table></td></tr></table></body></html>""", assunto

# ---------------------------------------------------------------- PDF (WeasyPrint, fontes embutidas, paginação controlada)
class Pdf(Base):
    def a(self, s):
        return inline(s, links=True).replace("—", '<span class="dash">—</span>').replace(" + ", ' <span class="dash">+</span> ')
    SERIF = "Gloock, Georgia, serif"
    MONO = "'DM Mono', 'Courier New', monospace"
    SANS = "'Instrument Sans', Helvetica, Arial, sans-serif"

    def p(self, text, cls="p"):
        return f'<p class="{cls}">{self.a(text)}</p>'
    def board(self, text):
        return f'<div class="board"><div class="rot ac">O que eu diria num board</div>{self.p(text, "pb")}</div>'
    def amanha(self, text):
        return f'<div class="amanha"><div class="rot">Pra usar amanhã</div>{self.p(text, "pa")}</div>'
    def lista(self, items, ordered=False):
        tag = "ol" if ordered else "ul"
        return f'<{tag} class="lst">' + "".join(f"<li>{self.a(i)}</li>" for i in items) + f"</{tag}>"
    def termometro(self, head, rows):
        cells = ""
        for r in rows:
            num, leitura, fonte = (r + ["", "", ""])[:3]
            cells += f'<div class="term"><div class="num">{numero_tabela(num)}</div><div class="lei">{self.a(leitura)}</div><div class="fon">{self.a(fonte)}</div></div>'
        return f'<div class="termos">{cells}</div>'
    def grafico(self, head, rows, nota):
        maxv = max((pct(r[1]) or 0) for r in rows) or 1
        out = '<div class="graf">'
        for i, r in enumerate(rows):
            v = pct(r[1]) or 0
            out += (f'<div class="gl">{self.a(r[0])}</div><div class="gb"><div class="bar {"b0" if i == 0 else "bn"}" style="width:{100*v/maxv:.1f}%"></div>'
                    f'<span class="gv">{html.escape(r[1])}</span></div>')
        out += "</div>"
        if nota: out += self.p(nota, "nota")
        return out
    def blocos(self, blocks, fontes=False):
        out = ""
        for b in blocks:
            if b["t"] == "p":
                for k, t in split_board(b["text"]):
                    out += self.board(t) if k == "board" else self.p(t, "fon-p" if fontes else "p")
            elif b["t"] == "board": out += self.board(b["text"])
            elif b["t"] == "amanha": out += self.amanha(b["text"])
            elif b["t"] == "ol": out += self.lista(b["items"], True)
            elif b["t"] == "ul": out += self.lista(b["items"])
            elif b["t"] == "table" and len(b["head"]) >= 3: out += self.termometro(b["head"], b["rows"])
        return out
    def item(self, it):
        ks, t = selos_no_titulo((it["emoji"] + " " + it["title"]).strip())
        return f'<section class="item">{self.selos(ks)}<h3>{self.a(t)}</h3>{self.blocos(it["blocks"])}</section>'
    def secao(self, s, idx):
        t = s["title"]; blocks = s["blocks"]
        head = f'<div class="sec-head"><div class="rot">Seção {idx:02d}</div><h2>{s["emoji"]} {self.a(t)}</h2></div>'
        if t.startswith("Como ler"):
            return f'<div class="como"><div class="rot">{s["emoji"]} Como ler este briefing</div>' + "".join(self.p(b["text"], "pc") for b in blocks if b["t"] == "p") + "</div>"
        if t.startswith("Os 3 pontos"):
            return f'<div class="pontos"><div class="rot ac">{s["emoji"]} {t}</div>{self.blocos(blocks)}</div>'
        if t.startswith("Termômetro"):
            return f'<div class="termo-wrap"><div class="rot">{s["emoji"]} {t}</div>{self.blocos(blocks)}</div>'
        if t.startswith("A leitura de hoje"):
            ks = selos_inline(t)
            inner = ""
            for b in blocks:
                if b["t"] == "p": inner += self.p(b["text"], "pl")
                elif b["t"] == "board": inner += f'<div class="board dk"><div class="rot ac2">O que eu diria num board</div>{self.p(b["text"], "pb")}</div>'
                elif b["t"] == "amanha": inner += f'<div class="amanha dk"><div class="rot">Pra usar amanhã</div>{self.p(b["text"], "pa")}</div>'
            return f'<div class="leitura"><div class="rot pl-rot">{s["emoji"]} A leitura de hoje</div><div class="selos-dk">{self.selos(ks)}</div>{inner}</div>'
        if t.startswith("Gráfico"):
            tb = next((b for b in blocks if b["t"] == "table"), None)
            nota = next((b["text"] for b in blocks if b["t"] == "p"), "")
            return f'<section class="bloco">{head}{self.grafico(tb["head"], tb["rows"], nota) if tb else ""}</section>'
        if t.startswith("Aprendizado"):
            return f'<section class="bloco">{head}<div class="aprend">' + "".join(self.p(b["text"], "p") for b in blocks if b["t"] == "p") + "</div></section>"
        if t.startswith("Fontes"):
            return f'<section class="bloco fontes">{head}{self.blocos(blocks, fontes=True)}</section>'
        if t.startswith("No Radar"):
            return f'<section class="bloco">{head}{self.blocos(blocks)}</section>'
        return f'<div class="sec">{head}{self.blocos(blocks)}' + "".join(self.item(it) for it in s["items"]) + "</div>"

    def css(self, cab_uri, papel_uri):
        fp = lambda n: f"file://{FONTES}/{n}"
        return f"""
@font-face{{font-family:Gloock;src:url('{fp("Gloock-Regular.ttf")}');}}
@font-face{{font-family:'DM Mono';src:url('{fp("DMMono-Regular.ttf")}');}}
@font-face{{font-family:'Instrument Sans';src:url('{fp("InstrumentSans-Regular.ttf")}');}}
@font-face{{font-family:'Instrument Sans';src:url('{fp("InstrumentSans-Bold.ttf")}');font-weight:700;}}
@page{{size:A4;margin:18mm 17mm 20mm 17mm;background:{PAPEL} url('{papel_uri}') repeat;
  @bottom-left{{content:"One Banking AI · Nº {self.ed} · {self.data}";font-family:'DM Mono';font-size:7.5pt;letter-spacing:1.6pt;text-transform:uppercase;color:{MUDO};}}
  @bottom-right{{content:"Uso interno · p. " counter(page) " / " counter(pages);font-family:'DM Mono';font-size:7.5pt;letter-spacing:1.6pt;text-transform:uppercase;color:{MUDO};}}}}
@page:first{{margin-top:0;}}
html,body{{margin:0;padding:0;color:#2A2825;font-family:{self.SANS};font-size:9.6pt;line-height:1.52;}}
.dash{{font-family:{self.SANS};}}
.star{{font-family:'DejaVu Sans';font-size:0.85em;}}
img.emo{{height:0.95em;width:auto;vertical-align:-0.12em;margin-right:0.12em;}}
a{{color:{TINTA};text-decoration:none;border-bottom:0.5pt solid {LINHA};}}
b{{font-weight:700;color:{TINTA};}} h1 b,h2 b,h3 b,.lede b{{font-weight:normal;}}
i{{font-style:italic;}}
.cab{{margin:0 -17mm 0 -17mm;height:52mm;background:url('{cab_uri}') center/cover no-repeat;}}
.mast{{margin-top:7mm;}}
.mast .linha{{display:flex;justify-content:space-between;font-family:{self.MONO};font-size:7.5pt;letter-spacing:2pt;text-transform:uppercase;color:{MUDO};}}
.mast h1{{font-family:{self.SERIF};font-weight:normal;font-size:34pt;line-height:1;letter-spacing:-0.5pt;margin:5mm 0 2mm;}}
.mast h1 span{{color:{ACENTO};}}
.mast .data{{font-family:{self.MONO};font-size:8.5pt;letter-spacing:1.6pt;text-transform:uppercase;color:{CINZA};}}
.regra{{border-top:1.6pt solid {TINTA};border-bottom:0.6pt solid {TINTA};height:1.2pt;margin:5mm 0 6mm;}}
.lede{{font-family:{self.SERIF};font-size:12.4pt;line-height:1.45;margin:0 0 3mm;color:{TINTA};}}
.curad{{font-family:{self.MONO};font-size:7.5pt;letter-spacing:1.6pt;text-transform:uppercase;color:{MUDO};margin:0 0 7mm;}}
.rot{{font-family:{self.MONO};font-size:7.5pt;letter-spacing:2pt;text-transform:uppercase;color:{MUDO};margin:0 0 2mm;}}
.rot.ac{{color:{ACENTO};}} .rot.ac2{{color:{ACENTO_C};}}
p{{margin:0 0 3mm;orphans:3;widows:3;}}
p.pc{{font-family:{self.SANS};font-size:8.6pt;color:{CINZA};line-height:1.45;margin-bottom:1.5mm;}}
.como{{border:0.6pt solid {LINHA};padding:3.5mm 4mm 2.5mm;margin:0 0 6mm;}}
.pontos{{margin:0 0 7mm;}}
ol.lst,ul.lst{{margin:0;padding:0;list-style:none;counter-reset:n;}}
ol.lst li,ul.lst li{{position:relative;padding-left:7mm;margin:0 0 2.4mm;page-break-inside:avoid;}}
ol.lst li::before{{counter-increment:n;content:counter(n) ".";position:absolute;left:0;top:0.3mm;font-family:{self.MONO};font-size:8.5pt;color:{ACENTO};}}
ul.lst li::before{{content:"—";position:absolute;left:0;top:0;font-family:{self.MONO};font-size:8.5pt;color:{ACENTO};}}
.termo-wrap{{margin:0 0 8mm;page-break-inside:avoid;}}
.termos{{display:flex;gap:4mm;}}
.term{{flex:1;border-top:1.4pt solid {TINTA};padding-top:2.5mm;}}
.term .num{{font-family:{self.SERIF};font-size:15pt;line-height:1.05;color:{TINTA};}}
.term .lei{{font-family:{self.SANS};font-size:7.8pt;line-height:1.4;color:{CINZA};margin-top:1.8mm;}}
.term .fon{{font-family:{self.MONO};font-size:6.6pt;line-height:1.4;color:{MUDO};margin-top:1.6mm;}}
.leitura{{background:{TINTA};color:{PAPEL_F};padding:6mm 7mm 4mm;margin:0 0 8mm;}}
.leitura .pl-rot,.leitura .selos-dk{{page-break-after:avoid;}}
.leitura .pl-rot{{color:{PAPEL_S};}}
.leitura p.pl{{font-family:{self.SERIF};font-size:10.6pt;line-height:1.5;color:{PAPEL_F};}}
.leitura a{{color:{PAPEL_F};border-bottom-color:#4A4945;}}
.leitura b{{color:{PAPEL_F};background:none;}}
.selos-dk span{{color:#8FB0D1 !important;border-color:#4F6D8C !important;}}
.board{{border-left:2pt solid {ACENTO};padding:1mm 0 1mm 4.5mm;margin:2.5mm 0 4mm;}}
.board p.pb{{font-size:9.3pt;line-height:1.52;margin:0;}}
.board.dk p.pb{{color:{PAPEL_S};}} .board.dk b{{color:{PAPEL_F};}}
.amanha{{background:{PAPEL_S};padding:3.5mm 4mm 3mm;margin:0 0 4mm;page-break-inside:avoid;}}
.amanha.dk{{background:transparent;border-top:0.6pt solid #4A4945;padding:3mm 0 0;}}
.amanha.dk .rot{{color:{PAPEL_S};}}
.amanha p.pa{{font-size:9pt;color:{CINZA};margin:0;}} .amanha.dk p.pa{{color:{PAPEL_S};}}
.sec-head{{page-break-after:avoid;break-after:avoid;margin:8mm 0 4mm;}}
.sec-head h2{{font-family:{self.SERIF};font-weight:normal;font-size:17pt;line-height:1.15;margin:1mm 0 0;padding-bottom:2.2mm;border-bottom:1.4pt solid {TINTA};}}
.sec > .sec-head + .item{{border-top:0;padding-top:0;}}
.item{{border-top:0.6pt solid {LINHA};padding-top:3.5mm;margin:0 0 5mm;page-break-inside:auto;}}
.item h3{{font-family:{self.SERIF};font-weight:normal;font-size:12.6pt;line-height:1.3;margin:1mm 0 2.5mm;page-break-after:avoid;break-after:avoid;}}
.item .selos-wrap{{margin-bottom:1mm;}}
.bloco{{page-break-inside:avoid;}}
.aprend{{background:{PAPEL_S};padding:4mm 4.5mm 2mm;}}
.graf{{margin:2mm 0 3mm;}}
.graf .gl{{font-family:{self.SANS};font-size:8.4pt;color:{CINZA};margin:0 0 1mm;}}
.graf .gb{{display:flex;align-items:center;gap:2.5mm;margin:0 0 3.2mm;}}
.graf .bar{{height:3.2mm;}} .graf .b0{{background:{TINTA};}} .graf .bn{{background:{CINZA};}}
.graf .gv{{font-family:{self.MONO};font-size:9pt;}}
p.nota{{font-style:italic;font-size:9pt;color:{MUDO};}}
.fontes p.fon-p,.fontes li{{font-family:{self.SANS};font-size:8.2pt;color:{CINZA};line-height:1.45;}}
.fontes ul.lst li::before{{color:{MUDO};}}
.fim{{margin-top:10mm;border-top:1.6pt solid {TINTA};padding-top:3mm;display:flex;justify-content:space-between;font-family:{self.MONO};font-size:7.5pt;letter-spacing:1.8pt;text-transform:uppercase;color:{MUDO};}}
.fim span{{color:{ACENTO};}}
"""

    def render(self, doc, cab_png, papel_jpg):
        self.ed, self.data = doc["edicao"], doc["data"]
        cab_uri = "data:image/png;base64," + base64.b64encode(open(cab_png, "rb").read()).decode()
        papel_uri = "data:image/jpeg;base64," + base64.b64encode(open(papel_jpg, "rb").read()).decode()
        secs = ""; idx = 0
        for s in doc["sections"]:
            t = s["title"]
            if not any(t.startswith(k) for k in ("Como ler", "Os 3 pontos", "Termômetro", "A leitura", "Gráfico", "Aprendizado", "Fontes", "No Radar")):
                idx += 1
            secs += self.secao(s, idx)
        lede = doc["lede"]
        curadoria = re.sub(r"\*\*", "", lede[0]) if lede else ""
        resumo = lede[1] if len(lede) > 1 else ""
        return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>{html.escape(doc['title'])}</title><style>{self.css(cab_uri, papel_uri)}</style></head>
<body>
<div class="cab"></div>
<div class="mast"><div class="linha"><span>Briefing diário · IA no setor financeiro</span><span>Edição Nº {doc['edicao']}</span></div>
<h1>One Banking <span>AI</span></h1><div class="data">{data_extenso(doc['data'])}</div><div class="regra"></div></div>
<p class="lede">{self.a(resumo)}</p><div class="curad">{html.escape(curadoria)}</div>
{secs}
<div class="fim"><div>One Banking AI · Edição Nº {doc['edicao']} · {doc['data']} · uso interno e confidencial</div><span>Team Sector Banking</span></div>
</body></html>"""

# ---------------------------------------------------------------- emoji → imagem (WeasyPrint não desenha fonte bitmap)
_EMO_CACHE = {}
def emoji_img(seq):
    if seq not in _EMO_CACHE:
        from PIL import Image, ImageFont, ImageDraw
        import io
        cands = ["/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", "/System/Library/Fonts/Apple Color Emoji.ttc"]
        path = next((c for c in cands if os.path.exists(c)), None)
        if not path:
            _EMO_CACHE[seq] = None
            return f'<span class="star">{seq}</span>'
        f = ImageFont.truetype(path, 109 if path.endswith(".ttf") else 160)
        im = Image.new("RGBA", (160, 140), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 0), seq, font=f, embedded_color=True)
        bb = im.getbbox()
        im = im.crop(bb) if bb else im
        # dessatura levemente para sentar no papel
        r, g, b, a = im.split()
        gray = Image.merge("RGB", (r, g, b)).convert("L")
        im = Image.merge("RGBA", (Image.blend(r, gray, 0.35), Image.blend(g, gray, 0.35), Image.blend(b, gray, 0.35), a))
        buf = io.BytesIO(); im.save(buf, "PNG")
        _EMO_CACHE[seq] = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    return f'<img class="emo" src="{_EMO_CACHE[seq]}" alt="{seq}">' if _EMO_CACHE[seq] else f'<span class="star">{seq}</span>'

# ---------------------------------------------------------------- main
def main(md_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    doc = parse(open(md_path, encoding="utf-8").read())
    data = doc["data"] or os.path.basename(md_path)[:10]
    base = os.path.join(out_dir, f"One-Banking-AI-{data}")
    cab = os.path.join(HERE, "cabecalho.png"); papel = os.path.join(HERE, "papel.jpg")
    if not os.path.exists(cab): masthead.cabecalho(cab)
    if not os.path.exists(papel): masthead.fundo_papel(papel)
    email_html, assunto = Email().render(doc)
    open(base + "-email.html", "w", encoding="utf-8").write(email_html)
    open(base + "-assunto.txt", "w", encoding="utf-8").write(assunto)
    pdf_html = Pdf().render(doc, cab, papel)
    EMO = re.compile(r"((?:[\U0001F300-\U0001FAFF\u2600-\u2725\u2727-\u27BF\u2B50\U0001F1E6-\U0001F1FF]\uFE0F?)+)")
    pdf_html = pdf_html.replace("✦", '<span class="star">✦</span>')
    pdf_html = re.sub(r">([^<]*)<", lambda m: ">" + EMO.sub(lambda e: emoji_img(e.group(1)), m.group(1)) + "<", pdf_html)
    open(base + ".html", "w", encoding="utf-8").write(pdf_html)
    try:
        from weasyprint import HTML
        HTML(string=pdf_html, base_url=HERE).write_pdf(base + ".pdf")
    except ImportError:
        print("weasyprint ausente: instale com `pip install weasyprint` (o HTML do PDF foi gerado mesmo assim)")
    print("ok", base)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "/home/claude/ob/out")
