import { memo, type PropsWithChildren } from "react";
import { Grid } from "@mui/material";

export interface ResponsiveGridProps
  extends PropsWithChildren {
  spacing?: number;
}

export interface GridItemProps
  extends PropsWithChildren {
  xs?: number;
  sm?: number;
  md?: number;
  lg?: number;
  xl?: number;
}

function ResponsiveGridComponent({
  children,
  spacing = 2,
}: ResponsiveGridProps) {
  return (
    <Grid
      container
      spacing={spacing}
      sx={{
        width: "100%",
        margin: 0,
      }}
    >
      {children}
    </Grid>
  );
}

function GridItemComponent({
  xs = 12,
  sm = 12,
  md = 6,
  lg = 4,
  xl = 3,
  children,
}: GridItemProps) {
  return (
    <Grid
      size={{
        xs,
        sm,
        md,
        lg,
        xl,
      }}
    >
      {children}
    </Grid>
  );
}

export const ResponsiveGrid = memo(
  ResponsiveGridComponent,
);

export const GridItem = memo(
  GridItemComponent,
);

export default ResponsiveGrid;