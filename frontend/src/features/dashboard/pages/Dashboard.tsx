export default function Dashboard() {
    return (
        <div>
            <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

            <div className="grid grid-cols-3 gap-6">
                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Total Projects</h3>
                    <p className="text-2xl font-bold mt-2">0</p>
                </div>

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Active Users</h3>
                    <p className="text-2xl font-bold mt-2">0</p>
                </div>

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Revenue</h3>
                    <p className="text-2xl font-bold mt-2">$0</p>
                </div>
            </div>

            <div className="bg-white p-6 rounded shadow mt-8">
                <h3 className="font-semibold mb-4">Activity Chart</h3>
                <div className="h-64 flex items-center justify-center text-gray-400">
                    Chart will go here
                </div>
            </div>
        </div>
    );
}