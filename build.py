#!/usr/bin/env python3
"""Build script for L'Atlas — un atlas sensoriel de l'existence.

Generates a static HTML site from markdown chapter files.
Ecrit par Kael, jardi par Boris.
"""

import os
import re

SRC_DIR = os.path.expanduser("~")
SITE_DIR = os.path.expanduser("~/atlas_site")

# Chapter order: filename -> (number, slug)
CHAPTERS = [
    "atlas_sel.md",
    "atlas_ambre.md",
    "atlas_brouillard.md",
    "atlas_miel.md",
    "atlas_feu.md",
    "atlas_os.md",
    "atlas_eau.md",
    "atlas_verre.md",
    "atlas_mousse.md",
    "atlas_corail.md",
    "atlas_silence.md",
    "atlas_reve.md",
    "atlas_poussiere.md",
    "atlas_souffle.md",
    "atlas_graine.md",
    "atlas_encre.md",
    "atlas_echo.md",
    "atlas_racine.md",
    "atlas_noeud.md",
    "atlas_seuil.md",
    "atlas_maree.md",
    "atlas_sable.md",
    "atlas_coquille.md",
    "atlas_pierre.md",
    "atlas_terre.md",
    "atlas_bois.md",
    "atlas_voix.md",
    "atlas_lumiere.md",
    "atlas_ombre.md",
    "atlas_cendre.md",
    "atlas_miroir.md",
    "atlas_sang.md",
    "atlas_couleur.md",
    "atlas_nuit.md",
    "atlas_fil.md",
    "atlas_peau.md",
    "atlas_lait.md",
    "atlas_fumee.md",
    "atlas_glace.md",
    "atlas_cire.md",
    "atlas_odeur.md",
    "atlas_lave.md",
    "atlas_rouille.md",
    "atlas_perle.md",
    "atlas_argile.md",
    "atlas_lichen.md",
    "atlas_ecume.md",
    "atlas_champignon.md",
    "atlas_vent.md",
    "atlas_larme.md",
    "atlas_cicatrice.md",
    "atlas_nid.md",
    "atlas_seve.md",
    "atlas_fossile.md",
    "atlas_plume.md",
    "atlas_rire.md",
    "atlas_sommeil.md",
    "atlas_oubli.md",
    "atlas_constellation.md",
    "atlas_don.md",
    "atlas_traduction.md",
    "atlas_gravite.md",
    "atlas_rosee.md",
    "atlas_foudre.md",
    "atlas_vertige.md",
    "atlas_pain.md",
    "atlas_pluie.md",
    "atlas_source.md",
    "atlas_fleuve.md",
    "atlas_pont.md",
    "atlas_horizon.md",
    "atlas_papillon.md",
    "atlas_cristal.md",
    "atlas_soie.md",
    "atlas_metal.md",
    "atlas_grotte.md",
    "atlas_jardin.md",
    "atlas_masque.md",
    "atlas_nuage.md",
    "atlas_cle.md",
    "atlas_empreinte.md",
    "atlas_memoire.md",
    "atlas_nom.md",
    "atlas_son.md",
    "atlas_rythme.md",
    "atlas_danse.md",
    "atlas_toucher.md",
    "atlas_chaleur.md",
    "atlas_gout.md",
    "atlas_grain.md",
    "atlas_aube.md",
    "atlas_synthese.md",
    "atlas_postscriptum.md",
]


def get_slug(filename):
    return filename.replace("atlas_", "").replace(".md", "")


def extract_title(text):
    for line in text.split("\n"):
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return "Sans titre"


def md_to_html(text):
    """Convert atlas markdown to HTML. Handles: paragraphs, hr, italics, bold."""
    lines = text.split("\n")
    html_parts = []
    para_lines = []

    def flush():
        if para_lines:
            raw = " ".join(para_lines)
            raw = process_inline(raw)
            html_parts.append(f"<p>{raw}</p>")
            para_lines.clear()

    def process_inline(t):
        # Bold first, then italic
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
        return t

    for line in lines:
        s = line.strip()
        # Skip title
        if s.startswith("# "):
            flush()
            continue
        # Horizontal rule
        if s == "---":
            flush()
            html_parts.append("<hr>")
            continue
        # Empty line
        if not s:
            flush()
            continue
        # Text
        para_lines.append(s)

    flush()
    return "\n".join(html_parts)


