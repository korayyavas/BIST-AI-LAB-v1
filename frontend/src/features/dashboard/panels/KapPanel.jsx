import {

    Paper,
    Typography,
    Stack

} from "@mui/material";

import { useEffect,useState } from "react";

import axios from "../../../api/api";

export default function KapPanel(){

    const [items,setItems]=useState([]);

    useEffect(()=>{

        load();

    },[]);

    async function load(){

        try{

            const res=await axios.post(

                "/kap",

                {

                    symbol:"ASELS"

                }

            );

            setItems(

                res.data.events ||

                res.data.kap ||

                []

            );

        }

        catch{

            setItems([]);

        }

    }

    return(

        <Paper sx={{p:2,height:420,overflow:"auto"}}>

            <Typography variant="h6" mb={2}>

                KAP Timeline

            </Typography>

            <Stack spacing={2}>

                {

                    items.map((k,i)=>(

                        <Paper key={i} sx={{p:2}}>

                            <Typography fontWeight={700}>

                                {k.title}

                            </Typography>

                            <Typography variant="body2">

                                {k.event_type}

                            </Typography>

                        </Paper>

                    ))

                }

            </Stack>

        </Paper>

    );

}