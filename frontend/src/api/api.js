import axios from "axios";

const api = axios.create({

    baseURL: "http://127.0.0.1:8000",

    timeout: 60000,

    headers: {

        "Content-Type": "application/json",

    },

});

api.interceptors.request.use(

    (config) => {

        config.headers["Accept"] = "application/json";

        return config;

    },

    (error) => Promise.reject(error),

);

api.interceptors.response.use(

    (response) => response,

    (error) => {

        if (error.response) {

            console.error(

                "API ERROR:",

                error.response.status,

                error.response.data,

            );

        } else if (error.request) {

            console.error(

                "BACKEND NOT REACHABLE",

            );

        } else {

            console.error(

                error.message,

            );

        }

        return Promise.reject(error);

    },

);

export default api;