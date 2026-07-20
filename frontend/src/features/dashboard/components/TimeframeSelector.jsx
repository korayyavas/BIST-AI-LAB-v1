import {
  FormControl,
  MenuItem,
  Select,
} from "@mui/material";

import { useDashboardContext } from "../DashboardContext";

const TIMEFRAMES = [
  "1D",
  "1W",
  "1M",
  "3M",
  "6M",
  "1Y",
];

export default function TimeframeSelector() {
  const {
    timeframe,
    setTimeframe,
  } = useDashboardContext();

  return (
    <FormControl
      size="small"
      sx={{ minWidth: 100 }}
    >
      <Select
        value={timeframe}
        onChange={(e) =>
          setTimeframe(e.target.value)
        }
      >
        {TIMEFRAMES.map((frame) => (
          <MenuItem
            key={frame}
            value={frame}
          >
            {frame}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
