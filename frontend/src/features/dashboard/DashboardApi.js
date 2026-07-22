import axios from "../../api/api";

// =====================================================
// HTTP
// =====================================================

async function get(url) {

    const { data } = await axios.get(url);

    return data;

}

async function post(url, body) {

    const { data } = await axios.post(

        url,

        body,

    );

    return data;

}

// =====================================================
// Dashboard Loader
// =====================================================

export async function loadDashboard(

    symbol = "ASELS",

) {

    const requests = await Promise.allSettled([

        get(

            `/intelligence/${symbol}`,

        ),

        post(

            "/news",

            {

                symbol,

            },

        ),

        post(

            "/research",

            {

                symbol,

            },

        ),

        post(

            "/kap",

            {

                symbol,

            },

        ),

        post(

            "/top-picks",

            {

                top: 10,

                signal: "ALL",

                min_confidence: 0,

            },

        ),

        get(

            "/version",

        ),

        get(

            "/modules",

        ),

    ]);

    const [

        intelligence,

        news,

        research,

        kap,

        topPicks,

        version,

        modules,

    ] = requests;

    return {

        intelligence:

            intelligence.status === "fulfilled"

                ? intelligence.value

                : {},

        news:

            news.status === "fulfilled"

                ? (

                    news.value.news ??

                    []

                )

                : [],

        research:

            research.status === "fulfilled"

                ? (

                    research.value.reports ??

                    []

                )

                : [],

        kap:

            kap.status === "fulfilled"

                ? (

                    kap.value.kap ??

                    []

                )

                : [],

        topPicks:

            topPicks.status === "fulfilled"

                ? (

                    topPicks.value.top_picks ??

                    []

                )

                : [],

        version:

            version.status === "fulfilled"

                ? version.value

                : {},

        modules:

            modules.status === "fulfilled"

                ? modules.value

                : {},

        loadedAt:

            new Date().toISOString(),

        errors: {

            intelligence:

                intelligence.status === "rejected",

            news:

                news.status === "rejected",

            research:

                research.status === "rejected",

            kap:

                kap.status === "rejected",

            topPicks:

                topPicks.status === "rejected",

            version:

                version.status === "rejected",

            modules:

                modules.status === "rejected",

        },

    };

}

// =====================================================
// Refresh
// =====================================================

export async function refreshDashboard(

    symbol,

) {

    return await loadDashboard(

        symbol,

    );

}

// =====================================================
// Health
// =====================================================

export async function getHealth() {

    return await get(

        "/health",

    );

}

// =====================================================
// System
// =====================================================

export async function getSystemInfo() {

    return await get(

        "/system",

    );

}

// =====================================================
// API Version
// =====================================================

export async function getVersion() {

    return await get(

        "/version",

    );

}

// =====================================================
// Modules
// =====================================================

export async function getModules() {

    return await get(

        "/modules",

    );

}