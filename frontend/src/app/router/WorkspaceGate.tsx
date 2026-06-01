import { Navigate } from "react-router-dom";

import { PATHS } from "../../constants/paths";
import { useAuth } from "../../features/auth/useAuth";


export default function WorkspaceGate({ children }: { children: React.ReactNode; }) {

    const { user, loading } = useAuth();

    if (loading) {
        console.log("WorkspaceGate loading...");
        return <div>Loading...</div>;
    }

    /* if user has not completed onboarding */
    if (!user?.onboarding_completed) {
        return (
            <Navigate
                to={PATHS.WELCOME}
                replace
            />
        );
    }

    return <>{children}</>;
}