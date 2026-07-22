import {
    Paper,
    Typography,
    Box,
    CircularProgress,
    Stack,
    Chip,
    Divider,
    List,
    ListItem,
    ListItemText,
} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";


export default function AIScoreCard({

    loading = false,

    data = {},

}) {

    if (loading) {

        return (

            <Paper
                sx={{
                    height: 520,
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                }}
            >

                <CircularProgress />

            </Paper>

        );

    }

    const score = Number(

        data.ai_score ??

        data.score ??

        0,

    );

    const decision =

        data.decision ??

        data.recommendation ??

        "HOLD";

    const confidence = Number(

        data.confidence ??

        50,

    );

    const strengths =

        data.strengths ??

        [];

    const weaknesses =

        data.weaknesses ??

        [];

    const explanations =

        data.explanations ??

        [];

    let color = "#FFC107";

    let icon = <RemoveIcon />;

    if (decision.includes("BUY")) {

        color = "#00C853";

        icon = <TrendingUpIcon />;

    }

    if (decision.includes("SELL")) {

        color = "#F44336";

        icon = <TrendingDownIcon />;

    }

    return (

        <Paper

            sx={{

                p: 3,

                height: 520,

                background: "#10151d",

                border: "1px solid #243041",

                borderRadius: 4,

            }}

        >

            <Stack

                spacing={2}

                alignItems="center"

            >

                <Typography

                    variant="h5"

                    fontWeight={700}

                >

                    🤖 AI INTELLIGENCE

                </Typography>

                <Box

                    sx={{

                        position: "relative",

                        display: "inline-flex",

                    }}

                >

                    <CircularProgress

                        variant="determinate"

                        value={100}

                        size={170}

                        thickness={2}

                        sx={{

                            color: "#263238",

                            position: "absolute",

                        }}

                    />

                    <CircularProgress

                        variant="determinate"

                        value={score}

                        size={170}

                        thickness={6}

                        sx={{

                            color,

                        }}

                    />

                    <Box

                        sx={{

                            inset: 0,

                            position: "absolute",

                            display: "flex",

                            flexDirection: "column",

                            justifyContent: "center",

                            alignItems: "center",

                        }}

                    >

                        <Typography

                            variant="h2"

                            fontWeight={700}

                        >

                            {score.toFixed(1)}

                        </Typography>

                        <Typography>

                            AI SCORE

                        </Typography>

                    </Box>

                </Box>

                <Chip

                    icon={icon}

                    label={decision}

                    sx={{

                        bgcolor: color,

                        color: "#fff",

                        fontWeight: 700,

                    }}

                />

                <Typography>

                    Confidence : {confidence.toFixed(1)}%

                </Typography>

                <Divider flexItem />

                <Box width="100%">

                    <Typography

                        variant="subtitle2"

                        gutterBottom

                    >

                        ✅ Güçlü Yönler

                    </Typography>

                    <Stack

                        direction="row"

                        spacing={1}

                        flexWrap="wrap"

                    >

                        {

                            strengths.length === 0

                                ?

                                <Chip

                                    size="small"

                                    label="-"

                                />

                                :

                                strengths.map((item) => (

                                    <Chip

                                        key={item}

                                        size="small"

                                        color="success"

                                        label={item}

                                    />

                                ))

                        }

                    </Stack>

                </Box>

                <Box width="100%">

                    <Typography

                        variant="subtitle2"

                        gutterBottom

                    >

                        ⚠ Riskler

                    </Typography>

                    <Stack

                        direction="row"

                        spacing={1}

                        flexWrap="wrap"

                    >

                        {

                            weaknesses.length === 0

                                ?

                                <Chip

                                    size="small"

                                    label="-"

                                />

                                :

                                weaknesses.map((item) => (

                                    <Chip

                                        key={item}

                                        size="small"

                                        color="warning"

                                        label={item}

                                    />

                                ))

                        }

                    </Stack>

                </Box>

                <Divider flexItem />

                <Box width="100%">

                    <Typography

                        variant="subtitle2"

                        gutterBottom

                    >

                        🧠 Explainable AI

                    </Typography>

                    <List dense>

                        {

                            explanations.length === 0

                                ?

                                <ListItem>

                                    <ListItemText

                                        primary="-"

                                    />

                                </ListItem>

                                :

                                explanations.map((item, index) => (

                                    <ListItem key={index}>

                                        <ListItemText

                                            primary={item}

                                        />

                                    </ListItem>

                                ))

                        }

                    </List>

                </Box>

            </Stack>

        </Paper>

    );

}