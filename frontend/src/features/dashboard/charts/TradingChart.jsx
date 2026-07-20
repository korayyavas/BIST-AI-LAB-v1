import {

    Paper,

    Typography,

    Box

} from "@mui/material";

export default function TradingChart(){

    return(

        <Paper

            sx={{

                p:2,

                height:420,

                bgcolor:"#11161d",

                border:"1px solid #26313d"

            }}

        >

            <Typography

                variant="h5"

                mb={2}

            >

                Price Chart

            </Typography>

            <Box

                sx={{

                    width:"100%",

                    height:"350px",

                    borderRadius:3,

                    overflow:"hidden"

                }}

            >

                <iframe

                    title="TradingView"

                    width="100%"

                    height="100%"

                    frameBorder="0"

                    allowTransparency

                    scrolling="no"

                    src="https://s.tradingview.com/widgetembed/?symbol=BIST:ASELS&interval=D&theme=dark"

                />

            </Box>

        </Paper>

    );

}