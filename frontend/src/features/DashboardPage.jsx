import { useMemo } from "react";

import {
    Alert,
    Box,
    Grid,
    Stack,
    Typography,
} from "@mui/material";


import { useDashboard } from "./dashboard/hooks";

import {
    DashboardProvider,
    useDashboardContext,
} from "./dashboard/DashboardContext";


import AIScoreCard from "./dashboard/cards/AIScoreCard";
import KPICard from "./dashboard/cards/KPICard";

import TradingChart from "./dashboard/charts/TradingChart";
import RadarChart from "./dashboard/charts/RadarChart";

import PortfolioPanel from "./dashboard/panels/PortfolioPanel";
import NewsPanel from "./dashboard/panels/NewsPanel";
import ResearchPanel from "./dashboard/panels/ResearchPanel";
import KapPanel from "./dashboard/panels/KapPanel";

import StatusBar from "./dashboard/widgets/StatusBar";





function DashboardContent(){


    const { selectedSymbol } = useDashboardContext();



    const {
        loading,
        error,
        data,
    } = useDashboard(selectedSymbol);






    const intelligence = useMemo(()=>{


        const backendIntel =
            data?.intelligence ?? {};


        const consensus =
            data?.consensus ?? {};



        let explanations =
            backendIntel.explanations ??
            consensus.explanations ??
            [];



        if(
            explanations.length === 0 &&
            typeof consensus.explanation === "string"
        ){

            explanations =
                consensus.explanation
                .split("|")
                .map(x=>x.trim())
                .filter(Boolean);

        }



        return {


            ai_score:
                backendIntel.ai_score ??
                consensus.score ??
                0,


            decision:
                backendIntel.decision ??
                consensus.decision ??
                "HOLD",


            confidence:
                backendIntel.confidence ??
                50,


            ml_score:
                backendIntel.ml_score ?? 0,


            technical_score:
                backendIntel.technical_score ?? 0,


            news_score:
                backendIntel.news_score ?? 0,


            research_score:
                backendIntel.research_score ?? 0,


            kap_score:
                backendIntel.kap_score ?? 0,


            strengths:
                backendIntel.strengths ??
                consensus.strengths ??
                [],


            weaknesses:
                backendIntel.weaknesses ??
                consensus.risks ??
                [],


            explanations,

        };


    },[data]);







    if(error){

        return (

            <Alert severity="error">

                Dashboard yüklenemedi.

            </Alert>

        );

    }






    return (

        <Box sx={{p:3}}>


            <Typography

                variant="h4"

                fontWeight={700}

                mb={2}

            >

                🤖 BIST AI LAB v10

            </Typography>





            <Grid

                container

                spacing={2}

            >







                {/* WATCHLIST */}

                <Grid size={{xs:12,lg:2}}>

                    <PortfolioPanel/>

                </Grid>








                {/* AI */}

                <Grid size={{xs:12,lg:4}}>


                    <AIScoreCard

                        loading={loading}

                        data={intelligence}

                    />


                </Grid>








                {/* NEWS */}

                <Grid size={{xs:12,lg:6}}>


                    <Box

                        sx={{

                            height:300,

                            overflow:"auto"

                        }}

                    >

                        <NewsPanel

                            news={

                                data?.news?.news ?? []

                            }


                            loading={loading}

                        />


                    </Box>


                </Grid>








                {/* KPI */}

                <Grid size={{xs:12,lg:3}}>


                    <Stack spacing={1}>


                        <KPICard

                            title="ML"

                            subtitle="Makine Öğrenmesi"

                            value={intelligence.ml_score}

                        />



                        <KPICard

                            title="Technical"

                            subtitle="Teknik Analiz"

                            value={intelligence.technical_score}

                        />



                        <KPICard

                            title="News"

                            subtitle="AI Haber"

                            value={intelligence.news_score}

                        />



                        <KPICard

                            title="Research"

                            subtitle="Araştırma"

                            value={intelligence.research_score}

                        />



                        <KPICard

                            title="KAP"

                            subtitle="KAP"

                            value={intelligence.kap_score}

                        />


                    </Stack>


                </Grid>








                {/* RADAR */}

                <Grid size={{xs:12,lg:4}}>


                    <Box

                        sx={{

                            height:320

                        }}

                    >

                        <RadarChart

                            intelligence={intelligence}

                        />


                    </Box>


                </Grid>








                {/* RESEARCH */}

                <Grid size={{xs:12,lg:5}}>


                    <Box

                        sx={{

                            height:320,

                            overflow:"auto"

                        }}

                    >

                        <ResearchPanel

                            reports={

                                data?.research?.items ?? []

                            }

                            loading={loading}

                        />


                    </Box>


                </Grid>









                {/* CHART */}

                <Grid size={{xs:12,lg:8}}>


                    <TradingChart

                        symbol={selectedSymbol}

                        market={data?.market}

                        prediction={data?.prediction}

                    />


                </Grid>








                {/* KAP */}

                <Grid size={{xs:12,lg:4}}>


                    <KapPanel

                        events={

                            data?.kap?.items ?? []

                        }

                        loading={loading}

                    />


                </Grid>






            </Grid>







            <Box mt={2}>


                <StatusBar

                    loadedAt={data?.loadedAt}

                    version={data?.version?.version}

                    modules={data?.modules}

                />


            </Box>





        </Box>


    );


}







export default function DashboardPage(){


    return (

        <DashboardProvider>

            <DashboardContent/>

        </DashboardProvider>

    );


}