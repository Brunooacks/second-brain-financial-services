#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parser do One Banking AI (nota diária .md) → estrutura neutra usada pelo e-mail e pelo PDF."""
import re, html

LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")

def inline(md, links=True):
    """Markdown inline → HTML (negrito, itálico, links)."""
    s = html.escape(md, quote=False)
    s = LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>' if links else m.group(1), s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = s.replace(" · ", " &middot; ")
    return s

def split_emoji(title):
    m = re.match(r"^\s*((?:[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-↪⌀-⏿️\U0001F1E6-\U0001F1FF]\s*)+)(.*)$", title)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", title.strip()

def parse_table(lines):
    rows = []
    for l in lines:
        if re.match(r"^\|\s*-", l):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        rows.append(cells)
    return rows[0], rows[1:]

def parse(md_text):
    lines = md_text.splitlines()
    doc = {"meta": {}, "title": "", "edicao": "", "data": "", "lede": [], "sections": []}
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            if ":" in lines[i]:
                k, v = lines[i].split(":", 1)
                doc["meta"][k.strip()] = v.strip()
            i += 1
        i += 1
    doc["data"] = doc["meta"].get("data", "")
    cur = None      # seção (H2)
    item = None     # item (H3)
    def container():
        return item if item is not None else cur
    buf = []
    def flush():
        nonlocal buf
        if not buf:
            return
        text = " ".join(x.strip() for x in buf).strip()
        buf = []
        if not text:
            return
        tgt = container()
        if tgt is None:
            doc["lede"].append(text)
            return
        m = re.match(r"^\*(O que eu diria num board|Pra usar amanhã)\s*:\*\s*(.*)$", text)
        if m:
            tgt["blocks"].append({"t": "board" if m.group(1).startswith("O que") else "amanha", "text": m.group(2)})
        else:
            tgt["blocks"].append({"t": "p", "text": text})
    while i < len(lines):
        l = lines[i]
        if l.startswith("# "):
            flush()
            doc["title"] = l[2:].strip()
            m = re.search(r"Edição\s*N[ºo°]\s*(\d+)", doc["title"])
            doc["edicao"] = m.group(1) if m else ""
        elif l.startswith("## "):
            flush()
            emoji, t = split_emoji(l[3:])
            cur = {"emoji": emoji, "title": t, "blocks": [], "items": []}
            item = None
            doc["sections"].append(cur)
        elif l.startswith("### "):
            flush()
            emoji, t = split_emoji(l[4:])
            item = {"emoji": emoji, "title": t, "blocks": []}
            cur["items"].append(item)
        elif l.startswith("> "):
            flush()
            if cur is None:
                doc["lede"].append(l[2:].strip())
            else:
                buf.append(l[2:])
        elif l.startswith("|"):
            flush()
            tb = []
            while i < len(lines) and lines[i].startswith("|"):
                tb.append(lines[i]); i += 1
            head, rows = parse_table(tb)
            container()["blocks"].append({"t": "table", "head": head, "rows": rows})
            continue
        elif re.match(r"^\s*[-*]\s+", l):
            flush()
            lst = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                lst.append(re.sub(r"^\s*[-*]\s+", "", lines[i]).strip()); i += 1
            container()["blocks"].append({"t": "ul", "items": lst})
            continue
        elif re.match(r"^\s*\d+\.\s+", l):
            flush()
            lst = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                lst.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()); i += 1
            container()["blocks"].append({"t": "ol", "items": lst})
            continue
        elif l.strip() == "---":
            flush()
        elif l.strip() == "":
            flush()
        else:
            buf.append(l)
        i += 1
    flush()
    return doc

if __name__ == "__main__":
    import sys, json
    d = parse(open(sys.argv[1], encoding="utf-8").read())
    print(json.dumps({k: v for k, v in d.items() if k != "sections"}, ensure_ascii=False, indent=1))
    for s in d["sections"]:
        print(s["emoji"], s["title"], [b["t"] for b in s["blocks"]], [(it["emoji"], it["title"][:40], [b["t"] for b in it["blocks"]]) for it in s["items"]])
