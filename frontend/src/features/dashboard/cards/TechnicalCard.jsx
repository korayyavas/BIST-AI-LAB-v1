import {
    Paper,
    Typography,
    Stack,
    Box,
    Chip,
} from "@mui/material";



export default function TechnicalCard({

    technical = {},

}) {



    const macd =
        technical.macd ?? {};



    const ma =
        technical.moving_average ?? {};



    const trendColor =

        technical.trend === "BULLISH"

            ? "success"

            :

        technical.trend === "BEARISH"

            ? "error"

            :

            "warning";




    const macdColor =

        macd.trend === "POSITIVE"

            ? "success"

            :

            "error";






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



            <Typography

                variant="h6"

                fontWeight={700}

                mb={2}

            >

                📈 Technical Intelligence

            </Typography>





            <Stack spacing={1.5}>



                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        Trend

                    </Typography>


                    <Chip

                        label={technical.trend ?? "N/A"}

                        color={trendColor}

                        size="small"

                    />


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        RSI

                    </Typography>


                    <Typography fontWeight={700}>

                        {technical.rsi ?? "-"}

                    </Typography>


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        MACD

                    </Typography>


                    <Chip

                        label={macd.trend ?? "-"}

                        color={macdColor}

                        size="small"

                    />


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        MA20

                    </Typography>


                    <Typography>

                        {ma.ma20 ?? "-"}

                    </Typography>


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        MA50

                    </Typography>


                    <Typography>

                        {ma.ma50 ?? "-"}

                    </Typography>


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        Support

                    </Typography>


                    <Typography>

                        {technical.support ?? "-"}

                    </Typography>


                </Box>







                <Box

                    display="flex"

                    justifyContent="space-between"

                >

                    <Typography>

                        Resistance

                    </Typography>


                    <Typography>

                        {technical.resistance ?? "-"}

                    </Typography>


                </Box>







                <Box

                    mt={1}

                    sx={{

                        p:1.5,

                        borderRadius:2,

                        background:"#18212d"

                    }}

                >


                    <Typography

                        variant="caption"

                    >

                        Technical Score

                    </Typography>



                    <Typography

                        variant="h4"

                        fontWeight={700}

                    >

                        {technical.score ?? 0}

                        /100

                    </Typography>


                </Box>



            </Stack>



        </Paper>


    );

}