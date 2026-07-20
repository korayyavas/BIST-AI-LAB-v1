import {

    Paper,

    Grid,

    Typography

} from "@mui/material";

export default function StatusBar(){

    return(

        <Paper

            sx={{

                p:2,

                bgcolor:"#11161d",

                border:"1px solid #26313d"

            }}

        >

            <Grid container>

                <Grid item xs={3}>

                    <Typography>

                        Backend

                    </Typography>

                    <Typography color="#00e676">

                        ● Connected

                    </Typography>

                </Grid>

                <Grid item xs={3}>

                    <Typography>

                        AI Engine

                    </Typography>

                    <Typography>

                        Gemini + ML

                    </Typography>

                </Grid>

                <Grid item xs={3}>

                    <Typography>

                        Cache

                    </Typography>

                    <Typography>

                        Enabled

                    </Typography>

                </Grid>

                <Grid item xs={3}>

                    <Typography>

                        Version

                    </Typography>

                    <Typography>

                        BIST AI LAB v7

                    </Typography>

                </Grid>

            </Grid>

        </Paper>

    );

}