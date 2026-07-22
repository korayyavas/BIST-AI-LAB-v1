import axios from "../../api/api";

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

export async function loadDashboard(

    symbol = "ASELS",

) {

    const [

        intelligence,

        news,

        research,

        kap,

        topPicks,

    ] = await Promise.allSettled([

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

    ]);

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

        },

    };

}