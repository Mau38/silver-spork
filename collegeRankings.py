from bs4 import BeautifulSoup
import requests
import re

BASE_RANKING_URL: str = "https://www.niche.com/colleges/search/best-colleges/?page="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
}
def getHTMLDocument(url: str) -> str:
    return requests.get(url, headers=HEADERS).text 

if __name__ == "__main__":
    for i in range(1,112):
        ranking_page: str = getHTMLDocument(BASE_RANKING_URL+str(i))
        soup = BeautifulSoup(ranking_page, 'html.parser')
        results = soup.find_all(attrs={"aria-describedby": re.compile(r"search-result__description--\d+")})

        for result in results:
            print(result.get("href"))
