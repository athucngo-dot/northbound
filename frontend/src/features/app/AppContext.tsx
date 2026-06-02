import { createContext, useCallback, useEffect, useState, type ReactNode } from "react";
import { organizationsApi } from "../organizations/api";
import type { MyOrganization } from "../organizations/types";
import { ACTIVE_ORGANIZATION_KEY } from "./constants";
import { useAuth } from "../auth/useAuth";

type AppContextType = {
    organizations: MyOrganization[];

    activeOrganization: MyOrganization | null;

    switchOrganization: (
        organization: MyOrganization | null
    ) => void;

    refreshOrganizations:
    () => Promise<void>;

    loading: boolean;
};

export const AppContext = createContext<AppContextType | undefined>(undefined);

type Props = {
    children: ReactNode;
};

export function AppProvider({ children }: Props) {

    const { user, loading: authLoading } = useAuth();

    const [organizations, setOrganizations] = useState<MyOrganization[]>([]);

    const [activeOrganization, setActiveOrganization] =
        useState<MyOrganization | null>(null);

    const [loading, setLoading] = useState(true);

    const loadOrganizations = useCallback(async () => {

        // if user not logged in, do nothing
        if (!user) {
            setOrganizations([]);
            setActiveOrganization(null);
            setLoading(false);

            return;
        }

        try {
            const orgs = await organizationsApi.getMy();

            setOrganizations(orgs);

            /* User has no organizations */
            if (orgs.length === 0) {
                setActiveOrganization(null);
                return;
            }

            /* get saved organization ID in localStorage */
            const savedOrgId = localStorage.getItem(ACTIVE_ORGANIZATION_KEY);

            /* Validate saved ID */
            const matchingOrganization =
                orgs.find(
                    (org) => org.organization.id === savedOrgId
                );

            /* Restore if valid */
            if (matchingOrganization) {
                setActiveOrganization(matchingOrganization);
                return;
            }

            /* Fallback to first organization */
            setActiveOrganization(orgs[0]);

            /* Persist fallback */
            localStorage.setItem(ACTIVE_ORGANIZATION_KEY, orgs[0].organization.id);

        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }, [user]);

    useEffect(() => {
        // if auth is still loading, wait
        if (authLoading) return;

        loadOrganizations();

    }, [authLoading, loadOrganizations]);

    const switchOrganization = useCallback((organization: MyOrganization | null) => {
        setActiveOrganization(organization);
        if (organization) {
            localStorage.setItem(ACTIVE_ORGANIZATION_KEY, organization.organization.id);
        } else {
            localStorage.setItem(ACTIVE_ORGANIZATION_KEY, '');
        }
    }, []);

    return (
        <AppContext.Provider
            value={{
                organizations,
                activeOrganization,
                switchOrganization,
                refreshOrganizations: loadOrganizations,
                loading,
            }}
        >
            {children}
        </AppContext.Provider>
    );
}