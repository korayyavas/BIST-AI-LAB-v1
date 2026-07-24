import { useEffect, useState } from "react";

import {
    Paper,
    Typography,
    Box,
    Chip,
    CircularProgress,
    Divider,
} from "@mui/material";


import apiClient from "../../../services/apiClient";






export default function AIDecisionTimeline({

    symbol = "ASELS",

}){


    const [history,setHistory] = useState([]);

    const [loading,setLoading] = useState(true);







    useEffect(()=>{


        async function loadTimeline(){


            try{


                const response = await apiClient.get(

                    `/decision-timeline/${symbol}`

                );


                setHistory(

                    response.data.history ?? []

                );


            }


            catch(error){


                console.error(

                    "Decision timeline error",

                    error

                );


            }


            finally{


                setLoading(false);


            }


        }





        loadTimeline();




    },[symbol]);








    if(loading){


        return (

            <Paper

                sx={{

                    p:2,

                    background:"#10151d",

                    borderRadius:3

                }}

            >

                <CircularProgress size={25}/>


            </Paper>

        );


    }








    const decisionColor = (decision)=>{


        if(decision==="BUY")

            return "success";



        if(decision==="SELL")

            return "error";



        return "warning";


    };






    return (

        <Paper

            sx={{

                p:2,

                borderRadius:3,

                background:"#10151d",

                border:"1px solid #243041"

            }}

        >



            <Typography

                variant="h6"

                fontWeight={700}

            >

                🕒 AI Decision Timeline

            </Typography>





            <Divider sx={{my:1}} />






            {

                history.length === 0 &&


                <Typography

                    variant="body2"

                >

                    Henüz karar geçmişi bulunmuyor.

                </Typography>


            }
            



            {

                history.map(

                    (item,index)=>(


                        <Box

                            key={index}

                            sx={{

                                borderTop:

                                "1px solid #243041",

                                pt:1,

                                mt:1

                            }}

                        >




                            <Chip

                                size="small"

                                color={

                                    decisionColor(

                                        item.decision

                                    )

                                }

                                label={

                                    item.decision

                                }

                            />







                            <Typography

                                fontWeight={700}

                                sx={{mt:1}}

                            >

                                Score:

                                {" "}

                                {item.score}

                            </Typography>






                            <Typography

                                variant="body2"

                            >

                                Confidence:

                                {" "}

                                {item.confidence}

                            </Typography>






                            {

                                item.explanation?.map(

                                    (text,i)=>(


                                        <Typography

                                            key={i}

                                            variant="body2"

                                        >

                                            • {text}

                                        </Typography>


                                    )

                                )

                            }






                            <Typography

                                variant="caption"

                                color="text.secondary"

                            >

                                {item.timestamp}

                            </Typography>





                        </Box>


                    )

                )

            }





        </Paper>

    );


}