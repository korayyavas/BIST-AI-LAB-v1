import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        mode: "dark",

        primary: {

            main: "#3b82f6"

        },

        secondary: {

            main: "#06b6d4"

        },

        background: {

            default: "#090c10",

            paper: "#11161d"

        }

    },

    typography: {

        fontFamily: "Inter, Segoe UI, sans-serif",

        h2: {

            fontWeight: 700

        },

        h3: {

            fontWeight: 700

        },

        h4: {

            fontWeight: 700

        },

        h5: {

            fontWeight: 600

        }

    },

    shape: {

        borderRadius: 18

    },

    components: {

        MuiPaper: {

            styleOverrides: {

                root: {

                    background: "#11161d",

                    border: "1px solid #202734",

                    boxShadow:

                        "0 0 25px rgba(0,0,0,.45)"

                }

            }

        }

    }

});

export default theme;