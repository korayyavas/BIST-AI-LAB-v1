
"""
API Test
BIST AI LAB v6
"""

from fastapi.testclient import TestClient

from api.api_server import app


def main():

    print("API TEST")

    client = TestClient(app)

    r1 = client.get("/")
    r2 = client.get("/health")
    r3 = client.get("/system")

    print("\nROOT")
    print(r1.json())

    print("\nHEALTH")
    print(r2.json())

    print("\nSYSTEM")
    print(r3.json())

    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()
