import {
    Paper,
    Typography,
    LinearProgress,
    Box,
    Chip,
    Stack,
    Tooltip,
} from "@mui/material";

function getStatus(score) {

    if (score >= 90) {

        return {

            text: "MÜKEMMEL",

            color: "#00E676",

        };

    }

    if (score >= 80) {

        return {

            text: "ÇOK GÜÇLÜ",

            color: "#00C853",

        };

    }

    if (score >= 65) {

        return {

            text: "GÜÇLÜ",

            color: "#4CAF50",

        };

    }

    if (score >= 50) {

        return {

            text: "NÖTR",

            color: "#FFC107",

        };

    }

    if (score >= 35) {

        return {

            text: "ZAYIF",

            color: "#FF7043",

        };

    }

    return {

        text: "ÇOK ZAYIF",

        color: "#F44336",

    };

}

export default function KPICard({

    title,

    value = 0,

    subtitle = "",

}) {

    const score = Math.max(

        0,

        Math.min(

            100,

            Number(value) || 0,

        ),

    );

    const status = getStatus(score);

    return (

        <Paper

            elevation={3}

            sx={{

                p: 2,

                height: "100%",

                borderRadius: 4,

                background: "#10151d",

                border: "1px solid #26313d",

            }}

        >

            <Stack

                direction="row"

                justifyContent="space-between"

                alignItems="center"

            >

                <Box>

                    <Typography

                        fontWeight={700}

                        color="#fff"

                    >

                        {title}

                    </Typography>

                    {

                        subtitle &&

                        <Typography

                            variant="caption"

                            color="#8b98a5"

                        >

                            {subtitle}

                        </Typography>

                    }

                </Box>

                <Chip

                    size="small"

                    label={status.text}

                    sx={{

                        bgcolor: status.color,

                        color: "#fff",

                        fontWeight: 700,

                    }}

                />

            </Stack>

            <Box

                sx={{

                    display: "flex",

                    justifyContent: "space-between",

                    alignItems: "flex-end",

                    mt: 2,

                }}

            >

                <Typography

                    variant="h3"

                    fontWeight={700}

                    color="#fff"

                >

                    {score.toFixed(1)}

                </Typography>

                <Typography

                    color="#8b98a5"

                >

                    /100

                </Typography>

            </Box>

            <Tooltip

                title={`${status.text} (${score.toFixed(1)})`}

            >

                <LinearProgress

                    variant="determinate"

                    value={score}

                    sx={{

                        mt: 2,

                        height: 12,

                        borderRadius: 12,

                        backgroundColor: "#26313d",

                        "& .MuiLinearProgress-bar": {

                            backgroundColor: status.color,

                            borderRadius: 12,

                        },

                    }}

                />

            </Tooltip>

        </Paper>

    );

}