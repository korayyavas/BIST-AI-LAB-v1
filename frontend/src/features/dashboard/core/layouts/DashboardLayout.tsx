import type { PropsWithChildren, ReactNode } from "react";

import {
  Box,
  Container,
  Grid,
  Stack,
} from "@mui/material";

import StatusBar from "../components/StatusBar";

export interface DashboardLayoutProps
  extends PropsWithChildren {
  header?: ReactNode;
  toolbar?: ReactNode;
  sidebar?: ReactNode;
  footer?: ReactNode;
}

export default function DashboardLayout({
  header,
  toolbar,
  sidebar,
  footer,
  children,
}: DashboardLayoutProps) {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        overflow: "hidden",
        bgcolor: "background.default",
      }}
    >
      {header}

      {toolbar}

      <Box
        sx={{
          flex: 1,
          overflow: "auto",
          py: 2,
        }}
      >
        <Container
          maxWidth={false}
        >
          <Grid
            container
            spacing={2}
          >
            {sidebar && (
              <Grid
                size={{
                  xs: 12,
                  lg: 3,
                }}
              >
                {sidebar}
              </Grid>
            )}

            <Grid
              size={{
                xs: 12,
                lg: sidebar
                  ? 9
                  : 12,
              }}
            >
              <Stack
                spacing={2}
              >
                {children}
              </Stack>
            </Grid>
          </Grid>
        </Container>
      </Box>

      {footer ?? <StatusBar />}
    </Box>
  );
}