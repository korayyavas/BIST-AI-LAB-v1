import { Backdrop, Box, CircularProgress, Fade, Typography } from "@mui/material";

export interface LoadingOverlayProps {
  open: boolean;
  message?: string;
}

export default function LoadingOverlay({
  open,
  message = "Loading...",
}: LoadingOverlayProps) {
  return (
    <Backdrop
      open={open}
      sx={{
        zIndex: (theme) => theme.zIndex.drawer + 100,
        backgroundColor: "rgba(15,23,42,.35)",
        backdropFilter: "blur(4px)",
      }}
    >
      <Fade in={open}>
        <Box
          sx={{
            minWidth: 220,
            px: 4,
            py: 3,
            borderRadius: 3,
            bgcolor: "background.paper",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 2,
            boxShadow: 8,
          }}
        >
          <CircularProgress size={34} />

          <Typography
            variant="body2"
            color="text.secondary"
          >
            {message}
          </Typography>
        </Box>
      </Fade>
    </Backdrop>
  );
}