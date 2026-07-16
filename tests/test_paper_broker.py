
"""
Paper Broker Test
BIST AI LAB v5
"""

from broker.paper_broker import PaperBroker


def main():

    print("PAPER BROKER TEST")

    broker = PaperBroker()

    broker.connect()

    print("Connected :", broker.connected)
    print("Balance   :", broker.get_balance())

    buy = broker.place_order(
        symbol="ASELS",
        side="BUY",
        quantity=100,
        price=125.50,
    )

    sell = broker.place_order(
        symbol="ASELS",
        side="SELL",
        quantity=40,
        price=128.20,
    )

    print("\nBUY ORDER")
    print(buy)

    print("\nSELL ORDER")
    print(sell)

    print("\nPositions")
    print(broker.get_positions())

    broker.disconnect()

    print("\nDisconnected :", not broker.connected)
    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()
