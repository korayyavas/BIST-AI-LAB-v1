from pathlib import Path


class DocumentLoader:

    def load(self, path: str) -> str:

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(path)

        return file.read_text(
            encoding="utf-8",
            errors="ignore",
        )