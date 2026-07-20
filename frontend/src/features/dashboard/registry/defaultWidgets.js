import WidgetRegistry from "./WidgetRegistry";

import AIScoreCard from "../cards/AIScoreCard";

import KPICard from "../cards/KPICard";

import PortfolioPanel from "../panels/PortfolioPanel";

import NewsPanel from "../panels/NewsPanel";

import ResearchPanel from "../panels/ResearchPanel";

import KapPanel from "../panels/KapPanel";

import TradingChart from "../charts/TradingChart";

import RadarChart from "../charts/RadarChart";

WidgetRegistry.register({

    id: "portfolio",

    title: "Portfolio",

    component: PortfolioPanel,

    order: 1,

});

WidgetRegistry.register({

    id: "ai",

    title: "AI Score",

    component: AIScoreCard,

    order: 2,

});

WidgetRegistry.register({

    id: "news",

    title: "News",

    component: NewsPanel,

    order: 3,

});

WidgetRegistry.register({

    id: "radar",

    title: "Radar",

    component: RadarChart,

    order: 4,

});

WidgetRegistry.register({

    id: "research",

    title: "Research",

    component: ResearchPanel,

    order: 5,

});

WidgetRegistry.register({

    id: "chart",

    title: "Trading",

    component: TradingChart,

    order: 6,

});

WidgetRegistry.register({

    id: "kap",

    title: "KAP",

    component: KapPanel,

    order: 7,

});

WidgetRegistry.register({

    id: "kpi",

    title: "KPIs",

    component: KPICard,

    order: 8,

});