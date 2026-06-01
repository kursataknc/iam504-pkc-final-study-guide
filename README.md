# IAM504 — Public Key Cryptography · Final Study Guide

Worked solutions to the Boneh–Shoup *A Graduate Course in Applied Cryptography*
exercises flagged as "exam-similar" for the IAM504 final, presented as a single,
self-contained **interactive HTML study guide**.

## 📖 How to use

Just open **[`IAM504_study_guide.html`](IAM504_study_guide.html)** in any browser
(double-click it, or download and open). No server or build step needed — math is
rendered with MathJax (loaded from a CDN, so the first open needs internet).

Features:
- Sidebar navigation by chapter + live search (try `DDH` or `12.3`)
- Click **Show solution** on any problem to reveal the full proof
- Per-problem **"mastered"** checkbox with a progress bar (saved in your browser)

## ✍️ What's covered

32 exercises across 6 chapters, each with an **Idea** (intuition) and a full
**Solution** in the course recitation's reduction style ("elementary wrapper"
arguments, explicit advantage bounds, game hops):

| Ch | Topic | Problems |
|----|-------|----------|
| 10 | Public-key tools (DL/CDH/DDH) | 10.1, 10.2, 10.3, 10.17 |
| 11 | Public-key encryption | 11.1, 11.2, 11.3, 11.5, 11.6, 11.13 |
| 12 | CCA-secure encryption | 12.1, 12.2, 12.3, 12.11, 12.22, 12.23 |
| 13 | Digital signatures | 13.1, 13.2, 13.3, 13.5, 13.13, 13.15 |
| 14 | Signatures from one-way functions | 14.1, 14.5, 14.8, 14.9, 14.13 |
| 15 | Elliptic curves & pairings | 15.1, 15.2, 15.4, 15.7, 15.16 |

(Problems already covered in the recitation — 10.21, 11.8, 12.20, 13.6, 15.3 — are
noted but not repeated.)

## 🔧 Rebuilding

The guide is assembled from per-chapter fragments (`sol_ch*.html`) by `build.py`:

```bash
python3 build.py   # → IAM504_study_guide.html
```

`STYLE_GUIDE.md` documents the formatting/notation conventions the solutions follow.

## ⚠️ Notes & disclaimer

- The **textbook itself is not included** here. Boneh & Shoup publish it for free at
  <https://toc.cryptobook.us/> — get the official PDF there.
- Problem statements are paraphrased; solutions are original write-ups for study
  purposes. These are study aids, not official solutions — verify before relying on
  them, especially the trickier reductions (14.5(b), 15.16).
