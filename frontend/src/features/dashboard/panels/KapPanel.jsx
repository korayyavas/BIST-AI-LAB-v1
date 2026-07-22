import {
    Paper,
    Typography,
    Stack,
    Chip,
    CircularProgress,
    Divider,
} from "@mui/material";

export default function KapPanel({

    events = [],

    loading = false,

}) {

    if (loading) {

        return (

            <Paper
                sx={{
                    p: 2,
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
            }}
        >

            <Typography
                variant="h6"
                mb={2}
            >
                KAP Timeline
            </Typography>

            {

                events.length === 0 && (

                    <Typography color="text.secondary">

                        KAP bildirimi bulunamadı.

                    </Typography>

                )

            }

            <Stack spacing={2}>

                {

                    events.map((item, index) => (

                        <Paper
                            key={index}
                            variant="outlined"
                            sx={{ p: 2 }}
                        >

                            <Typography
                                fontWeight={700}
                            >
                                {item.title}
                            </Typography>

                            <Divider sx={{ my: 1 }} />

                            <Chip
                                size="small"
                                label={item.event_type ?? "INFO"}
                            />

                            <Typography
                                variant="body2"
                                mt={1}
                            >
                                Score : {item.score ?? "-"}
                            </Typography>

                        </Paper>

                    ))

                }

            </Stack>

        </Paper>

    );

}