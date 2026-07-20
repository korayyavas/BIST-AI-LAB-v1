import React, { Component, ErrorInfo, ReactNode } from "react";
import {
  Alert,
  Box,
  Button,
  Paper,
  Stack,
  Typography,
} from "@mui/material";

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export default class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
  };

  public static getDerivedStateFromError(
    error: Error,
  ): State {
    return {
      hasError: true,
      error,
    };
  }

  public componentDidCatch(
    error: Error,
    errorInfo: ErrorInfo,
  ) {
    console.error(
      "[Dashboard ErrorBoundary]",
      error,
      errorInfo,
    );
  }

  private handleReload = () => {
    this.setState({
      hasError: false,
      error: undefined,
    });
  };

  public render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }

      return (
        <Paper
          elevation={0}
          sx={{
            p: 4,
            borderRadius: 3,
            border: "1px solid",
            borderColor: "divider",
          }}
        >
          <Stack spacing={2}>
            <Typography
              variant="h6"
              fontWeight={700}
            >
              Widget Error
            </Typography>

            <Alert severity="error">
              {this.state.error?.message ??
                "Unexpected error."}
            </Alert>

            <Box>
              <Button
                variant="contained"
                onClick={this.handleReload}
              >
                Retry
              </Button>
            </Box>
          </Stack>
        </Paper>
      );
    }

    return this.props.children;
  }
}