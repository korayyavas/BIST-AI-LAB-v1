import { lazy, Suspense, useMemo } from "react";

import {
    Paper,
    Box,
    CircularProgress,
} from "@mui/material";


const EChart = lazy(() => import("echarts-for-react"));



function Loading() {

    return (

        <Box
            sx={{
                height: 520,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >

            <CircularProgress />

        </Box>

    );

}





export default function TradingChart({

    symbol = "ASELS",

    market,

    prediction,

}) {



    const ohlcv = market?.ohlcv ?? [];



    const signal = prediction?.signal ?? "HOLD";



    const chartData = useMemo(() => {


        if (!ohlcv.length) {

            return {

                dates: [],

                candles: [],

                volumes: [],

                signalPoints: [],

            };

        }



        const dates = ohlcv.map(

            item => item.date.substring(0,10)

        );



        const candles = ohlcv.map(

            item => [

                item.open,

                item.close,

                item.low,

                item.high,

            ]

        );



        const volumes = ohlcv.map(

            item => item.volume

        );



        const last = ohlcv[ohlcv.length - 1];



        const signalPoints = [

            {

                value: [

                    dates[dates.length - 1],

                    last.close

                ],


                signal,

            }

        ];



        return {

            dates,

            candles,

            volumes,

            signalPoints,

        };



    }, [ohlcv, signal]);







    const signalColor =

        signal === "BUY"

            ? "#26a69a"

            : signal === "SELL"

                ? "#ef5350"

                : "#ffc107";






    const option = {



        backgroundColor: "#10151d",



        animation: true,



        title: {


            text:

                `${symbol} AI MARKET INTELLIGENCE`,



            left:

                "center",



            textStyle: {


                color:

                    "#ffffff",


                fontSize:

                    18,


                fontWeight:

                    "bold",


            },


        },






        tooltip: {


            trigger:

                "axis",



            axisPointer: {


                type:

                    "cross",


            },


        },







        grid: [

            {

                left:55,

                right:25,

                top:60,

                height:"60%",

            },


            {

                left:55,

                right:25,

                top:"75%",

                height:"15%",

            }

        ],







        xAxis:[


            {

                type:"category",

                data:chartData.dates,

                boundaryGap:true,

            },


            {

                type:"category",

                gridIndex:1,

                data:chartData.dates,

                show:false,

            }


        ],







        yAxis:[


            {

                scale:true,

                splitLine:{

                    lineStyle:{

                        color:"#2b3440"

                    }

                }

            },


            {

                gridIndex:1,

                splitLine:{

                    show:false

                }

            }


        ],







        series:[



            {

                name:symbol,


                type:"candlestick",


                data:chartData.candles,


                itemStyle:{


                    color:"#26a69a",


                    color0:"#ef5350",


                    borderColor:"#26a69a",


                    borderColor0:"#ef5350",


                },


            },







            {

                name:"Volume",


                type:"bar",


                xAxisIndex:1,


                yAxisIndex:1,


                data:chartData.volumes,


            },








            {

                name:"AI SIGNAL LINE",


                type:"line",


                data:


                    chartData.dates.map(

                        () =>

                        prediction?.current_price ??

                        prediction?.price ??

                        market?.price

                    ),


                symbol:"none",


                lineStyle:{


                    type:"dashed",


                    width:2,


                    color:signalColor,


                },


            },








            {

                name:`AI ${signal}`,


                type:"scatter",


                data:


                    chartData.signalPoints.map(

                        item => item.value

                    ),



                symbolSize:18,


                itemStyle:{


                    color:signalColor,


                },



                label:{


                    show:true,


                    formatter:

                        `AI ${signal}`,


                    position:"top",


                    color:"#ffffff",


                },


            }





        ],



    };







    return (


        <Paper

            sx={{

                p:2,

                borderRadius:3,

                background:"#10151d",

                border:"1px solid #243041",

            }}

        >


            <Suspense

                fallback={<Loading />}

            >


                <EChart

                    option={option}


                    style={{

                        width:"100%",

                        height:520,

                    }}

                />


            </Suspense>


        </Paper>


    );

}