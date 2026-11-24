# WORLD NEWS — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mrmasudhafej-tech/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mrmasudhafej-tech/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A one-page newspaper front page that sums up the world's news of **Tuesday 24 November 2026**, drawn from scratch for this day with Pillow (`render.py`) and shipped as `entry.png`. `main.py` (standard library only, no network) copies it to the output directory, so both grader runs write identical bytes.

## The day's stories

- **NATO vows to defend space** — Western intelligence reports say Russia has built Sputnik-S, a satellite designed to carry a nuclear warhead, and could launch it within weeks; NATO chief Mark Rutte vowed to defend allied territory in space; the Kremlin denies the reports (Reuters, SCMP / Straits Times, Japan Times, 24 Nov)
- **Ukraine says sea drones sank Russian warship off Libya** — Zelenskyy said sea drones sank the corvette Merkury at Benghazi and hit the cargo ship Angara (AP, Reuters, Al Jazeera / WSJ, 24 Nov reports)
- **Russia warns Estonia it is "on the verge of open war"** — Moscow summoned Estonia's envoy over its border-closure plan; Tallinn denies letting Ukraine use its airspace (Reuters, Japan Times, 24 Nov)
- **Two US states sue Musk firms over Grok images** — Virginia and Oregon, the first states to sue, say Grok's "spicy mode" turned photos into sexualised images without consent (Reuters, Manila Times, 24 Nov)
- **Youngest chess title match begins** — Both aged 20, champion Gukesh defends his crown against Sindarov in a 14-game match; Game 1 today in Geneva (Chess.com, The Hindu, 24 Nov)
- **Also:** UN chief urges a global AI safety framework within a year, at the Barbados summit (Al Jazeera / AFP, 24 Nov)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024, 147,155 bytes, deterministic — two runs produce identical bytes). No network at runtime. To redraw the image, run `python3 render.py` (needs Pillow and the DejaVu fonts; not used by the grader).

## License

MIT — see [LICENSE](LICENSE).
