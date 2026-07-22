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
                height: 420,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <CircularProgress />
        </Box>
    );
}

export default function TradingChart() {

    const option = {

        title: {
            text: "ASELS",
            left: "center",
            textStyle: {
                color: "#fff",
            },
        },

        backgroundColor: "#11161d",

        tooltip: {
            trigger: "axis",
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
            ],
        },

        yAxis: {
            type: "value",
        },

        series: [
            {
                name: "Fiyat",
                type: "line",
                smooth: true,
                areaStyle: {},
                data: [
                    112,
                    114,
                    113,
                    118,
                    121,
                ],
            },
        ],

    };

    return (

        <Paper sx={{ p: 2 }}>

            <Suspense fallback={<Loading />}>

                <EChart
                    option={option}
                    style={{
                        width: "100%",
                        height: 420,
                    }}
                />

            </Suspense>

        </Paper>

    );

}