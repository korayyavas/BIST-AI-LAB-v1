import {

    Box,

    Grid,

    Typography,

    Paper,

    Stack,

    Button,

    TextField

} from "@mui/material";

import { useState } from "react";

import axios from "../api/api";

import ScoreCard from "../components/ScoreCard";
import PortfolioTable from "../components/PortfolioTable";
import RadarChart from "../components/RadarChart";
import NewsPanel from "../components/NewsPanel";
import ResearchPanel from "../components/ResearchPanel";

export default function Dashboard(){

    const [symbol,setSymbol]=useState("ASELS");

    const [data,setData]=useState(null);

    const analyze=async()=>{

        const res=await axios.post(

            "/intelligence",

            {

                symbol

            }

        );

        setData(res.data);

    };

    return(

        <Box
            sx={{
                p:3,
                minHeight:"100vh",
                bgcolor:"#090c10"
            }}
        >

            <Grid
                container
                spacing={2}
            >

                <Grid item xs={12}>

                    <Paper
                        className="card glow"
                    >

                        <Stack
                            direction="row"
                            justifyContent="space-between"
                            alignItems="center"
                        >

                            <Typography
                                variant="h3"
                            >

                                BIST AI LAB

                            </Typography>

                            <Stack
                                direction="row"
                                spacing={2}
                            >

                                <TextField

                                    size="small"

                                    value={symbol}

                                    onChange={(e)=>

                                        setSymbol(

                                            e.target.value.toUpperCase()

                                        )

                                    }

                                />

                                <Button

                                    variant="contained"

                                    onClick={analyze}

                                >

                                    ANALYZE

                                </Button>

                            </Stack>

                        </Stack>

                    </Paper>

                </Grid>

                <Grid item xs={2.5}>

                    <Paper
                        className="card"
                        sx={{
                            height:850,
                            overflow:"auto"
                        }}
                    >

                        <PortfolioTable/>

                    </Paper>

                </Grid>

                <Grid item xs={9.5}>

                    <Grid
                        container
                        spacing={2}
                    >

                        <Grid item xs={12}>

                            <ScoreCard
                                data={data}
                            />

                        </Grid>

                        <Grid item xs={6}>

                            <Paper
                                className="card glow"
                                sx={{
                                    height:350
                                }}
                            >

                                <RadarChart
                                    data={data}
                                />

                            </Paper>

                        </Grid>

                        <Grid item xs={6}>

                            <Paper
                                className="card"
                                sx={{
                                    height:350,
                                    overflow:"auto"
                                }}
                            >

                                <NewsPanel
                                    symbol={symbol}
                                />

                            </Paper>

                        </Grid>

                        <Grid item xs={12}>

                            <Paper
                                className="card"
                                sx={{
                                    height:260,
                                    overflow:"auto"
                                }}
                            >

                                <ResearchPanel
                                    symbol={symbol}
                                />

                            </Paper>

                        </Grid>

                    </Grid>

                </Grid>

            </Grid>

        </Box>

    );

}