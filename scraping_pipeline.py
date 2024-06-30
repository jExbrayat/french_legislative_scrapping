from get_statics import scrap_write_commune_results
from utils import get_links_from_csv
import json

communes_links = get_links_from_csv("communes_links.csv")

logs = {}  # Init logs dictionary
for id, link in communes_links:
    try:
        scrap_write_commune_results(
            commune_link=link,
            result_table_path=f"scraped_data/results_tables/{id}.csv",
            stats_table_path=f"scraped_data/stats_tables/{id}.csv",
        )
        logs[id] = "Data scraped successfully"
    except:
        logs[id] = "Scraping failed"

with open("logs.json", "w") as logs_file:
    json.dump(logs, logs_file)
