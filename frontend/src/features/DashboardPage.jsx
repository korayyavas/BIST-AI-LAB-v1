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

function DashboardContent() {

    const { selectedSymbol } = useDashboardContext();

    const {

        loading,

        error,

        data,

    } = useDashboard(

        selectedSymbol,

    );

    const intelligence = useMemo(

        () => data?.intelligence ?? {},

        [data],

    );
    console.log("========== DASHBOARD ==========");
    console.log(data);
    console.log("NEWS LENGTH:", data?.news?.length);
    console.log("NEWS:", data?.news);
    console.log("===============================");

    if (error) {

        return (

            <Alert severity="error">

                Dashboard yüklenemedi.

            </Alert>

        );

    }

    return (

        <Box sx={{ p: 3 }}>

            <Typography

                variant="h4"

                fontWeight={700}

                mb={3}

            >

                🤖 BIST AI LAB v10

            </Typography>

            <Grid container spacing={2}>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 3 }}>

                    <PortfolioPanel />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 4 }}>

                    <AIScoreCard

                        loading={loading}

                        data={{

                            ai_score:

                                intelligence.ai_score,

                            decision:

                                intelligence.decision,

                            confidence:

                                intelligence.confidence,

                            strengths:

                                intelligence.strengths ?? [],

                            weaknesses:

                                intelligence.weaknesses ?? [],

                            explanations:

                                intelligence.explanations ?? [],

                        }}

                    />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 5 }}>

                    
                    
                    <NewsPanel

                        news={

                            data?.news ?? []

                        }

                        loading={loading}

                    />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 3 }}>

                    <Stack spacing={2}>

                        <KPICard

                            title="ML"

                            subtitle="Makine Öğrenmesi"

                            value={

                                intelligence.ml_score

                            }

                        />

                        <KPICard

                            title="Technical"

                            subtitle="Teknik Analiz"

                            value={

                                intelligence.technical_score

                            }

                        />

                        <KPICard

                            title="News"

                            subtitle="AI Haber Analizi"

                            value={

                                intelligence.news_score

                            }

                        />

                        <KPICard

                            title="Research"

                            subtitle="Araştırma Raporları"

                            value={

                                intelligence.research_score

                            }

                        />

                        <KPICard

                            title="KAP"

                            subtitle="Kamuyu Aydınlatma"

                            value={

                                intelligence.kap_score

                            }

                        />

                    </Stack>

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 4 }}>

                    <RadarChart

                        intelligence={

                            intelligence

                        }

                    />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 5 }}>

                    <ResearchPanel

                        reports={

                            data?.research ?? []

                        }

                        loading={loading}

                    />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 8 }}>

                    <TradingChart

                        symbol={selectedSymbol}

                    />

                </Grid>

                {/* ================================================= */}

                <Grid size={{ xs: 12, lg: 4 }}>

                    <KapPanel

                        events={

                            data?.kap ?? []

                        }

                        loading={loading}

                    />

                </Grid>

            </Grid>

            <Box mt={3}>

                <StatusBar

                    loadedAt={

                        data?.loadedAt

                    }

                    version={

                        data?.version?.version

                    }

                    modules={

                        data?.modules

                    }

                />

            </Box>

        </Box>

    );

}

export default function DashboardPage() {

    return (

        <DashboardProvider>

            <DashboardContent />

        </DashboardProvider>

    );

}