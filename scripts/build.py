"""Regenerate tokens.css, tailwind-theme.css and theme.ts from tokens.json.

Run from anywhere:  python3 scripts/build.py
"""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ROOT
os.makedirs(OUT, exist_ok=True)
t = json.load(open(os.path.join(ROOT, "tokens.json")))
colors = t["color"]["tokens"]

def raw(tok, th):
    v = tok["value"]
    return v if isinstance(v, str) else v.get(th, v["marketing"])
def css(val):
    return re.sub(r"\{([^}]+)\}", r"var(--\1)", val)
byname = {c["name"]: c for c in colors}
def resolve(val, th):
    m = re.fullmatch(r"\{([^}]+)\}", val)
    return resolve(raw(byname[m.group(1)], th), th) if m else val

HDR = "/* PAL Design System — generated from tokens.json (scripts/build.py). Do not edit by hand; change tokens.json and regenerate. */\n"

# ── tokens.css ──────────────────────────────────────────────
L = [HDR, "@import url(\"https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700&family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500;600;700&display=swap\");\n",
     "/* Primitives + marketing semantics (default scope). */", ":root, [data-app=\"marketing\"] {"]
for c in colors: L.append(f"  --{c['name']}: {css(raw(c,'marketing'))};")
L.append("}\n")
L.append("/* Driver app: semantic overrides only. Primitives never change per product. */")
L.append("[data-app=\"driver\"] {")
for c in colors:
    v = c["value"]
    if isinstance(v, dict) and "driver" in v and v["driver"] != v["marketing"]:
        L.append(f"  --{c['name']}: {css(v['driver'])};")
L.append("}\n")
L.append("/* Apps set text in Geist; the marketing site in Barlow. */")
L.append("[data-app=\"driver\"] { font-family: var(--font-app); }\n")
L.append(":root {")
for fam in ["spacing", "radius", "shadow", "duration", "easing"]:
    L.append(f"  /* {fam} */")
    for c in t[fam]["tokens"]: L.append(f"  --{c['name']}: {c['value']};")
