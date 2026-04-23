import { Navigate } from "react-router-dom";
import { useAuth } from "../../features/auth/useAuth";
import { PATHS } from "../../constants/paths";


export default function ProtectedRoute({ children }: { children: React.ReactNode }) {
    const { user, loading } = useAuth();

    // Show loading state while checking auth status
    if (loading) return null;

    // If not authenticated, redirect to login
    if (!user) {
        return <Navigate to={PATHS.LOGIN} replace />;
    }

    // If authenticated, show the protected page
    return <>{children}</>;
}