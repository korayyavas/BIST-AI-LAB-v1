import type { ReactNode } from "react";

import {
  Box,
  Chip,
  IconButton,
  Stack,
  Tooltip,
  Typography,
} from "@mui/material";

import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";
import OpenInFullRoundedIcon from "@mui/icons-material/OpenInFullRounded";
import MoreVertRoundedIcon from "@mui/icons-material/MoreVertRounded";

export interface WidgetHeaderProps {
  title: string;
  subtitle?: string;

  badge?: string;

  loading?: boolean;

  actions?: ReactNode;

  onRefresh?: () => void;

  onFullscreen?: () => void;

  onMenu?: () => void;
}

export default function WidgetHeader({
  title,
  subtitle,
  badge,
  loading = false,
  actions,
  onRefresh,
  onFullscreen,
  onMenu,
}: WidgetHeaderProps) {
  return (
    <Box
      sx={{
        px: 2,
        py: 1.5,
        borderBottom: "1px solid",
        borderColor: "divider",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        minHeight: 64,
      }}
    >
      <Stack spacing={0.25}>
        <Stack
          direction="row"
          spacing={1}
          alignItems="center"
        >
          <Typography
            variant="subtitle1"
            fontWeight={700}
          >
            {title}
          </Typography>

          {badge && (
            <Chip
              label={badge}
              color="primary"
              size="small"
            />
          )}

          {loading && (
            <Chip
              label="Loading..."
              size="small"
              color="warning"
              variant="outlined"
            />
          )}
        </Stack>

        {subtitle && (
          <Typography
            variant="caption"
            color="text.secondary"
          >
            {subtitle}
          </Typography>
        )}
      </Stack>

      <Stack
        direction="row"
        spacing={0.5}
        alignItems="center"
      >
        {actions}

        <Tooltip title="Refresh">
          <IconButton
            size="small"
            onClick={onRefresh}
          >
            <RefreshRoundedIcon
              fontSize="small"
            />
          </IconButton>
        </Tooltip>

        <Tooltip title="Fullscreen">
          <IconButton
            size="small"
            onClick={onFullscreen}
          >
            <OpenInFullRoundedIcon
              fontSize="small"
            />
          </IconButton>
        </Tooltip>

        <Tooltip title="More">
          <IconButton
            size="small"
            onClick={onMenu}
          >
            <MoreVertRoundedIcon
              fontSize="small"
            />
          </IconButton>
        </Tooltip>
      </Stack>
    </Box>
  );
}