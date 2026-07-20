import { Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import DashboardPage from "./features/DashboardPage";

import Portfolio from "./pages/Portfolio";
import Scanner from "./pages/Scanner";
import News from "./pages/News";
import Research from "./pages/Research";
import Settings from "./pages/Settings";

export default function App() {

    return (

        <MainLayout>

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

        </MainLayout>

    );

}