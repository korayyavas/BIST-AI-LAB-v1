import {

    Box,
    Card,
    CardContent,
    Typography,
    Chip,
    Stack,
    CircularProgress

} from "@mui/material";


import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";


import { useEffect, useState } from "react";


import axios from "../api/api";



export default function PortfolioTable(){


    const [stocks, setStocks] = useState([]);


    const [loading, setLoading] = useState(false);




    useEffect(()=>{


        load();


    },[]);





    const load = async()=>{


        try{


            setLoading(true);



            const res = await axios.post(

                "/top-picks",

                {

                    top:10,

                    signal:"ALL",

                    min_confidence:0

                }

            );



            console.log(

                "TOP PICKS RESPONSE:",

                res.data

            );



            setStocks(

                res.data?.top_picks ?? []

            );



        }


        catch(error){


            console.error(

                "TOP PICKS ERROR:",

                error

            );


            setStocks([]);



        }


        finally{


            setLoading(false);



        }



    };






    if(loading){


        return(


            <Box

                display="flex"

                justifyContent="center"

                mt={8}

            >


                <CircularProgress/>


            </Box>


        );


    }







    return(


        <>


            <Typography

                variant="h5"

                mb={3}

                fontWeight={700}

            >

                AI Portfolio

            </Typography>





            {

                stocks.length === 0 && (


                    <Typography

                        color="#9ca3af"

                    >

                        Veri bekleniyor...

                    </Typography>


                )


            }






            <Stack spacing={2}>


                {


                    stocks.map((s,index)=>{



                        let color = "#ffc107";


                        let icon = <RemoveIcon/>;





                        if(

                            s.signal === "BUY" ||

                            s.signal === "STRONG BUY"

                        ){


                            color="#00e676";


                            icon=<TrendingUpIcon/>;


                        }





                        if(

                            s.signal === "SELL" ||

                            s.signal === "STRONG SELL"

                        ){


                            color="#ff5252";


                            icon=<TrendingDownIcon/>;


                        }






                        return(



                            <Card


                                key={

                                    s.symbol || index

                                }


                                sx={{


                                    bgcolor:"#161b22",


                                    border:"1px solid #283241",


                                    transition:".25s",


                                    "&:hover":{


                                        borderColor:"#3b82f6",


                                        transform:"translateY(-3px)"


                                    }


                                }}



                            >



                                <CardContent>



                                    <Stack


                                        direction="row"


                                        justifyContent="space-between"


                                        alignItems="center"


                                    >



                                        <Typography


                                            variant="h6"


                                            fontWeight={700}


                                        >


                                            {s.symbol}


                                        </Typography>





                                        <Chip


                                            icon={icon}


                                            label={s.signal}


                                            sx={{


                                                bgcolor:color,


                                                color:"white",


                                                fontWeight:700


                                            }}


                                        />



                                    </Stack>





                                    <Typography

                                        mt={2}

                                        color="#9ca3af"

                                    >

                                        Confidence


                                    </Typography>





                                    <Typography


                                        variant="h4"


                                        color={color}


                                    >


                                        {

                                            Math.round(

                                                s.confidence ?? 0

                                            )

                                        }%



                                    </Typography>





                                    <Typography


                                        mt={1}


                                        color="#9ca3af"


                                    >


                                        AI Score:

                                        {" "}

                                        {

                                            Math.round(

                                                s.score ??

                                                s.top_score ??

                                                0

                                            )

                                        }



                                    </Typography>





                                    <Typography


                                        mt={1}


                                        color="#9ca3af"


                                    >


                                        Risk:

                                        {" "}

                                        {

                                            Math.round(

                                                s.risk_score ?? 0

                                            )

                                        }



                                    </Typography>



                                </CardContent>



                            </Card>


                        );



                    })



                }



            </Stack>



        </>


    );



}