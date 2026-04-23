import { apiClient } from "../../lib/apiClient";
import { API_ENDPOINTS } from "../../constants/api";

type RegisterRequest = {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
};

type LoginRequest = {
    email: string;
    password: string;
};


// Authentication API functions
export const authApi = {
    login: (payload: LoginRequest) =>
        apiClient.post(API_ENDPOINTS.LOGIN, payload),

    register: (payload: RegisterRequest) =>
        apiClient.post(API_ENDPOINTS.REGISTER, payload),

    forgotPassword: (email: string) =>
        apiClient.post(API_ENDPOINTS.FORGOT_PASSWORD, { email }),

    logout: () =>
        apiClient.post(API_ENDPOINTS.LOGOUT),
};