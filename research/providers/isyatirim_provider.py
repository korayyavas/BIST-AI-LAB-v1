"""
İş Yatırım Research Provider
BIST AI LAB v7
"""

from __future__ import annotations

import requests
from bs4 import BeautifulSoup


class IsYatirimProvider:

    BASE_URL = "https://www.isyatirim.com.tr"

    SEARCH_URL = (
        "https://www.isyatirim.com.tr/tr-tr/analiz/"
        "Pages/arastirma-raporlari.aspx"
    )

    def get_reports(self, symbol: str):

        try:

            r = requests.get(
                self.SEARCH_URL,
                timeout=20,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
            )

            soup = BeautifulSoup(
                r.text,
                "html.parser",
            )

            reports = []

            for a in soup.find_all("a", href=True):

                href = a["href"]

                text = a.get_text(
                    " ",
                    strip=True,
                )

                if symbol.upper() not in text.upper():
                    continue

                if ".pdf" not in href.lower():
                    continue

                if href.startswith("/"):

                    href = self.BASE_URL + href

                reports.append(
                    {
                        "broker": "İş Yatırım",
                        "title": text,
                        "url": href,
                    }
                )

            return reports

        except Exception as e:

            print("İş Yatırım:", e)

            return []