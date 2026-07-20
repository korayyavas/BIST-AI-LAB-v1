"""
News Cache Test
BIST AI LAB v8
"""

from time import perf_counter

from services.news_service import NewsService


def main():

    service = NewsService()

    t0 = perf_counter()

    news1 = service.get_news("ASELS.IS")

    t1 = perf_counter()

    news2 = service.get_news("ASELS.IS")

    t2 = perf_counter()

    print()

    print("FIRST :", round(t1 - t0, 3), "sec")
    print("SECOND:", round(t2 - t1, 3), "sec")

    print()

    print("NEWS COUNT :", len(news2))

    if news2:
        print(news2[0].title)


if __name__ == "__main__":
    main()