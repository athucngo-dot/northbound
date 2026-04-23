import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { authApi } from "../api";
import { PATHS } from "../../../constants/paths";
import { useAuth } from "../useAuth";
import type { FieldError } from "../../../types/errors";
import FormErrorList from "../../../components/form/FormErrorList";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [fieldErrors, setFieldErrors] = useState<FieldError[]>([]);
    const [loading, setLoading] = useState(false);

    const { refreshUser } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        setError("");
        setLoading(true);

        try {
            // Call login API
            await authApi.login({ email, password });

            // update global state
            await refreshUser();

            // Navigate to dashboard
            navigate(PATHS.DASHBOARD);
        } catch (err: any) {

            const status = err.response?.status;
            const data = err.response?.data;

            // Handle FastAPI validation errors
            if (status === 422 && data?.errors) {

                const errorList: FieldError[] = Object.entries(data.errors).map(
                    ([field, message]) => ({
                        field,
                        message: String(message),
                    }));

                setFieldErrors(errorList);
                setError("");

            } else {
                setFieldErrors([]);
                setError(data?.message || "Something went wrong");
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">

                {/* Error message */}
                {error && (
                    <p className="text-red-500 text-sm">{error}</p>
                )}

                {/* Field-specific errors */}
                <FormErrorList errors={fieldErrors} />

                <input
                    type="email"
                    placeholder="Email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                />

                <input
                    type="password"
                    placeholder="Password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                />

                {/*<div className="flex justify-end">
                    <Link
                        to={PATHS.FORGOT_PASSWORD}
                        className="text-sm text-blue-500 hover:underline"
                    >
                        Forgot password?
                    </Link>
                </div>*/}

                <button
                    type="submit"
                    disabled={loading}
                    className="w-full py-3 rounded-lg bg-blue-500 text-white font-semibold hover:bg-blue-600 transition disabled:opacity-70"
                >
                    {loading ? "Signing in..." : "Sign In"}
                </button>
            </form>

            <p className="text-center text-sm mt-5 text-gray-600">
                Don't have an account?{" "}
                <Link to={PATHS.REGISTER} className="text-blue-500 hover:underline">
                    Create account
                </Link>
            </p>
        </>
    );
}