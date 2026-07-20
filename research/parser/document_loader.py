"""
Document Loader
BIST AI LAB v7
"""

from __future__ import annotations

from pathlib import Path

from research.parser.pdf_parser import PdfParser


class DocumentLoader:

    def __init__(self):

        self.pdf = PdfParser()

    def load(self, path: str) -> str:

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(path)

        suffix = file.suffix.lower()

        if suffix == ".pdf":

            return self.pdf.parse(str(file))

        return file.read_text(
            encoding="utf-8",
            errors="ignore",
        )