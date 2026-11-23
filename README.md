# THE WORLD — 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Erwinsp27/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Erwinsp27/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

One newspaper front page summing up the world's news of Monday,
23 November 2026, rendered as a single 1024x1024 PNG. The masthead
reads "THE WORLD" and the dateline sits directly beneath it, so the
day the image sums up is named on the page itself.

## The stories

- **Lead:** the COP31 climate talks in Antalya ended without an
  agreement — the draft "Antalya Pact" was rejected because it did
  not mention fossil fuels, after record overtime.
- **Second story:** Iran struck a civilian industrial site in Bahrain
  and two tankers near the Strait of Hormuz; Gulf states condemned
  the attacks.
- **Grid:** the cartel boss captured in Guasave, Mexico; a Russian
  drone hitting an apartment block in Dymer near Kyiv; a Russian
  ballistic missile striking Kryvyi Rih; and the Trump–Xi–Putin
  meeting in Shenzhen agreeing to start nuclear risk-reduction talks.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library and copies the
bundled `entry.png` byte for byte to the output directory, so every
run produces identical output. It needs no network access.

## License

MIT — see [LICENSE](LICENSE).
