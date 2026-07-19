from transformers import pipeline


class SentimentService:

    POSITIVE_WORDS = [
        "contract",
        "agreement",
        "deal",
        "export",
        "order",
        "investment",
        "capacity",
        "growth",
        "profit",
        "record",
        "award",
        "expands",
        "expansion",
        "partnership",
        "cooperation",
        "nato",
        "defense",
        "air defense",
        "production",
        "signed",
        "signs",
        "new project",
        "new business",
        "new order",
        "dividend",
        "buyback",
    ]

    NEGATIVE_WORDS = [
        "loss",
        "bankruptcy",
        "lawsuit",
        "fine",
        "investigation",
        "fraud",
        "default",
        "downgrade",
        "recall",
        "crisis",
        "delay",
        "cancelled",
        "terminated",
        "debt",
        "risk",
    ]

    def __init__(self):

        self.model = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert",
        )

    def analyze(self, text: str):

        result = self.model(text[:512])[0]

        sentiment = result["label"].upper()
        confidence = round(result["score"] * 100, 2)

        title = text.lower()

        bonus = 0

        for word in self.POSITIVE_WORDS:
            if word in title:
                bonus += 15

        for word in self.NEGATIVE_WORDS:
            if word in title:
                bonus -= 20

        if sentiment == "POSITIVE":
            score = 80

        elif sentiment == "NEGATIVE":
            score = 20

        else:
            score = 50

        score += bonus

        score = max(0, min(score, 100))

        if score >= 70:
            sentiment = "POSITIVE"

        elif score <= 30:
            sentiment = "NEGATIVE"

        else:
            sentiment = "NEUTRAL"

        return {
            "sentiment": sentiment,
            "confidence": confidence,
            "score": round(score, 2),
        }