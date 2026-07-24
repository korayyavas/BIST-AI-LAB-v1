import { useEffect, useState } from "react";

import {
    Paper,
    Typography,
    Stack,
    Box,
    Chip,
    CircularProgress,
    Divider,
} from "@mui/material";


import apiClient from "../../../services/apiClient";





export default function PortfolioPanel(){


    const [portfolio,setPortfolio] = useState(null);

    const [loading,setLoading] = useState(true);





    useEffect(()=>{


        async function loadPortfolio(){


            try{


                const response = await apiClient.get(
                    "/portfolio"
                );


                setPortfolio(
                    response.data
                );


            }

            catch(error){

                console.error(
                    "Portfolio error",
                    error
                );

            }

            finally{

                setLoading(false);

            }


        }



        loadPortfolio();


    },[]);








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






    if(!portfolio){

        return null;

    }







    const risk =

        portfolio.risk ?? {};






    const riskColor =


        risk.risk_level === "HIGH"

        ? "error"

        :

        risk.risk_level === "MEDIUM"

        ? "warning"

        :

        "success";







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

                mb={2}

            >

                💼 Portfolio Intelligence

            </Typography>






            <Stack spacing={1.5}>





                <Box>


                    <Typography variant="caption">

                        Portfolio Value

                    </Typography>


                    <Typography

                        variant="h5"

                        fontWeight={700}

                    >

                        {portfolio.portfolio_value}

                    </Typography>


                </Box>






                <Box>


                    <Typography variant="caption">

                        Profit / Loss

                    </Typography>


                    <Typography

                        color="success.main"

                        fontWeight={700}

                    >

                        +{portfolio.profit_loss}

                    </Typography>


                </Box>







                <Chip

                    label={

                        `AI Portfolio Score ${portfolio.portfolio_ai_score}`

                    }

                    color="primary"

                />







                <Chip

                    label={

                        `Risk ${risk.risk_level} (${risk.risk_score})`

                    }

                    color={riskColor}

                />








                <Divider />







                <Typography

                    fontWeight={700}

                >

                    Positions

                </Typography>






                {

                    portfolio.positions?.map(item=>(


                        <Box

                            key={item.symbol}

                            sx={{

                                borderTop:

                                "1px solid #243041",

                                pt:1

                            }}

                        >


                            <Typography

                                fontWeight={700}

                            >

                                {item.symbol}

                            </Typography>



                            <Typography variant="body2">

                                Adet: {item.quantity}

                            </Typography>



                            <Typography variant="body2">

                                Ağırlık: %{item.weight}

                            </Typography>



                            <Typography variant="body2">

                                AI Score: {item.ai_score}

                            </Typography>



                        </Box>


                    ))

                }









                {

                    risk.warnings?.length > 0 &&


                    <Box>


                        <Typography

                            color="error.main"

                            fontWeight={700}

                        >

                            Risk Warnings

                        </Typography>



                        {

                            risk.warnings.map(

                                (warning,index)=>(


                                    <Typography

                                        key={index}

                                        variant="body2"

                                    >

                                        ⚠️ {warning}

                                    </Typography>


                                )

                            )

                        }


                    </Box>


                }





            </Stack>



        </Paper>


    );

}