import {
    Paper,
    Typography,
    Stack,
    Chip,
    CircularProgress,
    Divider,
} from "@mui/material";

export default function ResearchPanel({

    reports = [],

    loading = false,

}) {

    if (loading) {

        return (

            <Paper
                sx={{
                    p: 2,
                    height: 340,
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
                height: 340,
                overflow: "auto",
            }}
        >

            <Typography
                variant="h6"
                mb={2}
            >
                Research
            </Typography>

            {

                reports.length === 0 && (

                    <Typography color="text.secondary">

                        Araştırma raporu bulunamadı.

                    </Typography>

                )

            }

            <Stack spacing={2}>

                {

                    reports.map((item, index) => (

                        <Paper
                            key={index}
                            variant="outlined"
                            sx={{ p: 2 }}
                        >

                            <Typography
                                fontWeight={700}
                            >
                                {item.broker}
                            </Typography>

                            <Divider sx={{ my: 1 }} />

                            <Chip
                                label={item.recommendation ?? "HOLD"}
                                color={
                                    item.recommendation === "BUY"
                                        ? "success"
                                        : item.recommendation === "SELL"
                                        ? "error"
                                        : "warning"
                                }
                            />

                            <Typography mt={2}>
                                Target :
                                {" "}
                                ₺
                                {item.target_price ?? "-"}
                            </Typography>

                            <Typography
                                variant="body2"
                                mt={1}
                            >
                                {item.summary}
                            </Typography>

                        </Paper>

                    ))

                }

            </Stack>

        </Paper>

    );

}