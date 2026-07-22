from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class KAPProvider:

    def __init__(self):
        self.source = "KAP"


    def fetch(self, symbol: str):

        symbol = symbol.upper()

        logger.info(
            "KAP provider request: %s",
            symbol
        )

        if symbol != "ASELS":
            return []


        return [
            {
                "title": "ASELSAN yeni sözleşme bildirimi",
                "summary": "Savunma sistemleri kapsamında yeni sipariş sözleşmesi imzalanmıştır.",
                "category": "CONTRACT",
                "published_at": datetime.utcnow().isoformat(),
                "url": ""
            }
        ]


    def normalize(self, items, symbol):

        result = []

        for item in items:

            result.append(
                {
                    "symbol": symbol.upper(),
                    "title": item.get("title", ""),
                    "summary": item.get("summary", ""),
                    "category": item.get("category", "OTHER"),
                    "published_at": item.get(
                        "published_at",
                        datetime.utcnow().isoformat()
                    ),
                    "url": item.get("url", "")
                }
            )

        return result


kap_provider = KAPProvider()