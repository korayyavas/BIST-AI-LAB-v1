import {
    AppBar,
    Box,
    Chip,
    CssBaseline,
    Divider,
    Drawer,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Stack,
    Toolbar,
    Typography,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import ShowChartIcon from "@mui/icons-material/ShowChart";
import NewspaperIcon from "@mui/icons-material/Newspaper";
import DescriptionIcon from "@mui/icons-material/Description";
import AccountBalanceWalletIcon from "@mui/icons-material/AccountBalanceWallet";
import SettingsIcon from "@mui/icons-material/Settings";
import CircleIcon from "@mui/icons-material/Circle";

import { Link, useLocation } from "react-router-dom";

const drawerWidth = 260;

const menu = [
    { text: "Dashboard", icon: <DashboardIcon />, path: "/" },
    { text: "Portfolio", icon: <AccountBalanceWalletIcon />, path: "/portfolio" },
    { text: "Scanner", icon: <ShowChartIcon />, path: "/scanner" },
    { text: "Research", icon: <DescriptionIcon />, path: "/research" },
    { text: "News", icon: <NewspaperIcon />, path: "/news" },
    { text: "Settings", icon: <SettingsIcon />, path: "/settings" },
];

export default function MainLayout({ children }) {

    const location = useLocation();

    return (
        <Box sx={{ display: "flex", bgcolor: "#090c10" }}>

            <CssBaseline />

            <AppBar
                elevation={0}
                position="fixed"
                sx={{
                    bgcolor: "#11161d",
                    borderBottom: "1px solid #1f2937",
                    zIndex: (theme) => theme.zIndex.drawer + 1,
                }}
            >
                <Toolbar
                    sx={{
                        display: "flex",
                        justifyContent: "space-between",
                    }}
                >
                    <Stack
                        direction="row"
                        spacing={2}
                        alignItems="center"
                    >
                        <Typography
                            variant="h5"
                            fontWeight={800}
                        >
                            BIST AI LAB
                        </Typography>

                        <Chip
                            label="v7"
                            size="small"
                            color="primary"
                        />
                    </Stack>

                    <Stack
                        direction="row"
                        spacing={2}
                        alignItems="center"
                    >
                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            Backend
                        </Typography>

                        <CircleIcon
                            sx={{
                                fontSize: 11,
                                color: "#22c55e",
                            }}
                        />

                        <Typography variant="body2">
                            Connected
                        </Typography>
                    </Stack>
                </Toolbar>
            </AppBar>

            <Drawer
                variant="permanent"
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,

                    "& .MuiDrawer-paper": {
                        width: drawerWidth,
                        bgcolor: "#0f141b",
                        color: "#fff",
                        borderRight: "1px solid #1f2937",
                    },
                }}
            >
                <Toolbar />

                <Divider />

                <List sx={{ mt: 1 }}>
                    {menu.map((item) => (
                        <ListItemButton
                            key={item.path}
                            component={Link}
                            to={item.path}
                            selected={location.pathname === item.path}
                            sx={{
                                mx: 1,
                                mb: 0.5,
                                borderRadius: 2,

                                "&.Mui-selected": {
                                    bgcolor: "primary.main",
                                    color: "#fff",
                                },

                                "&.Mui-selected:hover": {
                                    bgcolor: "primary.dark",
                                },
                            }}
                        >
                            <ListItemIcon
                                sx={{
                                    color: "inherit",
                                    minWidth: 40,
                                }}
                            >
                                {item.icon}
                            </ListItemIcon>

                            <ListItemText primary={item.text} />
                        </ListItemButton>
                    ))}
                </List>
            </Drawer>

            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    minHeight: "100vh",
                    bgcolor: "#090c10",
                }}
            >
                <Toolbar />

                <Box sx={{ p: 3 }}>
                    {children}
                </Box>
            </Box>

        </Box>
    );
}