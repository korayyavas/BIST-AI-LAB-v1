import {

    Paper,
    Typography,
    Stack,
    Chip

} from "@mui/material";

import { useEffect,useState } from "react";

import axios from "../../../api/api";

export default function ResearchPanel(){

    const [reports,setReports]=useState([]);

    useEffect(()=>{

        load();

    },[]);

    async function load(){

        const res=await axios.post(

            "/research",

            {

                symbol:"ASELS"

            }

        );

        setReports(res.data.reports||[]);

    }

    return(

        <Paper sx={{p:2,height:340,overflow:"auto"}}>

            <Typography variant="h6" mb={2}>

                Research

            </Typography>

            <Stack spacing={2}>

                {

                    reports.map((r,i)=>(

                        <Paper key={i} sx={{p:2}}>

                            <Typography fontWeight={700}>

                                {r.broker}

                            </Typography>

                            <Chip

                                label={r.recommendation}

                                color={

                                    r.recommendation==="BUY"

                                    ?"success"

                                    :"warning"

                                }

                                sx={{mt:1}}

                            />

                            <Typography mt={2}>

                                Target ₺ {r.target_price}

                            </Typography>

                            <Typography variant="body2">

                                {r.summary}

                            </Typography>

                        </Paper>

                    ))

                }

            </Stack>

        </Paper>

    );

}