import { apiGet } from "./apiClient";

export async function getIntelligence(symbol = "ASELS") {

    try {

        const result = await apiGet(
            `/intelligence/${symbol}`
        );

        return result;

    } catch (error) {

        console.error(
            "Intelligence API Error",
            error
        );

        return null;

    }

}

export default {

    getIntelligence,

};