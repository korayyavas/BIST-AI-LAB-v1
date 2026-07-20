import { memo } from "react";
import {
  Box,
  Chip,
  Divider,
  Stack,
  Typography,
} from "@mui/material";

import CircleIcon from "@mui/icons-material/Circle";

export interface StatusBarProps {
  symbol?: string;
  market?: string;
  updatedAt?: string;
  apiStatus?: "online" | "offline";
  aiStatus?: "ready" | "busy";
}

function StatusBarComponent({
  symbol = "BIST",
  market = "OPEN",
  updatedAt,
  apiStatus = "online",
  aiStatus = "ready",
}: StatusBarProps) {
  const now =
    updatedAt ??
    new Date().toLocaleTimeString("tr-TR");

  return (
    <Box
      sx={{
        height: 34,
        px: 2,
        borderTop: "1px solid",
        borderColor: "divider",
        bgcolor: "background.paper",
        display: "flex",
        alignItems: "center",
      }}
    >
      <Stack
        direction="row"
        spacing={2}
        divider={
          <Divider
            orientation="vertical"
            flexItem
          />
        }
        alignItems="center"
      >
        <Typography variant="caption">
          {symbol}
        </Typography>

        <Chip
          size="small"
          color={
            market === "OPEN"
              ? "success"
              : "default"
          }
          label={market}
        />

        <Stack
          direction="row"
          spacing={0.5}
          alignItems="center"
        >
          <CircleIcon
            sx={{
              fontSize: 10,
              color:
                apiStatus === "online"
                  ? "success.main"
                  : "error.main",
            }}
          />

          <Typography variant="caption">
            API
          </Typography>
        </Stack>

        <Stack
          direction="row"
          spacing={0.5}
          alignItems="center"
        >
          <CircleIcon
            sx={{
              fontSize: 10,
              color:
                aiStatus === "ready"
                  ? "success.main"
                  : "warning.main",
            }}
          />

          <Typography variant="caption">
            AI
          </Typography>
        </Stack>

        <Typography
          variant="caption"
          color="text.secondary"
        >
          Last Update : {now}
        </Typography>
      </Stack>
    </Box>
  );
}

export default memo(StatusBarComponent);