from core.decision_engine import DecisionEngine

engine = DecisionEngine()

result = engine.evaluate(
    ml_score=82,
    technical_score=75,
    news_score=78,
    kap_score=80,
    research_score=92,
    risk_score=25,
)

print(result)