from get_statics import scrap_write_commune_results
from utils import get_links_from_csv

communes_links = get_links_from_csv("communes_links.csv")

# TODO: remove debugging
communes_links = communes_links[:10]

for id, link in communes_links:
    scrap_write_commune_results(
        commune_link=link,
        result_table_path=f"scraped_data/results_tables/{id}.csv",
        stats_table_path=f"scraped_data/stats_tables/{id}.csv",
    )
