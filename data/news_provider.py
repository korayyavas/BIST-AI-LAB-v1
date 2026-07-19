from abc import ABC, abstractmethod


class NewsProvider(ABC):

    @abstractmethod
    def search(self, symbol: str):
        pass