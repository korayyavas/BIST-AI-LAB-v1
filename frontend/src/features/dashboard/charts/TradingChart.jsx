import { lazy, Suspense } from "react";

import {
    Box,
    CircularProgress,
} from "@mui/material";

const EChart = lazy(() =>
    import("echarts-for-react")
);

function ChartLoading() {
    return (
        <Box
            sx={{
                height: 420,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
            }}
        >
            <CircularProgress />
        </Box>
    );
}

export default function TradingChart(props) {

    const option = {
        animation: true,

        tooltip: {
            trigger: "axis",
        },

        xAxis: {
            type: "category",
            data: [],
        },

        yAxis: {
            type: "value",
        },

        series: [],
    };

    return (

        <Suspense
            fallback={<ChartLoading />}
        >

            <EChart
                option={option}
                style={{
                    width: "100%",
                    height: 420,
                }}
                {...props}
            />

        </Suspense>

    );

}