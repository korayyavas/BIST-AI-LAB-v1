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

function effectColor(effect) {

    switch (effect) {

        case "POZITIF":
            return "success";

        case "NEGATIF":
            return "error";

        default:
            return "warning";

    }

}

function sentimentColor(sentiment) {

    switch (sentiment) {

        case "POSITIVE":
            return "success";

        case "NEGATIVE":
            return "error";

        default:
            return "warning";

    }

}

function categoryColor(category) {

    switch (category) {

        case "COMPANY":
            return "primary";

        case "SECTOR":
            return "success";

        case "MACRO":
            return "warning";

        case "GEOPOLITICAL":
            return "secondary";

        default:
            return "default";

    }

}

export default function NewsPanel({

    news = [],

    loading = false,

}) {

    if (loading) {

        return (

            <Paper
                sx={{
                    p: 2,
                    height: 700,
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
                height: 700,
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

            <Typography
                variant="body2"
                color="text.secondary"
                mb={3}
            >
                AI önem puanına göre sıralanmış haberler
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
                        elevation={3}
                        sx={{
                            p: 2,
                            borderRadius: 3,
                        }}
                    >

                        <Stack
                            direction="row"
                            justifyContent="space-between"
                            alignItems="center"
                            flexWrap="wrap"
                            spacing={1}
                            mb={2}
                        >

                            <Stack
                                direction="row"
                                spacing={1}
                                flexWrap="wrap"
                            >

                                <Chip

                                    label={item.source}

                                    color="primary"

                                    size="small"

                                />

                                <Chip

                                    label={item.category || "OTHER"}

                                    color={categoryColor(item.category)}

                                    size="small"

                                />

                            </Stack>

                            <Chip

                                label={item.market_effect}

                                color={effectColor(item.market_effect)}

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

                        {(item.short_effect || item.long_effect) && (

                            <>

                                <Divider sx={{ my: 2 }} />

                                <Typography
                                    fontWeight="bold"
                                    gutterBottom
                                >
                                    📈 Etki Analizi
                                </Typography>

                                {item.short_effect && (

                                    <Typography variant="body2">

                                        <b>Kısa Vade:</b> {item.short_effect}

                                    </Typography>

                                )}

                                {item.long_effect && (

                                    <Typography
                                        variant="body2"
                                        mt={1}
                                    >

                                        <b>Uzun Vade:</b> {item.long_effect}

                                    </Typography>

                                )}

                            </>

                        )}

                        <Divider sx={{ my: 2 }} />

                        <Typography
                            fontWeight="bold"
                            gutterBottom
                        >
                            🤖 AI Yorumu
                        </Typography>

                        <Typography variant="body2">

                            {item.ai_comment || "AI yorumu bulunmuyor."}

                        </Typography>

                        <Divider sx={{ my: 2 }} />

                        <Stack
                            direction="row"
                            spacing={1}
                            flexWrap="wrap"
                            alignItems="center"
                        >

                            <Rating

                                value={item.importance}

                                readOnly

                            />

                            <Chip

                                label={item.sentiment}

                                color={sentimentColor(item.sentiment)}

                            />

                            <Chip

                                color="info"

                                label={`AI ${item.score}`}

                            />

                            {item.relevance && (

                                <Chip

                                    color="secondary"

                                    label={`İlgi ${item.relevance}`}

                                />

                            )}

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