from data.google_news_provider import GoogleNewsProvider

provider = GoogleNewsProvider()

news = provider.search("ASELSAN")

print(f"Haber Sayısı: {len(news)}")

for article in news[:5]:
    print(article["title"])