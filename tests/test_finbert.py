from services.sentiment_service import SentimentService

ai = SentimentService()

texts = [
    "ASELSAN signs 1.47 billion euro air defense contract",
    "Company reports record quarterly profit",
    "Company files for bankruptcy",
]

for t in texts:
    print(t)
    print(ai.analyze(t))
    print()