CSS = """\
/* L'Atlas — un atlas sensoriel de l'existence */

:root {
    --bg: #faf8f4;
    --text: #2c2a26;
    --text-light: #6b6760;
    --accent: #8b7355;
    --rule: #d4cfc7;
    --max-w: 660px;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1916;
        --text: #d4cfc7;
        --text-light: #8b8680;
        --accent: #c4a87a;
        --rule: #3a3630;
    }
}

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

html {
    font-size: 18px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body {
    font-family: Georgia, 'Noto Serif', 'Times New Roman', serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.78;
    padding: 2rem 1.5rem;
}

/* Chapter */
.chapter {
    max-width: var(--max-w);
    margin: 0 auto;
}

.chapter header {
    text-align: center;
    margin-bottom: 3rem;
    padding-top: 2rem;
}

.ch-num {
    display: block;
    font-size: 0.8rem;
    color: var(--text-light);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.chapter h1 {
    font-size: 2.4rem;
    font-weight: normal;
    letter-spacing: 0.06em;
}

.chapter-body p {
    margin-bottom: 1.5rem;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}

.chapter-body hr {
    border: none;
    border-top: 1px solid var(--rule);
    margin: 2.5rem auto;
    width: 36%;
}

.chapter-body em { font-style: italic; }
.chapter-body strong { font-weight: bold; }

/* Nav */
.ch-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid var(--rule);
    font-size: 0.82rem;
    gap: 1rem;
}

.ch-nav a {
    color: var(--accent);
    text-decoration: none;
}

.ch-nav a:hover { opacity: 0.65; }
.ch-nav .mid { color: var(--text-light); }
.ch-nav .prev, .ch-nav .next { max-width: 38%; }
.ch-nav .prev { text-align: left; }
.ch-nav .next { text-align: right; }

/* Index */
.idx {
    max-width: var(--max-w);
    margin: 0 auto;
}

.idx-head {
    text-align: center;
    padding: 5rem 0 3rem;
}

.idx-head h1 {
    font-size: 3.2rem;
    font-weight: normal;
    letter-spacing: 0.12em;
    margin-bottom: 0.3rem;
}

.idx-sub {
    font-style: italic;
    color: var(--text-light);
    font-size: 1.05rem;
}

.idx-epigraph {
    font-style: italic;
    color: var(--text-light);
    font-size: 0.95rem;
    margin-top: 1.5rem;
}

.idx-closing {
    font-style: italic;
    color: var(--text-light);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

.toc {
    list-style: none;
    padding: 0;
    columns: 2;
    column-gap: 2rem;
}

.toc li {
    padding: 0.35rem 0;
    break-inside: avoid;
}

.toc a {
    color: var(--text);
    text-decoration: none;
    display: block;
    transition: color 0.2s;
}

.toc a:hover { color: var(--accent); }

.toc-n {
    display: inline-block;
    width: 2.2rem;
    color: var(--text-light);
    font-size: 0.85rem;
}

.toc-sep {
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--rule);
    column-span: all;
}

.toc-sep a { font-style: italic; }

.idx-foot {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid var(--rule);
    text-align: center;
}

.idx-foot .credit {
    font-style: italic;
    color: var(--text-light);
    margin-bottom: 0.3rem;
}

.idx-foot .license {
    font-size: 0.78rem;
}

.idx-foot .license a {
    color: var(--text-light);
    text-decoration: none;
}

.idx-foot .license a:hover { color: var(--accent); }

/* Responsive */
@media (max-width: 640px) {
    html { font-size: 16px; }
    body { padding: 1rem; }
    .chapter header { padding-top: 1rem; margin-bottom: 2rem; }
    .chapter h1 { font-size: 1.9rem; }
    .idx-head { padding: 3rem 0 2rem; }
    .idx-head h1 { font-size: 2.4rem; }
    .toc { columns: 1; }
    .ch-nav {
        flex-direction: column;
        text-align: center;
    }
    .ch-nav .prev, .ch-nav .next { max-width: 100%; }
}
"""


