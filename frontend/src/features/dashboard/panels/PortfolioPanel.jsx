import {
    Paper,
    Typography,
    Stack,
    Chip,
    Box,
    CircularProgress,
    LinearProgress,
} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import RemoveIcon from "@mui/icons-material/Remove";

import { useEffect, useState } from "react";

import axios from "../../../api/api";

export default function PortfolioPanel() {

    const [items, setItems] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        load();

    }, []);

    async function load() {

        setLoading(true);

        try {

            const res = await axios.post(

                "/top-picks",

                {

                    top: 10,

                    signal: "ALL",

                    min_confidence: 0,

                }

            );

            setItems(

                res.data.top_picks ?? []

            );

        }

        catch (e) {

            console.error(e);

            setItems([]);

        }

        finally {

            setLoading(false);

        }

    }

    if (loading) {

        return (

            <Paper

                sx={{

                    height: 420,

                    display: "flex",

                    justifyContent: "center",

                    alignItems: "center",

                }}

            >

                <CircularProgress />

            </Paper>

        );

    }

    return (

        <Paper

            sx={{

                p: 2,

                height: 420,

                overflow: "auto",

                bgcolor: "#10151d",

                border: "1px solid #243041",

                borderRadius: 4,

            }}

        >

            <Typography

                variant="h6"

                fontWeight={700}

                mb={2}

            >

                📈 AI WATCHLIST

            </Typography>

            {

                items.length === 0 && (

                    <Typography>

                        Veri bulunamadı.

                    </Typography>

                )

            }

            <Stack spacing={2}>

                {

                    items.map((item) => {

                        let color = "warning";

                        let icon = <RemoveIcon />;

                        if ((item.signal ?? "").includes("BUY")) {

                            color = "success";

                            icon = <TrendingUpIcon />;

                        }

                        if ((item.signal ?? "").includes("SELL")) {

                            color = "error";

                            icon = <TrendingDownIcon />;

                        }

                        return (

                            <Paper

                                key={item.symbol}

                                variant="outlined"

                                sx={{

                                    p: 2,

                                    bgcolor: "#161d28",

                                    borderRadius: 2,

                                }}

                            >

                                <Box

                                    display="flex"

                                    justifyContent="space-between"

                                    alignItems="center"

                                >

                                    <Box>

                                        <Typography

                                            fontWeight={700}

                                        >

                                            {item.symbol}

                                        </Typography>

                                        <Typography

                                            variant="caption"

                                        >

                                            {item.current_price} ₺

                                        </Typography>

                                    </Box>

                                    <Chip

                                        icon={icon}

                                        color={color}

                                        label={item.signal}

                                    />

                                </Box>

                                <Box mt={2}>

                                    <Typography

                                        variant="caption"

                                    >

                                        Confidence {Number(item.confidence).toFixed(1)}%

                                    </Typography>

                                    <LinearProgress

                                        variant="determinate"

                                        value={item.confidence}

                                        sx={{

                                            mt: 0.5,

                                            height: 8,

                                            borderRadius: 10,

                                        }}

                                    />

                                </Box>

                                <Stack

                                    direction="row"

                                    spacing={1}

                                    mt={2}

                                    flexWrap="wrap"

                                >

                                    <Chip

                                        size="small"

                                        label={`Risk ${item.risk_score}`}

                                    />

                                    <Chip

                                        size="small"

                                        color="primary"

                                        label={`Top ${item.top_score}`}

                                    />

                                </Stack>

                            </Paper>

                        );

                    })

                }

            </Stack>

        </Paper>

    );

}