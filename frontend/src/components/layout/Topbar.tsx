export default function Topbar() {
    return (
        <header className="bg-white shadow px-6 py-4 flex justify-between items-center">
            <h2 className="font-semibold text-lg">Admin Panel</h2>

            <button className="text-sm bg-gray-900 text-white px-4 py-2 rounded">
                Logout
            </button>
        </header>
    );
}