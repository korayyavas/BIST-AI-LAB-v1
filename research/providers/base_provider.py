from abc import ABC, abstractmethod


class BaseResearchProvider(ABC):

    @abstractmethod
    def get_reports(self, symbol: str):
        ...