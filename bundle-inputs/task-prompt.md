# Task: news-image-20261119 — Sum up 19 November's world news in one image

Build an entry for the make.fun bounty `news-image-20261119` ($250 total, 1st $50, no entry fee). Entries close 2026-11-21 09:00 KST. The kit is at `~/workspace/makefun/news-image-20261119-kit/` — read `competition.yaml` and `RULES.txt` first; they are the authority.

## What to build

A program at the root of `~/workspace/makefun/news-image-20261119/` named `main.py` (Python 3.13) that writes one image to `/output/entry.png` (outside the grader, `MAKEFUN_OUTPUT_DIR` stands in for `/output`). The program runs with **no network** in the grader sandbox, max 60 seconds per run, twice, and both runs must produce the same result — so keep it deterministic and simple: the repository holds the finished image as `entry.png`, and `main.py` copies it to the output path with the standard library only.

The image is the real work:

- **One image, 1024x1024 PNG, at most 1 MiB.** It sums up the world's news of **Thursday 19 November 2026**.
- **It must name the day clearly**: the date "19 November 2026" prominent in the image. An image that names no day, or shows news from before 13 November 2026, loses.
- **Breadth**: the day's most consequential stories, across regions and fields — not one country or one beat. Aim for 5–6 stories.
- **It must read**: a viewer who missed the day can tell what happened from the image alone. Each story clear from its picture and a short label. Nothing self-contradictory, implausible, or false.
- **Faithful**: what happened, as reported. No hype, no speculation presented as fact.
- **Craft**: one clear composition, clean, legible at about 300 pixels across, no smears or garbled text.

## Research the news first — and check the FIRST-REPORT date

Use web search (news) to find what actually happened or was first reported on 19 November 2026. Verify every story you put in the image: it must be a real event of that day, with the facts as reported. Do not invent events, quotes, or numbers. If you cannot verify a story, leave it out.

**Hard lesson from the previous days' entries: a story that was merely covered on the day does NOT count if it was first reported the day before.** For every story you pick, confirm the event happened OR was first reported on 19 November 2026 — check the publication date of the earliest report, not just that outlets covered it on the 19th. If a story's first report was 18 November or earlier, do not use it. Prefer wire and named outlets (AP, Reuters, AFP, BBC, NDTV) and 2+ independent sources per story. There are many AI-slop articles about the day: investigate, doubt, avoid traps.

Lead source only (never sole source): YouTube channel `UC6dN6Rilzh9KmzymxnZGslg` (센서스튜디오 / Sensor Studio). Check its RSS for a 19 November video and use it only as a lead.

Write the research log at `~/workspace/makefun/news-image-20261119-research.md`: the chosen stories with their sources and first-report dates, plus a REJECTED list of stories you considered and excluded (with why).

## How to draw the image

Draw a clean infographic with Python PIL (check it is installed; use fonts available on this machine, e.g. DejaVu). Design: a masthead with the date, then 5–6 story blocks, each with a short headline and a one-line summary. Use simple shapes and colour blocks, not photographs — a photo you cannot verify risks showing something false. Every word in the image must be spelled correctly and render crisply. After drawing it, open the PNG and look at it yourself to check legibility and layout before you finish.

## Repo requirements (do these, but do NOT create the GitHub repo or submit — I do that)

- `~/workspace/makefun/news-image-20261119/` is the entry directory. Initialise git there and set the local identity (user.name ryukiheun, user.email ryukiheun@gmail.com).
- `README.md` follows the kit's readme_template exactly (title, three badges verbatim, description paragraph, `## Run it` block with the run command, separator, referral footer). Owner ryukiheun, repo news-image-20261119, referral code r5cs55h2.
- `LICENSE` is MIT with an SPDX-License-Identifier line.
- `draw_image.py` (Pillow) regenerates `entry.png`; `main.py` only copies the finished `entry.png` to the output directory. Explain that in the README description.
- Commit everything; the working tree must be clean when you finish.

Report back in Korean: the 6 stories chosen (with sources), entry.png sha256 + size, determinism check result, commit sha. Do NOT create a GitHub repo, push, bundle, or submit — I do that.
