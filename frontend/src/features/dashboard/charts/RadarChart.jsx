import { lazy, Suspense } from "react";

import {
    Box,
    CircularProgress,
} from "@mui/material";

const EChart = lazy(() =>
    import("echarts-for-react")
);

function Loading() {

    return (

        <Box
            sx={{
                height: 320,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >

            <CircularProgress />

        </Box>

    );

}

export default function RadarChart(props) {

    const option = {
        radar: {},
        series: [],
    };

    return (

        <Suspense
            fallback={<Loading />}
        >

            <EChart
                option={option}
                style={{
                    height: 320,
                }}
                {...props}
            />

        </Suspense>

    );

}