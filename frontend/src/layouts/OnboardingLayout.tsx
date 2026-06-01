import { Outlet } from "react-router-dom";
import logo from "../assets/images/northbound_logo.png";

export default function OnboardingLayout() {
    return (
        <div className="min-h-screen bg-gray-50 flex flex-col">

            <header className="h-16 border-b bg-white flex items-center px-6">
                <img src={logo} alt="Northbound logo" className="h-10 mr-2" />
                <h1 className="text-lg font-bold text-blue-600">
                    Northbound
                </h1>
            </header>

            <main className="flex-1 flex items-center justify-center p-6">
                <div className="w-full max-w-md">
                    <Outlet />
                </div>
            </main>

        </div>
    );
}