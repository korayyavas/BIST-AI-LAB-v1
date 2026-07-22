import { lazy, Suspense } from "react";

import {
    Box,
    CircularProgress,
    Paper,
} from "@mui/material";

const EChart = lazy(() =>
    import("echarts-for-react")
);

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

export default function RadarChart({

    intelligence = {},

}) {

    const option = {

        tooltip: {},

        radar: {

            radius: "68%",

            indicator: [

                { name: "ML", max: 100 },

                { name: "Technical", max: 100 },

                { name: "News", max: 100 },

                { name: "Research", max: 100 },

                { name: "KAP", max: 100 },

            ],

        },

        series: [

            {

                type: "radar",

                areaStyle: {

                    opacity: 0.35,

                },

                data: [

                    {

                        name: "AI",

                        value: [

                            intelligence.ml_score ?? 0,

                            intelligence.technical_score ?? 0,

                            intelligence.news_score ?? 0,

                            intelligence.research_score ?? 0,

                            intelligence.kap_score ?? 0,

                        ],

                    },

                ],

            },

        ],

    };

    return (

        <Paper
            sx={{
                p: 2,
                borderRadius: 3,
                height: 420,
            }}
        >

            <Suspense fallback={<Loading />}>

                <EChart

                    option={option}

                    style={{

                        height: 380,

                    }}

                />

            </Suspense>

        </Paper>

    );

}