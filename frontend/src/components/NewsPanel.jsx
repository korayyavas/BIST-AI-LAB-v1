import {
    Typography,
    Box,
    Stack,
    Chip,
    CircularProgress
} from "@mui/material";

import PublicIcon from "@mui/icons-material/Public";

import { useEffect, useState } from "react";

import axios from "../api/api";

export default function NewsPanel({ symbol }) {

    const [news, setNews] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (!symbol) return;

        loadNews();

    }, [symbol]);

    const loadNews = async () => {

        try {

            setLoading(true);

            const res = await axios.post(

                "/news",

                {

                    symbol

                }

            );

            if (res.data.news) {

                setNews(res.data.news);

            } else {

                setNews([]);

            }

        }

        catch {

            setNews([]);

        }

        finally {

            setLoading(false);

        }

    };

    if (loading)

        return (

            <Box

                display="flex"

                justifyContent="center"

                mt={10}

            >

                <CircularProgress/>

            </Box>

        );

    return (

        <>

            <Typography

                variant="h5"

                mb={3}

                fontWeight={700}

            >

                Live News

            </Typography>

            <Stack spacing={2}>

                {

                    news.length===0 &&

                    <Typography color="gray">

                        No news found.

                    </Typography>

                }

                {

                    news.map((item,index)=>(

                        <Box

                            key={index}

                            sx={{

                                p:2,

                                borderRadius:3,

                                background:"#161b22",

                                border:"1px solid #26313d",

                                transition:".25s",

                                "&:hover":{

                                    borderColor:"#3b82f6",

                                    transform:"translateY(-2px)"

                                }

                            }}

                        >

                            <Stack

                                direction="row"

                                justifyContent="space-between"

                            >

                                <Chip

                                    icon={<PublicIcon/>}

                                    label={item.source}

                                    color="primary"

                                    size="small"

                                />

                                <Chip

                                    label={item.sentiment}

                                    color={

                                        item.sentiment==="POSITIVE"

                                        ? "success"

                                        : item.sentiment==="NEGATIVE"

                                        ? "error"

                                        : "warning"

                                    }

                                    size="small"

                                />

                            </Stack>

                            <Typography

                                mt={2}

                                fontWeight={600}

                            >

                                {item.title}

                            </Typography>

                            <Typography

                                mt={1}

                                color="#7d8590"

                            >

                                Score : {Math.round(item.score)}

                            </Typography>

                        </Box>

                    ))

                }

            </Stack>

        </>

    );

}