import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({

    plugins: [
        react(),
    ],

    build: {

        sourcemap: false,

        minify: "esbuild",

        target: "es2022",

        chunkSizeWarningLimit: 1200,

        rollupOptions: {

            output: {

                manualChunks: {

                    react: [

                        "react",
                        "react-dom",
                        "react-router-dom",

                    ],

                    mui: [

                        "@mui/material",
                        "@mui/icons-material",

                    ],

                    charts: [

                        "echarts",
                        "echarts-for-react",

                    ],

                    query: [

                        "@tanstack/react-query",

                    ],

                },

            },

        },

    },

});