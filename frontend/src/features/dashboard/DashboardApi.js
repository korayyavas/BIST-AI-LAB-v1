import axios from "../../api/api";

async function post(endpoint, symbol) {
    const { data } = await axios.post(endpoint, {
        symbol,
    });

    return data;
}

export async function loadDashboard(symbol) {

    const [
        intelligence,
        news,
        research,
        kap,
    ] = await Promise.allSettled([
        post("/intelligence", symbol),
        post("/news", symbol),
        post("/research", symbol),
        post("/kap", symbol),
    ]);

    return {
        intelligence:
            intelligence.status === "fulfilled"
                ? intelligence.value
                : null,

        news:
            news.status === "fulfilled"
                ? news.value.news ?? []
                : [],

        research:
            research.status === "fulfilled"
                ? research.value.reports ?? []
                : [],

        kap:
            kap.status === "fulfilled"
                ? (
                      kap.value.events ??
                      kap.value.kap ??
                      []
                  )
                : [],

        errors: {
            intelligence:
                intelligence.status === "rejected",

            news:
                news.status === "rejected",

            research:
                research.status === "rejected",

            kap:
                kap.status === "rejected",
        },

        loadedAt: new Date().toISOString(),
    };
}