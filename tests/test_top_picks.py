from fastapi.testclient import TestClient

from api.api_server import app


def main():

    client = TestClient(app)

    response = client.post(
        "/top-picks",
        json={
            "top": 10,
            "signal": "BUY",
            "min_confidence": 70,
        },
    )

    print(response.status_code)
    print()
    print(response.json())


if __name__ == "__main__":
    main()