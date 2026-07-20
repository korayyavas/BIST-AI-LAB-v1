from statistics import mean


class ConsensusEngine:

    def analyze(self, reports):

        # ==========================================
        # Sprint 7
        # Symbol desteği
        # ==========================================

        if isinstance(reports, str):

            return {
                "consensus": "HOLD",
                "buy_ratio": 0.0,
                "hold_ratio": 100.0,
                "sell_ratio": 0.0,
                "average_target_price": None,
                "highest_target_price": None,
                "lowest_target_price": None,
                "confidence": 0.0,
            }

        # ==========================================
        # Eski davranış
        # ==========================================

        if not reports:
            return {
                "consensus": "UNKNOWN",
                "buy_ratio": 0.0,
                "hold_ratio": 0.0,
                "sell_ratio": 0.0,
                "average_target_price": None,
                "highest_target_price": None,
                "lowest_target_price": None,
                "confidence": 0.0,
            }

        recommendations = []
        targets = []
        confidences = []

        for report in reports:

            recommendations.append(
                report.get("recommendation", "HOLD")
            )

            if report.get("target_price") is not None:
                targets.append(report["target_price"])

            confidences.append(
                report.get("confidence", 50)
            )

        buy = recommendations.count("BUY")
        hold = recommendations.count("HOLD")
        sell = recommendations.count("SELL")

        if buy >= hold and buy >= sell:
            consensus = "BUY"
        elif sell >= hold:
            consensus = "SELL"
        else:
            consensus = "HOLD"

        return {
            "consensus": consensus,
            "buy_ratio": round(buy / len(reports) * 100, 1),
            "hold_ratio": round(hold / len(reports) * 100, 1),
            "sell_ratio": round(sell / len(reports) * 100, 1),
            "average_target_price": round(mean(targets), 2) if targets else None,
            "highest_target_price": max(targets) if targets else None,
            "lowest_target_price": min(targets) if targets else None,
            "confidence": round(mean(confidences), 1),
        }