from services.prediction_controller import PredictionController

class ScanController:
    def __init__(self):
        self.predictor = PredictionController()

    def scan(self, symbols, signal=None, min_confidence=0):
        results=[]
        for symbol in symbols:
            try:
                r=self.predictor.predict(symbol)
                for k,v in list(r.items()):
                    if isinstance(v,float):
                        r[k]=round(v,2)
                if signal and r["signal"]!=signal:
                    continue
                if r["confidence"]<min_confidence:
                    continue
                results.append(r)
            except Exception as e:
                results.append({"symbol":symbol,"error":str(e)})
        results.sort(key=lambda x:x.get("confidence",0),reverse=True)
        return results
