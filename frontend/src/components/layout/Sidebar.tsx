import { NavLink } from "react-router-dom";

export default function Sidebar() {
    const linkStyle =
        "block px-4 py-2 rounded hover:bg-gray-200 transition-colors";

    return (
        <aside className="w-64 bg-white shadow-md p-4">
            <h1 className="text-xl font-bold mb-6">Northbound</h1>

            <nav className="space-y-2">
                <NavLink to="/" className={linkStyle}>
                    Dashboard
                </NavLink>

                <NavLink to="/projects" className={linkStyle}>
                    Projects
                </NavLink>

                <NavLink to="/users" className={linkStyle}>
                    Users
                </NavLink>
            </nav>
        </aside>
    );
}