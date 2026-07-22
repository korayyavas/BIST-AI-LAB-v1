from ollama import Client
import time


class OllamaService:

    def __init__(self):

        self.client = Client(
            host="http://127.0.0.1:11434"
        )

    def ask(self, prompt: str):

        print("=" * 80)
        print("OLLAMA REQUEST")
        print(time.strftime("%H:%M:%S"))

        start = time.time()

        response = self.client.chat(

            model="gemma3:4b",

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            options={
                "temperature": 0.2,
                "num_predict": 300,
            },

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        print(
            f"OLLAMA RESPONSE {elapsed} sec"
        )
        print("=" * 80)

        return response["message"]["content"]