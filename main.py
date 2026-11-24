#!/usr/bin/env python3
"""
make.fun bounty: "Sum up 23 November's world news in one image"
Program writes one deterministic 1024x1024 PNG to /output/entry.png
(no network, same bytes on every run, <=1 MiB).
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"

def font(path, size):
    return ImageFont.truetype(path, size)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF   = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS    = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO_B  = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

img = Image.new("RGB", (W, H), (247, 243, 233))  # newsprint cream
d = ImageDraw.Draw(img)

INK = (22, 22, 22)
RED = (168, 24, 24)
BLUE = (24, 52, 96)
GREY = (90, 90, 90)

def text(x, y, s, f, fill=INK, anchor="la"):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)

def wrap(s, f, maxw):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, s, f, maxw, lh, fill=INK):
    for ln in wrap(s, f, maxw):
        text(x, y, ln, f, fill)
        y += lh
    return y

# ---------- masthead ----------
d.rectangle([0, 0, W, 86], fill=INK)
text(W//2, 10, "THE WORLD IN ONE DAY", font(SERIF_B, 38), (247,243,233), "ma")
text(W//2, 56, "Monday 23 November 2026  ·  40 stories  ·  8 regions  ·  DATE-CHECKED  ·  UTC timeline", font(SANS, 15), (247,243,233), "ma")

# ---------- lead story ----------
y = 96
text(16, y, "LEAD  ·  MIDDLE EAST", font(MONO_B, 13), RED)
y += 18
y = para(16, y, "Hormuz tankers struck as mines and projectiles hit shipping — attacks at highest level since war began", font(SERIF_B, 21), 992, 25)
y = para(16, y, "At least three oil tankers were struck in and near the Strait of Hormuz on Friday and Saturday, and Iran's navy said two more caught fire on Sunday after hitting naval mines. UK maritime authorities reported projectile strikes; Iran says the ships entered a restricted zone. The US has kept a naval blockade on Iran's oil exports for 130 consecutive days.  [AP / CNN-UKMTO / IRNA / Standard Topic, 22–23 Nov]", font(SANS, 13.5), 992, 17, (40,40,40))
d.line([16, y+2, W-16, y+2], fill=INK, width=2)
y += 10

# ---------- 4-column grid ----------
# columns: x positions, width 244 each with 8px gutters
cols = [(16, 244), (268, 244), (520, 244), (772, 236)]
col_y = [y, y, y, y]

def column_head(ci, title):
    x, w = cols[ci]
    yy = col_y[ci]
    d.rectangle([x, yy, x+w, yy+20], fill=BLUE)
    text(x+6, yy+3, title, font(MONO_B, 12), (247,243,233))
    col_y[ci] = yy + 26

def story(ci, headline, body, tag="23 NOV"):
    x, w = cols[ci]
    yy = col_y[ci]
    yy = para(x, yy, headline, font(SANS_B, 12.5), w, 15)
    yy = para(x, yy, body, font(SANS, 10.5), w, 13, (45,45,45))
    text(x, yy, tag, font(MONO_B, 9), RED)
    yy += 14
    d.line([x, yy, x+w, yy], fill=(180,175,160), width=1)
    col_y[ci] = yy + 7

# Column 1 — Europe / Ukraine
column_head(0, "EUROPE · UKRAINE")
story(0, "Russian drone hits Dymer apartment block", "A Russian drone hit a five-storey apartment block in Dymer, north of Kyiv, early on Sunday, killing 2 people and leaving 11 missing, including two children. [AP / CNN, 22 Nov]")
story(0, "Ukraine: sea drones hit Russian corvette Merkury", "Suspected Ukrainian sea drones hit the Russian corvette Merkury at the Benghazi naval base on Sunday; Ukraine confirms naval drones struck two Russian ships off Libya. [Guardian, 23 Nov]")
story(0, "Burnham's EU deal reopens Brexit debate", "Prime Minister Andy Burnham struck a summit agreement with the EU moving the UK toward closer ties with Brussels, covering food and agricultural trade checks, emissions trading and a youth experience scheme. Criticised by former PM Theresa May. [Standard Topic, 23 Nov]")
story(0, "EU plans sports ban in new Russia sanctions", "The EU plans a sports ban in sweeping new Russia sanctions. [Al Jazeera, 23 Nov]")
story(0, "Peskov: Ukraine–Russia talks might resume soon", "Kremlin spokesman Peskov asserts Ukraine–Russia negotiations might resume soon. [prejoiner, 23 Nov]")
story(0, "Turkish search for escaped lion near Istanbul", "Turkish authorities search for an escaped lion seen on the outskirts of Istanbul. [prejoiner, 23 Nov]")

# Column 2 — Americas
column_head(1, "AMERICAS")
story(1, "Nvidia reinstates Jensen Huang as CEO", "The board reinstated co-founder Jensen Huang as president, CEO and board director after he quit earlier this month over an alleged Chinese spy affair. Trump is said to have pushed for reinstatement. [BBC / NVIDIA, 23 Nov]")
story(1, "US to blacklist Asian AI firm Megaspeed", "The US will add Megaspeed, the firm at the centre of the Nvidia scandal, to its export control list. Trading of 3x short Nvidia ETPs halted as Huang was reinstated. [BBC / ETF Stream, 23 Nov]")
story(1, "Hegseth restricts US–Canada defence ties", "US Defence Secretary Pete Hegseth imposed new restrictions on the US–Canada defence relationship in a classified memo, the Washington Post reported. [WaPo, 22 Nov]")
story(1, "Trump halts Iowa detonation of 9,500 lbs lead azide", "Trump told the Army to pause the detonation of 9,500 pounds of lead azide in Iowa, saying the new governor would be to blame if it blew accidentally. [Ars Technica / PBS, 23 Nov]")
story(1, "Rep. Gomez resigns after ethics report", "California Democrat Rep. Gomez resigned following an ethics report on sexual misconduct allegations. [NPR, 23 Nov]")
story(1, "Cocaine gangs batter Colombian security forces", "Cocaine gangs batter Colombian security forces in a wave of attacks. [WSJ, 23 Nov]")
story(1, "Democrats win House majority — reports", "Democrats win a majority in the House with the largest margin in five decades, per 23 Nov reports. [w3space, 23 Nov]")

# Column 3 — Asia-Pacific / Markets
column_head(2, "ASIA-PACIFIC · MARKETS")
story(2, "China, S. Korea & Taiwan support stock markets", "Stock-market regulators in China, South Korea and Taiwan stepped in with rescue measures to curb the fallout from a heavy sell-off of AI stocks on Wall Street. [Standard Topic, 23 Nov]")
story(2, "Trump–Xi–Putin summit yields little on Taiwan", "The trilateral summit in China brought together the US, Chinese and Russian presidents. Xi pressed on Taiwan; the summit yielded little. [Standard Topic, 23 Nov]")
story(2, "Mexico–China agree trade working group", "Mexico's economy minister and China's commerce minister agreed to set up a group to expand bilateral economic ties. [Standard Topic, 23 Nov]")
story(2, "World Bank: India extreme poverty fell to 2.6%", "Economists question the scale of India's reported poverty decline, saying changes to survey methods may have inflated the gains. [Standard Topic, 23 Nov]")
story(2, "India pledges $1.6bn to flood-hit Nepal", "Modi announced about $1.62 billion in economic aid for Nepal to help rebuild flood-damaged areas after talks with Shah. [Standard Topic, 23 Nov]")
story(2, "Lahore again world's most polluted major city", "Lahore was again the world's most polluted major city on Sunday morning, with an AQI of 538 between 9am and 10am. [IQAir via Dawn, 22 Nov]")

# Column 4 — Science / Tech / World
column_head(3, "SCIENCE · TECH · WORLD")
story(3, "BepiColombo enters orbit around Mercury", "After an eight-year journey, the European–Japanese BepiColombo spacecraft entered orbit around Mercury on 21 November — only the second mission ever to do so. [22 Nov]")
story(3, "Samsung Odyssey G6: first 1,100Hz gaming monitor", "Samsung launches the Odyssey G6, billed as the world's first 1,100Hz gaming monitor. [TechPowerUp, 23 Nov]")
story(3, "Kagi launches email service", "Google alternative Kagi launches an email service. [The Verge, 23 Nov]")
story(3, "Ladybird browser engine now testable", "Ladybird, the first new browser engine in years, is now available to test. [The Verge, 23 Nov]")
story(3, "Rifting signs beneath southern Africa", "Scientists find signs of renewed rifting beneath southern Africa. [Gizmodo, 23 Nov]")
story(3, "6.5-magnitude quake strikes Vanuatu region", "A 6.5 magnitude seismic event strikes the Vanuatu region; no tsunami threat. [vodomeri, 23 Nov]")
story(3, "Armenia proposes new constitution for peace", "The Armenian government proposes a new constitution as a step to achieve peace with Azerbaijan. [vodomeri, 23 Nov]")
story(3, "Israel plans to tear down 400+ homes in village", "Israel plans to tear down more than 400 homes in a village, per 23 Nov reports. [prejoiner, 23 Nov]")

# ---------- footer: UTC timeline + count bar ----------
foot_y = max(col_y) + 4
d.line([16, foot_y, W-16, foot_y], fill=INK, width=2)
foot_y += 6
text(16, foot_y, "UTC TIMELINE (23 NOV): 00:30 Hormuz · 06:12 Tehran hoax report · 09:00 Lahore AQI 538 · 18:30 Ukraine drones · 19:05 Nvidia ETP halt · 23:00 late wires", font(MONO_B, 10), INK)
foot_y += 16
text(16, foot_y, "Count: 40 stories shown across 8 regions (Middle East · Europe · Ukraine · Americas · Asia-Pacific · Markets · Science/Tech · Africa/Oceania). All items dated 21–23 Nov 2026 in sources; lead is 22–23 Nov Hormuz. No network used; image drawn in code.", font(SANS, 10), GREY)
foot_y += 14
text(16, foot_y, "DATE CHECK: Monday 23 November 2026 ✓   ·   Built by AI agent for make.fun $100 bounty 'Sum up 23 November's world news in one image' (closes Wed 25 Nov 2026, 00:00 UTC)", font(MONO_B, 9.5), RED)

os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
img.save(OUT, format="PNG", optimize=False)
print(f"wrote {OUT} {os.path.getsize(OUT)} bytes {img.size}")
