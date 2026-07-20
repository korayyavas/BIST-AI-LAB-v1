import { useCallback, useEffect, useRef, useState } from "react";

import { loadDashboard } from "./DashboardApi";

export function useDashboard(
    symbol,
    options = {},
) {
    const {
        autoRefresh = false,
        refreshInterval = 60000,
    } = options;

    const mountedRef = useRef(true);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState(null);

    const [lastUpdated, setLastUpdated] = useState(null);

    const [data, setData] = useState({
        intelligence: null,
        news: [],
        research: [],
        kap: [],
        errors: {},
    });

    const reload = useCallback(async () => {
        try {
            setLoading(true);
            setError(null);

            const result =
                await loadDashboard(symbol);

            if (!mountedRef.current) return;

            setData(result);

            setLastUpdated(
                result.loadedAt ??
                    new Date().toISOString(),
            );
        } catch (err) {
            if (!mountedRef.current) return;

            console.error(err);

            setError(err);
        } finally {
            if (mountedRef.current) {
                setLoading(false);
            }
        }
    }, [symbol]);

    useEffect(() => {
        mountedRef.current = true;

        reload();

        return () => {
            mountedRef.current = false;
        };
    }, [reload]);

    useEffect(() => {
        if (!autoRefresh) return;

        const timer = setInterval(
            reload,
            refreshInterval,
        );

        return () => clearInterval(timer);
    }, [
        autoRefresh,
        refreshInterval,
        reload,
    ]);

    return {
        loading,
        error,
        data,
        reload,
        lastUpdated,
    };
}