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



    const chartData = useMemo(() => {


        if (!ohlcv.length) {

            return {

                dates: [],

                candles: [],

                volumes: [],

            };

        }



        return {


            dates:

                ohlcv.map(

                    item =>

                    item.date.substring(0,10)

                ),



            candles:

                ohlcv.map(

                    item => [

                        item.open,

                        item.close,

                        item.low,

                        item.high,

                    ]

                ),




            volumes:

                ohlcv.map(

                    item =>

                    item.volume

                ),



        };



    }, [ohlcv]);






    const signalPrice =

        prediction?.current_price ??

        prediction?.price ??

        market?.price;






    const option = {



        backgroundColor: "#10151d",



        animation: true,



        title: {


            text:

                `${symbol} REAL MARKET DATA`,



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

                left:

                    55,

                right:

                    25,

                top:

                    60,

                height:

                    "60%",


            },


            {

                left:

                    55,

                right:

                    25,

                top:

                    "75%",


                height:

                    "15%",


            },

        ],







        xAxis: [

            {


                type:

                    "category",



                data:

                    chartData.dates,



                boundaryGap:

                    true,



                axisLine: {


                    lineStyle: {


                        color:

                            "#888",


                    },


                },



            },


            {


                type:

                    "category",



                gridIndex:

                    1,



                data:

                    chartData.dates,



                show:

                    false,


            },


        ],







        yAxis: [

            {


                scale:

                    true,



                splitLine: {


                    lineStyle: {


                        color:

                            "#2b3440",


                    },


                },



                axisLine: {


                    lineStyle: {


                        color:

                            "#888",


                    },


                },


            },



            {


                gridIndex:

                    1,



                splitLine:

                    {

                        show:false

                    },


            },


        ],







        series: [



            {


                name:

                    symbol,



                type:

                    "candlestick",



                data:

                    chartData.candles,



                itemStyle: {


                    color:

                        "#26a69a",



                    color0:

                        "#ef5350",


                    borderColor:

                        "#26a69a",



                    borderColor0:

                        "#ef5350",



                },



            },





            {


                name:

                    "Volume",



                type:

                    "bar",



                xAxisIndex:

                    1,



                yAxisIndex:

                    1,



                data:

                    chartData.volumes,



            },





            {


                name:

                    "AI SIGNAL",



                type:

                    "line",



                data:

                    chartData.dates.map(

                        () => signalPrice

                    ),



                smooth:

                    true,



                symbol:

                    "none",



                lineStyle:


                    {


                        width:

                            2,



                        type:

                            "dashed",


                    },



            },



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


                        width:

                            "100%",



                        height:

                            520,



                    }}



                />



            </Suspense>



        </Paper>


    );

}