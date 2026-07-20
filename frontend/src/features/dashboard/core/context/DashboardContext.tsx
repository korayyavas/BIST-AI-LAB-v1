import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
  type PropsWithChildren,
} from "react";

export type WidgetId = string;

export interface DashboardWidgetState {
  id: WidgetId;
  title: string;
  visible: boolean;
  loading: boolean;
  refreshedAt?: string;
}

export interface DashboardContextValue {
  widgets: DashboardWidgetState[];

  registerWidget: (widget: DashboardWidgetState) => void;

  unregisterWidget: (id: WidgetId) => void;

  setWidgetLoading: (
    id: WidgetId,
    loading: boolean,
  ) => void;

  setWidgetVisible: (
    id: WidgetId,
    visible: boolean,
  ) => void;

  refreshWidget: (id: WidgetId) => void;

  refreshAll: () => void;
}

const DashboardContext =
  createContext<DashboardContextValue | null>(null);

export function DashboardProvider({
  children,
}: PropsWithChildren) {
  const [widgets, setWidgets] = useState<
    DashboardWidgetState[]
  >([]);

  const registerWidget = useCallback(
    (widget: DashboardWidgetState) => {
      setWidgets((current) => {
        if (
          current.some(
            (item) => item.id === widget.id,
          )
        ) {
          return current;
        }

        return [...current, widget];
      });
    },
    [],
  );

  const unregisterWidget = useCallback(
    (id: WidgetId) => {
      setWidgets((current) =>
        current.filter(
          (widget) => widget.id !== id,
        ),
      );
    },
    [],
  );

  const setWidgetLoading = useCallback(
    (
      id: WidgetId,
      loading: boolean,
    ) => {
      setWidgets((current) =>
        current.map((widget) =>
          widget.id === id
            ? {
                ...widget,
                loading,
              }
            : widget,
        ),
      );
    },
    [],
  );

  const setWidgetVisible = useCallback(
    (
      id: WidgetId,
      visible: boolean,
    ) => {
      setWidgets((current) =>
        current.map((widget) =>
          widget.id === id
            ? {
                ...widget,
                visible,
              }
            : widget,
        ),
      );
    },
    [],
  );

  const refreshWidget = useCallback(
    (id: WidgetId) => {
      setWidgets((current) =>
        current.map((widget) =>
          widget.id === id
            ? {
                ...widget,
                refreshedAt:
                  new Date().toISOString(),
              }
            : widget,
        ),
      );
    },
    [],
  );

  const refreshAll = useCallback(() => {
    const now =
      new Date().toISOString();

    setWidgets((current) =>
      current.map((widget) => ({
        ...widget,
        refreshedAt: now,
      })),
    );
  }, []);

  const value = useMemo(
    () => ({
      widgets,
      registerWidget,
      unregisterWidget,
      setWidgetLoading,
      setWidgetVisible,
      refreshWidget,
      refreshAll,
    }),
    [
      widgets,
      registerWidget,
      unregisterWidget,
      setWidgetLoading,
      setWidgetVisible,
      refreshWidget,
      refreshAll,
    ],
  );

  return (
    <DashboardContext.Provider value={value}>
      {children}
    </DashboardContext.Provider>
  );
}

export function useDashboardContext() {
  const context =
    useContext(DashboardContext);

  if (!context) {
    throw new Error(
      "useDashboardContext must be used inside DashboardProvider",
    );
  }

  return context;
}