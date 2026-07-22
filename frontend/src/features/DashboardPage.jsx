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
    } = useDashboard(selectedSymbol);

    const intelligence = useMemo(
        () => data?.intelligence ?? {},
        [data],
    );

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
                BIST AI LAB
            </Typography>

            <Grid container spacing={2}>

                <Grid size={{ xs:12, lg:3 }}>
                    <PortfolioPanel />
                </Grid>

                <Grid size={{ xs:12, lg:4 }}>
                    <AIScoreCard
                        loading={loading}
                        data={{
                            score: intelligence.ai_score,
                            recommendation: intelligence.decision,
                            confidence: intelligence.confidence,
                            strengths: [],
                            weaknesses: [],
                        }}
                    />
                </Grid>

                <Grid size={{ xs:12, lg:5 }}>
                    <NewsPanel
                        news={data?.news ?? []}
                        loading={loading}
                    />
                </Grid>

                <Grid size={{ xs:12, lg:3 }}>
                    <Stack spacing={2}>

                        <KPICard
                            title="ML"
                            value={intelligence.ml_score}
                        />

                        <KPICard
                            title="Technical"
                            value={intelligence.technical_score}
                        />

                        <KPICard
                            title="News"
                            value={intelligence.news_score}
                        />

                        <KPICard
                            title="Research"
                            value={intelligence.research_score}
                        />

                        <KPICard
                            title="KAP"
                            value={intelligence.kap_score}
                        />

                    </Stack>
                </Grid>

                <Grid size={{ xs:12, lg:4 }}>
                    <RadarChart />
                </Grid>

                <Grid size={{ xs:12, lg:5 }}>
                    <ResearchPanel
                        reports={data?.research ?? []}
                        loading={loading}
                    />
                </Grid>

                <Grid size={{ xs:12, lg:8 }}>
                    <TradingChart />
                </Grid>

                <Grid size={{ xs:12, lg:4 }}>
                    <KapPanel
                        events={data?.kap ?? []}
                        loading={loading}
                    />
                </Grid>

            </Grid>

            <StatusBar />

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