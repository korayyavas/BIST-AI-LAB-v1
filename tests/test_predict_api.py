"""
Predict API Test
"""

from fastapi.testclient import TestClient

from api.api_server import app


def main():

    client = TestClient(app)

    response = client.post(
        "/predict",
        json={
            "symbols": [
                "ASELS.IS",
                "THYAO.IS",
                "KCHOL.IS",
            ]
        },
    )

    print(response.status_code)
    print()
    print(response.json())


if __name__ == "__main__":
    main()