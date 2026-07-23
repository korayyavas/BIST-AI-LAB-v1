"""
AI News Intelligence Service
BIST AI LAB v10.1

News Translation + Financial Intelligence
"""

from __future__ import annotations


import json
import logging


from services.ollama_service import OllamaService



logger = logging.getLogger(__name__)





class NewsAIService:



    def __init__(self):

        self.ollama = OllamaService()





    # =====================================================
    # ANALYZE
    # =====================================================


    def analyze(

        self,

        headlines:list[str]

    ):


        if not headlines:

            return []



        headlines = headlines[:5]



        prompt = f"""

Sen BIST uzmanı finans analisti ve Türkçe ekonomi editörüsün.


Aşağıdaki haberleri analiz et.


SADECE JSON döndür.


Markdown yok.

Açıklama yok.



Çok önemli:

JSON tamamen kapanmalı.

Her alan kısa olmalı.


title_tr:
maksimum 12 kelime


summary:
maksimum 20 kelime


ai_comment:
maksimum 15 kelime



FORMAT:


[
{{
"title_tr":"",
"summary":"",
"market_effect":"POZITIF",
"importance":3,
"ai_comment":""
}}
]



market_effect:

POZITIF

NOTR

NEGATIF



Haberler:


{chr(10).join(

    f"{i+1}. {x}"

    for i,x in enumerate(headlines)

)}



"""



        try:


            content = self.ollama.ask(

                prompt

            )


        except Exception as e:


            logger.exception(

                "Ollama news error %s",

                e

            )


            return []



        if not content:

            return []



        return self._parse_json(

            content

        )
        # =====================================================
    # JSON PARSER + REPAIR
    # =====================================================


    def _parse_json(

        self,

        content:str

    ):


        try:


            content = content.strip()



            # Markdown temizleme


            if "```" in content:


                content = (

                    content

                    .replace(

                        "```json",

                        ""

                    )

                    .replace(

                        "```JSON",

                        ""

                    )

                    .replace(

                        "```",

                        ""

                    )

                    .strip()

                )



            # JSON başlangıcı bul


            start = content.find("[")



            if start == -1:


                return []



            content = content[start:]



            # Önce normal parse dene


            try:


                data = json.loads(

                    content

                )


                return self._clean_result(

                    data

                )



            except json.JSONDecodeError:


                pass





            # =================================================
            # JSON REPAIR
            # =================================================


            repaired = content



            # yarım kalan satırları temizle


            last_object = repaired.rfind("}")



            if last_object != -1:


                repaired = repaired[:last_object+1]



            else:


                return []




            # Array kapanışı ekle


            if not repaired.endswith("]"):


                repaired += "]"




            # Açık string düzeltme


            quote_count = repaired.count('"')



            if quote_count % 2 != 0:


                repaired += '"'




            try:


                data = json.loads(

                    repaired

                )


                return self._clean_result(

                    data

                )



            except Exception:


                logger.warning(

                    "JSON repair failed"

                )



                return []




        except Exception:


            logger.exception(

                "News AI JSON parse failed"

            )


            return []





    # =====================================================
    # CLEAN RESULT
    # =====================================================


    def _clean_result(

        self,

        data

    ):


        if not isinstance(

            data,

            list

        ):


            return []



        result=[]



        for item in data:


            if not isinstance(

                item,

                dict

            ):


                continue



            result.append(

                {


                    "title_tr":

                    str(

                        item.get(

                            "title_tr",

                            ""

                        )

                    ),



                    "summary":

                    str(

                        item.get(

                            "summary",

                            ""

                        )

                    ),



                    "market_effect":

                    self._effect(

                        item.get(

                            "market_effect",

                            "NOTR"

                        )

                    ),



                    "importance":

                    self._importance(

                        item.get(

                            "importance",

                            3

                        )

                    ),



                    "ai_comment":

                    str(

                        item.get(

                            "ai_comment",

                            ""

                        )

                    )

                }

            )



        return result





    # =====================================================
    # NORMALIZERS
    # =====================================================


    def _effect(

        self,

        value

    ):


        value = str(

            value

        ).upper()



        if value in [

            "POSITIVE",

            "OLUMLU",

            "POZITIF"

        ]:

            return "POZITIF"



        if value in [

            "NEGATIVE",

            "OLUMSUZ",

            "NEGATIF"

        ]:

            return "NEGATIF"



        return "NOTR"





    def _importance(

        self,

        value

    ):


        try:


            value=int(

                value

            )


        except Exception:


            value=3



        return max(

            1,

            min(

                value,

                5

            )

        )





# =====================================================
# SINGLETON
# =====================================================


news_ai_service = NewsAIService()



__all__ = [

    "NewsAIService",

    "news_ai_service",

]