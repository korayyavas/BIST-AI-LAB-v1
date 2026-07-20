import {

    Paper,

    Typography,

    LinearProgress

} from "@mui/material";

export default function KPICard({

    title,

    value=0

}){

    return(

        <Paper

            sx={{

                p:2,

                borderRadius:3,

                bgcolor:"#11161d",

                border:"1px solid #26313d"

            }}

        >

            <Typography

                color="#9ca3af"

            >

                {title}

            </Typography>

            <Typography

                variant="h4"

                fontWeight={700}

                mt={1}

            >

                {value}

            </Typography>

            <LinearProgress

                value={value}

                variant="determinate"

                sx={{

                    mt:2,

                    height:8,

                    borderRadius:8

                }}

            />

        </Paper>

    );

}