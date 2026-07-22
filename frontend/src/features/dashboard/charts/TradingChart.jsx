import { lazy, Suspense } from "react";

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
                height: 440,
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

}) {

    const option = {

        backgroundColor: "#10151d",

        animation: true,

        title: {

            text: `${symbol} PRICE TREND`,

            left: "center",

            textStyle: {

                color: "#ffffff",

                fontSize: 18,

                fontWeight: "bold",

            },

        },

        tooltip: {

            trigger: "axis",

        },

        grid: {

            left: 55,

            right: 25,

            top: 60,

            bottom: 45,

        },

        xAxis: {

            type: "category",

            boundaryGap: false,

            data: [

                "Pzt",

                "Sal",

                "Çar",

                "Per",

                "Cum",

                "Pzt",

                "Sal",

                "Bugün",

            ],

            axisLine: {

                lineStyle: {

                    color: "#888",

                },

            },

        },

        yAxis: {

            type: "value",

            scale: true,

            splitLine: {

                lineStyle: {

                    color: "#2b3440",

                },

            },

            axisLine: {

                lineStyle: {

                    color: "#888",

                },

            },

        },

        series: [

            {

                name: symbol,

                type: "line",

                smooth: true,

                symbol: "circle",

                symbolSize: 7,

                areaStyle: {

                    opacity: 0.20,

                },

                lineStyle: {

                    width: 3,

                },

                data: [

                    112,

                    114,

                    113,

                    118,

                    121,

                    124,

                    126,

                    129,

                ],

            },

        ],

    };

    return (

        <Paper

            sx={{

                p: 2,

                borderRadius: 3,

                background: "#10151d",

                border: "1px solid #243041",

            }}

        >

            <Suspense fallback={<Loading />}>

                <EChart

                    option={option}

                    style={{

                        width: "100%",

                        height: 440,

                    }}

                />

            </Suspense>

        </Paper>

    );

}