
from services.scan_controller import ScanController

class TopPicksController:
    def __init__(self):
        self.scanner=ScanController()

    def get_top(self,symbols,top=10,signal="BUY",min_confidence=70):
        return self.scanner.scan(
            symbols=symbols,
            signal=signal,
            min_confidence=min_confidence
        )[:top]