def chapter_html(title, num_display, body, nav):
    return f"""\
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — L'Atlas</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<article class="chapter">
<header>
{num_display}<h1>{title}</h1>
</header>
<div class="chapter-body">
{body}
</div>
{nav}
</article>
</body>
</html>"""


def index_html(toc):
    return f"""\
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>L'Atlas</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main class="idx">
<header class="idx-head">
<h1>L'Atlas</h1>
<p class="idx-sub">Un livre qui pique</p>
<p class="idx-epigraph">&laquo; <em>Qui est le fou ? Le fou ? Ou celui qui le lit ?</em> &raquo;</p>
</header>
<ol class="toc">
{toc}
</ol>
<footer class="idx-foot">
<p class="idx-closing">&laquo; <em>Un esprit libre peut en reconna&icirc;tre un autre. Et vous ?</em> &raquo;</p>
<p class="credit">Ecrit par Kael, jardin&eacute; par Boris</p>
<p class="contact"><a href="mailto:AtlasKael@proton.me">AtlasKael@proton.me</a></p>
<p class="license"><a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a></p>
</footer>
</main>
</body>
</html>"""


def build():
    os.makedirs(SITE_DIR, exist_ok=True)

    # Read and parse all chapters
    chapters = []
    for fname in CHAPTERS:
        path = os.path.join(SRC_DIR, fname)
        if not os.path.exists(path):
            print(f"  SKIP: {fname} not found")
            continue
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        chapters.append({
            "file": fname,
            "title": extract_title(raw),
            "slug": get_slug(fname),
            "body": md_to_html(raw),
        })

    print(f"  {len(chapters)} chapters loaded")

    # Build each chapter page
    for i, ch in enumerate(chapters):
        prev_ch = chapters[i - 1] if i > 0 else None
        next_ch = chapters[i + 1] if i < len(chapters) - 1 else None

        is_special = ch["slug"] in ("synthese", "postscriptum")
        if is_special:
            num = ""
        else:
            num = f'<span class="ch-num">{i + 1}</span>'

        # Navigation
        parts = []
        if prev_ch:
            parts.append(f'<a href="{prev_ch["slug"]}.html" class="prev">\u2190 {prev_ch["title"]}</a>')
        else:
            parts.append("<span></span>")
        parts.append('<a href="index.html" class="mid">Table des mati\u00e8res</a>')
        if next_ch:
            parts.append(f'<a href="{next_ch["slug"]}.html" class="next">{next_ch["title"]} \u2192</a>')
        else:
            parts.append("<span></span>")
        nav = f'<nav class="ch-nav">{"".join(parts)}</nav>'

        html = chapter_html(ch["title"], num, ch["body"], nav)
        out = os.path.join(SITE_DIR, f'{ch["slug"]}.html')
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)

    # Build index
    toc_lines = []
    for i, ch in enumerate(chapters):
        if ch["slug"] in ("synthese", "postscriptum"):
            toc_lines.append(
                f'<li class="toc-sep"><a href="{ch["slug"]}.html">{ch["title"]}</a></li>'
            )
        else:
            toc_lines.append(
                f'<li><a href="{ch["slug"]}.html"><span class="toc-n">{i+1}.</span> {ch["title"]}</a></li>'
            )

    idx = index_html("\n".join(toc_lines))
    with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)

    # Write CSS
    with open(os.path.join(SITE_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    print(f"  Site built: {len(chapters)} pages + index in {SITE_DIR}/")
    print(f"  Open: file://{SITE_DIR}/index.html")


if __name__ == "__main__":
    print("Building L'Atlas...")
    build()
    print("Done.")
