from get_statics import get_links_to_circonscriptions, get_tables_from_circ
from utils import html_table_to_csv
import os

table_names = ["resultat_tour_2", "stats_tour_2", "resultat_tour_1", "stats_tour_1"]

# Generate the list of French departments
dept_numbers = [str(i).zfill(3) for i in range(1, 97)]

for dept in dept_numbers:  # Iterate over departments
    circ_links = get_links_to_circonscriptions(dept)

    for circ_number, circ_link in enumerate(
        circ_links
    ):  # Iterate over circonscriptions
        tables = get_tables_from_circ(circ_link)

        for table, table_name in zip(tables, table_names):

            # Write files
            # Create directory
            save_folder = f"scraped_data/{dept}/circonscription_{circ_number}/"
            os.makedirs(save_folder, exist_ok=True)

            html_table_to_csv(table, csv_filepath=f"{save_folder}/{table_name}.csv")
