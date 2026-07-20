import { Stack, Typography, Box } from "@mui/material";
import SymbolSelector from "./SymbolSelector";
import TimeframeSelector from "./TimeframeSelector";
import RefreshButton from "./RefreshButton";
import ConnectionStatus from "./ConnectionStatus";

export default function DashboardToolbar() {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        mb: 3,
        gap: 2,
        flexWrap: "wrap",
      }}
    >
      <Typography variant="h5" fontWeight={700}>
        Dashboard
      </Typography>

      <Stack direction="row" spacing={2} alignItems="center">
        <SymbolSelector />
        <TimeframeSelector />
        <RefreshButton />
        <ConnectionStatus />
      </Stack>
    </Box>
  );
}
