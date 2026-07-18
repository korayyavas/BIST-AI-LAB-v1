from services.scan_controller import ScanController


class TopPicksController:

    def __init__(self):
        self.scanner = ScanController()

    def get_top(
        self,
        symbols,
        top=10,
        signal=None,
        min_confidence=0,
    ):

        results = self.scanner.scan(
            symbols=symbols,
            signal=signal,
            min_confidence=min_confidence,
        )

        for r in results:

            buy = r.get("buy_probability", 0)
            conf = r.get("confidence", 0)
            risk = r.get("risk_score", 100)

            top_score = (
                0.50 * buy +
                0.30 * conf +
                0.20 * (100 - risk)
            )

            r["top_score"] = round(top_score, 2)

        results.sort(
            key=lambda x: x["top_score"],
            reverse=True,
        )

        return results[:top]