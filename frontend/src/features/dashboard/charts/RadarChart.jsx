import ReactECharts from "echarts-for-react";

export default function RadarChart(){

    const option={

        backgroundColor:"#11161d",

        tooltip:{},

        radar:{

            radius:"70%",

            indicator:[

                {name:"ML",max:100},

                {name:"Technical",max:100},

                {name:"News",max:100},

                {name:"Research",max:100},

                {name:"KAP",max:100}

            ],

            axisName:{

                color:"#ffffff",

                fontSize:13

            },

            splitLine:{

                lineStyle:{

                    color:"#2d3748"

                }

            },

            splitArea:{

                areaStyle:{

                    color:["#11161d"]

                }

            }

        },

        series:[

            {

                type:"radar",

                areaStyle:{

                    opacity:.35

                },

                lineStyle:{

                    width:3

                },

                data:[

                    {

                        value:[

                            52,

                            40,

                            77,

                            86,

                            50

                        ]

                    }

                ]

            }

        ]

    };

    return(

        <ReactECharts

            option={option}

            style={{

                height:340

            }}

        />

    );

}