for k, s in t["type"]["families"].items(): L.append(f"  --font-{k}: {s};")
L.append("}\n")
L.append("/* Type styles */")
for g in t["type"]["groups"]:
    fam = g["family"]
    for s in g["styles"]:
        d = [f"font-family: var(--font-{s.get('family', fam)})", f"font-size: {s['fontSize']}", f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
        if s.get("letterSpacing"): d.append(f"letter-spacing: {s['letterSpacing']}")
        if "eyebrow" in s["name"]: d.append("text-transform: uppercase")
        L.append(f".text-{s['name']} {{ {'; '.join(d)}; }}")
L.append("@media (max-width: 768px) { .text-section-heading { font-size: 30px; line-height: 36px; } }")
L.append(".text-hero-headline { font-size: clamp(2.8rem, 6vw, 4.5rem); }")
open(OUT + "/tokens.css", "w").write("\n".join(L) + "\n")

# ── tailwind-theme.css (Tailwind v4 + shadcn, driver app) ─────
TW = [HDR,
"/* Tailwind v4 theme for PAL products.\n   Usage (driver web app, src/index.css):\n     @import \"tailwindcss\";\n     @import \"../../pal-design-system/tailwind-theme.css\";\n   and put data-app=\"driver\" on <html>.\n   Apps use Geist; Barlow is for the marketing site only. */\n",
"@import \"./tokens.css\";\n",
"@theme inline {",
"  /* Literal stacks: tokens.css declares --font-sans too, and a self-reference would be a cycle. */", f"  --font-sans: {t['type']['families']['app']};", f"  --font-heading: {t['type']['families']['app']};", f"  --font-mono: {t['type']['families']['mono']};",
"",
"  /* shadcn semantic colours mapped to PAL tokens */",
"  --color-background: var(--bg-app);",
"  --color-foreground: var(--text-primary);",
"  --color-card: var(--bg-surface);",
"  --color-card-foreground: var(--text-primary);",
"  --color-popover: var(--bg-app);",
"  --color-popover-foreground: var(--text-primary);",
"  --color-primary: var(--accent);",
"  --color-primary-foreground: var(--on-accent);",
"  --color-secondary: var(--bg-elevated);",
"  --color-secondary-foreground: var(--text-primary);",
"  --color-muted: var(--bg-elevated);",
"  --color-muted-foreground: var(--text-muted);",
"  --color-accent: var(--accent-fill);",
"  --color-accent-foreground: var(--accent-text);",
"  --color-destructive: var(--destructive);",
"  --color-border: var(--border);",
"  --color-input: var(--border);",
"  --color-ring: var(--focus);",
"",
"  /* Brand scales as utilities: bg-husk-400, text-cod-700 ... */"]
for c in colors:
    if c["name"].startswith(("cod-", "husk-")): TW.append(f"  --color-{c['name']}: var(--{c['name']});")
TW.append("")
TW.append("  /* Status pills and tones: bg-pill-new-bg, text-tone-warn-fg ... */")
for c in colors:
    if c["name"].startswith(("pill-", "tone-")): TW.append(f"  --color-{c['name']}: var(--{c['name']});")
TW.append("")
TW.append("  /* Semantic spacing: p-app-card, gap-app-gutter, h-app-bar-h ... */")
for c in t["spacing"]["tokens"]:
    n = c["name"]
    if n.startswith("container-"): TW.append(f"  --{n}: {c['value']};")
    elif not n.startswith("sp-"): TW.append(f"  --spacing-{n}: {c['value']};")
TW.append("")
TW.append("  /* Radius by role: rounded-control, rounded-app-card, rounded-sheet, rounded-card, rounded-cta.\n     sm / md / full are left to Tailwind so shadcn primitives keep their current corners. */")
for c in t["radius"]["tokens"]:
    if c["name"] in ("radius-sm", "radius-md", "radius-full"): continue
    TW.append(f"  --radius-{c['name'].replace('radius-','')}: {c['value']};")
TW.append("")
TW.append("  /* Shadow: shadow-lifted, shadow-gold ... */")
for c in t["shadow"]["tokens"]: TW.append(f"  --shadow-{c['name'].replace('shadow-','')}: {c['value']};")
TW.append("")
TW.append("  /* Type: text-app-body, text-eyebrow ... */")
for g in t["type"]["groups"]:
    for s in g["styles"]:
        n = s["name"]
        TW.append(f"  --text-{n}: {s['fontSize']};")
        TW.append(f"  --text-{n}--line-height: {s['lineHeight']};")
        TW.append(f"  --text-{n}--font-weight: {s['fontWeight']};")
        if s.get("letterSpacing"): TW.append(f"  --text-{n}--letter-spacing: {s['letterSpacing']};")
TW.append("")
for c in t["duration"]["tokens"]: TW.append(f"  --{c['name']}: {c['value']};")
for c in t["easing"]["tokens"]: TW.append(f"  --{c['name']}: {c['value']};")
TW.append("}")
TW.append("\n/* Status pill palette as data attributes (matches the shipped driver CSS). */")
for k in ["new","accepted","ontheway","onlocation","pob","complete","cancelled","noshow"]:
    TW.append(f"[data-pill=\"{k}\"] {{ background-color: var(--pill-{k}-bg); color: var(--pill-{k}-fg); }}")
for k in ["ok","warn","info","danger","husk"]:
    TW.append(f"[data-tone=\"{k}\"] {{ background-color: var(--tone-{k}-bg); color: var(--tone-{k}-fg); }}")
open(OUT + "/tailwind-theme.css", "w").write("\n".join(TW) + "\n")

# ── theme.ts (React Native / Expo) ────────────────────────────
def tsobj(d, ind="  "):
    return "{\n" + "".join(f"{ind}{json.dumps(k) if '-' in k else k}: {json.dumps(v)},\n" for k, v in d.items()) + ind[:-2] + "}"
def camel(n): return re.sub(r"-([a-z0-9])", lambda m: m.group(1).upper(), n)
prim = {"cod": {c["name"][4:]: c["value"] for c in colors if c["name"].startswith("cod-")},
        "husk": {c["name"][5:]: c["value"] for c in colors if c["name"].startswith("husk-")}}
def sem(th):
    out = {}
    for c in colors:
        n = c["name"]
        if n.startswith(("cod-", "husk-")): continue
        out[camel(n)] = resolve(raw(c, th), th)
    return out
ts = [HDR.replace("/*", "/**").replace(" */", "\n */"),
"export const Palette = {",
"  cod: " + tsobj(prim["cod"], "    ") + ",",
"  husk: " + tsobj(prim["husk"], "    ") + ",",
"} as const;\n",
"/** Semantic colours per product. The native driver app uses `driver`. */",
"export const Colors = {",
"  marketing: " + tsobj(sem("marketing"), "    ") + ",",
"  driver: " + tsobj(sem("driver"), "    ") + ",",
"} as const;\n",
"export type ThemeColor = keyof typeof Colors.driver;\n",
"/** Apps use Geist. Load with expo-font: @expo-google-fonts/geist and @expo-google-fonts/geist-mono. */",
"export const Fonts = {",
"  regular: 'Geist_400Regular',", "  medium: 'Geist_500Medium',", "  semibold: 'Geist_600SemiBold',", "  bold: 'Geist_700Bold',", "  mono: 'GeistMono_500Medium',",
"} as const;\n"]
px = lambda v: float(v[:-2]) if isinstance(v, str) and v.endswith("px") else v
ts.append("export const Spacing = " + tsobj({camel(c["name"]): px(c["value"]) for c in t["spacing"]["tokens"]}) + " as const;\n")
ts.append("export const Radius = " + tsobj({camel(c["name"].replace("radius-", "")): px(c["value"]) for c in t["radius"]["tokens"]}) + " as const;\n")
typ = {}
for g in t["type"]["groups"]:
    for s in g["styles"]:
        fs = px(s["fontSize"]); lh = s["lineHeight"]
        lhv = px(lh) if isinstance(lh, str) else round(fs * lh, 1)
        e = {"fontSize": fs, "lineHeight": lhv, "fontWeight": str(s["fontWeight"])}
        if s.get("letterSpacing"): e["letterSpacing"] = round(float(s["letterSpacing"].replace("em", "")) * fs, 2)
        typ[camel(s["name"])] = e
ts.append("export const Type = {\n" + "".join(f"  {k}: {json.dumps(v)},\n" for k, v in typ.items()) + "} as const;\n")
ts.append("export const MaxContentWidth = 520;")
open(OUT + "/theme.ts", "w").write("\n".join(ts) + "\n")

pass
print(os.listdir(OUT))
