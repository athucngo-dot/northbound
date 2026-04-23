import { Navigate } from "react-router-dom";
import { useAuth } from "../../features/auth/useAuth";
import { PATHS } from "../../constants/paths";


export default function GuestRoute({ children }: { children: React.ReactNode }) {

    const { user, loading } = useAuth();

    // show loading state while checking auth status
    if (loading) return null;

    // If already authenticated, redirect to dashboard
    if (user) {
        return <Navigate to={PATHS.DASHBOARD} replace />;
    }

    // If not authenticated, show the guest page
    return <>{children}</>;
}