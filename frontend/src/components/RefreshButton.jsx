import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";

import { useDashboardContext } from "../DashboardContext";

export default function RefreshButton() {
  const { refreshAll } = useDashboardContext();

  return (
    <Tooltip title="Refresh Dashboard">
      <IconButton
        color="primary"
        onClick={refreshAll}
        aria-label="Refresh Dashboard"
      >
        <RefreshRoundedIcon />
      </IconButton>
    </Tooltip>
  );
}
