"""
BIST AI LAB
AI Decision Timeline Service v1.0
"""


from datetime import datetime





class AIDecisionTimelineService:




    def __init__(self):


        self.history = []






    def add_decision(

        self,

        symbol,

        decision,

        score,

        confidence,

        explanation=None

    ):


        item = {


            "symbol":

                symbol,


            "decision":

                decision,


            "score":

                score,


            "confidence":

                confidence,


            "explanation":

                explanation or [],


            "timestamp":

                datetime.utcnow().isoformat()


        }



        self.history.append(item)



        return item







    def get_history(

        self,

        symbol=None

    ):


        if symbol:


            return [

                x

                for x in self.history

                if x["symbol"] == symbol

            ]



        return self.history







ai_decision_timeline_service = AIDecisionTimelineService()