import { useNavigate } from "react-router-dom";

export default function Login() {
    const navigate = useNavigate();

    return (
        <div className="flex items-center justify-center h-screen bg-gray-100">
            <div className="bg-white p-8 rounded shadow w-96">
                <h1 className="text-xl font-bold mb-6">Login</h1>

                <input
                    type="email"
                    placeholder="Email"
                    className="w-full mb-4 px-3 py-2 border rounded"
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="w-full mb-6 px-3 py-2 border rounded"
                />

                <button
                    onClick={() => navigate("/")}
                    className="w-full bg-gray-900 text-white py-2 rounded"
                >
                    Login
                </button>
            </div>
        </div>
    );
}