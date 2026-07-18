"""
Scan API Test
"""

from fastapi.testclient import TestClient

from api.api_server import app


def main():

    client = TestClient(app)

    response = client.post(
        "/scan",
        json={
            "symbols": [
                "ASELS.IS",
                "THYAO.IS",
                "KCHOL.IS",
                "SISE.IS",
                "EREGL.IS",
                "TUPRS.IS",
                "AKBNK.IS",
                "GARAN.IS",
            ]
        },
    )

    print(response.status_code)
    print()
    print(response.json())


if __name__ == "__main__":
    main()