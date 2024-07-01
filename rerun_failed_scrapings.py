import json
import csv
from scraping_pipeline import scrap_and_write

# Load logs file
with open("logs_01-07-1h30.json", "r") as logs:
    logs = json.load(logs)

fails = [key for key, value in logs.items() if value == "Scraping failed"]

# Get links of which the scraping failed
failed_links = []
with open("communes_links.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip header
    for row in reader:
        if row[4] in fails:  # If geographic code is in the failed scrapings list
            failed_links.append(
                [row[4], row[7]]
            )  # Retrieve link and official geographic code


scrap_and_write(
    failed_links, save_folder="./scraped_data", logs_path="logs_01-07-15h30.json"
)
