from api.scan_models import ScanRequest
from services.scan_controller import ScanController

scanner=ScanController()

@app.post("/scan")
def scan(req:ScanRequest):
    return {
        "results":scanner.scan(
            req.symbols,
            signal=req.signal,
            min_confidence=req.min_confidence,
        )
    }
