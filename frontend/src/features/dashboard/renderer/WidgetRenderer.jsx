import { memo } from "react";

import {
    Grid,
    Paper,
} from "@mui/material";

import WidgetRegistry from "../registry/WidgetRegistry";

function WidgetRenderer() {

    const widgets =
        WidgetRegistry.getAll();

    return (

        <Grid
            container
            spacing={2}
        >

            {widgets.map((widget) => {

                const Component =
                    widget.component;

                return (

                    <Grid
                        key={widget.id}
                        size={{
                            xs: 12,
                            md: 6,
                            lg: 4,
                        }}
                    >

                        <Paper
                            elevation={0}
                            sx={{
                                p: 2,
                                borderRadius: 3,
                                border: "1px solid",
                                borderColor: "divider",
                                height: "100%",
                            }}
                        >

                            <Component />

                        </Paper>

                    </Grid>

                );

            })}

        </Grid>

    );

}

export default memo(
    WidgetRenderer,
);