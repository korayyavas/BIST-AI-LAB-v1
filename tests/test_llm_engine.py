from core.llm_engine import LLMEngine

ai = LLMEngine()

answer = ai.ask(
    """
ASELSAN signed a 1.47 billion euro air defense contract.

Explain in 5 sentences why this is important for investors.
"""
)

print(answer)