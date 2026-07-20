"""
Local Research Provider
BIST AI LAB v7
"""

from __future__ import annotations

from pathlib import Path


class LocalResearchProvider:

    def __init__(self, folder="reports"):

        self.folder = Path(folder)

    def get_reports(self, symbol: str):

        reports = []

        if not self.folder.exists():
            return reports

        for pdf in self.folder.glob("*.pdf"):

            reports.append(
                {
                    "broker": "LOCAL",
                    "title": pdf.stem,
                    "path": str(pdf),
                }
            )

        return reports