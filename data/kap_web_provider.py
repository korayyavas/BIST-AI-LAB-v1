import requests
from bs4 import BeautifulSoup


class KapWebProvider:

    BASE_URL = "https://www.kap.org.tr/tr/BildirimAra"

    def search(self, keyword: str):

        try:

            response = requests.get(
                self.BASE_URL,
                params={
                    "text": keyword
                },
                timeout=20,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            results = []

            for link in soup.select("a"):

                text = link.get_text(strip=True)

                href = link.get("href")

                if not text:
                    continue

                if keyword.lower() in text.lower():

                    results.append({

                        "title": text,

                        "url": "https://www.kap.org.tr" + href
                        if href and href.startswith("/")
                        else href

                    })

            return results[:20]

        except Exception:

            return []