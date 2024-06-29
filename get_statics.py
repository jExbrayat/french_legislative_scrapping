import requests
from bs4 import BeautifulSoup


def get_links_to_circonscriptions(dept_number: str) -> list[str]:

    source_uri = "https://mobile.interieur.gouv.fr/fr/Elections/Les-resultats/Legislatives/elecresult__legislatives-2022/(path)/legislatives-2022/"
    get_dept = requests.get(f"{source_uri}/{dept_number}/index.html")  # Get document

    dept_html = get_dept.text
    dept_html_soup = BeautifulSoup(dept_html, "html.parser")  # Parse html document

    find_circ_hrefs = dept_html_soup.find(
        "p", {"align": "left"}
    )  # Find the p tag containing all the links to circonscriptions

    get_circ_a_tags = find_circ_hrefs.find_all("a")  # Get list of 'a' tags
    get_circ_hrefs = [a_tag["href"] for a_tag in get_circ_a_tags]

    # Get links to each circonscription
    # A href value is in the following format: ../dept_number/dept_number-circ_number
    get_circ_hrefs_links = [
        f"{source_uri}/{path[2:]}" for path in get_circ_hrefs
    ]  # Exclude ".." from the string

    return get_circ_hrefs_links


def get_tables_from_circ(circ_link: str) -> BeautifulSoup:

    request_response = requests.get(circ_link)
    circ_table_static = request_response.text
    circ_table_soup = BeautifulSoup(circ_table_static, "html.parser")

    find_tables = circ_table_soup.find_all("table")

    return find_tables
