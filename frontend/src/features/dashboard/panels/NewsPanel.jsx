import {
    Paper,
    Typography,
    Stack,
    Chip,
    CircularProgress,
    Divider,
    Link,
    Rating,
    Box,
} from "@mui/material";

export default function NewsPanel({

    news = [],

    loading = false,

}) {

    if (loading) {

        return (

            <Paper
                sx={{
                    p: 2,
                    height: 650,
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
                height: 650,
                overflow: "auto",
            }}
        >

            <Typography
                variant="h5"
                fontWeight="bold"
                mb={2}
            >
                📰 AI NEWS INTELLIGENCE
            </Typography>

            {news.length === 0 && (

                <Typography color="text.secondary">

                    Haber bulunamadı.

                </Typography>

            )}

            <Stack spacing={2}>

                {news.map((item, index) => (

                    <Paper
                        key={index}
                        elevation={2}
                        sx={{
                            p: 2,
                            borderRadius: 3,
                        }}
                    >

                        <Stack
                            direction="row"
                            justifyContent="space-between"
                            alignItems="center"
                            mb={1}
                        >

                            <Chip

                                label={item.source}

                                size="small"

                                color="primary"

                            />

                            <Chip

                                label={item.market_effect}

                                color={

                                    item.market_effect === "POZITIF"

                                        ? "success"

                                        : item.market_effect === "NEGATIF"

                                        ? "error"

                                        : "warning"

                                }

                            />

                        </Stack>

                        <Typography

                            variant="h6"

                            fontWeight="bold"

                        >

                            {item.title_tr || item.title}

                        </Typography>

                        <Typography

                            variant="body2"

                            color="text.secondary"

                            mt={1}

                        >

                            {item.summary}

                        </Typography>

                        <Divider sx={{ my: 2 }} />

                        <Typography

                            variant="subtitle2"

                            fontWeight="bold"

                        >

                            🤖 AI Yorumu

                        </Typography>

                        <Typography

                            variant="body2"

                            mt={1}

                        >

                            {item.ai_comment}

                        </Typography>

                        <Divider sx={{ my: 2 }} />

                        <Stack

                            direction="row"

                            spacing={2}

                            alignItems="center"

                            flexWrap="wrap"

                        >

                            <Rating

                                value={item.importance}

                                readOnly

                            />

                            <Chip

                                label={item.sentiment}

                                color={

                                    item.sentiment === "POSITIVE"

                                        ? "success"

                                        : item.sentiment === "NEGATIVE"

                                        ? "error"

                                        : "warning"

                                }

                            />

                            <Chip

                                color="info"

                                label={`AI Score ${item.score}`}

                            />

                        </Stack>

                        <Box mt={2}>

                            <Link

                                href={item.url}

                                target="_blank"

                                underline="hover"

                            >

                                🔗 Orijinal Haberi Oku

                            </Link>

                        </Box>

                    </Paper>

                ))}

            </Stack>

        </Paper>

    );

}