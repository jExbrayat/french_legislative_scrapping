import bs4
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
