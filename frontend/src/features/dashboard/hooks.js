import { useDashboardQuery } from "./query/dashboardQuery";

const EMPTY_DATA = {
    intelligence: null,
    news: [],
    research: [],
    kap: [],
    errors: {},
};

export function useDashboard(symbol) {

    const query = useDashboardQuery(symbol);

    return {

        loading: query.isPending,

        fetching: query.isFetching,

        error: query.error,

        data: query.data ?? EMPTY_DATA,

        reload: query.refetch,

        lastUpdated:
            query.data?.loadedAt ?? null,

    };

}