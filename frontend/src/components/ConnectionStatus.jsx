import {
  Chip,
  Stack,
} from "@mui/material";

import CircleIcon from "@mui/icons-material/Circle";

export default function ConnectionStatus({
  connected = true,
}) {
  return (
    <Chip
      icon={
        <CircleIcon
          sx={{
            color: connected
              ? "#22c55e"
              : "#ef4444",
            fontSize: 12,
          }}
        />
      }
      label={
        connected
          ? "Connected"
          : "Offline"
      }
      color={
        connected
          ? "success"
          : "error"
      }
      variant="outlined"
      size="small"
    />
  );
}
