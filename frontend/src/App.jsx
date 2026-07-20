import { lazy, Suspense } from "react";

import {
    Routes,
    Route,
} from "react-router-dom";

import {
    Box,
    CircularProgress,
} from "@mui/material";

import MainLayout from "./layouts/MainLayout";

const DashboardPage = lazy(() =>
    import("./features/DashboardPage"),
);

const Portfolio = lazy(() =>
    import("./pages/Portfolio"),
);

const Scanner = lazy(() =>
    import("./pages/Scanner"),
);

const News = lazy(() =>
    import("./pages/News"),
);

const Research = lazy(() =>
    import("./pages/Research"),
);

const Settings = lazy(() =>
    import("./pages/Settings"),
);

function Loading() {

    return (

        <Box
            sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
            }}
        >

            <CircularProgress />

        </Box>

    );

}

export default function App() {

    return (

        <MainLayout>

            <Suspense
                fallback={<Loading />}
            >

                <Routes>

                    <Route
                        path="/"
                        element={<DashboardPage />}
                    />

                    <Route
                        path="/portfolio"
                        element={<Portfolio />}
                    />

                    <Route
                        path="/scanner"
                        element={<Scanner />}
                    />

                    <Route
                        path="/news"
                        element={<News />}
                    />

                    <Route
                        path="/research"
                        element={<Research />}
                    />

                    <Route
                        path="/settings"
                        element={<Settings />}
                    />

                </Routes>

            </Suspense>

        </MainLayout>

    );

}