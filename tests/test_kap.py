from data.kap_provider import KapProvider

kap = KapProvider()

items = kap.get_latest()

print("KAP Sayısı:", len(items))

for item in items[:10]:
    print(item["title"])