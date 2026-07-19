from abc import ABC, abstractmethod


class BaseResearchProvider(ABC):

    @abstractmethod
    def search(self, symbol: str):
        pass