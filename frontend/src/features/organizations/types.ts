export type Organization = {
    id: string;
    name: string;
    slug: string;
    description: string | null;
    is_active: boolean;
};

export type MyOrganization = {
    organization: Organization;

    role: string;
}

export type CreateOrganizationPayload = {
    name: string;
    description?: string | null;
};