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







export default function PortfolioPerformanceChart({

    backtest = {},

}){



    const chartData = useMemo(()=>{


        const initial =

            backtest.initial_value ?? 0;



        const current =

            backtest.current_value ?? 0;



        const profit =

            backtest.profit_loss ?? 0;




        return {


            labels:[

                "Başlangıç",

                "Güncel"

            ],



            values:[

                initial,

                current

            ],



            profit:[

                0,

                profit

            ]


        };


    },[backtest]);







    const option = {


        backgroundColor:"#10151d",



        tooltip:{


            trigger:"axis"


        },



        grid:{


            left:50,

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


            type:"value"


        },





        series:[


            {

                name:"Portfolio Value",

                type:"line",

                smooth:true,

                data:

                    chartData.values

            },


            {

                name:"Profit",

                type:"bar",

                data:

                    chartData.profit

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

                        height:380,

                        width:"100%"

                    }}

                />


            </Suspense>


        </Paper>


    );


}