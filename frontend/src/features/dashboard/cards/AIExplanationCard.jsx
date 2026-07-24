import {
    Paper,
    Typography,
    Stack,
    Box,
    Chip,
} from "@mui/material";



export default function AIExplanationCard({

    intelligence = {},

}) {



    const explanations =

        intelligence.explanations ?? [];



    const strengths =

        intelligence.strengths ?? [];



    const weaknesses =

        intelligence.weaknesses ?? [];




    const decision =

        intelligence.decision ?? "HOLD";



    const confidence =

        intelligence.confidence ?? 0;






    const decisionColor =


        decision === "BUY"

            ? "success"

            :

        decision === "SELL"

            ? "error"

            :

            "warning";






    return (



        <Paper

            sx={{

                p:2,

                borderRadius:3,

                background:"#10151d",

                border:"1px solid #243041",

                height:"100%"

            }}

        >





            <Stack spacing={2}>



                <Box

                    display="flex"

                    justifyContent="space-between"

                    alignItems="center"

                >


                    <Typography

                        variant="h6"

                        fontWeight={700}

                    >

                        🧠 AI Decision

                    </Typography>



                    <Chip

                        label={decision}

                        color={decisionColor}

                        size="small"

                    />


                </Box>







                <Box>


                    <Typography

                        variant="caption"

                    >

                        Confidence

                    </Typography>



                    <Typography

                        variant="h5"

                        fontWeight={700}

                    >

                        {confidence}%

                    </Typography>


                </Box>









                <Box>


                    <Typography

                        fontWeight={700}

                        mb={1}

                    >

                        Neden?

                    </Typography>



                    <Stack spacing={1}>


                        {

                            explanations.length > 0

                            ?

                            explanations.map(

                                (item,index)=>(


                                    <Typography

                                        key={index}

                                        variant="body2"

                                    >

                                        • {item}

                                    </Typography>


                                )

                            )


                            :

                            <Typography

                                variant="body2"

                                color="gray"

                            >

                                Açıklama bulunamadı.

                            </Typography>


                        }


                    </Stack>


                </Box>









                {

                    strengths.length > 0 &&


                    <Box>


                        <Typography

                            color="success.main"

                            fontWeight={700}

                        >

                            Güçlü Noktalar

                        </Typography>



                        {

                            strengths.map(

                                (item,index)=>(


                                    <Typography

                                        key={index}

                                        variant="body2"

                                    >

                                        🟢 {item}

                                    </Typography>


                                )

                            )

                        }


                    </Box>


                }









                {

                    weaknesses.length > 0 &&


                    <Box>


                        <Typography

                            color="error.main"

                            fontWeight={700}

                        >

                            Riskler

                        </Typography>



                        {

                            weaknesses.map(

                                (item,index)=>(


                                    <Typography

                                        key={index}

                                        variant="body2"

                                    >

                                        🔴 {item}

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