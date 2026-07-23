import { apiGet } from "./apiClient";


export async function getIntelligence(
    symbol = "ASELS"
) {

    try {

        const result = await apiGet(
            `/dashboard/${symbol}`
        );

        return result;

    } catch (error) {

        console.error(
            "Dashboard Intelligence API Error",
            error
        );

        return null;

    }

}


export default {

    getIntelligence,

};