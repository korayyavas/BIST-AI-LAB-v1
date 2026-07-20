import {
    AppBar,
    Box,
    CssBaseline,
    Drawer,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Toolbar,
    Typography
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import ShowChartIcon from "@mui/icons-material/ShowChart";
import NewspaperIcon from "@mui/icons-material/Newspaper";
import DescriptionIcon from "@mui/icons-material/Description";
import AccountBalanceWalletIcon from "@mui/icons-material/AccountBalanceWallet";
import SettingsIcon from "@mui/icons-material/Settings";
import { Link } from "react-router-dom";

const drawerWidth = 250;

export default function MainLayout({ children }) {

    const menu = [

        {
            text: "Dashboard",
            icon: <DashboardIcon/>
        },

        {
            text: "Portfolio",
            icon: <AccountBalanceWalletIcon/>
        },

        {
            text: "Scanner",
            icon: <ShowChartIcon/>
        },

        {
            text: "Research",
            icon: <DescriptionIcon/>
        },

        {
            text: "News",
            icon: <NewspaperIcon/>
        },

        {
            text: "Settings",
            icon: <SettingsIcon/>
        }

    ];

    return (

        <Box sx={{ display:"flex" }}>

            <CssBaseline/>

            <AppBar
                position="fixed"
                sx={{
                    bgcolor:"#11161d",
                    zIndex:1300
                }}
            >

                <Toolbar>

                    <Typography
                        variant="h5"
                        fontWeight={700}
                    >

                        BIST AI LAB

                    </Typography>

                </Toolbar>

            </AppBar>

            <Drawer

                variant="permanent"

                sx={{

                    width:drawerWidth,

                    flexShrink:0,

                    "& .MuiDrawer-paper":{

                        width:drawerWidth,

                        bgcolor:"#0f141b",

                        color:"white",

                        borderRight:"1px solid #1f2937"

                    }

                }}

            >

                <Toolbar/>

                <List>

                    {

                        menu.map(item=>(

                            <ListItemButton
                                component={Link}
                                to={
                                    item.text==="Dashboard"
                                    ? "/"
                                    : "/" + item.text.toLowerCase()
                                }
                            >

                                <ListItemIcon
                                    sx={{
                                        color:"#3b82f6"
                                    }}
                                >

                                    {item.icon}

                                </ListItemIcon>

                                <ListItemText

                                    primary={item.text}

                                />

                            </ListItemButton>

                        ))

                    }

                </List>

            </Drawer>

            <Box

                component="main"

                sx={{

                    flexGrow:1,

                    p:3,

                    bgcolor:"#090c10",

                    minHeight:"100vh"

                }}

            >

                <Toolbar/>

                {children}

            </Box>

        </Box>

    );

}