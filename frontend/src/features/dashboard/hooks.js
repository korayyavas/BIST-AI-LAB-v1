import { useEffect,useState } from "react";

import { loadDashboard } from "./DashboardApi";

export function useDashboard(symbol){

    const [loading,setLoading]=useState(true);

    const [data,setData]=useState(null);

    useEffect(()=>{

        reload();

    },[symbol]);

    async function reload(){

        setLoading(true);

        try{

            const result=

                await loadDashboard(symbol);

            setData(result);

        }

        finally{

            setLoading(false);

        }

    }

    return{

        loading,

        data,

        reload

    };

}