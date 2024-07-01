from get_statics import scrap_write_commune_results
from utils import get_links_from_csv
import json


def scrap_and_write(
    communes_links: list[list], logs_path: str, save_folder: str
) -> None:

    logs = {}  # Init logs dictionary
    for id, link in communes_links:
        try:
            scrap_write_commune_results(
                commune_link=link,
                result_table_path=f"{save_folder}/results_tables/{id}.csv",
                stats_table_path=f"{save_folder}/stats_tables/{id}.csv",
            )
            print(f"{id} scraped successfully")
            logs[id] = "Data scraped successfully"
        except:
            print(f"{id} scraping failed")
            logs[id] = "Scraping failed"

    with open(logs_path, "w") as logs_file:
        json.dump(logs, logs_file)
