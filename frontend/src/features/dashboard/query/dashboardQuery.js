import { useQuery } from "@tanstack/react-query";

import { loadDashboard } from "../DashboardApi";

export const dashboardKeys = {

    all: ["dashboard"],

    symbol: (symbol) => [
        ...dashboardKeys.all,
        symbol,
    ],

};

export function useDashboardQuery(symbol) {

    return useQuery({

        queryKey:
            dashboardKeys.symbol(symbol),

        queryFn: () =>
            loadDashboard(symbol),

        staleTime: 60_000,

        gcTime: 300_000,

        retry: 2,

        refetchInterval: 60_000,

        refetchOnReconnect: true,

        refetchOnWindowFocus: false,

    });

}