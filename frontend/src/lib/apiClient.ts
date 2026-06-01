import axios from "axios";
import { CONFIG } from "../config/config";
import { PATHS } from "../constants/paths";
import { authEvents } from "../stores/authEvents";

// General API instance
export const apiClient = axios.create({
    baseURL: CONFIG.API_BASE,
    withCredentials: true, // Include cookies in requests
    headers: {
        "Content-Type": "application/json",
    },
});


// Add a response interceptor to handle 401 errors globally
apiClient.interceptors.response.use(
    response => response,

    error => {
        const url = error.config?.url || "";

        if (error.response?.status === 401 &&
            !url.endsWith("/me") &&
            window.location.pathname !== PATHS.LOGIN
        ) {
            authEvents.triggerLogout();
            window.location.href = PATHS.LOGIN;
        }

        return Promise.reject(error);
    }
);

