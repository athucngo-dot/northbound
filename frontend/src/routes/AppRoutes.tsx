import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import Projects from "../pages/Projects";
import Users from "../pages/Users";
import Login from "../pages/Login";
import AppLayout from "../components/layout/AppLayout";

export default function AppRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />

                <Route element={<AppLayout />}>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/projects" element={<Projects />} />
                    <Route path="/users" element={<Users />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}