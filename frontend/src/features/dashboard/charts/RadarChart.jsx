import { lazy, Suspense, useMemo } from "react";

import {
    Box,
    CircularProgress,
    Paper,
    Typography,
} from "@mui/material";


const EChart = lazy(() =>
    import("echarts-for-react")
);



function Loading() {

    return (

        <Box
            sx={{
                height:420,
                display:"flex",
                justifyContent:"center",
                alignItems:"center",
            }}
        >

            <CircularProgress />

        </Box>

    );

}




export default function RadarChart({

    intelligence = {},

}) {



    const radarData = useMemo(() => {


        return [


            intelligence.ml_score ?? 0,


            intelligence.technical_score ?? 0,


            intelligence.news_score ?? 0,


            intelligence.research_score ?? 0,


            intelligence.kap_score ?? 0,


        ];


    }, [intelligence]);






    const option = {



        title:{


            text:"AI COMPONENT ANALYSIS",


            left:"center",


            textStyle:{


                fontSize:16,


                fontWeight:"bold",


            },


        },






        tooltip:{


            trigger:"item",


        },






        radar:{


            radius:"68%",



            splitNumber:5,



            axisName:{


                color:"#ffffff",


                fontSize:14,


            },



            indicator:[



                {

                    name:"ML",

                    max:100,

                },



                {

                    name:"Technical",

                    max:100,

                },



                {

                    name:"News",

                    max:100,

                },



                {

                    name:"Research",

                    max:100,

                },



                {

                    name:"KAP",

                    max:100,

                },


            ],


        },






        series:[



            {


                type:"radar",



                symbol:"circle",



                symbolSize:6,



                areaStyle:{


                    opacity:0.35,


                },



                lineStyle:{


                    width:3,


                },



                data:[



                    {


                        name:"AI Score",



                        value:radarData,



                    },


                ],



            },


        ],



    };







    return (



        <Paper

            sx={{


                p:2,


                borderRadius:3,


                height:420,


                background:"#10151d",


                border:"1px solid #243041",


            }}

        >



            <Typography

                variant="h6"

                fontWeight={700}

                mb={1}

            >

                🧠 AI Intelligence Radar

            </Typography>





            <Suspense

                fallback={<Loading />}

            >



                <EChart


                    option={option}



                    style={{


                        height:360,


                        width:"100%",


                    }}



                />



            </Suspense>



        </Paper>


    );

}