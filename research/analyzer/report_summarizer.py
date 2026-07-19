from transformers import pipeline


class ReportSummarizer:

    def __init__(self):

        self.model = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
        )

    def summarize(self, text: str) -> str:

        text = text.replace("\n", " ")

        text = text[:3500]

        result = self.model(
            text,
            max_length=180,
            min_length=60,
            do_sample=False,
        )

        return result[0]["summary_text"]