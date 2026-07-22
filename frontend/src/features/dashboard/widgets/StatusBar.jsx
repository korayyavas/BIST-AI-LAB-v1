import {
    Paper,
    Grid,
    Typography,
    Chip,
    Stack,
} from "@mui/material";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import MemoryIcon from "@mui/icons-material/Memory";
import StorageIcon from "@mui/icons-material/Storage";
import PsychologyIcon from "@mui/icons-material/Psychology";

export default function StatusBar() {

    return (

        <Paper
            sx={{
                mt: 2,
                p: 2,
                bgcolor: "#10151d",
                border: "1px solid #243041",
                borderRadius: 3,
            }}
        >

            <Grid container spacing={2}>

                <Grid size={{ xs: 12, md: 3 }}>

                    <Stack spacing={1}>

                        <Typography variant="caption">
                            Backend
                        </Typography>

                        <Chip
                            icon={<CheckCircleIcon />}
                            label="ONLINE"
                            color="success"
                        />

                    </Stack>

                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>

                    <Stack spacing={1}>

                        <Typography variant="caption">
                            Intelligence Engine
                        </Typography>

                        <Chip
                            icon={<PsychologyIcon />}
                            label="ACTIVE"
                            color="primary"
                        />

                    </Stack>

                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>

                    <Stack spacing={1}>

                        <Typography variant="caption">
                            Cache
                        </Typography>

                        <Chip
                            icon={<StorageIcon />}
                            label="ENABLED"
                            color="success"
                        />

                    </Stack>

                </Grid>

                <Grid size={{ xs: 12, md: 3 }}>

                    <Stack spacing={1}>

                        <Typography variant="caption">
                            Version
                        </Typography>

                        <Chip
                            icon={<MemoryIcon />}
                            label="BIST AI LAB v9"
                            color="info"
                        />

                    </Stack>

                </Grid>

            </Grid>

        </Paper>

    );

}