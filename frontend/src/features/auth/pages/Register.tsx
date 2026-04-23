import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { authApi } from "../api";
import { PATHS } from "../../../constants/paths";
import { useAuth } from "../useAuth";
import type { FieldError } from "../../../types/errors";
import FormErrorList from "../../../components/form/FormErrorList";


export default function Register() {
    const [first_name, setFirst_name] = useState("");
    const [last_name, setLast_name] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState<string>("");
    const [fieldErrors, setFieldErrors] = useState<FieldError[]>([]);
    const [loading, setLoading] = useState(false);

    const { refreshUser } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        // Frontend validation confirming password match
        if (password !== confirmPassword) {
            setError("- Passwords do not match");
            return;
        }

        setError("");
        setLoading(true);

        try {
            await authApi.register({ first_name, last_name, email, password });

            // After successful registration, log the user in
            await authApi.login({ email, password });

            // update global state
            await refreshUser();

            // Redirect to dashboard
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

    const passwordsMatch = password === confirmPassword;

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
                    type="text"
                    placeholder="First name"
                    required
                    value={first_name}
                    onChange={(e) => setFirst_name(e.target.value)}
                    className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                />

                <input
                    type="text"
                    placeholder="Last name"
                    required
                    value={last_name}
                    onChange={(e) => setLast_name(e.target.value)}
                    className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                />

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

                <input
                    type="password"
                    placeholder="Confirm password"
                    required
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className={`w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 ${confirmPassword && !passwordsMatch
                        ? "border-red-500 focus:ring-red-400"
                        : "focus:ring-blue-400"
                        }`}
                />

                <button
                    type="submit"
                    disabled={loading}
                    className="w-full py-3 rounded-lg bg-blue-500 text-white font-semibold hover:bg-blue-600 transition disabled:opacity-70"
                >
                    {loading ? "Creating..." : "Create account"}
                </button>
            </form>

            <p className="text-center text-sm mt-5 text-gray-600">
                Already have an account?{" "}
                <Link to={PATHS.LOGIN} className="text-blue-500 hover:underline">
                    Sign in
                </Link>
            </p>
        </>
    );
}