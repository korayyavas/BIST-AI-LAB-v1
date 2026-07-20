import {

    Box,
    Grid,
    Stack,
    Typography

} from "@mui/material";

import AIScoreCard from "./dashboard/cards/AIScoreCard";
import KPICard from "./dashboard/cards/KPICard";
import RadarChart from "./charts/RadarChart";
import PortfolioPanel from "./panels/PortfolioPanel";
import NewsPanel from "./panels/NewsPanel";
import ResearchPanel from "./panels/ResearchPanel";
import KapPanel from "./panels/KapPanel";
import TradingChart from "./charts/TradingChart";
import StatusBar from "./widgets/StatusBar";

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