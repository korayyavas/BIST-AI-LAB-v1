import requests


class LLMEngine:

    def __init__(
        self,
        model="qwen2.5:7b",
        host="http://localhost:11434",
    ):
        self.model = model
        self.host = host

    def ask(self, prompt: str) -> str:

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0
                }
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["response"]