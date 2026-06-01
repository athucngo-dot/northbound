import { Routes, Route, Navigate } from "react-router-dom";

import AppLayout from "../../layouts/AppLayout";
import AuthLayout from "../../layouts/AuthLayout";
import OnboardingLayout from "../../layouts/OnboardingLayout";

import ProtectedRoute from "./ProtectedRoute";
import { PATHS } from "../../constants/paths";

// pages
import Dashboard from "../../features/dashboard/pages/Dashboard";
import Login from "../../features/auth/pages/Login";
import Register from "../../features/auth/pages/Register";
import ForgotPassword from "../../features/auth/pages/ForgotPassword";
import WelcomePage from "../../features/onboarding/pages/WelcomePage";
import NewOrganization from "../../features/organizations/pages/NewOrganization";

import Projects from "../../pages/Projects";
import Users from "../../pages/Users";
import GuestRoute from "./GuestRoute";
import WorkspaceGate from "./WorkspaceGate";

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

            {/* PROTECTED MAIN APP */}
            <Route
                element={
                    <ProtectedRoute>
                        <WorkspaceGate>
                            <AppLayout />
                        </WorkspaceGate>
                    </ProtectedRoute>
                }
            >
                <Route path={PATHS.DASHBOARD} element={<Dashboard />} />
                <Route path={PATHS.PROJECTS} element={<Projects />} />
                <Route path={PATHS.USERS} element={<Users />} />
            </Route>

            {/* PROTECTED ONBOARDING */}
            <Route
                element={
                    <ProtectedRoute>
                        <OnboardingLayout />
                    </ProtectedRoute>
                }
            >
                <Route path={PATHS.WELCOME} element={<WelcomePage />} />
                <Route path={PATHS.CREATE_ORGANIZATION} element={<NewOrganization />} />
            </Route>

            {/* fallback */}
            <Route path="*" element={<Navigate to={PATHS.LOGIN} />} />
        </Routes>
    );
}