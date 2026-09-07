#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cabeçalho ilustrado do One Banking AI — mesma gramática do Registro Húmido (papel, nanquim, aguada,
silhueta pequena, um acento). Gera PNG largo para o PDF e uma faixa de papel para fundo."""
import random, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

PAPEL   = (233, 229, 219)
PAPEL_S = (216, 210, 197)
TINTA   = (22, 22, 21)

def papel(W, H, rng, vinheta=True):
    base = np.zeros((H, W, 3), dtype=np.float32); base[:, :] = PAPEL
    peq = np.random.rand(H // 40 + 2, W // 40 + 2).astype(np.float32)
    nuvem = np.array(Image.fromarray((peq * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), dtype=np.float32) / 255.0
    base += ((nuvem - 0.5) * 8.5)[:, :, None]
    base += ((np.random.rand(H, W).astype(np.float32) - 0.5) * 11.0)[:, :, None]
    im = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(int(W * H / 9000)):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        ang = rng.uniform(-0.25, 0.25) + (0 if rng.random() < 0.5 else math.pi / 2)
        c = rng.randint(20, 60)
        d.line([x, y, x + math.cos(ang) * c, y + math.sin(ang) * c], fill=(120, 112, 100, rng.randint(6, 18)), width=2)
    for _ in range(int(W * H / 2200)):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        r = rng.uniform(0.8, 3.0)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(90, 84, 74, rng.randint(8, 26)))
    if vinheta:
        v = Image.new("L", (W, H), 0); dv = ImageDraw.Draw(v)
        dv.rectangle([0, 0, W, H], fill=255)
        dv.rectangle([int(W * 0.03), int(H * 0.08), int(W * 0.97), int(H * 0.92)], fill=0)
        v = v.filter(ImageFilter.GaussianBlur(min(W, H) * 0.12))
        im = Image.composite(Image.new("RGB", (W, H), PAPEL_S), im, v.point(lambda p: int(p * 0.5)))
    return im

def mancha(d, rng, cx, cy, raio, alpha, cor=TINTA, lobos=9, irreg=0.42, achata=1.0):
    pts = []
    for i in range(lobos):
        a = 2 * math.pi * i / lobos
        r = raio * (1 + rng.uniform(-irreg, irreg))
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r * achata * rng.uniform(0.72, 1.06)))
    d.polygon(pts, fill=cor + (alpha,))

def aguada(W, H, rng, passes, area, cor=TINTA, a=(5, 18), r=(40, 170), blur=(9, 22), achata=1.0):
    l = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(l, "RGBA")
    x0, y0, x1, y1 = area
    for _ in range(passes):
        mancha(d, rng, rng.uniform(x0, x1), rng.uniform(y0, y1), rng.uniform(*r), rng.randint(*a), cor, achata=achata)
    return l.filter(ImageFilter.GaussianBlur(rng.uniform(*blur)))

def figura(d, x, base, alt, cor=TINTA):
    cab = alt * 0.20
    d.ellipse([x - cab, base - alt, x + cab, base - alt + cab * 2], fill=cor + (255,))
    d.polygon([(x - alt * 0.135, base), (x - alt * 0.105, base - alt + cab * 1.85), (x, base - alt + cab * 1.55),
               (x + alt * 0.105, base - alt + cab * 1.85), (x + alt * 0.135, base)], fill=cor + (255,))
    d.ellipse([x - alt * 0.33, base - 2, x + alt * 0.33, base + alt * 0.055], fill=cor + (55,))

def cabecalho(dest, W=2400, H=760, semente=69, acento=(46, 84, 132)):
    """Cena: o horizonte de uma cidade-arquivo — blocos uniformes de aguada, uma torre com o módulo aceso,
    figura pequena no cais, fragmentos derivando. Sem texto: a tipografia entra pelo HTML."""
    rng = random.Random(semente); np.random.seed(semente)
    im = papel(W, H, rng).convert("RGBA")
    HORIZ = int(H * 0.74)
    im.alpha_composite(aguada(W, H, rng, 18, (0, H * 0.05, W, HORIZ - H * 0.05), a=(4, 11), r=(120, 380), blur=(14, 30)))

    # blocos: skyline de arquivos
    masc = Image.new("L", (W, H), 0); dm = ImageDraw.Draw(masc)
    x = W * 0.06
    blocos = []
    while x < W * 0.94:
        lar = rng.uniform(W * 0.035, W * 0.09)
        alt = rng.uniform(H * 0.12, H * 0.42)
        if rng.random() < 0.18: alt *= 1.35
        y0 = HORIZ - alt
        j = lambda: rng.uniform(-2.2, 2.2)
        dm.polygon([(x + j(), y0 + j()), (x + lar + j(), y0 + j()), (x + lar + j(), HORIZ + j()), (x + j(), HORIZ + j())], fill=255)
        blocos.append((x, y0, x + lar, HORIZ)); x += lar + rng.uniform(W * 0.006, W * 0.03)
    massa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(massa, "RGBA").bitmap((0, 0), masc, fill=TINTA + (222,))
    # textura interna
    t = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dt = ImageDraw.Draw(t)
    for _ in range(420):
        bx0, by0, bx1, by1 = rng.choice(blocos)
        cx, cy = rng.uniform(bx0, bx1), rng.uniform(by0, by1)
        if rng.random() < 0.5:
            lar, alt = rng.uniform(20, 160), rng.uniform(1.2, 4.0)
            dt.ellipse([cx - lar, cy - alt, cx + lar, cy + alt], fill=PAPEL + (rng.randint(40, 105),))
        else:
            mancha(dt, rng, cx, cy, rng.uniform(10, 45), rng.randint(30, 78))
    t = t.filter(ImageFilter.GaussianBlur(2.0))
    t.putalpha(Image.composite(t.getchannel("A"), Image.new("L", (W, H), 0), masc.filter(ImageFilter.GaussianBlur(1.2))))
    massa.alpha_composite(t)
    im.alpha_composite(massa.filter(ImageFilter.GaussianBlur(0.7)))

    d = ImageDraw.Draw(im, "RGBA")
    # janelas: linhas horizontais claras nos blocos mais altos
    for (bx0, by0, bx1, by1) in blocos:
        if by1 - by0 > H * 0.28:
            n = int((by1 - by0) / (H * 0.055))
            for k in range(1, n):
                yy = by0 + k * (by1 - by0) / n
                d.line([(bx0 + 6, yy), (bx1 - 6, yy)], fill=PAPEL + (rng.randint(28, 60),), width=2)
    # o módulo aceso (acento) num bloco alto, fora do centro
    altos = [b for b in blocos if b[3] - b[1] > H * 0.30 and b[0] > W * 0.55]
    b = altos[0] if altos else max(blocos, key=lambda b: b[3] - b[1])
    bw = b[2] - b[0]
    mx0, my0 = b[0] + bw * 0.18, b[1] + (b[3] - b[1]) * 0.22
    mx1, my1 = mx0 + bw * 0.42, my0 + H * 0.045
    face = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(face, "RGBA")
    df.polygon([(mx0, my0), (mx1, my0 + 1), (mx1 - 1, my1), (mx0 + 1, my1 + 1)], fill=acento + (238,))
    for _ in range(10):
        vy = rng.uniform(my0, my1); lar = rng.uniform(4, 14)
        cxm = rng.uniform(mx0, mx1)
        df.ellipse([cxm - lar, vy - 1, cxm + lar, vy + 1], fill=PAPEL + (rng.randint(14, 36),))
    im.alpha_composite(face.filter(ImageFilter.GaussianBlur(0.5)))

    # água/cais: lavagem horizontal e a linha de repouso
    im.alpha_composite(aguada(W, H, rng, 30, (0, HORIZ, W, HORIZ + H * 0.08), a=(6, 20), r=(80, 300), blur=(10, 20), achata=0.25))
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(30):
        y = rng.uniform(HORIZ, HORIZ + H * 0.09); x0 = rng.uniform(0, W * 0.8); comp = rng.uniform(80, 500)
        onda = [(x0 + comp * (i / 18), y + math.sin(i * 0.7 + x0) * rng.uniform(0.4, 1.8)) for i in range(19)]
        d.line(onda, fill=TINTA + (rng.randint(16, 54),), width=int(rng.uniform(1, 3)), joint="curve")
    pts = [(W * 0.03 + W * 0.94 * (i / 89), HORIZ + rng.uniform(-1.6, 1.6)) for i in range(90)]
    d.line(pts, fill=TINTA + (160,), width=2)
    # figura no cais, à esquerda
    figura(d, W * 0.145, HORIZ, H * 0.10)
    # fragmentos derivando para a direita, alto
    for i in range(90):
        t = (i / 89) ** 1.5
        fx = W * 0.30 + t * W * 0.62 + rng.uniform(-W * 0.03, W * 0.03)
        fy = H * 0.20 - t * H * 0.12 + rng.uniform(-H * 0.06, H * 0.06)
        if not (W * 0.05 < fx < W * 0.95) or fy < H * 0.04: continue
        s = rng.uniform(4, 13) * (1.05 - t * 0.4); op = int((140 - t * 100) * rng.uniform(0.55, 1.0))
        cor = acento if rng.random() < 0.08 else TINTA
        ang = rng.uniform(0, math.pi / 2)
        poly = [(fx + math.cos(ang + k * math.pi / 2) * s, fy + math.sin(ang + k * math.pi / 2) * s) for k in range(4)]
        if rng.random() < 0.3: d.polygon(poly, outline=cor + (op,), width=1)
        else: d.polygon(poly, fill=cor + (op,))
    # respingos
    for _ in range(90):
        x, y = rng.uniform(0, W), rng.uniform(H * 0.05, HORIZ)
        r = rng.uniform(0.8, 3.0)
        d.ellipse([x - r, y - r, x + r, y + r], fill=TINTA + (rng.randint(14, 62),))
    out = im.convert("RGB")
    a = np.array(out, dtype=np.float32); a += ((np.random.rand(H, W).astype(np.float32) - 0.5) * 6.0)[:, :, None]
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out.save(dest, quality=92)
    return dest

def fundo_papel(dest, W=1240, H=1754, semente=5):
    rng = random.Random(semente); np.random.seed(semente)
    papel(W, H, rng, vinheta=False).save(dest, quality=80)
    return dest

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    cabecalho(os.path.join(here, "cabecalho.png"))
    fundo_papel(os.path.join(here, "papel.jpg"))
    print("ok")
