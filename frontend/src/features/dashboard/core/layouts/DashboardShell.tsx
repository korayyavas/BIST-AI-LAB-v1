import type { PropsWithChildren, ReactNode } from "react";

import { Box, Stack } from "@mui/material";

import DashboardLayout from "./DashboardLayout";
import WidgetToolbar from "../components/WidgetToolbar";
import LoadingOverlay from "../components/LoadingOverlay";
import ErrorBoundary from "../components/ErrorBoundary";

export interface DashboardShellProps
  extends PropsWithChildren {
  header?: ReactNode;
  sidebar?: ReactNode;
  footer?: ReactNode;

  loading?: boolean;
  loadingMessage?: string;

  toolbar?: ReactNode;
}

export default function DashboardShell({
  children,
  header,
  sidebar,
  footer,
  toolbar,
  loading = false,
  loadingMessage = "Dashboard loading...",
}: DashboardShellProps) {
  return (
    <>
      <LoadingOverlay
        open={loading}
        message={loadingMessage}
      />

      <DashboardLayout
        header={header}
        sidebar={sidebar}
        footer={footer}
        toolbar={
          toolbar ?? (
            <WidgetToolbar
              title="Dashboard"
            />
          )
        }
      >
        <ErrorBoundary>
          <Box
            sx={{
              width: "100%",
              height: "100%",
            }}
          >
            <Stack spacing={2}>
              {children}
            </Stack>
          </Box>
        </ErrorBoundary>
      </DashboardLayout>
    </>
  );
}