import {
    FormControl,
    MenuItem,
    Select,
} from "@mui/material";

import {
    useDashboardContext,
} from "../DashboardContext";

const SYMBOLS = [

    "ASELS",
    "THYAO",
    "SISE",
    "EREGL",
    "TUPRS",
    "BIMAS",
    "KCHOL",
    "AKBNK",
    "GARAN",
    "ISCTR",

];

export default function SymbolSelector() {

    const {

        selectedSymbol,

        setSelectedSymbol,

    } = useDashboardContext();

    return (

        <FormControl
            size="small"
            sx={{
                minWidth: 130,
            }}
        >

            <Select

                value={selectedSymbol}

                onChange={(e) =>
                    setSelectedSymbol(
                        e.target.value,
                    )
                }

            >

                {

                    SYMBOLS.map(symbol => (

                        <MenuItem
                            key={symbol}
                            value={symbol}
                        >

                            {symbol}

                        </MenuItem>

                    ))

                }

            </Select>

        </FormControl>

    );

}