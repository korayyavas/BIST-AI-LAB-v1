import {
    Box,
    Stack,
    Typography,
    Chip,
    CircularProgress
} from "@mui/material";

import DescriptionIcon from "@mui/icons-material/Description";

import { useEffect, useState } from "react";

import axios from "../api/api";

export default function ResearchPanel({ symbol }) {

    const [reports, setReports] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (!symbol) return;

        loadReports();

    }, [symbol]);

    const loadReports = async () => {

        try {

            setLoading(true);

            const res = await axios.post(

                "/research",

                {

                    symbol

                }

            );

            setReports(

                res.data.reports || []

            );

        }

        catch {

            setReports([]);

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

                mt={8}

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

                AI Research

            </Typography>

            <Stack spacing={2}>

                {

                    reports.length===0 &&

                    <Typography color="gray">

                        No research found.

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

                                alignItems="center"

                            >

                                <Typography

                                    variant="h6"

                                    fontWeight={700}

                                >

                                    {r.broker}

                                </Typography>

                                <Chip

                                    icon={<DescriptionIcon/>}

                                    label={r.recommendation}

                                    color={

                                        r.recommendation==="BUY"

                                        ? "success"

                                        : r.recommendation==="SELL"

                                        ? "error"

                                        : "warning"

                                    }

                                />

                            </Stack>

                            <Typography

                                mt={2}

                                color="#9ca3af"

                            >

                                {r.title}

                            </Typography>

                            <Typography

                                mt={2}

                            >

                                {r.summary}

                            </Typography>

                            <Stack

                                direction="row"

                                spacing={4}

                                mt={3}

                            >

                                <Typography>

                                    Target

                                    <br/>

                                    <b>

                                        ₺ {r.target_price}

                                    </b>

                                </Typography>

                                <Typography>

                                    Confidence

                                    <br/>

                                    <b>

                                        {r.confidence}%

                                    </b>

                                </Typography>

                            </Stack>

                        </Box>

                    ))

                }

            </Stack>

        </>

    );

}