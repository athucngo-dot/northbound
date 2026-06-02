import { apiClient } from "../../lib/apiClient";
import { API_ENDPOINTS } from "../../constants/api";
import type { MyOrganization, CreateOrganizationPayload, Organization } from "./types";


export const organizationsApi = {
    getMy: async (): Promise<MyOrganization[]> => {
        const res = await apiClient.get<MyOrganization[]>(API_ENDPOINTS.MY_ORGANIZATIONS);
        return res.data;
    },

    create: async (
        payload: CreateOrganizationPayload
    ): Promise<Organization> => {

        const res = await apiClient.post<Organization>(
            API_ENDPOINTS.CREATE_ORGANIZATION,
            payload
        );

        return res.data;
    },
}