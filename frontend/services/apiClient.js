import axios from "axios";

const API_BASE_URL =
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    timeout: 30000,
    headers: {
        "Content-Type": "application/json",
    },
});

apiClient.interceptors.request.use(
    (config) => {

        console.log(
            `[API] ${config.method?.toUpperCase()} ${config.url}`
        );

        return config;
    },
    (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(
    (response) => response,

    (error) => {

        if (error.response) {

            console.error(
                "[API ERROR]",
                error.response.status,
                error.response.data
            );

        } else if (error.request) {

            console.error(
                "[NETWORK ERROR]",
                error.message
            );

        } else {

            console.error(
                "[REQUEST ERROR]",
                error.message
            );

        }

        return Promise.reject(error);

    }
);

export async function apiGet(url, config = {}) {

    const response = await apiClient.get(url, config);

    return response.data;

}

export async function apiPost(
    url,
    data = {},
    config = {}
) {

    const response = await apiClient.post(
        url,
        data,
        config
    );

    return response.data;

}

export async function apiPut(
    url,
    data = {},
    config = {}
) {

    const response = await apiClient.put(
        url,
        data,
        config
    );

    return response.data;

}

export async function apiDelete(
    url,
    config = {}
) {

    const response = await apiClient.delete(
        url,
        config
    );

    return response.data;

}

export default apiClient;