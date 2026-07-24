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




    const optimization =

        portfolio.optimization ?? {};




    const advisor =

        portfolio.advisor ?? {};




    const sector =

        portfolio.sector_analysis ?? {};




    const report =

        portfolio.report ?? {};




    const backtest =

        portfolio.backtest ?? {};






    const riskColor =


        risk.risk_level === "HIGH"

        ?

        "error"

        :

        risk.risk_level === "MEDIUM"

        ?

        "warning"

        :

        "success";







    const actionColor = (action)=>{


        if(action === "REDUCE")

            return "error";


        if(action === "INCREASE")

            return "success";


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

                    portfolio.positions?.map(item => (


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

                            ⚠️ Risk Warnings

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
                






                {

                    optimization.optimization?.length > 0 &&


                    <Box>


                        <Divider sx={{my:1}} />



                        <Typography

                            color="primary.main"

                            fontWeight={700}

                        >

                            🤖 AI Optimization

                        </Typography>





                        <Typography

                            variant="body2"

                            sx={{mb:1}}

                        >

                            {optimization.summary}

                        </Typography>






                        {

                            optimization.optimization.map(

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

                                                actionColor(

                                                    item.action

                                                )

                                            }

                                            label={item.action}

                                        />




                                        <Typography

                                            fontWeight={700}

                                            mt={0.5}

                                        >

                                            {item.symbol}

                                        </Typography>




                                        <Typography

                                            variant="body2"

                                        >

                                            {item.reason}

                                        </Typography>




                                    </Box>


                                )

                            )

                        }



                    </Box>


                }









                {

                    advisor.target_allocation?.length > 0 &&


                    <Box>


                        <Divider sx={{my:1}} />




                        <Typography

                            color="secondary.main"

                            fontWeight={700}

                        >

                            🧠 AI Advisor

                        </Typography>





                        <Typography

                            variant="body2"

                            sx={{mt:1}}

                        >

                            {advisor.summary}

                        </Typography>





                        <Chip

                            sx={{mt:1}}

                            label={

                                advisor.rebalance_required

                                ?

                                "REBALANCE REQUIRED"

                                :

                                "PORTFOLIO BALANCED"

                            }


                            color={

                                advisor.rebalance_required

                                ?

                                "error"

                                :

                                "success"

                            }

                        />







                        {

                            advisor.target_allocation.map(

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



                                        <Typography

                                            fontWeight={700}

                                        >

                                            {item.symbol}

                                        </Typography>





                                        <Typography

                                            variant="body2"

                                        >

                                            Mevcut:

                                            %

                                            {item.current_weight}

                                        </Typography>





                                        <Typography

                                            variant="body2"

                                        >

                                            Hedef:

                                            %

                                            {item.target_weight}

                                        </Typography>





                                        <Typography

                                            variant="body2"

                                            color={

                                                item.difference < 0

                                                ?

                                                "error.main"

                                                :

                                                "success.main"

                                            }

                                        >

                                            Fark:

                                            {item.difference}

                                        </Typography>



                                    </Box>


                                )

                            )

                        }



                    </Box>


                }
                








                {

                    sector.sectors &&


                    <Box>


                        <Divider sx={{my:1}} />



                        <Typography

                            color="info.main"

                            fontWeight={700}

                        >

                            📊 Sector Intelligence

                        </Typography>






                        <Chip

                            sx={{mt:1}}

                            label={

                                `Sector Risk ${sector.sector_risk}`

                            }

                            color={

                                sector.sector_risk === "HIGH"

                                ?

                                "error"

                                :

                                sector.sector_risk === "MEDIUM"

                                ?

                                "warning"

                                :

                                "success"

                            }

                        />






                        <Typography

                            variant="body2"

                            sx={{mt:1}}

                        >

                            {sector.summary}

                        </Typography>







                        {

                            Object.entries(

                                sector.sectors

                            ).map(

                                ([name,weight])=>(


                                    <Box

                                        key={name}

                                        sx={{

                                            borderTop:

                                            "1px solid #243041",

                                            pt:1,

                                            mt:1

                                        }}

                                    >



                                        <Typography

                                            fontWeight={700}

                                        >

                                            {name}

                                        </Typography>



                                        <Typography

                                            variant="body2"

                                        >

                                            Ağırlık:

                                            %

                                            {weight}

                                        </Typography>



                                    </Box>


                                )

                            )

                        }



                    </Box>


                }









                {

                    report.title &&


                    <Box>


                        <Divider sx={{my:1}} />



                        <Typography

                            color="warning.main"

                            fontWeight={700}

                        >

                            📄 AI Portfolio Report

                        </Typography>






                        <Typography

                            variant="subtitle2"

                            fontWeight={700}

                            sx={{mt:1}}

                        >

                            {report.title}

                        </Typography>






                        <Typography

                            variant="body2"

                            sx={{mt:1}}

                        >

                            {report.summary}

                        </Typography>







                        <Chip

                            sx={{mt:1}}

                            color="warning"

                            label={

                                report.recommendation

                            }

                        />



                    </Box>


                }









                {

                    backtest.initial_value &&


                    <Box>


                        <Divider sx={{my:1}} />



                        <Typography

                            color="success.main"

                            fontWeight={700}

                        >

                            📈 Backtest Intelligence

                        </Typography>






                        <Typography

                            variant="body2"

                            sx={{mt:1}}

                        >

                            Başlangıç Değeri:

                            {" "}

                            {backtest.initial_value}

                        </Typography>





                        <Typography

                            variant="body2"

                        >

                            Güncel Değer:

                            {" "}

                            {backtest.current_value}

                        </Typography>





                        <Typography

                            variant="body2"

                            color="success.main"

                        >

                            Getiri:

                            {" "}

                            %{backtest.return_percent}

                        </Typography>






                        <Typography

                            variant="body2"

                        >

                            Kâr/Zarar:

                            {" "}

                            {backtest.profit_loss}

                        </Typography>







                        <Chip

                            sx={{mt:1}}

                            color="success"

                            label={

                                `${backtest.benchmark?.name ?? "Benchmark"} karşılaştırması hazır`

                            }

                        />



                    </Box>


                }






            </Stack>



        </Paper>


    );

}