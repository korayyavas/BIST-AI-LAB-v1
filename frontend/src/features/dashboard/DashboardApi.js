import axios from "../../api/api";



async function get(url){

    const {data} = await axios.get(url);

    return data;

}





export async function loadDashboard(

    symbol="ASELS"

){


    try{


        const dashboard = await get(

            `/dashboard/${symbol}`

        );



        return {


            ...dashboard,



            // AI INTELLIGENCE

            intelligence:

                dashboard.intelligence ?? {},





            // NEWS KORUNUYOR

            news:

                dashboard.news ?? {

                    news: [],

                    statistics:{}

                },





            // RESEARCH KORUNUYOR

            research:

                dashboard.research ?? {

                    items: [],

                    consensus:{}

                },





            // KAP KORUNUYOR

            kap:

                dashboard.kap ?? {

                    items: [],

                    statistics:{}

                },





            topPicks:

                dashboard.topPicks ?? [],





            version:

                dashboard.version ?? {

                    version:"v10.0"

                },





            modules:

                dashboard.modules ?? {},





            loadedAt:

                dashboard.loadedAt ??

                new Date().toISOString(),





            errors:{}



        };


    }


    catch(error){


        console.error(

            "Dashboard load error",

            error

        );



        return {


            intelligence:{},


            news:{

                news:[]

            },


            research:{

                items:[]

            },


            kap:{

                items:[]

            },


            topPicks:[],


            errors:{

                dashboard:true

            }


        };


    }


}





export async function refreshDashboard(symbol){


    return loadDashboard(symbol);


}





export async function getHealth(){


    return get("/health");


}