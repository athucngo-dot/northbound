import { useNavigate } from "react-router-dom";
import { useAuth } from "../../features/auth/useAuth";
import { PATHS } from "../../constants/paths";

export default function Topbar() {
    const { logout } = useAuth();
    const navigate = useNavigate();

    const handleLogout = async () => {
        await logout(); // clear user from context
        navigate(PATHS.LOGIN, { replace: true });
    };

    return (
        <header className="bg-white shadow px-6 py-4 flex justify-between items-center">
            <h2 className="font-semibold text-lg">Admin Panel</h2>

            <button
                className="text-sm bg-gray-900 text-white px-4 py-2 rounded"
                onClick={handleLogout}
            >
                Logout
            </button>
        </header>
    );
}