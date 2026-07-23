import {
    Paper,
    Typography,
    Stack,
    Chip,
    CircularProgress,
    Divider,
    Box,
} from "@mui/material";


export default function KapPanel({

    events = [],

    loading = false,

}) {



    if (loading) {


        return (


            <Paper

                sx={{

                    p:2,

                    height:420,

                    display:"flex",

                    justifyContent:"center",

                    alignItems:"center",

                }}

            >


                <CircularProgress />


            </Paper>


        );


    }





    function getValue(obj, keys, fallback="-") {


        for (const key of keys) {


            if (

                obj &&

                obj[key] !== undefined &&

                obj[key] !== null

            ) {

                return obj[key];

            }


        }


        return fallback;


    }






    const data = Array.isArray(events)

        ? events

        : events?.kap ??

          events?.events ??

          [];







    return (


        <Paper


            sx={{


                p:2,

                height:420,

                overflow:"auto",

                bgcolor:"#10151d",

                border:"1px solid #243041",

                borderRadius:3,


            }}


        >



            <Typography

                variant="h6"

                mb={2}

                fontWeight={700}

            >

                📢 KAP Timeline

            </Typography>





            {

                data.length === 0 && (


                    <Typography color="text.secondary">


                        KAP bildirimi bulunamadı.


                    </Typography>


                )


            }





            <Stack spacing={2}>


                {


                    data.map((item,index)=>{



                        const title = getValue(

                            item,

                            [

                                "title",

                                "headline",

                                "subject",

                                "description"

                            ],

                            "KAP Bildirimi"

                        );





                        const type = getValue(

                            item,

                            [

                                "event_type",

                                "type",

                                "category"

                            ],

                            "INFO"

                        );





                        const score = getValue(

                            item,

                            [

                                "score",

                                "impact_score",

                                "rating"

                            ],

                            "-"

                        );





                        const date = getValue(

                            item,

                            [

                                "date",

                                "published_at",

                                "created_at"

                            ],

                            ""

                        );





                        let chipColor="default";



                        const text = String(type).toUpperCase();




                        if(

                            text.includes("POSITIVE") ||

                            text.includes("GOOD") ||

                            text.includes("BUY")

                        ){

                            chipColor="success";

                        }




                        if(

                            text.includes("NEGATIVE") ||

                            text.includes("RISK") ||

                            text.includes("SELL")

                        ){

                            chipColor="error";

                        }






                        return (


                            <Paper


                                key={index}


                                variant="outlined"


                                sx={{


                                    p:2,

                                    bgcolor:"#161d28",

                                    borderRadius:2,


                                }}



                            >



                                <Typography

                                    fontWeight={700}

                                >

                                    {title}


                                </Typography>





                                <Divider

                                    sx={{my:1}}

                                />





                                <Stack

                                    direction="row"

                                    spacing={1}

                                    flexWrap="wrap"

                                >



                                    <Chip


                                        size="small"

                                        label={type}

                                        color={chipColor}


                                    />



                                    {

                                        date && (


                                            <Chip

                                                size="small"

                                                label={date}

                                            />


                                        )

                                    }



                                </Stack>







                                <Box mt={1}>


                                    <Typography

                                        variant="body2"

                                    >


                                        Etki Skoru :

                                        {" "}

                                        {score}


                                    </Typography>



                                </Box>





                            </Paper>


                        );


                    })


                }


            </Stack>



        </Paper>


    );


}