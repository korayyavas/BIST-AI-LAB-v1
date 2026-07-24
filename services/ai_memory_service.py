"""
BIST AI LAB
AI Memory Engine v1.1

Karar geçmişi öğrenme ve performans takip sistemi
"""


from datetime import datetime





class AIMemoryService:




    def __init__(self):

        self.memory = []








    def store_decision(

        self,

        decision_data: dict

    ):


        record = {


            "symbol":

                decision_data.get(

                    "symbol"

                ),



            "decision":

                decision_data.get(

                    "decision"

                ),



            "score":

                decision_data.get(

                    "score",

                    0

                ),



            "confidence":

                decision_data.get(

                    "confidence"

                ),



            "result":

                None,



            "success":

                None,



            "created_at":

                datetime.utcnow().isoformat()


        }




        self.memory.append(record)



        return record







    def update_result(

        self,

        symbol,

        success: bool,

        result: str

    ):



        for item in reversed(self.memory):


            if (

                item["symbol"] == symbol

                and

                item["success"] is None

            ):


                item["success"] = success


                item["result"] = result


                item["updated_at"] = (

                    datetime.utcnow()

                    .isoformat()

                )


                return item




        return None
    



    def calculate_accuracy(self):


        total = 0

        success_count = 0





        for item in self.memory:



            if item["success"] is not None:


                total += 1



                if item["success"]:


                    success_count += 1






        accuracy = 0



        if total > 0:


            accuracy = (

                success_count

                /

                total

            ) * 100





        return {


            "total_decisions":

                len(self.memory),



            "evaluated_decisions":

                total,



            "successful_decisions":

                success_count,



            "accuracy":

                round(

                    accuracy,

                    2

                )

        }







    def performance(self):


        stats = self.calculate_accuracy()



        return {


            "ai_accuracy":

                stats["accuracy"],



            "total":

                stats["total_decisions"],



            "correct":

                stats["successful_decisions"],



            "evaluated":

                stats["evaluated_decisions"],



            "status":

                "learning"

                if stats["total_decisions"] > 0

                else

                "waiting"


        }







    def get_memory(


        self,


        symbol=None


    ):


        if symbol:


            return [


                item

                for item in self.memory

                if item["symbol"] == symbol.upper()


            ]



        return self.memory










ai_memory_service = AIMemoryService()