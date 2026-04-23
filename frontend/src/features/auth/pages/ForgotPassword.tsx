import { useState } from "react";
import { Link } from "react-router-dom";
import { authApi } from "../api";
import { PATHS } from "../../../constants/paths";

export default function ForgotPassword() {
    const [email, setEmail] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);

        try {
            await authApi.forgotPassword(email);
            alert("Password reset email sent.");
        } catch (err: any) {
            if (err.response?.data?.detail) {
                alert(err.response.data.detail);
            } else {
                alert(err.message);
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">

            <input
                type="email"
                placeholder="Enter your email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
            />

            <button
                type="submit"
                disabled={loading}
                className="w-full py-3 rounded-lg bg-blue-500 text-white font-semibold hover:bg-blue-600 transition disabled:opacity-70"
            >
                {loading ? "Sending..." : "Send reset link"}
            </button>

            <p className="text-center text-sm mt-5 text-gray-600">
                Back to{" "}
                <Link to={PATHS.LOGIN} className="text-blue-500 hover:underline">
                    sign in
                </Link>
            </p>
        </form>
    );
}