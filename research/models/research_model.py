from dataclasses import dataclass


@dataclass
class ResearchReport:

    institution: str

    symbol: str

    title: str

    summary: str

    recommendation: str

    target_price: float | None

    analyst: str

    report_date: str

    confidence: float

    url: str