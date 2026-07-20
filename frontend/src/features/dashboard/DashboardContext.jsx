import { createContext, useContext } from "react";

const DashboardContext = createContext(null);

export function DashboardProvider({ value, children }) {

    return (

        <DashboardContext.Provider value={value}>

            {children}

        </DashboardContext.Provider>

    );

}

export function useDashboardContext() {

    return useContext(DashboardContext);

}