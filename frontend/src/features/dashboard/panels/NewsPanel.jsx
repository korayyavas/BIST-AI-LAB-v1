import {
    Typography,
    Box,
    Stack,
    Chip,
} from "@mui/material";

import PublicIcon from "@mui/icons-material/Public";



export default function NewsPanel({

    news = [],

    loading = false,

}) {



    if(loading){

        return (

            <Typography>

                Haberler yükleniyor...

            </Typography>

        );

    }




    return (

        <Box

            sx={{

                height:"100%",

                overflow:"hidden"

            }}

        >


            <Typography

                variant="h6"

                mb={1}

                fontWeight={700}

            >

                📰 AI NEWS INTELLIGENCE

            </Typography>





            <Box

                sx={{

                    height:"calc(100% - 40px)",

                    overflow:"auto",

                    pr:1

                }}

            >


                <Stack spacing={1.2}>


                    {

                    news.length===0 &&

                    <Typography color="gray">

                        Haber bulunamadı.

                    </Typography>

                    }





                    {

                    news.map((item,index)=>(


                        <Box

                            key={index}

                            sx={{

                                p:1.5,

                                borderRadius:3,

                                background:"#161b22",

                                border:"1px solid #26313d"

                            }}

                        >




                            <Stack

                                direction="row"

                                justifyContent="space-between"

                                alignItems="center"

                                spacing={1}

                            >



                                <Chip

                                    icon={<PublicIcon/>}

                                    label={

                                        item.source || "NEWS"

                                    }

                                    size="small"

                                    color="primary"

                                />





                                <Chip

                                    label={

                                        item.market_effect ||

                                        item.sentiment ||

                                        "UNKNOWN"

                                    }

                                    size="small"

                                    color={

                                        item.market_effect==="POZITIF"

                                        ?

                                        "success"

                                        :

                                        item.market_effect==="NEGATIF"

                                        ?

                                        "error"

                                        :

                                        "warning"

                                    }

                                />



                            </Stack>







                            <Typography

                                mt={1}

                                fontWeight={700}

                                sx={{

                                    display:"-webkit-box",

                                    WebkitLineClamp:2,

                                    WebkitBoxOrient:"vertical",

                                    overflow:"hidden"

                                }}

                            >

                                {

                                    item.title_tr ||

                                    item.title ||

                                    "-"

                                }


                            </Typography>







                            <Typography

                                mt={0.5}

                                color="#9ca3af"

                                fontSize={14}

                                sx={{

                                    display:"-webkit-box",

                                    WebkitLineClamp:2,

                                    WebkitBoxOrient:"vertical",

                                    overflow:"hidden"

                                }}

                            >

                                {

                                    item.summary ||

                                    "-"

                                }


                            </Typography>







                            <Typography

                                mt={0.5}

                                fontSize={13}

                            >

                                🤖 AI:

                                {" "}

                                {

                                    item.ai_comment ||

                                    "-"

                                }


                            </Typography>







                            <Typography

                                mt={0.5}

                                color="#60a5fa"

                                fontSize={13}

                            >

                                AI Score:

                                {" "}

                                {

                                    Math.round(

                                        item.score || 0

                                    )

                                }


                            </Typography>





                        </Box>


                    ))

                    }



                </Stack>


            </Box>


        </Box>


    );

}