import apiClient from "./apiClient";

export async function getIntelligence(symbol = "ASELS") {
    const response = await apiClient.get(`/intelligence/${symbol}`);
    return response.data;
}