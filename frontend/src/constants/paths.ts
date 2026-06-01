export const PATHS = {
    LOGIN: "/login",
    REGISTER: "/register",
    FORGOT_PASSWORD: "/forgot-password",
    DASHBOARD: "/dashboard",
    PROJECTS: "/projects",
    USERS: "/users",

    WELCOME:
        "/welcome",

    CREATE_ORGANIZATION:
        "/organizations/new",

    ORGANIZATION_DASHBOARD:
        (slug: string) =>
            `/org/${slug}/dashboard`,

    PROJECT_BOARD:
        (
            slug: string,
            projectId: string
        ) =>
            `/org/${slug}/projects/${projectId}/board`,
};