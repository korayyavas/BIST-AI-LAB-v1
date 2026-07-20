import {

    Paper,
    Typography,
    Box,
    CircularProgress,
    Stack,
    Chip

} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";

import { useEffect,useState } from "react";

import axios from "../../../api/api";

export default function AIScoreCard(){

    const [data,setData]=useState(null);

    useEffect(()=>{

        load();

    },[]);

    const load=async()=>{

        const res=await axios.post(

            "/intelligence",

            {

                symbol:"ASELS"

            }

        );

        setData(res.data);

    };

    if(!data)

        return(

            <Paper
                sx={{
                    height:340,
                    display:"flex",
                    justifyContent:"center",
                    alignItems:"center"
                }}
            >

                <CircularProgress/>

            </Paper>

        );

    let color="#ffc107";

    let icon=<RemoveIcon/>;

    if(data.decision.includes("BUY")){

        color="#00e676";

        icon=<TrendingUpIcon/>;

    }

    if(data.decision.includes("SELL")){

        color="#ff5252";

        icon=<TrendingDownIcon/>;

    }

    return(

        <Paper

            sx={{

                p:4,

                height:340,

                background:"#11161d",

                border:"1px solid #243041",

                borderRadius:4

            }}

        >

            <Stack

                alignItems="center"

                spacing={2}

            >

                <Typography

                    variant="h5"

                >

                    AI SCORE

                </Typography>

                <Box

                    sx={{

                        position:"relative",

                        display:"inline-flex"

                    }}

                >

                    <CircularProgress

                        variant="determinate"

                        value={100}

                        size={180}

                        thickness={2}

                        sx={{

                            color:"#1f2937",

                            position:"absolute"

                        }}

                    />

                    <CircularProgress

                        variant="determinate"

                        value={data.ai_score}

                        size={180}

                        thickness={5}

                        sx={{

                            color

                        }}

                    />

                    <Box

                        sx={{

                            top:0,

                            left:0,

                            bottom:0,

                            right:0,

                            position:"absolute",

                            display:"flex",

                            alignItems:"center",

                            justifyContent:"center",

                            flexDirection:"column"

                        }}

                    >

                        <Typography

                            variant="h2"

                            fontWeight={700}

                        >

                            {data.ai_score}

                        </Typography>

                        <Typography>

                            {data.symbol}

                        </Typography>

                    </Box>

                </Box>

                <Chip

                    icon={icon}

                    label={data.decision}

                    sx={{

                        bgcolor:color,

                        color:"white",

                        fontWeight:700

                    }}

                />

                <Typography>

                    Confidence {data.confidence}%

                </Typography>

            </Stack>

        </Paper>

    );

}