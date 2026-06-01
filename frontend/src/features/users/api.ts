import { apiClient } from "../../lib/apiClient";
import { API_ENDPOINTS } from "../../constants/api";
import type { User } from "../../types/user";


// User API functions
export const usersApi = {
    me: async (): Promise<User | null> => {
        try {
            const res = await apiClient.get<User>(API_ENDPOINTS.ME);
            return res.data;
        } catch (err: any) {
            if (err.response?.status === 401) {
                return null;
            }
            throw err;
        }
    },

    completeOnboarding: async (): Promise<void> => {
        try {
            await apiClient.put(API_ENDPOINTS.COMPLETE_ONBOARDING);
        } catch (err: any) {
            throw err;
        }
    }
};