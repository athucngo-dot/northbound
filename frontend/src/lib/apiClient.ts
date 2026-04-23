import axios from "axios";
import { CONFIG } from "../config/config";

// General API instance
export const apiClient = axios.create({
    baseURL: CONFIG.API_BASE,
    withCredentials: true, // Include cookies in requests
    headers: {
        "Content-Type": "application/json",
    },
});
