"""
İş Yatırım Provider Test
"""

from research.providers.isyatirim_provider import IsYatirimProvider


def main():

    provider = IsYatirimProvider()

    reports = provider.get_reports("ASELS")

    print()

    print("REPORT COUNT :", len(reports))

    print()

    for report in reports[:10]:

        print(report["title"])

        print(report["url"])

        print()


if __name__ == "__main__":
    main()