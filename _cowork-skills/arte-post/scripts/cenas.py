#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGISTRO HÚMIDO — biblioteca de cenas.
Mesma gramática de traço; a cena muda conforme a tese. 4:5, supersampling 2x."""

import random, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 2
W, H = 1080 * S, 1350 * S
FONTES = "/root/.claude/skills/synced/canvas-design/canvas-fonts"

PAPEL   = (233, 229, 219)
PAPEL_S = (216, 210, 197)
TINTA   = (22, 22, 21)
MARGEM  = int(W * 0.082)
HORIZ   = int(H * 0.600)


def f(nome, tam):
    return ImageFont.truetype(f"{FONTES}/{nome}", tam)


# ========================================================== MATÉRIA
def suporte(rng):
    base = np.zeros((H, W, 3), dtype=np.float32)
    base[:, :] = PAPEL
    peq = np.random.rand(H // 40 + 2, W // 40 + 2).astype(np.float32)
    nuvem = np.array(Image.fromarray((peq * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC),
                     dtype=np.float32) / 255.0
    base += ((nuvem - 0.5) * 8.5)[:, :, None]
    base += ((np.random.rand(H, W).astype(np.float32) - 0.5) * 11.0)[:, :, None]
    im = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(320):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        ang = rng.uniform(-0.25, 0.25) + (0 if rng.random() < 0.5 else math.pi / 2)
        c = rng.randint(28, 70)
        d.line([x, y, x + math.cos(ang) * c, y + math.sin(ang) * c],
               fill=(120, 112, 100, rng.randint(6, 18)), width=S)
    for _ in range(1400):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        r = rng.uniform(0.6, 2.0) * S
        d.ellipse([x - r, y - r, x + r, y + r], fill=(90, 84, 74, rng.randint(8, 26)))
    v = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(v)
    dv.rectangle([0, 0, W, H], fill=255)
    dv.rectangle([int(W * 0.05), int(H * 0.04), int(W * 0.95), int(H * 0.96)], fill=0)
    v = v.filter(ImageFilter.GaussianBlur(70 * S))
    return Image.composite(Image.new("RGB", (W, H), PAPEL_S), im, v.point(lambda p: int(p * 0.55)))


def mancha(d, rng, cx, cy, raio, alpha, cor=TINTA, lobos=9, irreg=0.42, achata=1.0):
    pts = []
    for i in range(lobos):
        a = 2 * math.pi * i / lobos
        r = raio * (1 + rng.uniform(-irreg, irreg))
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r * achata * rng.uniform(0.72, 1.06)))
    d.polygon(pts, fill=cor + (alpha,))


def aguada(rng, passes, area, cor=TINTA, a=(5, 18), r=(40, 170), blur=(9, 22), achata=1.0):
    l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(l, "RGBA")
    x0, y0, x1, y1 = area
    for _ in range(passes):
        mancha(d, rng, rng.uniform(x0, x1), rng.uniform(y0, y1),
               rng.uniform(*r) * S, rng.randint(*a), cor, achata=achata)
    return l.filter(ImageFilter.GaussianBlur(rng.uniform(*blur) * S))


def textura_massa(cam, rng, mascara, densidade=90):
    """Dá corpo de aguada a uma massa sólida: veios claros e poças escuras dentro dela."""
    t = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(t)
    bb = mascara.getbbox()
    if not bb:
        return cam
    x0, y0, x1, y1 = bb
    for _ in range(densidade):
        cx, cy = rng.uniform(x0, x1), rng.uniform(y0, y1)
        if rng.random() < 0.45:                      # veio claro (dry brush)
            lar = rng.uniform(30, 190) * S
            alt = rng.uniform(1.2, 4.5) * S
            d.ellipse([cx - lar, cy - alt, cx + lar, cy + alt],
                      fill=PAPEL + (rng.randint(40, 105),))
        else:                                        # poça escura
            mancha(d, rng, cx, cy, rng.uniform(18, 70) * S, rng.randint(30, 78))
    t = t.filter(ImageFilter.GaussianBlur(2.2 * S))
    t.putalpha(Image.composite(t.getchannel("A"), Image.new("L", (W, H), 0), mascara))
    cam.alpha_composite(t)
    return cam


def figura(d, rng, x, base, alt, cor=TINTA, andando=False):
    cab = alt * 0.20
    d.ellipse([x - cab, base - alt, x + cab, base - alt + cab * 2], fill=cor + (255,))
    d.polygon([(x - alt * 0.135, base), (x - alt * 0.105, base - alt + cab * 1.85),
               (x, base - alt + cab * 1.55), (x + alt * 0.105, base - alt + cab * 1.85),
               (x + alt * 0.135, base)], fill=cor + (255,))
    if andando:
        d.line([x, base - alt * 0.02, x - alt * 0.16, base + alt * 0.02], fill=cor + (255,), width=int(2.4 * S))
    d.ellipse([x - alt * 0.33, base - 2 * S, x + alt * 0.33, base + alt * 0.055], fill=cor + (55,))


def respingo(im, rng, ate=None):
    ate = ate or HORIZ + H * 0.03
    im = im.convert("RGBA")
    cam = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(cam, "RGBA")
    for _ in range(70):
        x, y = rng.uniform(0, W), rng.uniform(H * 0.05, ate)
        r = rng.uniform(0.8, 3.4) * S
        d.ellipse([x - r, y - r, x + r, y + r], fill=TINTA + (rng.randint(14, 62),))
    im.alpha_composite(cam)
    return im.convert("RGB")


def deriva(im, rng, ox, oy, dx, dy, n=130, acento=None, prob_acento=0.09):
    cam = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(cam, "RGBA")
    for i in range(n):
        t = (i / max(1, n - 1)) ** 1.55
        x = ox + t * dx + rng.uniform(-W * 0.055, W * 0.055)
        y = oy + rng.uniform(-1, 1) * H * 0.22 * (0.35 + t) + t * dy
        if not (MARGEM * 0.8 < x < W - MARGEM * 1.1) or y < H * 0.04 or y > HORIZ - H * 0.01:
            continue
        s = rng.uniform(4, 15) * S * (1.05 - t * 0.45)
        op = int((150 - t * 116) * rng.uniform(0.55, 1.0))
        cor = acento if (acento and rng.random() < prob_acento) else TINTA
        ang = rng.uniform(0, math.pi / 2)
        pts = [(x + math.cos(ang + k * math.pi / 2) * s, y + math.sin(ang + k * math.pi / 2) * s) for k in range(4)]
        if rng.random() < 0.30:
            d.polygon(pts, outline=cor + (op,), width=max(1, int(1.2 * S)))
        else:
            d.polygon(pts, fill=cor + (op,))
    im = im.convert("RGBA")
    im.alpha_composite(cam.filter(ImageFilter.GaussianBlur(0.35 * S)))
    return im.convert("RGB")


def acabamento(im, rng):
    a = np.array(im, dtype=np.float32)
    a += ((np.random.rand(H, W).astype(np.float32) - 0.5) * 6.0)[:, :, None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


# ========================================================== TIPOGRAFIA
def tipografia(im, indice, eixo, tese, dados, fonte_ref):
    d = ImageDraw.Draw(im)
    fm = f("GeistMono-Regular.ttf", int(W * 0.0155))
    ft = f("Gloock-Regular.ttf", int(W * 0.0445))
    fl = f("DMMono-Regular.ttf", int(W * 0.0155))
    fr = f("InstrumentSans-Regular.ttf", int(W * 0.0145))
    h_marc, h_tese, h_dado = int(H * 0.027), int(W * 0.0545), int(H * 0.0225)
    fo1, fo2 = int(H * 0.014), int(H * 0.026)
    bloco = h_marc + len(tese) * h_tese + fo1 + fo2 + len(dados) * h_dado
    y_rod = H - MARGEM - int(W * 0.016)
    topo = HORIZ + int(H * 0.062)
    y = max(topo, min(y_rod - int(H * 0.036) - bloco, topo + int(H * 0.010)))
    d.text((MARGEM, y), f"ÍNDICE  {indice}  ·  {eixo.upper()}", font=fm, fill=(112, 106, 96))
    y += h_marc + fo1
    for l in tese:
        d.text((MARGEM, y), l, font=ft, fill=TINTA)
        y += h_tese
    y += fo2
    for l in dados:
        d.text((MARGEM, y), l, font=fl, fill=(88, 84, 76))
        y += h_dado
    d.text((MARGEM, y_rod), fonte_ref, font=fr, fill=(140, 134, 124))
    t = "BRUNO ACKS"
    d.text((W - MARGEM - d.textlength(t, font=fr), y_rod), t, font=fr, fill=(140, 134, 124))
    return im


# ========================================================== CENA: A PONTE
def cena_ponte(rng, acento):
    im = suporte(rng).convert("RGBA")
    im.alpha_composite(aguada(rng, 14, (0, H * 0.10, W, HORIZ - H * 0.05), a=(4, 12), r=(90, 240)))

    # disco do acento, atrás
    disc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dd = ImageDraw.Draw(disc)
    cx, cy, r = W * 0.665, H * 0.235, W * 0.115
    for k in range(4):
        dd.ellipse([cx - r + rng.uniform(-3, 3) * S, cy - r + rng.uniform(-3, 3) * S,
                    cx + r + rng.uniform(-3, 3) * S, cy + r + rng.uniform(-3, 3) * S],
                   fill=acento + (238 if k == 3 else 90,))
    im.alpha_composite(disc.filter(ImageFilter.GaussianBlur(1.6 * S)))

    # a ponte: máscara do tabuleiro + arco vazado
    masc = Image.new("L", (W, H), 0)
    dm = ImageDraw.Draw(masc)
    deck_y = H * 0.395
    dm.polygon([(W * 0.055, deck_y + H * 0.030), (W * 0.98, deck_y - H * 0.004),
                (W * 0.98, HORIZ), (W * 0.055, HORIZ)], fill=255)
    ax, ay, arx, ary = W * 0.505, HORIZ, W * 0.335, H * 0.150
    dm.ellipse([ax - arx, ay - ary, ax + arx, ay + ary], fill=0)          # vão do arco
    dm.rectangle([0, HORIZ, W, H], fill=0)

    massa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(massa, "RGBA").bitmap((0, 0), masc, fill=TINTA + (232,))
    masc = masc.filter(ImageFilter.GaussianBlur(1.4 * S))
    massa = textura_massa(massa, rng, masc, densidade=210)
    im.alpha_composite(massa.filter(ImageFilter.GaussianBlur(0.6 * S)))

    d = ImageDraw.Draw(im, "RGBA")
    # sólidos sob o arco
    base_s = HORIZ - H * 0.004
    d.rectangle([W * 0.335, base_s - H * 0.052, W * 0.400, base_s], fill=TINTA + (205,))
    d.polygon([(W * 0.470, base_s), (W * 0.535, base_s), (W * 0.5025, base_s - H * 0.058)], fill=TINTA + (185,))
    d.ellipse([W * 0.600, base_s - H * 0.048, W * 0.667, base_s], fill=TINTA + (150,))

    # água: lavagem horizontal + reflexo
    ag = aguada(rng, 26, (0, HORIZ, W, HORIZ + H * 0.055), a=(6, 20), r=(70, 230), blur=(10, 20), achata=0.28)
    im.alpha_composite(ag)
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(26):
        y = rng.uniform(HORIZ - H * 0.002, HORIZ + H * 0.045)
        x0 = rng.uniform(0, W * 0.75)
        comp = rng.uniform(60, 420) * S
        onda = [(x0 + comp * (i / 18), y + math.sin(i * 0.7 + x0) * rng.uniform(0.4, 1.8) * S)
                for i in range(19)]
        d.line(onda, fill=TINTA + (rng.randint(16, 54),),
               width=max(1, int(rng.uniform(0.8, 2.6) * S)), joint="curve")

    # figura caminhando sobre o tabuleiro, contra o disco
    figura(d, rng, W * 0.655, deck_y + H * 0.016, H * 0.056, andando=True)

    im = respingo(im.convert("RGB"), rng, ate=HORIZ + H * 0.03)
    return im


# ========================================================== CENA: O BALÃO
def cena_balao(rng, acento):
    im = suporte(rng).convert("RGBA")
    im.alpha_composite(aguada(rng, 12, (W * 0.10, H * 0.08, W * 0.85, HORIZ), a=(4, 11), r=(80, 200)))

    cx, cy, r = W * 0.435, H * 0.225, W * 0.205

    # esfera: metade escura de aguada, metade clara com meridianos
    masc = Image.new("L", (W, H), 0)
    ImageDraw.Draw(masc).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    esc = Image.new("L", (W, H), 0)
    ImageDraw.Draw(esc).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    ImageDraw.Draw(esc).rectangle([cx, 0, W, H], fill=0)

    massa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(massa, "RGBA").bitmap((0, 0), esc, fill=TINTA + (225,))
    massa = textura_massa(massa, rng, esc, densidade=120)
    im.alpha_composite(massa.filter(ImageFilter.GaussianBlur(0.8 * S)))

    # meridianos e paralelos por cima de toda a esfera
    mer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dm = ImageDraw.Draw(mer, "RGBA")
    for k in range(-4, 5):
        rx = abs(r * k / 4.6)
        if rx < 2:
            dm.line([cx, cy - r, cx, cy + r], fill=TINTA + (120,), width=int(1.4 * S))
        else:
            dm.ellipse([cx - rx, cy - r, cx + rx, cy + r], outline=TINTA + (105,), width=int(1.3 * S))
    for k in range(1, 5):
        yy = cy - r + 2 * r * k / 5
        dx = math.sqrt(max(0.0, r * r - (yy - cy) ** 2))
        dm.line([cx - dx, yy, cx + dx, yy], fill=TINTA + (85,), width=int(1.2 * S))
    dm.ellipse([cx - r, cy - r, cx + r, cy + r], outline=TINTA + (215,), width=int(2.0 * S))
    mer.putalpha(Image.composite(mer.getchannel("A"), Image.new("L", (W, H), 0), masc))
    im.alpha_composite(mer)

    d = ImageDraw.Draw(im, "RGBA")
    # cabo até o chão, com o nó emaranhado
    topo_cabo = cy + r
    chao = HORIZ
    d.line([cx, topo_cabo, cx + W * 0.006, chao], fill=TINTA + (185,), width=int(1.6 * S))
    ny = topo_cabo + (chao - topo_cabo) * 0.34
    pts = []
    for i in range(230):
        a = i * 0.42
        rr = (W * 0.038) * (0.35 + 0.65 * abs(math.sin(i * 0.11)))
        pts.append((cx + math.cos(a) * rr * rng.uniform(0.85, 1.15),
                    ny + math.sin(a * 1.3) * rr * 0.72 * rng.uniform(0.85, 1.15)))
    d.line(pts, fill=TINTA + (155,), width=int(1.5 * S), joint="curve")

    # figura ao pé do cabo
    figura(d, rng, cx - W * 0.055, chao, H * 0.062)

    im = im.convert("RGB")
    im = deriva(im, rng, W * 0.62, H * 0.20, W * 0.30, H * 0.16, n=120, acento=acento, prob_acento=0.12)
    im = respingo(im, rng, ate=HORIZ - H * 0.01)

    # linha de repouso
    d = ImageDraw.Draw(im.convert("RGBA"), "RGBA")
    im = im.convert("RGBA")
    d = ImageDraw.Draw(im, "RGBA")
    pts = [(MARGEM * 0.5 + (W - MARGEM) * (i / 89), HORIZ + rng.uniform(-1.6, 1.6) * S) for i in range(90)]
    d.line(pts, fill=TINTA + (160,), width=max(1, int(1.5 * S)))
    return im.convert("RGB")


# ========================================================== SAÍDA
PECAS = [
    dict(arq="peca-ponte", cena=cena_ponte, semente=7, acento=(186, 78, 50), indice="01",
         eixo="agentes · governança",
         tese=["O agente atravessou.", "A responsabilidade ficou."],
         dados=["um trilho novo   ·   um passivo antigo",
                "quem responde quando o agente decide sozinho?"],
         fonte="MAPA DE PASSIVO POR TRILHO · 05-FRAMEWORKS"),
    dict(arq="peca-balao", cena=cena_balao, semente=19, acento=(46, 84, 132), indice="02",
         eixo="economia de ia",
         tese=["ROI de IA sem custo de", "inferência é fé, não FinOps."],
         dados=["tokens · contexto · cache · latência · volume",
                "o que não medimos, não otimizamos"],
         fonte="DEMONSTRAÇÃO DE RESULTADO DE IA (VCAT) · 05-FRAMEWORKS"),
]

if __name__ == "__main__":
    import sys
    for p in PECAS:
        rng = random.Random(p["semente"])
        np.random.seed(p["semente"])
        im = p["cena"](rng, p["acento"])
        im = acabamento(im, rng)
        im = tipografia(im, p["indice"], p["eixo"], p["tese"], p["dados"], p["fonte"])
        im = im.resize((W // S, H // S), Image.LANCZOS)
        im.save(f"/home/claude/{p['arq']}.png", quality=97)
        print("ok", p["arq"])
