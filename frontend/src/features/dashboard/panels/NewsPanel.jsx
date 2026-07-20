import {

    Paper,
    Typography,
    Stack,
    Chip

} from "@mui/material";

import { useEffect,useState } from "react";

import axios from "../../../api/api";

export default function NewsPanel(){

    const [news,setNews]=useState([]);

    useEffect(()=>{

        load();

    },[]);

    async function load(){

        const res=await axios.post(

            "/news",

            {

                symbol:"ASELS"

            }

        );

        setNews(res.data.news||[]);

    }

    return(

        <Paper sx={{p:2,height:340,overflow:"auto"}}>

            <Typography variant="h6" mb={2}>

                Live News

            </Typography>

            <Stack spacing={2}>

                {

                    news.map((n,i)=>(

                        <Paper

                            key={i}

                            sx={{p:2}}

                        >

                            <Chip

                                size="small"

                                label={n.source}

                            />

                            <Typography mt={1}>

                                {n.title}

                            </Typography>

                        </Paper>

                    ))

                }

            </Stack>

        </Paper>

    );

}