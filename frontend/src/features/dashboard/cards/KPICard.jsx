import {
    Paper,
    Typography,
    LinearProgress,
    Box,
    Chip,
    Stack,
} from "@mui/material";

export default function KPICard({

    title,

    value = 0,

}) {

    const score = Math.max(
        0,
        Math.min(100, Number(value) || 0),
    );

    let color = "#2196F3";
    let status = "NÖTR";

    if (score >= 80) {

        color = "#00C853";
        status = "ÇOK GÜÇLÜ";

    }

    else if (score >= 65) {

        color = "#4CAF50";
        status = "GÜÇLÜ";

    }

    else if (score >= 50) {

        color = "#FFB300";
        status = "NÖTR";

    }

    else if (score >= 30) {

        color = "#FF7043";
        status = "ZAYIF";

    }

    else {

        color = "#F44336";
        status = "ÇOK ZAYIF";

    }

    return (

        <Paper

            sx={{

                p: 2,

                borderRadius: 3,

                bgcolor: "#11161d",

                border: "1px solid #26313d",

                height: "100%",

            }}

        >

            <Stack

                direction="row"

                justifyContent="space-between"

                alignItems="center"

            >

                <Typography

                    color="#9ca3af"

                    fontWeight={600}

                >

                    {title}

                </Typography>

                <Chip

                    size="small"

                    label={status}

                    sx={{

                        bgcolor: color,

                        color: "#fff",

                        fontWeight: 600,

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

                >

                    {score.toFixed(1)}

                </Typography>

                <Typography

                    color="#9ca3af"

                    mb={0.5}

                >

                    /100

                </Typography>

            </Box>

            <LinearProgress

                variant="determinate"

                value={score}

                sx={{

                    mt: 2,

                    height: 10,

                    borderRadius: 10,

                    backgroundColor: "#26313d",

                    "& .MuiLinearProgress-bar": {

                        backgroundColor: color,

                    },

                }}

            />

        </Paper>

    );

}