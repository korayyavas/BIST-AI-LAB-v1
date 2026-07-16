
"""
Startup Test
BIST AI LAB v6
"""

from core.startup import Startup


def main():

    print("STARTUP TEST")

    startup = Startup()

    result = startup.boot()

    print()

    for k, v in result["system"].items():
        print(f"{k:12}: {v}")

    print()
    print("Container OK :", result["container"] is not None)
    print("Success      :", result["success"])
    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
