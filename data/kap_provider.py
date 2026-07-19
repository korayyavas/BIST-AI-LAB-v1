import requests
import xml.etree.ElementTree as ET


class KapProvider:

    RSS_URL = "https://www.kap.org.tr/tr/api/disclosures/rss"

    def get_latest(self):

        try:

            response = requests.get(
                self.RSS_URL,
                timeout=20
            )

            response.raise_for_status()

            root = ET.fromstring(response.content)

            items = []

            for item in root.findall(".//item"):

                items.append({

                    "title": item.findtext("title", ""),

                    "link": item.findtext("link", ""),

                    "description": item.findtext("description", ""),

                    "pubDate": item.findtext("pubDate", "")

                })

            return items

        except Exception:

            return []