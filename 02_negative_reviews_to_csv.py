"""Export negative reviews with the most helpful votes: a quick 'what do players hate' list."""
import sys
import pandas as pd
from common import run_actor

app_id = sys.argv[1] if len(sys.argv) > 1 else "730"
rows = [r for r in run_actor({"appIds": [app_id], "maxReviewsPerApp": 500, "language": "english", "filter": "all", "reviewType": "negative"}) if r.get("type") == "review"]
df = pd.DataFrame(rows).sort_values("votesUp", ascending=False)
df[["votesUp", "playtimeForever", "review", "url"]].head(100).to_csv("negative_reviews.csv", index=False)
print(df[["votesUp", "review"]].head(5).to_string(index=False, max_colwidth=100))
