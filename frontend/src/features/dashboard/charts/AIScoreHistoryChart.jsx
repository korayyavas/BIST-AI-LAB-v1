import { lazy, Suspense, useMemo } from "react";

import {
    Paper,
    Box,
    CircularProgress,
} from "@mui/material";


const EChart = lazy(() =>
    import("echarts-for-react")
);





function Loading(){


    return (

        <Box

            sx={{

                height:380,

                display:"flex",

                justifyContent:"center",

                alignItems:"center"

            }}

        >

            <CircularProgress/>

        </Box>

    );

}







export default function AIScoreHistoryChart({

    intelligence = {},

}){



    const chartData = useMemo(()=>{


        return {


            labels:[

                "ML",

                "Technical",

                "News",

                "Research",

                "KAP",

                "TOTAL"

            ],



            values:[


                intelligence.ml_score ?? 0,


                intelligence.technical_score ?? 0,


                intelligence.news_score ?? 0,


                intelligence.research_score ?? 0,


                intelligence.kap_score ?? 0,


                intelligence.ai_score ?? 0


            ]



        };


    },[intelligence]);








    const option = {


        backgroundColor:"#10151d",




        tooltip:{


            trigger:"axis"


        },






        grid:{


            left:40,

            right:30,

            top:40,

            bottom:40


        },







        xAxis:{


            type:"category",


            data:

                chartData.labels


        },







        yAxis:{


            type:"value",


            max:100


        },






        series:[


            {


                name:"AI Score",


                type:"bar",


                data:

                    chartData.values


            },



            {


                name:"Trend",


                type:"line",


                smooth:true,


                data:

                    chartData.values


            }



        ]



    };





    return (

        <Paper

            sx={{

                p:2,

                borderRadius:3,

                background:"#10151d",

                border:"1px solid #243041"

            }}

        >


            <Suspense

                fallback={<Loading/>}

            >


                <EChart

                    option={option}

                    style={{

                        width:"100%",

                        height:380

                    }}

                />


            </Suspense>


        </Paper>

    );


}