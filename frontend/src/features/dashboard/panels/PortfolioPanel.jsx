import {
    Paper,
    Typography,
    Stack,
    Chip,
    Box,
    CircularProgress,
    LinearProgress,
} from "@mui/material";


import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";


import { useEffect, useState } from "react";

import axios from "../../../api/api";




export default function PortfolioPanel(){



    const [items,setItems] = useState([]);

    const [loading,setLoading] = useState(true);





    useEffect(()=>{

        load();

    },[]);






    async function load(){


        setLoading(true);


        try{


            const res = await axios.post(

                "/top-picks",

                {

                    top:10,

                    signal:"ALL",

                    min_confidence:0,

                }

            );



            setItems(

                res.data.top_picks ??

                res.data.items ??

                []

            );


        }

        catch(e){


            console.error(

                "Portfolio load error",

                e

            );


            setItems([]);


        }

        finally{


            setLoading(false);


        }


    }







    function safeNumber(

        value,

        fallback=0

    ){


        const n = Number(value);


        return Number.isFinite(n)

            ?

            n

            :

            fallback;


    }








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







    return (



        <Paper


            sx={{


                p:1.5,

                height:360,

                bgcolor:"#10151d",

                border:"1px solid #243041",

                borderRadius:4,

                overflow:"hidden",


            }}



        >





            <Typography

                variant="h6"

                fontWeight={700}

                mb={1}


            >


                📈 AI WATCHLIST


            </Typography>







            <Box

                sx={{

                    height:"calc(100% - 40px)",

                    overflow:"auto",

                    pr:0.5,

                }}

            >




                {

                items.length===0 &&


                <Typography>

                    Veri bulunamadı.

                </Typography>


                }






                <Stack spacing={1}>


                {


                items.map((item,index)=>{



                    const signal =

                        item.signal ??

                        "HOLD";




                    const confidence =

                        safeNumber(

                            item.confidence ??

                            item.confidence_score

                        );




                    const risk =

                        safeNumber(

                            item.risk_score

                        );




                    const score =

                        safeNumber(

                            item.top_score ??

                            item.score

                        );





                    let color="warning";

                    let icon=<RemoveIcon/>;





                    if(signal.includes("BUY")){


                        color="success";

                        icon=<TrendingUpIcon/>;


                    }





                    if(signal.includes("SELL")){


                        color="error";

                        icon=<TrendingDownIcon/>;


                    }







                    return (



                        <Paper


                            key={item.symbol ?? index}


                            variant="outlined"


                            sx={{


                                p:1,

                                bgcolor:"#161d28",

                                borderRadius:2,


                            }}



                        >





                            <Box

                                display="flex"

                                justifyContent="space-between"

                                alignItems="center"

                            >



                                <Typography

                                    fontWeight={700}

                                    fontSize={14}

                                >

                                    {item.symbol}


                                </Typography>




                                <Chip


                                    icon={icon}

                                    color={color}

                                    label={signal}

                                    size="small"


                                />



                            </Box>







                            <Typography

                                variant="caption"

                            >


                                Confidence {confidence.toFixed(1)}%


                            </Typography>





                            <LinearProgress


                                variant="determinate"


                                value={Math.min(

                                    confidence,

                                    100

                                )}


                                sx={{


                                    mt:.3,

                                    height:5,

                                    borderRadius:5,


                                }}



                            />







                            <Stack


                                direction="row"

                                spacing={.5}

                                mt={.8}


                            >



                                <Chip

                                    size="small"

                                    label={

                                        `Risk ${risk.toFixed(0)}`

                                    }

                                />




                                <Chip

                                    size="small"

                                    color="primary"

                                    label={

                                        `AI ${score.toFixed(1)}`

                                    }

                                />


                            </Stack>





                        </Paper>


                    );


                })


                }



                </Stack>





            </Box>





        </Paper>



    );

}