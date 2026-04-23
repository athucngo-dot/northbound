import { apiClient } from "../../lib/apiClient";
import { API_ENDPOINTS } from "../../constants/api";
import type { User } from "../../types/user";


// User API functions
export const usersApi = {
    me: async (): Promise<User> => {
        const res = await apiClient.get<User>(API_ENDPOINTS.ME);
        return res.data; // return only the user
    },
};