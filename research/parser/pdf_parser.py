import fitz


class PdfParser:

    def parse(self, path: str) -> str:

        doc = fitz.open(path)

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        return text