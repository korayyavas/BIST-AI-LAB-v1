from data.yahoo_provider import YahooFinanceProvider

class MarketDataService:
    def __init__(self):
        self.provider=YahooFinanceProvider()
    def download(self,symbol:str):
        return self.provider.download(symbol)
