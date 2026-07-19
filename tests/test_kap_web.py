from data.kap_web_provider import KapWebProvider

provider = KapWebProvider()

items = provider.search("ASELSAN")

print("Bulunan:", len(items))

for item in items:
    print(item["title"])