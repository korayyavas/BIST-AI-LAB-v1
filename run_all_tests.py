"""
Run All Tests
BIST AI LAB v3
"""

from __future__ import annotations

import subprocess
import sys


TESTS = [

    "tests.test_training",

    "tests.test_prediction",

    "tests.test_screener",

    "tests.test_backtest",

    "tests.test_portfolio",

]


def run(test_name: str) -> bool:

    print("\n" + "=" * 70)

    print(f"RUNNING -> {test_name}")

    print("=" * 70)

    result = subprocess.run(

        [

            sys.executable,

            "-m",

            test_name,

        ]

    )

    return result.returncode == 0


# ======================================================

def main():

    success = 0

    failed = 0

    failed_tests = []

    print("\n")

    print("=" * 70)

    print("BIST AI LAB v3 TEST SUITE")

    print("=" * 70)

    for test in TESTS:

        ok = run(test)

        if ok:

            success += 1

        else:

            failed += 1

            failed_tests.append(test)

    print("\n")

    print("=" * 70)

    print("TEST SUMMARY")

    print("=" * 70)

    print(f"PASSED : {success}")

    print(f"FAILED : {failed}")

    print(f"TOTAL  : {len(TESTS)}")

    if failed_tests:

        print("\nFAILED TESTS")

        for test in failed_tests:

            print("-", test)

    else:

        print("\nALL TESTS PASSED ✅")

    print("=" * 70)


if __name__ == "__main__":

    main()