import type { ReactNode } from "react";

import {
  Box,
  Button,
  Divider,
  Stack,
  Tooltip,
  Typography,
} from "@mui/material";

import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";
import FilterAltRoundedIcon from "@mui/icons-material/FilterAltRounded";
import DownloadRoundedIcon from "@mui/icons-material/DownloadRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";

export interface WidgetToolbarProps {
  title?: string;
  leftContent?: ReactNode;
  rightContent?: ReactNode;

  onRefresh?: () => void;
  onFilter?: () => void;
  onExport?: () => void;
  onSettings?: () => void;
}

export default function WidgetToolbar({
  title,
  leftContent,
  rightContent,
  onRefresh,
  onFilter,
  onExport,
  onSettings,
}: WidgetToolbarProps) {
  return (
    <Stack
      direction="row"
      alignItems="center"
      justifyContent="space-between"
      spacing={2}
      sx={{
        px: 2,
        py: 1,
        borderBottom: "1px solid",
        borderColor: "divider",
        bgcolor: "background.paper",
      }}
    >
      <Stack
        direction="row"
        spacing={2}
        alignItems="center"
      >
        {title && (
          <Typography
            variant="subtitle2"
            fontWeight={700}
          >
            {title}
          </Typography>
        )}

        {leftContent}
      </Stack>

      <Stack
        direction="row"
        spacing={1}
        alignItems="center"
      >
        {rightContent}

        <Divider
          orientation="vertical"
          flexItem
        />

        <Tooltip title="Yenile">
          <Button
            size="small"
            startIcon={<RefreshRoundedIcon />}
            onClick={onRefresh}
          >
            Refresh
          </Button>
        </Tooltip>

        <Tooltip title="Filtre">
          <Button
            size="small"
            startIcon={<FilterAltRoundedIcon />}
            onClick={onFilter}
          >
            Filter
          </Button>
        </Tooltip>

        <Tooltip title="Dışa Aktar">
          <Button
            size="small"
            startIcon={<DownloadRoundedIcon />}
            onClick={onExport}
          >
            Export
          </Button>
        </Tooltip>

        <Tooltip title="Ayarlar">
          <Button
            size="small"
            startIcon={<SettingsRoundedIcon />}
            onClick={onSettings}
          >
            Settings
          </Button>
        </Tooltip>
      </Stack>
    </Stack>
  );
}