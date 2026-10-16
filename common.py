"""Run the Apify Actor and iterate its dataset items."""
import os
from apify_client import ApifyClient

ACTOR = "best_apis/steam-reviews-scraper"


def run_actor(run_input: dict, max_cost_usd: float = 1.0):
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(run_input=run_input, max_total_charge_usd=max_cost_usd)
    return client.dataset(run.default_dataset_id).iterate_items()
