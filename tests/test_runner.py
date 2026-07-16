
"""
Test Runner
BIST AI LAB v6
"""

from __future__ import annotations

import subprocess
import sys

TESTS = [
    "tests.test_startup",
    "tests.test_system_integration",
    "tests.test_classifier_training",
    "tests.test_classification",
    "tests.test_walk_forward",
    "tests.test_backtest_v5",
    "tests.test_portfolio_optimizer",
    "tests.test_paper_trading",
    "tests.test_paper_broker",
    "tests.test_live_engine",
    "tests.test_api",
]


def main():

    print("BIST AI LAB TEST RUNNER\n")

    passed = 0

    for test in TESTS:

        print(f">>> {test}")

        result = subprocess.run(
            [sys.executable, "-m", test]
        )

        if result.returncode == 0:
            passed += 1
            print("PASS\n")
        else:
            print("FAIL\n")

    print("=" * 50)
    print(f"Passed : {passed}/{len(TESTS)}")
    print("=" * 50)


if __name__ == "__main__":
    main()
