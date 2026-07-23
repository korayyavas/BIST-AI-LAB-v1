import {

    Box,

    Stack,

    Typography,

    Chip,

} from "@mui/material";



export default function ResearchPanel({

    reports = [],

    loading = false,

}) {


    if(loading){

        return (

            <Typography>

                Araştırma yükleniyor...

            </Typography>

        );

    }



    return (

        <>

            <Typography

                variant="h5"

                mb={2}

                fontWeight={700}

            >

                📄 Research Intelligence

            </Typography>



            <Stack spacing={2}>


                {

                    reports.length===0 &&

                    <Typography color="gray">

                        Araştırma raporu bulunamadı.

                    </Typography>

                }



                {

                    reports.map((r,index)=>(


                        <Box

                            key={index}

                            sx={{

                                p:2,

                                borderRadius:3,

                                bgcolor:"#161b22",

                                border:"1px solid #26313d"

                            }}

                        >


                            <Stack

                                direction="row"

                                justifyContent="space-between"

                            >


                                <Typography

                                    fontWeight={700}

                                >

                                    {r.broker || "Research"}

                                </Typography>


                                <Chip

                                    label={

                                        r.recommendation ||

                                        "NEUTRAL"

                                    }

                                />


                            </Stack>



                            <Typography mt={2}>

                                {r.title}

                            </Typography>



                            <Typography

                                mt={1}

                                color="#9ca3af"

                            >

                                {r.summary}

                            </Typography>



                            <Typography mt={1}>

                                Target:

                                {" "}

                                ₺{r.target_price || "-"}

                            </Typography>


                        </Box>


                    ))

                }


            </Stack>


        </>

    );

}