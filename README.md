# Steam reviews analysis: Python examples

Examples for the [**Steam Reviews Scraper**](https://apify.com/best_apis/steam-reviews-scraper) Apify Actor (public Steam store reviews and app details, no login).

[![Steam Reviews Scraper on Apify](https://apify.com/actor-badge?actor=best_apis/steam-reviews-scraper)](https://apify.com/best_apis/steam-reviews-scraper)

| Script | What it does |
|---|---|
| `01_review_sentiment.py` | Weekly positive-review share and playtime for any app ID |
| `02_negative_reviews_to_csv.py` | Most helpful negative reviews to CSV |

```bash
pip install -r requirements.txt
export APIFY_TOKEN=...
python 01_review_sentiment.py 730
```
MIT licensed examples. Not affiliated with Valve.
