import {
    Paper,
    Typography,
    Box,
    CircularProgress,
    Stack,
    Chip,
    Divider,
    List,
    ListItem,
    ListItemText,
    LinearProgress,
} from "@mui/material";


import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";



export default function AIScoreCard({

    loading=false,

    data={},

}){


    if(loading){

        return (

            <Paper

                sx={{

                    height:360,

                    display:"flex",

                    justifyContent:"center",

                    alignItems:"center",

                    bgcolor:"#10151d",

                    borderRadius:4,

                }}

            >

                <CircularProgress/>

            </Paper>

        );

    }





    const score = Number(

        data.ai_score ??

        data.score ??

        0

    );




    const decision =

        data.decision ??

        "HOLD";




    const confidence = Number(

        data.confidence ??

        50

    );





    const strengths =

        Array.isArray(data.strengths)

        ?

        data.strengths

        :

        [];





    const weaknesses =

        Array.isArray(data.weaknesses)

        ?

        data.weaknesses

        :

        [];





    let explanations =

        data.explanations ??

        [];





    if(typeof explanations==="string"){

        explanations = explanations

            .split("|")

            .map(x=>x.trim())

            .filter(Boolean);

    }






    const scores=[


        {
            name:"ML",
            value:Number(data.ml_score ?? 0)
        },

        {
            name:"Technical",
            value:Number(data.technical_score ?? 0)
        },

        {
            name:"News",
            value:Number(data.news_score ?? 0)
        },

        {
            name:"Research",
            value:Number(data.research_score ?? 0)
        },

        {
            name:"KAP",
            value:Number(data.kap_score ?? 0)
        },


    ];







    let color="#FFC107";

    let icon=<RemoveIcon/>;





    if(decision.includes("BUY")){

        color="#00C853";

        icon=<TrendingUpIcon/>;

    }





    if(decision.includes("SELL")){

        color="#F44336";

        icon=<TrendingDownIcon/>;

    }







    return (


        <Paper


            sx={{


                height:360,

                p:2,

                bgcolor:"#10151d",

                border:"1px solid #243041",

                borderRadius:4,

                overflow:"hidden",


            }}



        >



            <Stack spacing={1} height="100%">






                <Typography

                    variant="h6"

                    fontWeight={700}

                    textAlign="center"

                >

                    🤖 AI INTELLIGENCE

                </Typography>







                <Box

                    sx={{

                        position:"relative",

                        display:"inline-flex",

                        alignSelf:"center"

                    }}

                >



                    <CircularProgress

                        variant="determinate"

                        value={100}

                        size={110}

                        thickness={5}

                        sx={{

                            color:"#263238",

                            position:"absolute"

                        }}

                    />



                    <CircularProgress

                        variant="determinate"

                        value={Math.min(score,100)}

                        size={110}

                        thickness={5}

                        sx={{

                            color

                        }}

                    />




                    <Box

                        sx={{

                            inset:0,

                            position:"absolute",

                            display:"flex",

                            justifyContent:"center",

                            alignItems:"center",

                            flexDirection:"column"

                        }}

                    >

                        <Typography

                            variant="h4"

                            fontWeight={700}

                        >

                            {score.toFixed(1)}

                        </Typography>


                        <Typography

                            fontSize={10}

                        >

                            AI SCORE

                        </Typography>


                    </Box>


                </Box>








                <Chip

                    icon={icon}

                    label={decision}

                    size="small"

                    sx={{

                        alignSelf:"center",

                        bgcolor:color,

                        color:"#fff",

                        fontWeight:700

                    }}

                />







                <Typography

                    textAlign="center"

                    fontSize={13}

                >

                    Confidence : {confidence.toFixed(1)}%

                </Typography>






                <Divider/>






                <Typography

                    variant="caption"

                    fontWeight={700}

                >

                    📊 AI COMPONENT SCORES

                </Typography>







                <Stack spacing={0.3}>


                    {

                    scores.map((item,index)=>(


                        <Box key={index}>


                            <Box

                                display="flex"

                                justifyContent="space-between"

                            >

                                <Typography fontSize={11}>

                                    {item.name}

                                </Typography>


                                <Typography fontSize={11}>

                                    {item.value.toFixed(1)}

                                </Typography>


                            </Box>




                            <LinearProgress

                                variant="determinate"

                                value={Math.min(item.value,100)}

                                sx={{

                                    height:3

                                }}

                            />



                        </Box>


                    ))

                    }


                </Stack>








                <Divider/>






                <Box>


                    <Typography fontSize={11}>

                        ✅ Güçlü Yönler

                    </Typography>


                    <Stack

                        direction="row"

                        spacing={0.5}

                        sx={{

                            overflow:"hidden"

                        }}

                    >


                        {

                        strengths.length

                        ?

                        strengths.slice(0,2).map((x,i)=>(

                            <Chip

                                key={i}

                                size="small"

                                color="success"

                                label={x}

                            />

                        ))

                        :

                        <Chip

                            size="small"

                            label="-"

                        />


                        }


                    </Stack>


                </Box>







                <Box>


                    <Typography fontSize={11}>

                        ⚠ Riskler

                    </Typography>


                    <Stack

                        direction="row"

                        spacing={0.5}

                    >

                        {

                        weaknesses.length

                        ?

                        weaknesses.slice(0,2).map((x,i)=>(

                            <Chip

                                key={i}

                                size="small"

                                color="warning"

                                label={x}

                            />

                        ))

                        :

                        <Chip

                            size="small"

                            label="-"

                        />


                        }


                    </Stack>


                </Box>







                <Divider/>






                <Box

                    sx={{

                        flex:1,

                        overflow:"hidden"

                    }}

                >



                    <Typography

                        fontSize={11}

                        fontWeight={700}

                    >

                        🧠 Explainable AI

                    </Typography>






                    <List

                        dense

                        sx={{

                            maxHeight:55,

                            overflow:"auto",

                            p:0

                        }}

                    >



                    {

                    explanations.length

                    ?

                    explanations.map((x,i)=>(


                        <ListItem

                            key={i}

                            sx={{py:0}}

                        >

                            <ListItemText

                                primary={x}

                                primaryTypographyProps={{

                                    fontSize:11

                                }}

                            />

                        </ListItem>


                    ))

                    :

                    <ListItem sx={{py:0}}>

                        <ListItemText primary="-"/>

                    </ListItem>


                    }



                    </List>



                </Box>






            </Stack>



        </Paper>


    );


}