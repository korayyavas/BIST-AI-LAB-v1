import {
    createContext,
    useContext,
    useMemo,
    useState,
    useCallback,
} from "react";

const DashboardContext = createContext(null);

export function DashboardProvider({
    children,
}) {

    const [
        selectedSymbol,
        setSelectedSymbol,
    ] = useState("ASELS");

    const [
        timeframe,
        setTimeframe,
    ] = useState("1D");

    const [
        workspace,
        setWorkspace,
    ] = useState("default");

    const [
        widgetState,
        setWidgetState,
    ] = useState({});

    const refreshAll = useCallback(() => {

        window.dispatchEvent(
            new CustomEvent(
                "dashboard-refresh",
            ),
        );

    }, []);

    const showWidget = useCallback(
        (id) => {

            setWidgetState((prev) => ({
                ...prev,
                [id]: true,
            }));

        },
        [],
    );

    const hideWidget = useCallback(
        (id) => {

            setWidgetState((prev) => ({
                ...prev,
                [id]: false,
            }));

        },
        [],
    );

    const toggleWidget = useCallback(
        (id) => {

            setWidgetState((prev) => ({
                ...prev,
                [id]: !prev[id],
            }));

        },
        [],
    );

    const value = useMemo(
        () => ({
            selectedSymbol,
            setSelectedSymbol,

            timeframe,
            setTimeframe,

            workspace,
            setWorkspace,

            widgetState,

            showWidget,
            hideWidget,
            toggleWidget,

            refreshAll,
        }),
        [
            selectedSymbol,
            timeframe,
            workspace,
            widgetState,
            refreshAll,
            showWidget,
            hideWidget,
            toggleWidget,
        ],
    );

    return (
        <DashboardContext.Provider
            value={value}
        >
            {children}
        </DashboardContext.Provider>
    );
}

export function useDashboardContext() {

    const context =
        useContext(DashboardContext);

    if (!context) {

        throw new Error(
            "DashboardProvider missing.",
        );

    }

    return context;
}