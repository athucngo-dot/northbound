import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { PATHS } from "../../../constants/paths";
import { organizationsApi } from "../api";
import { useAuth } from "../../auth/useAuth";
import { useApp } from "../../app/useApp";

export default function NewOrganization() {
    const navigate = useNavigate();
    const { refreshUser } = useAuth();
    const { refreshOrganizations } = useApp();

    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [loading, setLoading] = useState(false);

    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        if (!name.trim()) {
            setError("Organization name is required.");
            return;
        }

        try {
            setLoading(true);
            setError(null);

            await organizationsApi.create({
                name: name.trim(),
                description: description.trim() || null,
            });

            await refreshUser();
            await refreshOrganizations();

            navigate(PATHS.DASHBOARD);

        } catch (err: any) {
            setError(
                err?.response?.data?.detail ||
                "Failed to create organization."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-white p-8 rounded-xl shadow-sm border">

            {/* Header */}
            <div className="mb-6">
                <h1 className="text-2xl font-bold">
                    Create organization
                </h1>

                <p className="text-sm text-gray-500 mt-2">
                    Organizations are shared workspaces where you can manage
                    projects, tickets, and collaborate with your team.
                </p>
            </div>

            {/* Form */}
            <form
                onSubmit={handleSubmit}
                className="flex flex-col gap-4"
            >

                {/* Global error */}
                {error && (
                    <p className="text-sm text-red-500">
                        {error}
                    </p>
                )}

                {/* Organization name */}
                <div className="flex flex-col gap-2">
                    <label className="text-sm font-medium text-gray-700">
                        Organization name
                    </label>

                    <input
                        type="text"
                        placeholder="Organization name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        className="w-full p-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                    />
                </div>

                <div className="flex flex-col gap-2">
                    <label className="text-sm font-medium text-gray-700">
                        Description
                    </label>

                    <textarea
                        placeholder="Tell your team what this organization is for..."
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        rows={4}
                        className="w-full p-3 border rounded-lg text-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-400 "
                    />
                </div>

                {/* Submit */}
                <button
                    type="submit"
                    disabled={loading}
                    className="
                        w-full
                        py-3
                        rounded-lg
                        bg-blue-500
                        text-white
                        font-semibold
                        hover:bg-blue-600
                        transition
                        disabled:opacity-70
                    "
                >
                    {loading
                        ? "Creating organization..."
                        : "Create organization"}
                </button>
            </form>
        </div>
    );
}