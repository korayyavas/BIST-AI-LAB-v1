import {

    Box,
    Grid,
    Stack,
    Typography

} from "@mui/material";

import AIScoreCard from "./dashboard/cards/AIScoreCard";
import KPICard from "./dashboard/cards/KPICard";
import RadarChart from "./dashboard/charts/RadarChart";
import TradingChart from "./dashboard/charts/TradingChart";

import PortfolioPanel from "./dashboard/panels/PortfolioPanel";
import NewsPanel from "./dashboard/panels/NewsPanel";
import ResearchPanel from "./dashboard/panels/ResearchPanel";
import KapPanel from "./dashboard/panels/KapPanel";

import StatusBar from "./dashboard/widgets/StatusBar";

export default function DashboardPage(){

    return(

        <Box sx={{p:3}}>

            <Typography
                variant="h3"
                fontWeight={700}
                mb={3}
            >

                Dashboard

            </Typography>

            <Grid container spacing={2}>

                <Grid item xs={2.5}>

                    <PortfolioPanel/>

                </Grid>

                <Grid item xs={4}>

                    <AIScoreCard/>

                </Grid>

                <Grid item xs={5.5}>

                    <NewsPanel/>

                </Grid>

                <Grid item xs={2.5}>

                    <Stack spacing={2}>

                        <KPICard title="ML"/>

                        <KPICard title="Technical"/>

                        <KPICard title="News"/>

                        <KPICard title="Research"/>

                        <KPICard title="KAP"/>

                    </Stack>

                </Grid>

                <Grid item xs={4}>

                    <RadarChart/>

                </Grid>

                <Grid item xs={5.5}>

                    <ResearchPanel/>

                </Grid>

                <Grid item xs={8}>

                    <TradingChart/>

                </Grid>

                <Grid item xs={4}>

                    <KapPanel/>

                </Grid>

                <Grid item xs={12}>

                    <StatusBar/>

                </Grid>

            </Grid>

        </Box>

    );

}