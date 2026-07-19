from research.consensus.consensus_engine import ConsensusEngine

reports = [

    {
        "recommendation":"BUY",
        "target_price":520,
        "confidence":95
    },

    {
        "recommendation":"BUY",
        "target_price":510,
        "confidence":90
    },

    {
        "recommendation":"HOLD",
        "target_price":495,
        "confidence":85
    },

    {
        "recommendation":"BUY",
        "target_price":530,
        "confidence":92
    },

    {
        "recommendation":"SELL",
        "target_price":430,
        "confidence":70
    }

]

engine = ConsensusEngine()

print(
    engine.analyze(reports)
)