"""Pull recent reviews for a Steam app and chart the share of positive reviews per week.
Usage: APIFY_TOKEN=... python 01_review_sentiment.py 730   (730 = Counter-Strike 2)"""
import sys
import pandas as pd
from common import run_actor

app_id = sys.argv[1] if len(sys.argv) > 1 else "730"
rows = [r for r in run_actor({"appIds": [app_id], "maxReviewsPerApp": 2000, "language": "english", "filter": "recent"}) if r.get("type") == "review"]
df = pd.DataFrame(rows)
df["created"] = pd.to_datetime(df.timestampCreated, unit="s")
weekly = df.set_index("created").resample("W").agg(reviews=("reviewId", "count"), positive=("votedUp", "mean")).round(3)
print(weekly.tail(12))
print(f"\nOverall positive share: {df.votedUp.mean():.1%} across {len(df):,} reviews")
print("Median playtime at review (hours):", round(df.playtimeAtReview.median() / 60, 1))
