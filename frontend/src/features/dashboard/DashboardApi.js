import axios from "../../api/api";

export async function loadDashboard(symbol){

    const intelligence=await axios.post(

        "/intelligence",

        {

            symbol

        }

    );

    const news=await axios.post(

        "/news",

        {

            symbol

        }

    );

    const research=await axios.post(

        "/research",

        {

            symbol

        }

    );

    const kap=await axios.post(

        "/kap",

        {

            symbol

        }

    );

    return{

        intelligence:intelligence.data,

        news:news.data.news||[],

        research:research.data.reports||[],

        kap:kap.data.events||

            kap.data.kap||

            []

    };

}