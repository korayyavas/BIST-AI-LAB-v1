from dataclasses import dataclass


@dataclass
class KapEvent:
    title: str
    event_type: str
    score: float


class KapService:

    def get_events(self, symbol: str):

        return [
            KapEvent(
                title=f"{symbol} KAP Service Ready",
                event_type="INFO",
                score=50,
            )
        ]