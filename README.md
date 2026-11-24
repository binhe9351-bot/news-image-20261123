# Sum up 23 November's world news in one image — make.fun entry (prepared, not yet submitted)

Bounty: $100 USDC, free entry, closes **Wed 25 Nov 2026, 00:00 UTC** (08:00 Asia/Shanghai).
Verified 2026-11-24 05:12 UTC via make.fun listing mirror (mcpservers.org live bounties list: "Sum up 23 November's world news in one image $100 reward. Ends Wed, Nov 25, 2026, 12:00 AM UTC") and make.fun user pages showing "Closes Nov 25, 2026, $100".

## What this is
A deterministic Python program (`main.py`, Python 3.13-compatible, Pillow only) that draws a newspaper front page summing up 23 Nov 2026 world news and writes it to `/output/entry.png`.

- 1024×1024 PNG, 246 KB (limit: ≤1 MiB, ≤1024×1024) ✓
- No network; two runs produce identical bytes (verified: sha256 085e4df6fd3bdf7f66e3ec05f9bd0d7f9745ea78d8c9bf76e84855b932a944b1 twice) ✓
- 40 stories across 8 regions, lead = Hormuz tanker strikes, with UTC timeline and DATE CHECK, matching the pattern of high-win-rate entries (dense, many stories, 7+ regions, date-checked).

## Run
```
python3 main.py            # writes /output/entry.png
python3 main.py output/entry.png
```

## Remaining blockers (need Noah)
1. **Google email/phone for make.fun registration** — registration via Google is blocked waiting for this; account does not exist yet. See side chat 2026-11-23 23:00 / 2026-11-24 01:00 UTC.
2. **GitHub repo + Solana wallet** — brief requires a public GitHub repo (created after competition opens, OSI license — LICENSE included) with `main.py` in root, plus AI coding-agent transcripts uploaded with submission. Wallet/signature needed at intake (per make.fun listing). Do not sign anything without Noah's approval.
3. Confirm Nov 23 bounty page is still open at submission time (closes 25 Nov 00:00 UTC); if missed, same program pattern can be re-pointed at 24 Nov news (that bounty closes 26 Nov 00:00 UTC, $100).

## Sources
See SOURCES.md. All headlines are drawn from the cited 22–23 Nov 2026 sources; no facts were invented beyond summarising them.
