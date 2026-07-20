import React from "react";
import ReactDOM from "react-dom/client";

import { BrowserRouter } from "react-router-dom";

import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

import {
    QueryClient,
    QueryClientProvider,
} from "@tanstack/react-query";

import App from "./App";
import theme from "./theme/theme";

import "./index.css";

const client = new QueryClient({

    defaultOptions: {

        queries: {

            retry: 2,

            staleTime: 60 * 1000,

            gcTime: 5 * 60 * 1000,

            refetchOnWindowFocus: false,

            refetchOnReconnect: true,

        },

    },

});

ReactDOM.createRoot(
    document.getElementById("root"),
).render(

    <React.StrictMode>

        <BrowserRouter>

            <ThemeProvider theme={theme}>

                <CssBaseline />

                <QueryClientProvider client={client}>

                    <App />

                </QueryClientProvider>

            </ThemeProvider>

        </BrowserRouter>

    </React.StrictMode>,

);