import { Outlet } from "react-router-dom";
import logo from "../assets/images/northbound_logo.png";

type AuthLayoutProps = {
    title?: string;
    subtitle?: string;
};

export default function AuthLayout({ title, subtitle }: AuthLayoutProps) {
    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">

                {/* Header */}
                <div className="text-center mb-6">
                    <img src={logo} alt="Northbound logo" className="mx-auto h-10" />
                    {title && (
                        <h1 className="text-2xl font-semibold mt-2">{title}</h1>
                    )}

                    {subtitle && (
                        <p className="text-sm text-gray-500 mt-1">{subtitle}</p>
                    )}
                </div>

                {/* Page content */}
                <Outlet />
            </div>
        </div>
    );
}