import csv


def html_table_to_csv(html_table, csv_filepath):
    # # Parse the HTML table
    # soup = BeautifulSoup(html_table, "html.parser")
    # table = soup.find("table", class_="table")
    table = html_table

    # Extract headers
    headers = []
    for th in table.find("thead").find_all("th"):
        headers.append(th.get_text(strip=True))

    # Extract rows
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        row = []
        for td in tr.find_all("td"):
            row.append(td.get_text(strip=True))
        rows.append(row)

    # Write to CSV
    with open(csv_filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def get_links_from_csv(csv_path: str) -> list[str]:

    communes_links = []
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            communes_links.append(row[7])

    return communes_links
