import { useEffect, useState } from "react";
import { AuthContext } from "../../features/auth/auth.context";
import { usersApi } from "../../features/users/api";
import { authApi } from "../../features/auth/api";
import type { User } from "../../types/user";

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    const fetchUser = async () => {
        try {
            const user = await usersApi.me();
            setUser(user);
        } catch (err: any) {
            if (err.response?.status === 401) {
                setUser(null);
            } else {
                console.error("Unexpected error fetching user:", err);
            }
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchUser();
    }, []);

    const refreshUser = async () => {
        setLoading(true);
        await fetchUser();
    };

    const logout = async () => {
        try {
            await authApi.logout();
        } finally {
            setUser(null);
        }
    };

    return (
        <AuthContext.Provider
            value={{ user, loading, refreshUser, logout }}
        >
            {children}
        </AuthContext.Provider>
    );
};