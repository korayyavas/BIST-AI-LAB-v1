import {

    Card,

    CardContent,

    Grid,

    Typography,

    LinearProgress,

    Box,

    Chip,

    Stack

} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";

export default function ScoreCard({ data }) {

    if (!data) {

        return (

            <Card
                className="card glow"
            >

                <CardContent>

                    <Typography
                        variant="h4"
                    >

                        Select a symbol and click Analyze

                    </Typography>

                </CardContent>

            </Card>

        );

    }

    const color =

        data.decision.includes("BUY")

            ? "#00e676"

            : data.decision.includes("SELL")

            ? "#ff5252"

            : "#ffc107";

    const icon =

        data.decision.includes("BUY")

            ? <TrendingUpIcon sx={{fontSize:34}}/>

            : data.decision.includes("SELL")

            ? <TrendingDownIcon sx={{fontSize:34}}/>

            : <RemoveIcon sx={{fontSize:34}}/>;

    return (

        <Card
            className="card glow"
        >

            <CardContent>

                <Grid
                    container
                    spacing={4}
                    alignItems="center"
                >

                    <Grid item xs={3}>

                        <Typography
                            variant="h3"
                            fontWeight="bold"
                        >

                            {data.symbol}

                        </Typography>

                        <Stack
                            direction="row"
                            spacing={1}
                            mt={2}
                        >

                            <Chip

                                icon={icon}

                                label={data.decision}

                                sx={{

                                    bgcolor:color,

                                    color:"#fff",

                                    fontWeight:700,

                                    fontSize:16

                                }}

                            />

                        </Stack>

                    </Grid>

                    <Grid item xs={3}>

                        <Typography
                            color="#8b949e"
                        >

                            AI SCORE

                        </Typography>

                        <Typography

                            variant="h1"

                            sx={{

                                fontWeight:800,

                                color

                            }}

                        >

                            {data.ai_score}

                        </Typography>

                        <LinearProgress

                            variant="determinate"

                            value={data.ai_score}

                            sx={{

                                mt:2,

                                height:10,

                                borderRadius:10,

                                bgcolor:"#1f2937",

                                "& .MuiLinearProgress-bar":{

                                    background:color

                                }

                            }}

                        />

                    </Grid>

                    <Grid item xs={2}>

                        <Typography
                            color="#8b949e"
                        >

                            Confidence

                        </Typography>

                        <Typography
                            variant="h4"
                        >

                            {data.confidence}%

                        </Typography>

                        <Box mt={3}/>

                        <Typography
                            color="#8b949e"
                        >

                            Risk

                        </Typography>

                        <Typography
                            variant="h4"
                        >

                            {data.risk}

                        </Typography>

                    </Grid>

                    <Grid item xs={2}>

                        <Typography
                            color="#8b949e"
                        >

                            Consensus

                        </Typography>

                        <Typography
                            variant="h4"
                        >

                            {data.consensus}

                        </Typography>

                        <Box mt={3}/>

                        <Typography
                            color="#8b949e"
                        >

                            Target

                        </Typography>

                        <Typography
                            variant="h4"
                        >

                            ₺ {data.target_price}

                        </Typography>

                    </Grid>

                    <Grid item xs={2}>

                        <Typography
                            color="#8b949e"
                            mb={1}
                        >

                            Intelligence

                        </Typography>

                        <Typography>

                            ML {Math.round(data.ml_score)}

                        </Typography>

                        <LinearProgress

                            value={data.ml_score}

                            variant="determinate"

                            sx={{mb:1}}

                        />

                        <Typography>

                            Technical {Math.round(data.technical_score)}

                        </Typography>

                        <LinearProgress

                            value={data.technical_score}

                            variant="determinate"

                            sx={{mb:1}}

                        />

                        <Typography>

                            Research {Math.round(data.research_score)}

                        </Typography>

                        <LinearProgress

                            value={data.research_score}

                            variant="determinate"

                            sx={{mb:1}}

                        />

                        <Typography>

                            News {Math.round(data.news_score)}

                        </Typography>

                        <LinearProgress

                            value={data.news_score}

                            variant="determinate"

                            sx={{mb:1}}

                        />

                        <Typography>

                            KAP {Math.round(data.kap_score)}

                        </Typography>

                        <LinearProgress

                            value={data.kap_score}

                            variant="determinate"

                        />

                    </Grid>

                </Grid>

            </CardContent>

        </Card>

    );

}