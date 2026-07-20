import {
    Paper,
    Typography,
    Stack,
    Chip,
    Box,
    CircularProgress
} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";

import { useEffect, useState } from "react";

import axios from "../../../api/api";

export default function PortfolioPanel(){

    const [items,setItems]=useState([]);

    const [loading,setLoading]=useState(true);

    useEffect(()=>{

        load();

    },[]);

    async function load(){

        try{

            const res=await axios.post(

                "/top-picks",

                {

                    top:10,

                    signal:"ALL",

                    min_confidence:0

                }

            );

            setItems(res.data.top_picks||[]);

        }

        finally{

            setLoading(false);

        }

    }

    if(loading)

        return(

            <Paper sx={{height:340,display:"flex",justifyContent:"center",alignItems:"center"}}>

                <CircularProgress/>

            </Paper>

        );

    return(

        <Paper sx={{p:2,height:340}}>

            <Typography variant="h6" mb={2}>

                Watchlist

            </Typography>

            <Stack spacing={1}>

                {

                    items.map((x,i)=>{

                        let color="warning";

                        let icon=<RemoveIcon/>;

                        if(x.signal?.includes("BUY")){

                            color="success";

                            icon=<TrendingUpIcon/>;

                        }

                        if(x.signal?.includes("SELL")){

                            color="error";

                            icon=<TrendingDownIcon/>;

                        }

                        return(

                            <Box

                                key={i}

                                sx={{

                                    display:"flex",

                                    justifyContent:"space-between",

                                    alignItems:"center",

                                    p:1,

                                    borderBottom:"1px solid #222"

                                }}

                            >

                                <Box>

                                    <Typography fontWeight={700}>

                                        {x.symbol}

                                    </Typography>

                                    <Typography variant="caption">

                                        {Math.round(x.confidence)}%

                                    </Typography>

                                </Box>

                                <Chip

                                    icon={icon}

                                    label={x.signal}

                                    color={color}

                                />

                            </Box>

                        );

                    })

                }

            </Stack>

        </Paper>

    );

}