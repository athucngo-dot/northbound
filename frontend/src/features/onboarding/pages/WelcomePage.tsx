import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PATHS } from "../../../constants/paths";
import { usersApi } from "../../users/api";
import { useAuth } from "../../auth/useAuth";

export default function WelcomePage() {
    const navigate = useNavigate();
    const [inviteCode, setInviteCode] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const { refreshUser } = useAuth();

    const handleJoin = async () => {
        if (!inviteCode.trim()) {
            setError("Please enter an invitation code");
            return;
        }

        try {
            setLoading(true);
            setError(null);

            // TODO: call API
            // await organizationApi.joinByInviteCode(inviteCode);

            navigate(PATHS.DASHBOARD);
        } catch (err) {
            setError("Invalid invitation code");
        } finally {
            setLoading(false);
        }
    };

    const handleSkip = async () => {
        await usersApi.completeOnboarding();
        await refreshUser();
        navigate(PATHS.DASHBOARD);
    };

    return (
        <div className="max-w-md mx-auto mt-10 flex flex-col gap-6">

            {/* Welcome message */}
            <div>
                <h1 className="text-2xl font-bold">Welcome to Northbound</h1>
                <p className="text-gray-600 text-sm mt-1">
                    You are not part of any organization yet.
                </p>
            </div>

            {/* Organization Card */}
            <div className="bg-white p-6 rounded-lg shadow flex flex-col gap-3">
                <h2 className="font-semibold">Create a new organization</h2>
                <p className="text-sm text-gray-500">
                    Start your workspace and invite your team.
                </p>

                <button
                    onClick={() => navigate(PATHS.CREATE_ORGANIZATION)}
                    className="w-full py-3 rounded-lg bg-blue-500 text-white font-semibold hover:bg-blue-600 transition"
                >
                    Create Organization
                </button>
            </div>

            {/* Join Organization Card */}
            <div className="bg-white p-6 rounded-lg shadow flex flex-col gap-3">
                <h2 className="font-semibold">Join with invitation code</h2>

                <input
                    type="text"
                    placeholder="Enter invite code"
                    value={inviteCode}
                    onChange={(e) => setInviteCode(e.target.value)}
                    className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                />

                {error && (
                    <p className="text-red-500 text-sm">{error}</p>
                )}

                <button
                    onClick={handleJoin}
                    disabled={loading}
                    className="w-full py-3 rounded-lg bg-gray-900 text-white font-semibold hover:bg-black transition disabled:opacity-70"
                >
                    {loading ? "Joining..." : "Join Organization"}
                </button>
            </div>

            {/* Skip */}
            <button
                onClick={handleSkip}
                className="text-sm text-gray-500 hover:underline"
            >
                Skip
            </button>
        </div>
    );
}