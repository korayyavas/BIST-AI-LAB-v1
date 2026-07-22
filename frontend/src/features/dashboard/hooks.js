import { useMemo } from "react";

import { useDashboardQuery } from "./query/dashboardQuery";

const EMPTY_DATA = {

    intelligence: {},

    news: [],

    research: [],

    kap: [],

    topPicks: [],

    version: {},

    modules: {},

    loadedAt: null,

    errors: {},

};

export function useDashboard(symbol = "ASELS") {

    const query = useDashboardQuery(symbol);

    const data = useMemo(

        () => ({

            ...EMPTY_DATA,

            ...(query.data ?? {}),

        }),

        [query.data],

    );

    return {

        loading: query.isPending,

        fetching: query.isFetching,

        success: query.isSuccess,

        error: query.error,

        data,

        reload: query.refetch,

        lastUpdated: data.loadedAt,

        intelligence: data.intelligence,

        news: data.news,

        research: data.research,

        kap: data.kap,

        topPicks: data.topPicks,

        version: data.version,

        modules: data.modules,

    };

}