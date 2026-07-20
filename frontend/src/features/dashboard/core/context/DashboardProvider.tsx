import { useEffect, type PropsWithChildren } from "react";

import {
  DashboardProvider as Provider,
  useDashboardContext,
} from "./DashboardContext";

interface BootstrapWidget {
  id: string;
  title: string;
  visible: boolean;
}

const DEFAULT_WIDGETS: BootstrapWidget[] = [
  {
    id: "market-overview",
    title: "Market Overview",
    visible: true,
  },
  {
    id: "portfolio",
    title: "Portfolio",
    visible: true,
  },
  {
    id: "watchlist",
    title: "Watchlist",
    visible: true,
  },
  {
    id: "news",
    title: "News",
    visible: true,
  },
  {
    id: "ai-signals",
    title: "AI Signals",
    visible: true,
  },
];

function DashboardBootstrap({
  children,
}: PropsWithChildren) {
  const { registerWidget } = useDashboardContext();

  useEffect(() => {
    DEFAULT_WIDGETS.forEach((widget) => {
      registerWidget({
        ...widget,
        loading: false,
      });
    });
  }, [registerWidget]);

  return <>{children}</>;
}

export default function DashboardProvider({
  children,
}: PropsWithChildren) {
  return (
    <Provider>
      <DashboardBootstrap>
        {children}
      </DashboardBootstrap>
    </Provider>
  );
}