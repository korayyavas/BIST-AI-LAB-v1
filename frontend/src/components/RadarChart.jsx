import ReactECharts from "echarts-for-react";

export default function RadarChart({ data }) {

    if (!data) return null;

    const option = {

        backgroundColor: "#161b22",

        radar: {

            indicator: [

                { name: "ML", max: 100 },

                { name: "Technical", max: 100 },

                { name: "Research", max: 100 },

                { name: "News", max: 100 },

                { name: "KAP", max: 100 }

            ],

            axisName: {

                color: "#ffffff"

            }

        },

        series: [

            {

                type: "radar",

                data: [

                    {

                        value: [

                            data.ml_score,

                            data.technical_score,

                            data.research_score,

                            data.news_score,

                            data.kap_score

                        ]

                    }

                ]

            }

        ]

    };

    return (

        <ReactECharts

            option={option}

            style={{

                height: 280

            }}

        />

    );

}