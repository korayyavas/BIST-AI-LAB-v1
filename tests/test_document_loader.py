from research.parser.document_loader import DocumentLoader

loader = DocumentLoader()

text = loader.load("README.md")

print(text[:1000])