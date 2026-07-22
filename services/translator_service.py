"""
Translator Service
BIST AI LAB v9.1
"""

from __future__ import annotations

import re


class TranslatorService:

    DICTIONARY = {

        "contract": "sözleşme",
        "agreement": "anlaşma",
        "signed": "imzaladı",
        "signs": "imzaladı",
        "order": "sipariş",
        "orders": "siparişler",
        "export": "ihracat",
        "investment": "yatırım",
        "investments": "yatırımlar",
        "profit": "kâr",
        "loss": "zarar",
        "growth": "büyüme",
        "record": "rekor",
        "award": "ödül",
        "partnership": "ortaklık",
        "cooperation": "iş birliği",
        "acquisition": "satın alma",
        "merger": "birleşme",
        "shares": "hisseler",
        "share": "hisse",
        "stock": "hisse",
        "dividend": "temettü",
        "buyback": "geri alım",
        "earnings": "finansal sonuçlar",
        "revenue": "gelir",
        "sales": "satışlar",
        "factory": "fabrika",
        "production": "üretim",
        "facility": "tesis",
        "air": "hava",
        "air defense": "hava savunma",
        "defense": "savunma",
        "military": "askeri",
        "nato": "NATO",
        "drone": "İHA",
        "market": "pazar",
        "technology": "teknoloji",
        "communication": "haberleşme",
        "system": "sistem",
        "systems": "sistemler",
        "global": "küresel",
        "company": "şirket",
        "billion": "milyar",
        "million": "milyon",
        "reaches": "ulaşıyor",
        "reach": "ulaşacak",
        "expands": "genişletiyor",
        "expand": "genişletmek",
        "ready": "hazır",
        "within": "içinde",
        "years": "yıl",
    }

    def translate(self, text: str):

        result = text

        for en, tr in sorted(
            self.DICTIONARY.items(),
            key=lambda x: len(x[0]),
            reverse=True,
        ):

            result = re.sub(
                rf"\b{re.escape(en)}\b",
                tr,
                result,
                flags=re.IGNORECASE,
            )

        return result

    def simple_summary(self, text: str):

        return self.translate(text)

    def market_comment(self, text: str):

        t = text.lower()

        if any(x in t for x in [
            "contract",
            "agreement",
            "order",
            "export",
            "investment",
            "growth",
            "profit",
            "award",
            "partnership",
            "cooperation",
        ]):

            return "Haber şirket açısından olumlu değerlendirilebilir."

        if any(x in t for x in [
            "loss",
            "lawsuit",
            "fraud",
            "bankruptcy",
            "delay",
            "debt",
            "default",
        ]):

            return "Haber kısa vadede hisse üzerinde baskı oluşturabilir."

        return "Haberin piyasa etkisi nötr görünmektedir."