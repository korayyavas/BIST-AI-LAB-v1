import {

    Card,
    CardContent,
    Grid,
    Typography,
    LinearProgress,
    Box,
    Chip,
    Stack

} from "@mui/material";


import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";



export default function ScoreCard({

    data = {}

}) {



    const score = Number(

        data.ai_score ?? 0

    );


    const decision =

        data.decision ??

        "HOLD";



    const confidence = Number(

        data.confidence ?? 0

    );



    const color =

        decision.includes("BUY")

            ? "#00e676"

            :

        decision.includes("SELL")

            ? "#ff5252"

            :

            "#ffc107";



    const icon =

        decision.includes("BUY")

            ?

            <TrendingUpIcon/>

            :

        decision.includes("SELL")

            ?

            <TrendingDownIcon/>

            :

            <RemoveIcon/>;



    const components = [

        {

            name:"ML",

            value:data.ml_score ?? 0

        },

        {

            name:"Technical",

            value:data.technical_score ?? 0

        },

        {

            name:"News",

            value:data.news_score ?? 0

        },

        {

            name:"Research",

            value:data.research_score ?? 0

        },

        {

            name:"KAP",

            value:data.kap_score ?? 0

        }

    ];



    return (

        <Card

            className="card glow"

        >

            <CardContent>


                <Grid

                    container

                    spacing={3}

                    alignItems="center"

                >



                    <Grid item xs={3}>


                        <Typography

                            color="#8b949e"

                        >

                            AI DECISION

                        </Typography>



                        <Chip

                            icon={icon}

                            label={decision}

                            sx={{

                                mt:2,

                                bgcolor:color,

                                color:"#fff",

                                fontWeight:700,

                                fontSize:16

                            }}

                        />



                    </Grid>






                    <Grid item xs={3}>


                        <Typography

                            color="#8b949e"

                        >

                            AI SCORE

                        </Typography>



                        <Typography

                            variant="h1"

                            fontWeight={800}

                            sx={{

                                color

                            }}

                        >

                            {score.toFixed(1)}

                        </Typography>



                        <LinearProgress

                            variant="determinate"

                            value={score}

                            sx={{

                                height:10,

                                borderRadius:10

                            }}

                        />



                    </Grid>







                    <Grid item xs={2}>


                        <Typography

                            color="#8b949e"

                        >

                            Confidence

                        </Typography>


                        <Typography

                            variant="h4"

                        >

                            {confidence.toFixed(1)}%

                        </Typography>



                    </Grid>







                    <Grid item xs={4}>


                        <Typography

                            color="#8b949e"

                            mb={1}

                        >

                            Intelligence Modules

                        </Typography>




                        <Stack spacing={1}>


                            {

                                components.map((item,index)=>(


                                    <Box key={index}>


                                        <Stack

                                            direction="row"

                                            justifyContent="space-between"

                                        >


                                            <Typography

                                                variant="caption"

                                            >

                                                {item.name}

                                            </Typography>



                                            <Typography

                                                variant="caption"

                                            >

                                                {Number(item.value).toFixed(1)}

                                            </Typography>



                                        </Stack>




                                        <LinearProgress

                                            variant="determinate"

                                            value={Number(item.value)}

                                        />



                                    </Box>


                                ))

                            }



                        </Stack>



                    </Grid>




                </Grid>



            </CardContent>


        </Card>

    );


}