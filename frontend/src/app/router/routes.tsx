import { Routes, Route, Navigate } from "react-router-dom";

import AppLayout from "../../layouts/AppLayout";
import AuthLayout from "../../layouts/AuthLayout";

import ProtectedRoute from "./ProtectedRoute";
import { PATHS } from "../../constants/paths";

// pages
import Dashboard from "../../features/dashboard/pages/Dashboard";
import Login from "../../features/auth/pages/Login";
import Register from "../../features/auth/pages/Register";
import ForgotPassword from "../../features/auth/pages/ForgotPassword";
import Projects from "../../pages/Projects";
import Users from "../../pages/Users";
import GuestRoute from "./GuestRoute";

export default function AppRouter() {
    return (
        <Routes>
            {/* AUTH */}
            <Route
                element={
                    <GuestRoute>
                        <AuthLayout />
                    </GuestRoute>
                }
            >
                <Route path={PATHS.LOGIN} element={<Login />} />
                <Route path={PATHS.REGISTER} element={<Register />} />
                <Route path={PATHS.FORGOT_PASSWORD} element={<ForgotPassword />} />
            </Route>

            {/* PROTECTED APP */}
            <Route
                element={
                    <ProtectedRoute>
                        <AppLayout />
                    </ProtectedRoute>
                }
            >
                <Route path={PATHS.DASHBOARD} element={<Dashboard />} />
                <Route path={PATHS.PROJECTS} element={<Projects />} />
                <Route path={PATHS.USERS} element={<Users />} />
            </Route>

            {/* fallback */}
            <Route path="*" element={<Navigate to={PATHS.LOGIN} />} />
        </Routes>
    );
}