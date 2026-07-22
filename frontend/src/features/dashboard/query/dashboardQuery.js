import { useQuery } from "@tanstack/react-query";

import { loadDashboard } from "../DashboardApi";

export const dashboardKeys = {

    all: ["dashboard"],

    symbol: (symbol) => [

        ...dashboardKeys.all,

        symbol,

    ],

};

export function useDashboardQuery(symbol = "ASELS") {

    return useQuery({

        queryKey: dashboardKeys.symbol(symbol),

        queryFn: () => loadDashboard(symbol),

        enabled: !!symbol,

        staleTime: 60 * 1000,

        gcTime: 5 * 60 * 1000,

        retry: 2,

        retryDelay: (attempt) =>

            Math.min(1000 * attempt, 5000),

        refetchInterval: 60 * 1000,

        refetchOnReconnect: true,

        refetchOnWindowFocus: false,

        refetchOnMount: true,

        networkMode: "online",

    });

}