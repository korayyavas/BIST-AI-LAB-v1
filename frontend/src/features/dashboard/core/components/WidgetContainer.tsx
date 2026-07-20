import { memo, type PropsWithChildren } from "react";
import {
  Box,
  Card,
  CardContent,
  CardHeader,
  CircularProgress,
  IconButton,
  Tooltip,
} from "@mui/material";

import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";
import FullscreenRoundedIcon from "@mui/icons-material/FullscreenRounded";
import VisibilityOffRoundedIcon from "@mui/icons-material/VisibilityOffRounded";

import { useDashboardContext } from "../context/DashboardContext";

export interface WidgetContainerProps
  extends PropsWithChildren {
  id: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  actions?: React.ReactNode;
  onRefresh?: () => void;
  onFullscreen?: () => void;
}

function WidgetContainerComponent({
  id,
  title,
  subtitle,
  loading = false,
  actions,
  onRefresh,
  onFullscreen,
  children,
}: WidgetContainerProps) {
  const {
    refreshWidget,
    setWidgetVisible,
  } = useDashboardContext();

  const handleRefresh = () => {
    refreshWidget(id);

    onRefresh?.();
  };

  return (
    <Card
      elevation={0}
      sx={{
        height: "100%",
        borderRadius: 3,
        border: "1px solid",
        borderColor: "divider",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
      }}
    >
      <CardHeader
        title={title}
        subheader={subtitle}
        action={
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 0.5,
            }}
          >
            {actions}

            <Tooltip title="Yenile">
              <IconButton
                size="small"
                onClick={handleRefresh}
              >
                <RefreshRoundedIcon
                  fontSize="small"
                />
              </IconButton>
            </Tooltip>

            <Tooltip title="Tam Ekran">
              <IconButton
                size="small"
                onClick={onFullscreen}
              >
                <FullscreenRoundedIcon
                  fontSize="small"
                />
              </IconButton>
            </Tooltip>

            <Tooltip title="Gizle">
              <IconButton
                size="small"
                onClick={() =>
                  setWidgetVisible(id, false)
                }
              >
                <VisibilityOffRoundedIcon
                  fontSize="small"
                />
              </IconButton>
            </Tooltip>
          </Box>
        }
      />

      <CardContent
        sx={{
          flex: 1,
          position: "relative",
          p: 2,
        }}
      >
        {loading && (
          <Box
            sx={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              bgcolor: "rgba(255,255,255,.55)",
              backdropFilter: "blur(2px)",
              zIndex: 10,
            }}
          >
            <CircularProgress
              size={28}
            />
          </Box>
        )}

        {children}
      </CardContent>
    </Card>
  );
}

export const WidgetContainer = memo(
  WidgetContainerComponent,
);

export default WidgetContainer;