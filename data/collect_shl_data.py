# data/collect_shl_data.py
import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_catalog():
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    for link in soup.find_all('a', href=True):
        if '/product-catalog/view/' in link['href']:
            data.append({
                'name': link.get_text(strip=True),
                'url': 'https://www.shl.com' + link['href']
            })

    with open("data/shl_assessments.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url"])
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Scraped {len(data)} assessments.")

if __name__ == "__main__":
    scrape_catalog()
